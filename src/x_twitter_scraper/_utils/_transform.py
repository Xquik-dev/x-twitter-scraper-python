# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import io
import os
import base64
import pathlib
from typing import Mapping, overload
from datetime import date, datetime
from dataclasses import dataclass
from typing_extensions import Literal, override, get_type_hints as _get_type_hints

from ._sync import to_thread
from ._utils import (
    is_dict,
    is_list,
    is_given,
    lru_cache,
    is_mapping,
    is_iterable,
    is_sequence,
)
from .._files import is_base64_file_input
from ._compat import get_args, get_origin, is_typeddict
from ._typing import (
    is_list_type,
    is_union_type,
    extract_type_arg,
    is_iterable_type,
    is_required_type,
    is_sequence_type,
    is_annotated_type,
    strip_annotated_type,
)

PropertyFormat = Literal["iso8601", "base64", "custom"]


@dataclass(kw_only=True, eq=False)
class PropertyInfo:
    alias: str | None = None
    format: PropertyFormat | None = None
    format_template: str | None = None
    discriminator: str | None = None

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(alias='{self.alias}', format={self.format}, format_template='{self.format_template}', discriminator='{self.discriminator}')"


@overload
def maybe_transform(data: Mapping[str, object], expected_type: object) -> Mapping[str, object]: ...


@overload
def maybe_transform(data: None, expected_type: object) -> None: ...


@overload
def maybe_transform(data: object, expected_type: object) -> object: ...


def maybe_transform(
    data: object,
    expected_type: object,
) -> object:
    if data is None:
        return None
    return transform(data, expected_type)


@overload
def transform(data: Mapping[str, object], expected_type: object) -> Mapping[str, object]: ...


@overload
def transform(data: object, expected_type: object) -> object: ...


def transform(
    data: object,
    expected_type: object,
) -> object:
    return _transform_recursive(data, annotation=expected_type)


@lru_cache(maxsize=8096)
def _get_property_info(type_: object) -> tuple[PropertyInfo, ...]:
    if is_required_type(type_):
        type_ = get_args(type_)[0]
    if not is_annotated_type(type_):
        return ()
    return tuple(info for info in get_args(type_)[1:] if isinstance(info, PropertyInfo))


def _maybe_transform_key(key: str, type_: object) -> str:
    for info in _get_property_info(type_):
        if info.alias is not None:
            return info.alias

    return key


def _transform_recursive(
    data: object,
    *,
    annotation: object,
    inner_type: object = None,
) -> object:
    from .._compat import PydanticModel, model_dump

    if inner_type is None:
        inner_type = annotation

    stripped_type = strip_annotated_type(inner_type)
    origin = get_origin(stripped_type) or stripped_type
    if is_typeddict(stripped_type) and is_mapping(data):
        return _transform_typeddict(data, stripped_type)

    if origin == dict and is_mapping(data):
        items_type = get_args(stripped_type)[1]
        return {key: _transform_recursive(value, annotation=items_type) for key, value in data.items()}

    if (
        (is_list_type(stripped_type) and is_list(data))
        or (is_iterable_type(stripped_type) and is_iterable(data) and not isinstance(data, str))
        or (is_sequence_type(stripped_type) and is_sequence(data) and not isinstance(data, str))
    ):
        if is_dict(data):
            return data

        inner_type = extract_type_arg(stripped_type, 0)
        if inner_type == float or inner_type == int:
            if is_list(data):
                return data
            return list(data)

        return [_transform_recursive(d, annotation=annotation, inner_type=inner_type) for d in data]

    if is_union_type(stripped_type):
        for subtype in get_args(stripped_type):
            data = _transform_recursive(data, annotation=annotation, inner_type=subtype)
        return data

    if isinstance(data, PydanticModel):
        return model_dump(data, exclude_unset=True, mode="json")

    for info in _get_property_info(annotation):
        if info.format is not None:
            return _format_data(data, info.format, info.format_template)

    return data


def _decode_path(value: object) -> str:
    if not isinstance(value, (str, bytes)):
        raise TypeError("File paths must resolve to strings or bytes")
    return os.fsdecode(value)


def _format_data(data: object, format_: PropertyFormat, format_template: str | None) -> object:
    if isinstance(data, (date, datetime)):
        if format_ == "iso8601":
            return data.isoformat()

        if format_ == "custom" and format_template is not None:
            return data.strftime(format_template)

    if format_ == "base64" and is_base64_file_input(data):
        binary: object = None

        if isinstance(data, os.PathLike):
            binary = pathlib.Path(_decode_path(data.__fspath__())).read_bytes()
        elif isinstance(data, io.IOBase):
            binary = data.read()

            if isinstance(binary, str):
                binary = binary.encode()

        if not isinstance(binary, bytes):
            raise RuntimeError(f"Could not read bytes from {data}; Received {type(binary)}")

        return base64.b64encode(binary).decode("ascii")

    return data


def _transform_typeddict(
    data: Mapping[str, object],
    expected_type: object,
) -> Mapping[str, object]:
    result: dict[str, object] = {}
    annotations = get_type_hints(expected_type, include_extras=True)
    for key, value in data.items():
        if not is_given(value):
            continue

        type_ = annotations.get(key)
        if type_ is None:
            result[key] = value
        else:
            result[_maybe_transform_key(key, type_)] = _transform_recursive(value, annotation=type_)
    return result


@overload
async def async_maybe_transform(data: Mapping[str, object], expected_type: object) -> Mapping[str, object]: ...


@overload
async def async_maybe_transform(data: None, expected_type: object) -> None: ...


@overload
async def async_maybe_transform(data: object, expected_type: object) -> object: ...


async def async_maybe_transform(
    data: object,
    expected_type: object,
) -> object:
    if data is None:
        return None
    return await async_transform(data, expected_type)


@overload
async def async_transform(data: Mapping[str, object], expected_type: object) -> Mapping[str, object]: ...


@overload
async def async_transform(data: object, expected_type: object) -> object: ...


async def async_transform(
    data: object,
    expected_type: object,
) -> object:
    return await _async_transform_recursive(data, annotation=expected_type)


async def _async_transform_recursive(
    data: object,
    *,
    annotation: object,
    inner_type: object = None,
) -> object:
    from .._compat import PydanticModel, model_dump

    if inner_type is None:
        inner_type = annotation

    stripped_type = strip_annotated_type(inner_type)
    origin = get_origin(stripped_type) or stripped_type
    if is_typeddict(stripped_type) and is_mapping(data):
        return await _async_transform_typeddict(data, stripped_type)

    if origin == dict and is_mapping(data):
        items_type = get_args(stripped_type)[1]
        return {key: await _async_transform_recursive(value, annotation=items_type) for key, value in data.items()}

    if (
        (is_list_type(stripped_type) and is_list(data))
        or (is_iterable_type(stripped_type) and is_iterable(data) and not isinstance(data, str))
        or (is_sequence_type(stripped_type) and is_sequence(data) and not isinstance(data, str))
    ):
        if is_dict(data):
            return data

        inner_type = extract_type_arg(stripped_type, 0)
        if inner_type == float or inner_type == int:
            if is_list(data):
                return data
            return list(data)

        return [await _async_transform_recursive(d, annotation=annotation, inner_type=inner_type) for d in data]

    if is_union_type(stripped_type):
        for subtype in get_args(stripped_type):
            data = await _async_transform_recursive(data, annotation=annotation, inner_type=subtype)
        return data

    if isinstance(data, PydanticModel):
        return model_dump(data, exclude_unset=True, mode="json")

    for info in _get_property_info(annotation):
        if info.format is not None:
            return await _async_format_data(data, info.format, info.format_template)

    return data


async def _async_format_data(data: object, format_: PropertyFormat, format_template: str | None) -> object:
    if format_ == "base64" and is_base64_file_input(data):
        return await to_thread(_format_data, data, format_, format_template)
    return _format_data(data, format_, format_template)


async def _async_transform_typeddict(
    data: Mapping[str, object],
    expected_type: object,
) -> Mapping[str, object]:
    result: dict[str, object] = {}
    annotations = get_type_hints(expected_type, include_extras=True)
    for key, value in data.items():
        if not is_given(value):
            continue

        type_ = annotations.get(key)
        if type_ is None:
            result[key] = value
        else:
            result[_maybe_transform_key(key, type_)] = await _async_transform_recursive(value, annotation=type_)
    return result


@lru_cache(maxsize=8096)
def get_type_hints(
    obj: object,
    globalns: dict[str, object] | None = None,
    localns: Mapping[str, object] | None = None,
    include_extras: bool = False,
) -> dict[str, object]:
    hints: dict[str, object] = _get_type_hints(obj, globalns=globalns, localns=localns, include_extras=include_extras)
    return hints
