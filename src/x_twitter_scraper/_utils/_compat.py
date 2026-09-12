# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import types
import typing_extensions
from typing import Any, Type, Union, Literal
from typing_extensions import get_args as get_args, get_origin as get_origin, is_typeddict as is_typeddict

from ._datetime_parse import parse_date as parse_date, parse_datetime as parse_datetime

_LITERAL_TYPES: frozenset[object] = frozenset({Literal, typing_extensions.Literal})


def is_union(tp: object) -> bool:
    return tp is Union or tp is types.UnionType


def is_literal_type(tp: Type[Any]) -> bool:
    return get_origin(tp) in _LITERAL_TYPES
