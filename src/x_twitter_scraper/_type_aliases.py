# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from types import GenericAlias
from typing import TYPE_CHECKING, Union, Callable, cast
from typing_extensions import Protocol

from ._utils import is_mapping, is_annotated_type, is_type_alias_type
from ._compat import PYDANTIC_V1, get_args, is_union, get_origin

if TYPE_CHECKING or not PYDANTIC_V1:
    from pydantic.v1.main import ModelMetaclass
else:
    from pydantic.main import ModelMetaclass


class _Subscription(Protocol):
    def __getitem__(self, arguments: tuple[object, ...]) -> object: ...


def _resolve_alias(annotation: object) -> object:
    if is_type_alias_type(annotation):
        return _resolve_alias(annotation.__value__)
    annotated = is_annotated_type(annotation)
    arguments = get_args(annotation)
    resolved = tuple(
        _resolve_alias(item) if index == 0 or not annotated else item for index, item in enumerate(arguments)
    )
    if arguments == resolved:
        return annotation
    copier: object = getattr(annotation, "copy_with", None)
    if callable(copier):
        return cast(Callable[[tuple[object, ...]], object], copier)(resolved[:1] if annotated else resolved)
    origin = get_origin(annotation)
    if is_union(origin):
        return cast(_Subscription, Union)[resolved]
    return GenericAlias(origin, resolved) if origin is not None else annotation


class AliasModelMetaclass(ModelMetaclass):
    def __new__(
        mcs: type[AliasModelMetaclass],
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, object],
        **kwargs: object,
    ) -> AliasModelMetaclass:
        annotations = namespace.get("__annotations__")
        if is_mapping(annotations):
            namespace = {
                **namespace,
                "__annotations__": {key: _resolve_alias(value) for key, value in annotations.items()},
            }
        create: Callable[..., AliasModelMetaclass] = ModelMetaclass.__dict__["__new__"]
        return create(mcs, name, bases, namespace, **kwargs)
