# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import ast
from typing import Iterator
from pathlib import Path
from dataclasses import dataclass

REQUEST_METHODS = {"_get": "GET", "_post": "POST", "_put": "PUT", "_patch": "PATCH", "_delete": "DELETE"}


class UnreadableRequestError(ValueError):
    def __init__(self, source: Path, line: int, reason: str) -> None:
        super().__init__(f"{source}:{line} {reason}.")
        self.source = source
        self.line = line
        self.reason = reason


@dataclass(frozen=True)
class RequestCall:
    method: str
    template: str
    cast_to: ast.expr
    source: Path
    call: ast.Call


def keyword(call: ast.Call, name: str) -> ast.expr | None:
    return next((item.value for item in call.keywords if item.arg == name), None)


def _path_template(node: ast.expr) -> str | None:
    match node:
        case ast.Constant(value=str() as value):
            return value
        case ast.Call(func=ast.Name(id="path_template"), args=[ast.Constant(value=str() as value), *_]):
            return value
        case _:
            return None


def request_calls(resources: Path) -> Iterator[RequestCall]:
    for source in sorted(resources.rglob("*.py")):
        try:
            syntax = ast.parse(source.read_bytes(), filename=str(source))
        except SyntaxError as error:
            raise UnreadableRequestError(source, error.lineno or 1, "is not valid Python") from error
        for node in ast.walk(syntax):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
                continue
            method = REQUEST_METHODS.get(node.func.attr)
            if method is None:
                continue
            template = _path_template(node.args[0]) if node.args else None
            cast_to = keyword(node, "cast_to")
            if template is None or cast_to is None:
                raise UnreadableRequestError(source, node.lineno, "has a request whose path or cast_to cannot be read")
            yield RequestCall(method, template, cast_to, source, node)
