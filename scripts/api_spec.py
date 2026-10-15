# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import re
import sys
import json
from typing import Callable, Iterator, cast
from pathlib import Path
from dataclasses import dataclass
from http.client import HTTPException
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import urlopen
from collections.abc import Mapping

from tests.resource_requests import RequestCall, UnreadableRequestError, request_calls
from x_twitter_scraper._constants import DEFAULT_BASE_URL

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = "https://xquik.com/openapi.json"
HTTP_METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")
METHOD_PATTERN = "|".join(method.upper() for method in HTTP_METHODS)
PLACEHOLDER = re.compile(r"\{[^{}/]*\}")


class CheckFailure(Exception):
    def __init__(self, *lines: str) -> None:
        super().__init__("\n".join(lines))
        self.lines = lines


def unreadable_spec(source: str) -> CheckFailure:
    return CheckFailure(
        f"Could not read the API spec from {source}. "
        f"Check network access, or set XQUIK_OPENAPI_SPEC to a local copy of {DEFAULT_SPEC}."
    )


def unexpected_spec(source: str) -> CheckFailure:
    return CheckFailure(
        f"The API spec from {source} has a part the check cannot read. "
        f"Fix the spec, or set XQUIK_OPENAPI_SPEC to a valid copy of {DEFAULT_SPEC}."
    )


def operation_key(method: str, path: str) -> str:
    return f"{method} {PLACEHOLDER.sub('{}', path)}"


def as_object(value: object) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise ValueError(f"Expected an object, not {value!r}")
    return cast(Mapping[str, object], value)


def server_path(*levels: object) -> str:
    for servers in levels:
        if servers is None:
            continue
        if not isinstance(servers, list):
            raise ValueError(f"Expected a list of servers, not {servers!r}")
        if servers:
            url = as_object(cast(list[object], servers)[0]).get("url")
            if not isinstance(url, str):
                raise ValueError(f"Expected a server URL, not {url!r}")
            return urlsplit(url).path.rstrip("/")
    return ""


@dataclass(frozen=True)
class Operation:
    method: str
    path: str
    item: Mapping[str, object]
    spec: Mapping[str, object]

    @property
    def key(self) -> str:
        return operation_key(self.method, self.path)

    @property
    def label(self) -> str:
        return f"{self.method} {self.path}"


def spec_operations(document: Mapping[str, object]) -> Iterator[Operation]:
    for path, value in as_object(document.get("paths")).items():
        item = as_object(value)
        if "$ref" in item:
            raise ValueError(f"The path item of {path} is a reference")
        for method in HTTP_METHODS:
            if method in item:
                operation = as_object(item[method])
                absolute = server_path(operation.get("servers"), item.get("servers"), document.get("servers")) + path
                yield Operation(method.upper(), absolute, item, operation)


def _download(url: str) -> bytes:
    try:
        with urlopen(url, timeout=60) as response:
            content: bytes = response.read()
            return content
    except HTTPError as error:
        error.close()
        raise


def load_spec(source: str) -> Mapping[str, object]:
    try:
        content = _download(source) if source.startswith(("https://", "http://")) else Path(source).read_bytes()
        document: object = json.loads(content)
    except (OSError, ValueError, HTTPException) as error:
        raise unreadable_spec(source) from error
    try:
        return as_object(document)
    except ValueError as error:
        raise unexpected_spec(source) from error


def spec_source() -> str:
    return os.environ.get("XQUIK_OPENAPI_SPEC") or DEFAULT_SPEC


def request_key(call: RequestCall) -> str:
    return operation_key(call.method, urlsplit(DEFAULT_BASE_URL).path.rstrip("/") + call.template)


def read_request_calls(root: Path, resources: Path) -> list[RequestCall]:
    try:
        return list(request_calls(resources))
    except UnreadableRequestError as error:
        raise CheckFailure(
            f"{error.source.relative_to(root)}:{error.line} {error.reason}.",
            "Fix that line. Write each request path as a string or a path_template call, and pass cast_to.",
        ) from error


@dataclass(frozen=True)
class ReviewedList:
    file: str
    entry: str
    section: str
    pattern: re.Pattern[str]
    example: str
    key: Callable[[str], str]

    def _invalid(self, problem: str) -> CheckFailure:
        return CheckFailure(
            f"{self.file} is not valid. {problem}",
            f"Fix {self.file} in the format CONTRIBUTING.md shows under {self.section}.",
        )

    def read(self, root: Path) -> dict[str, str]:
        try:
            groups: object = json.loads((root / self.file).read_bytes())
        except OSError as error:
            raise self._invalid("The file cannot be read.") from error
        except json.JSONDecodeError as error:
            raise self._invalid(f"Line {error.lineno} column {error.colno} breaks the JSON syntax.") from error
        except ValueError as error:
            raise self._invalid("Its bytes are not valid text.") from error
        if not isinstance(groups, list):
            raise self._invalid(f"It must be a list of groups, each with a reason and {self.entry}s.")
        entries: dict[str, str] = {}
        for number, group in enumerate(cast(list[object], groups), 1):
            fields: Mapping[str, object] = cast(Mapping[str, object], group) if isinstance(group, Mapping) else {}
            if set(fields) != {"reason", f"{self.entry}s"}:
                raise self._invalid(f"Group {number} must hold a reason and {self.entry}s, and nothing else.")
            reason, listed = fields["reason"], fields[f"{self.entry}s"]
            if not isinstance(reason, str) or not reason.strip():
                raise self._invalid(f"Group {number} needs a non-empty reason.")
            if not isinstance(listed, list) or not listed:
                raise self._invalid(f"Group {number} needs at least 1 {self.entry}.")
            for entry in cast(list[object], listed):
                if not isinstance(entry, str) or not self.pattern.fullmatch(entry):
                    raise self._invalid(f"Group {number} lists {json.dumps(entry)}. {self.example}")
                key = self.key(entry)
                if key in entries:
                    raise self._invalid(f"{entry} appears more than once.")
                entries[key] = entry
        return entries


def run(check: Callable[[], str]) -> int:
    try:
        print(check())
    except CheckFailure as failure:
        print("\n".join(failure.lines), file=sys.stderr)
        return 1
    return 0
