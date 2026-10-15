# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import re
import ast
import importlib
from enum import Enum
from typing import get_args
from pathlib import Path
from dataclasses import dataclass

from x_twitter_scraper import resources
from tests.resource_requests import request_calls
from x_twitter_scraper._models import BaseModel


class ResponseKind(Enum):
    EMPTY = "empty"
    BINARY = "binary"
    JSON_OBJECT = "json_object"


ResponseType = type[BaseModel] | ResponseKind


@dataclass(frozen=True)
class Route:
    method: str
    template: str
    pattern: re.Pattern[str]
    response_type: ResponseType


def _cast_name(node: ast.expr) -> str:
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name) or node.func.id != "cast":
            raise ValueError(f"Unsupported cast expression: {ast.unparse(node)}")
        if len(node.args) != 2:
            raise ValueError(f"Unsupported cast argument count: {ast.unparse(node)}")
        node = node.args[1]
    if not isinstance(node, ast.Name):
        raise ValueError(f"Unsupported response type: {ast.unparse(node)}")
    return node.id


def _route_pattern(template: str) -> re.Pattern[str]:
    parts = re.split(r"(\{[^{}]+\})", template)
    expression = "".join(r"[^/]+" if part.startswith("{") else re.escape(part) for part in parts)
    return re.compile(f"^{expression}$")


def _response_type(module_name: str, name: str) -> ResponseType:
    if name == "NoneType":
        return ResponseKind.EMPTY
    if name in {"BinaryAPIResponse", "AsyncBinaryAPIResponse"}:
        return ResponseKind.BINARY
    if name == "object":
        return ResponseKind.JSON_OBJECT

    module = importlib.import_module(module_name)
    pending = [getattr(module, name, None)]
    while pending:
        variant = pending.pop(0)
        if isinstance(variant, type) and issubclass(variant, BaseModel):
            return variant
        pending.extend(get_args(variant))
    raise TypeError(f"{module_name}.{name} is not a response model")


def _build_routes() -> tuple[Route, ...]:
    route_types: dict[tuple[str, str], tuple[str, ResponseType]] = {}
    root = Path(resources.__file__).parent
    for call in request_calls(root):
        relative = call.source.relative_to(root.parent)
        module_name = ".".join(("x_twitter_scraper", *relative.with_suffix("").parts))
        name = _cast_name(call.cast_to)
        response_type = _response_type(module_name, name)
        key = (call.method, call.template)
        previous = route_types.get(key)
        if previous is not None and previous[0] != name:
            binary_names = {"BinaryAPIResponse", "AsyncBinaryAPIResponse"}
            if {previous[0], name} != binary_names:
                raise ValueError(
                    f"Conflicting response types for {call.method} {call.template}: {previous[0]} and {name}"
                )
            continue
        route_types[key] = (name, response_type)

    return tuple(
        Route(
            method=method,
            template=template,
            pattern=_route_pattern(template),
            response_type=response_type,
        )
        for (method, template), (_, response_type) in sorted(route_types.items())
    )


ROUTES = _build_routes()
