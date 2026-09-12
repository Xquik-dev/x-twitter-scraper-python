# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Mapping, AbstractSet
from collections import deque
from typing_extensions import TypeAlias, TypeGuard

from ._types import IncEx
from ._utils import is_mapping, is_iterable
from ._compat import PYDANTIC_V1, is_union, get_origin
from ._models import _EagerIterable

if TYPE_CHECKING or not PYDANTIC_V1:
    from pydantic.v1 import BaseModel
    from pydantic.v1.utils import ValueItems
    from pydantic.v1.fields import SHAPE_TUPLE, SHAPE_SINGLETON, ModelField
else:
    from pydantic import BaseModel
    from pydantic.utils import ValueItems
    from pydantic.fields import SHAPE_TUPLE, SHAPE_SINGLETON, ModelField


Selection: TypeAlias = AbstractSet[int | str] | Mapping[int | str, object]


def serialize_fields(
    output: Mapping[str, object],
    source: BaseModel,
    include: IncEx | Selection | None,
    exclude: IncEx | Selection | None,
    by_alias: bool,
) -> dict[str, object]:
    return _fields(
        output,
        source.__dict__,
        source.__fields__,
        ValueItems.merge(source.__include_fields__, include, intersect=True),
        ValueItems.merge(source.__exclude_fields__, exclude),
        by_alias,
    )


def _fields(
    output: Mapping[str, object],
    source: Mapping[str, object],
    fields: Mapping[str, ModelField],
    include: Selection | None,
    exclude: Selection | None,
    by_alias: bool,
) -> dict[str, object]:
    aliases = {(field.alias if by_alias else name): name for name, field in fields.items()}
    included = ValueItems(source, include) if include is not None else None
    excluded = ValueItems(source, exclude) if exclude is not None else None
    result: dict[str, object] = {}
    for key, value in output.items():
        name = aliases.get(key, key)
        result[key] = _convert(
            value,
            source.get(name),
            fields.get(name),
            included.for_element(name) if included else None,
            excluded.for_element(name) if excluded else None,
            by_alias,
        )
    return result


def _matches(value: object, field: ModelField) -> bool:
    if value is None:
        return field.allow_none
    origin = get_origin(field.outer_type_) or field.type_
    if origin is Any:
        return True
    nested = getattr(origin, "__pydantic_model__", None)
    if nested is not None:
        return is_mapping(value) and all(
            _matches(value[name], child) if name in value else not child.required
            for name, child in nested.__fields__.items()
        )
    if origin is _EagerIterable:
        if not is_iterable(value) or isinstance(value, str):
            return False
    elif not (isinstance(origin, type) and isinstance(value, origin)):
        return False
    if field.sub_fields and is_mapping(value):
        return all(
            (field.key_field is None or _matches(key, field.key_field)) and _matches(item, field.sub_fields[0])
            for key, item in value.items()
        )
    if field.sub_fields and _container(value):
        if field.shape == SHAPE_TUPLE and len(value) != len(field.sub_fields):
            return False
        return all(
            _matches(item, field.sub_fields[index] if field.shape == SHAPE_TUPLE else field.sub_fields[0])
            for index, item in enumerate(value)
        )
    return True


def _container(
    value: object,
) -> TypeGuard[list[object] | tuple[object, ...] | set[object] | frozenset[object] | deque[object]]:
    return isinstance(value, (list, tuple, set, frozenset, deque))


def _convert(
    output: object,
    source: object,
    field: ModelField | None,
    include: Selection | None,
    exclude: Selection | None,
    by_alias: bool,
) -> object:
    if isinstance(source, BaseModel) and is_mapping(output):
        return serialize_fields(output, source, include, exclude, by_alias)
    if field is None or source is None:
        return output
    origin = get_origin(field.outer_type_)
    if is_union(origin):
        branch = next((branch for branch in field.sub_fields or [] if _matches(source, branch)), None)
        return _convert(output, source, branch, include, exclude, by_alias) if branch else output
    nested = getattr(field.type_, "__pydantic_model__", None)
    if nested is not None and field.shape == SHAPE_SINGLETON and is_mapping(output) and is_mapping(source):
        return _fields(output, source, nested.__fields__, include, exclude, False)
    if field.sub_fields and is_mapping(output) and is_mapping(source):
        return _fields(output, source, dict.fromkeys(output, field.sub_fields[0]), include, exclude, False)
    if field.sub_fields and _container(output) and is_iterable(source):
        included = ValueItems(source, include) if include is not None else None
        excluded = ValueItems(source, exclude) if exclude is not None else None
        originals = [
            (index, item)
            for index, item in enumerate(source)
            if (included is None or included.is_included(index))
            and (excluded is None or not excluded.is_excluded(index))
        ]
        converted = [
            _convert(
                item,
                original,
                field.sub_fields[index] if field.shape == SHAPE_TUPLE else field.sub_fields[0],
                included.for_element(index) if included else None,
                excluded.for_element(index) if excluded else None,
                by_alias,
            )
            for item, (index, original) in zip(output, originals, strict=True)
        ]
        if origin is _EagerIterable:
            return converted
        if all(item is previous for item, previous in zip(converted, output, strict=True)):
            return output
        return type(output)(converted)
    return list(output) if origin is _EagerIterable and is_iterable(output) else output
