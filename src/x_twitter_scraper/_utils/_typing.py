# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import typing
import typing_extensions
from typing import TypeVar, Iterable
from collections import abc as _c_abc
from typing_extensions import (
    TypeIs,
    Required,
    Annotated,
)

from ._utils import memoize, is_tuple
from ._compat import get_args, is_union as _is_union, get_origin


def is_annotated_type(typ: object) -> bool:
    return get_origin(typ) is Annotated


def is_list_type(typ: object) -> bool:
    return (get_origin(typ) or typ) == list


def is_sequence_type(typ: object) -> bool:
    origin = get_origin(typ) or typ
    return origin == typing_extensions.Sequence or origin == typing.Sequence or origin == _c_abc.Sequence


def is_iterable_type(typ: object) -> bool:
    origin = get_origin(typ) or typ
    return origin == Iterable or origin == _c_abc.Iterable


def is_union_type(typ: object) -> bool:
    return _is_union(get_origin(typ))


def is_required_type(typ: object) -> bool:
    return get_origin(typ) is Required


# TypeVar's constructor takes Any, so mypy reads the bare class as containing Any. A name typed as the class keeps the comparison free of it. https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-disallow-any-expr
_TYPE_VAR: type[TypeVar] = TypeVar


def is_typevar(typ: object) -> bool:
    return type(typ) == _TYPE_VAR


_TYPE_ALIAS_TYPES: tuple[type, ...] = (typing_extensions.TypeAliasType,)
if sys.version_info >= (3, 12):
    _TYPE_ALIAS_TYPES = (*_TYPE_ALIAS_TYPES, typing.TypeAliasType)


def is_type_alias_type(tp: object, /) -> TypeIs[typing_extensions.TypeAliasType]:
    return isinstance(tp, _TYPE_ALIAS_TYPES)


@memoize
def strip_annotated_type(typ: object) -> object:
    if is_required_type(typ) or is_annotated_type(typ):
        return strip_annotated_type(get_args(typ)[0])

    return typ


def extract_type_arg(typ: object, index: int) -> object:
    args = get_args(typ)
    try:
        return args[index]
    except IndexError as err:
        raise RuntimeError(f"Expected type {typ} to have a type argument at index {index} but it did not") from err


def _is_one_of(value: object, classes: tuple[type, ...]) -> bool:
    return any(value is cls for cls in classes)


def extract_type_var_from_base(
    typ: object,
    *,
    generic_bases: tuple[type, ...],
    index: int,
    failure_message: str | None = None,
) -> object:
    cls = get_origin(typ) or typ
    if _is_one_of(cls, generic_bases):
        return extract_type_arg(typ, index)

    orig_bases: object = getattr(cls, "__orig_bases__", None)
    if is_tuple(orig_bases):
        target_base_class: object = None
        for base in orig_bases:
            base_origin: object = getattr(base, "__origin__", None)
            if _is_one_of(base_origin, generic_bases):
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
