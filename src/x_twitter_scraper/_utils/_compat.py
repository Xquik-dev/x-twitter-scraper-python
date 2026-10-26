# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import types
import typing_extensions
from typing import Union, Literal, Callable
from typing_extensions import TypeIs, is_typeddict as is_typeddict

from ._datetime_parse import parse_date as parse_date, parse_datetime as parse_datetime

# typing_extensions declares these helpers to return Any, and they return a typing form or None, so these names declare object. https://typing-extensions.readthedocs.io/en/latest/#typing_extensions.get_origin
get_origin: Callable[[object], object] = typing_extensions.get_origin
get_args: Callable[[object], tuple[object, ...]] = typing_extensions.get_args

_LITERAL_TYPES: frozenset[object] = frozenset({Literal, typing_extensions.Literal})

# The constructor signature of the builtin type takes a dict[str, Any] namespace, so the bare class reads as Any. https://docs.python.org/3/library/functions.html#type
_class_type: type[type] = type


def is_class(value: object) -> TypeIs[type]:
    return isinstance(value, _class_type)


def is_union(tp: object) -> bool:
    return tp is Union or tp is types.UnionType


def is_literal_type(tp: object) -> bool:
    return get_origin(tp) in _LITERAL_TYPES
