from __future__ import annotations

import re
import ast
import importlib
from enum import Enum
from typing import get_args
from pathlib import Path
from dataclasses import dataclass

from x_twitter_scraper import resources
from x_twitter_scraper._models import BaseModel


class ResponseKind(Enum):
    EMPTY = "empty"
    BINARY = "binary"


ResponseType = type[BaseModel] | ResponseKind


@dataclass(frozen=True)
class Route:
    method: str
    template: str
    pattern: re.Pattern[str]
    response_type: ResponseType


def _resource_root() -> Path:
    return Path(resources.__file__).parent


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


def _path_template(node: ast.expr) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "path_template"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and isinstance(node.args[0].value, str)
    ):
        return node.args[0].value
    raise ValueError(f"Unsupported path expression: {ast.unparse(node)}")


def _route_pattern(template: str) -> re.Pattern[str]:
    parts = re.split(r"(\{[^{}]+\})", template)
    expression = "".join(r"[^/]+" if part.startswith("{") else re.escape(part) for part in parts)
    return re.compile(f"^{expression}$")


def _response_type(module_name: str, name: str) -> ResponseType:
    if name == "NoneType":
        return ResponseKind.EMPTY
    if name in {"BinaryAPIResponse", "AsyncBinaryAPIResponse"}:
        return ResponseKind.BINARY

    module = importlib.import_module(module_name)
    response_type = getattr(module, name, None)
    if isinstance(response_type, type) and issubclass(response_type, BaseModel):
        return response_type
    for variant in get_args(response_type):
        if isinstance(variant, type) and issubclass(variant, BaseModel):
            return variant
    raise TypeError(f"{module_name}.{name} is not a response model")


def _build_routes() -> tuple[Route, ...]:
    route_types: dict[tuple[str, str], tuple[str, ResponseType]] = {}
    root = _resource_root()
    for source_path in sorted(root.rglob("*.py")):
        relative = source_path.relative_to(root.parent)
        module_name = ".".join(("x_twitter_scraper", *relative.with_suffix("").parts))
        syntax = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
        for node in ast.walk(syntax):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            method = node.func.attr.removeprefix("_").upper()
            if method not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
                continue
            cast_node = next((keyword.value for keyword in node.keywords if keyword.arg == "cast_to"), None)
            if cast_node is None or not node.args:
                continue

            template = _path_template(node.args[0])
            name = _cast_name(cast_node)
            response_type = _response_type(module_name, name)
            key = (method, template)
            previous = route_types.get(key)
            if previous is not None and previous[0] != name:
                binary_names = {"BinaryAPIResponse", "AsyncBinaryAPIResponse"}
                if {previous[0], name} != binary_names:
                    raise ValueError(f"Conflicting response types for {method} {template}: {previous[0]} and {name}")
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
