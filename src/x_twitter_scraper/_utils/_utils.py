# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import re
import inspect
import functools
from typing import (
    Tuple,
    Mapping,
    TypeVar,
    Callable,
    Iterable,
    Sequence,
    cast,
    overload,
)
from pathlib import Path
from datetime import date, datetime
from typing_extensions import ParamSpec, TypeGuard, get_args

import httpx
import sniffio

from .._types import Omit, NotGiven, FileTypes, ArrayFormat, HeadersLike

_T = TypeVar("_T")
_P = ParamSpec("_P")
_TupleT = TypeVar("_TupleT", bound=Tuple[object, ...])
_MappingT = TypeVar("_MappingT", bound=Mapping[str, object])


def flatten(t: Iterable[Iterable[_T]]) -> list[_T]:
    return [item for sublist in t for item in sublist]


def extract_files(
    query: Mapping[str, object],
    *,
    paths: Sequence[Sequence[str]],
    array_format: ArrayFormat = "brackets",
) -> list[tuple[str, FileTypes]]:
    files: list[tuple[str, FileTypes]] = []
    for path in paths:
        files.extend(_extract_items(query, path, index=0, flattened_key=None, array_format=array_format))
    return files


def _array_suffix(array_format: ArrayFormat, array_index: int) -> str:
    if array_format == "brackets":
        return "[]"
    if array_format == "indices":
        return f"[{array_index}]"
    if array_format == "repeat" or array_format == "comma":
        return ""
    raise NotImplementedError(
        f"Unknown array_format value: {array_format}, choose from {', '.join(get_args(ArrayFormat))}"
    )


def _extract_items(
    obj: object,
    path: Sequence[str],
    *,
    index: int,
    flattened_key: str | None,
    array_format: ArrayFormat,
) -> list[tuple[str, FileTypes]]:
    try:
        key = path[index]
    except IndexError:
        if not is_given(obj):
            return []

        from .._files import assert_is_file_content

        assert flattened_key is not None

        if is_list(obj):
            files: list[tuple[str, FileTypes]] = []
            for array_index, entry in enumerate(obj):
                suffix = _array_suffix(array_format, array_index)
                emitted_key = (flattened_key + suffix) if flattened_key else suffix
                assert_is_file_content(entry, key=emitted_key)
                files.append((emitted_key, cast(FileTypes, entry)))
            return files

        assert_is_file_content(obj, key=flattened_key)
        return [(flattened_key, cast(FileTypes, obj))]

    index += 1
    if is_dict(obj):
        try:
            if all(p == "<array>" for p in path[index:]):
                item = obj.pop(key)
            else:
                item = obj[key]
        except KeyError:
            return []
        if flattened_key is None:
            flattened_key = key
        else:
            flattened_key += f"[{key}]"
        return _extract_items(
            item,
            path,
            index=index,
            flattened_key=flattened_key,
            array_format=array_format,
        )
    elif is_list(obj):
        if key != "<array>":
            return []

        return [
            file
            for array_index, item in enumerate(obj)
            for file in _extract_items(
                item,
                path,
                index=index,
                flattened_key=(flattened_key if flattened_key is not None else "")
                + _array_suffix(array_format, array_index),
                array_format=array_format,
            )
        ]

    return []


def is_given(obj: _T | NotGiven | Omit) -> TypeGuard[_T]:
    return not isinstance(obj, NotGiven) and not isinstance(obj, Omit)


def is_tuple(obj: object) -> TypeGuard[tuple[object, ...]]:
    return isinstance(obj, tuple)


def is_tuple_t(obj: _TupleT | object) -> TypeGuard[_TupleT]:
    return isinstance(obj, tuple)


def is_sequence(obj: object) -> TypeGuard[Sequence[object]]:
    return isinstance(obj, Sequence)


def is_mapping(obj: object) -> TypeGuard[Mapping[str, object]]:
    return isinstance(obj, Mapping)


def is_mapping_t(obj: _MappingT | object) -> TypeGuard[_MappingT]:
    return isinstance(obj, Mapping)


def is_dict(obj: object) -> TypeGuard[dict[object, object]]:
    return isinstance(obj, dict)


def is_list(obj: object) -> TypeGuard[list[object]]:
    return isinstance(obj, list)


def is_iterable(obj: object) -> TypeGuard[Iterable[object]]:
    return isinstance(obj, Iterable)


def human_join(seq: Sequence[str], *, delim: str = ", ", final: str = "or") -> str:
    if len(seq) < 2:
        return seq[0] if seq else ""
    return delim.join(seq[:-1]) + f" {final} {seq[-1]}"


def quote(string: str) -> str:
    return f"'{string}'"


def required_args(*variants: Sequence[str]) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    def inner(func: Callable[_P, _T]) -> Callable[_P, _T]:
        params = inspect.signature(func).parameters
        positional = [
            name
            for name, param in params.items()
            if param.kind
            in {
                param.POSITIONAL_ONLY,
                param.POSITIONAL_OR_KEYWORD,
            }
        ]

        @functools.wraps(func)
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _T:
            if len(args) > len(positional):
                raise TypeError(
                    f"{getattr(func, '__name__', type(func).__name__)}() takes {len(positional)} argument(s) but {len(args)} were given"
                ) from None
            given_params = set(positional[: len(args)]) | kwargs.keys()

            if not any(all(param in given_params for param in variant) for variant in variants):
                if len(variants) > 1:
                    variations = human_join(
                        ["(" + human_join([quote(arg) for arg in variant], final="and") + ")" for variant in variants]
                    )
                    msg = f"Missing required arguments; Expected either {variations} arguments to be given"
                else:
                    assert len(variants) > 0

                    missing = list(set(variants[0]) - given_params)
                    if len(missing) > 1:
                        msg = f"Missing required arguments: {human_join([quote(arg) for arg in missing])}"
                    else:
                        msg = f"Missing required argument: {quote(missing[0])}"
                raise TypeError(msg)
            return func(*args, **kwargs)

        return wrapper

    return inner


_K = TypeVar("_K")
_V = TypeVar("_V")


@overload
def strip_not_given(obj: None) -> None: ...


@overload
def strip_not_given(obj: Mapping[_K, _V | NotGiven]) -> dict[_K, _V]: ...


@overload
def strip_not_given(obj: object) -> object: ...


def strip_not_given(obj: object | None) -> object:
    if obj is None:
        return None

    if not is_mapping(obj):
        return obj

    return {key: value for key, value in obj.items() if not isinstance(value, NotGiven)}


def coerce_integer(val: str) -> int:
    return int(val, base=10)


def coerce_float(val: str) -> float:
    return float(val)


def coerce_boolean(val: str) -> bool:
    return val == "true" or val == "1" or val == "on"


def maybe_coerce_integer(val: str | None) -> int | None:
    if val is None:
        return None
    return coerce_integer(val)


def maybe_coerce_float(val: str | None) -> float | None:
    if val is None:
        return None
    return coerce_float(val)


def maybe_coerce_boolean(val: str | None) -> bool | None:
    if val is None:
        return None
    return coerce_boolean(val)


def removeprefix(string: str, prefix: str) -> str:
    return string.removeprefix(prefix)


def removesuffix(string: str, suffix: str) -> str:
    return string.removesuffix(suffix)


def file_from_path(path: str) -> FileTypes:
    contents = Path(path).read_bytes()
    file_name = os.path.basename(path)
    return (file_name, contents)


def _upper_after_separator(match: re.Match[str]) -> str:
    # Match.group returns str | Any, and both groups of the header pattern always match a string. https://docs.python.org/3/library/re.html#re.Match.group
    separator: str = match.group(1)
    letter: str = match.group(2)
    return separator + letter.upper()


def _find_mapping_header(headers: object, lower_header: str) -> str | None:
    if is_mapping(headers):
        for k, v in headers.items():
            if k.lower() == lower_header and isinstance(v, str):
                return v
    return None


def get_header(headers: httpx.Headers, name: str) -> str | None:
    return headers[name] if name in headers else None


def get_required_header(headers: HeadersLike, header: str) -> str:
    lower_header = header.lower()
    mapped = _find_mapping_header(headers, lower_header)
    if mapped is not None:
        return mapped

    intercaps_header = re.sub(r"([^\w])(\w)", _upper_after_separator, header.capitalize())

    for normalized_header in [header, lower_header, header.upper(), intercaps_header]:
        value = headers.get(normalized_header)
        if value:
            return value

    raise ValueError(f"Could not find {header} header")


def get_async_library() -> str:
    try:
        return sniffio.current_async_library()
    except Exception:
        return "false"


def memoize(func: Callable[_P, _T]) -> Callable[_P, _T]:
    cache: dict[tuple[tuple[object, ...], tuple[tuple[str, object], ...]], _T] = {}

    @functools.wraps(func)
    def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        key = (args, tuple(kwargs.items()))
        try:
            return cache[key]
        except KeyError:
            result = cache[key] = func(*args, **kwargs)
            return result

    return wrapper


def json_safe(data: object) -> object:
    if is_mapping(data):
        return {json_safe(key): json_safe(value) for key, value in data.items()}

    if is_iterable(data) and not isinstance(data, (str, bytes, bytearray)):
        return [json_safe(item) for item in data]

    if isinstance(data, (datetime, date)):
        return data.isoformat()

    return data
