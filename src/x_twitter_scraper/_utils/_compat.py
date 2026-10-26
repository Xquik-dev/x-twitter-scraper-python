# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import types
import typing_extensions
from typing import Union, Literal, Callable
from typing_extensions import is_typeddict as is_typeddict

from ._datetime_parse import parse_date as parse_date, parse_datetime as parse_datetime

# typing_extensions declares these helpers to return Any, and they return a typing form or None, so these names declare object. https://typing-extensions.readthedocs.io/en/latest/#typing_extensions.get_origin
get_origin: Callable[[object], object] = typing_extensions.get_origin
get_args: Callable[[object], tuple[object, ...]] = typing_extensions.get_args

_LITERAL_TYPES: frozenset[object] = frozenset({Literal, typing_extensions.Literal})


def is_union(tp: object) -> bool:
    return tp is Union or tp is types.UnionType


def is_literal_type(tp: object) -> bool:
    return get_origin(tp) in _LITERAL_TYPES
