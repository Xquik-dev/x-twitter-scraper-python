# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import typing
import typing_extensions
from typing import Any, TypeVar, Iterable, cast
from collections import abc as _c_abc
from typing_extensions import (
    TypeIs,
    Required,
    Annotated,
    get_args,
    get_origin,
)

from ._utils import lru_cache
from .._types import InheritsGeneric
from ._compat import is_union as _is_union


def is_annotated_type(typ: object) -> bool:
    return get_origin(typ) is Annotated


def is_list_type(typ: type) -> bool:
    return (get_origin(typ) or typ) == list


def is_sequence_type(typ: type) -> bool:
    origin = get_origin(typ) or typ
    return origin == typing_extensions.Sequence or origin == typing.Sequence or origin == _c_abc.Sequence


def is_iterable_type(typ: type) -> bool:
    origin = get_origin(typ) or typ
    return origin == Iterable or origin == _c_abc.Iterable


def is_union_type(typ: type) -> bool:
    return _is_union(get_origin(typ))


def is_required_type(typ: type) -> bool:
    return get_origin(typ) is Required


def is_typevar(typ: object) -> bool:
    return type(typ) == TypeVar


_TYPE_ALIAS_TYPES: tuple[type, ...] = (typing_extensions.TypeAliasType,)
if sys.version_info >= (3, 12):
    _TYPE_ALIAS_TYPES = (*_TYPE_ALIAS_TYPES, typing.TypeAliasType)


def is_type_alias_type(tp: Any, /) -> TypeIs[typing_extensions.TypeAliasType]:
    return isinstance(tp, _TYPE_ALIAS_TYPES)


@lru_cache(maxsize=8096)
def strip_annotated_type(typ: type) -> type:
    if is_required_type(typ) or is_annotated_type(typ):
        return strip_annotated_type(cast(type, get_args(typ)[0]))

    return typ


def extract_type_arg(typ: object, index: int) -> type:
    args = get_args(typ)
    try:
        return cast(type, args[index])
    except IndexError as err:
        raise RuntimeError(f"Expected type {typ} to have a type argument at index {index} but it did not") from err


def extract_type_var_from_base(
    typ: type,
    *,
    generic_bases: tuple[type, ...],
    index: int,
    failure_message: str | None = None,
) -> type:
    cls = cast(object, get_origin(typ) or typ)
    if cls in generic_bases:  # pyright: ignore[reportUnnecessaryContains]
        return extract_type_arg(typ, index)

    if hasattr(cls, "__orig_bases__"):
        target_base_class: Any | None = None
        for base in cast(InheritsGeneric, cls).__orig_bases__:
            if base.__origin__ in generic_bases:
                target_base_class = base
                break

        if target_base_class is None:
            raise RuntimeError(
                "Could not find the generic base class;\n"
                "This should never happen;\n"
                f"Does {cls} inherit from one of {generic_bases} ?"
            )

        extracted = extract_type_arg(target_base_class, index)
        if is_typevar(extracted):
            return extract_type_arg(typ, index)

        return extracted

    raise RuntimeError(failure_message or f"Could not resolve inner type variable at index {index} for {typ}")
