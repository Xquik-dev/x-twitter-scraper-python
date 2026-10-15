# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import re
import sys
import json
from typing import cast
from pathlib import Path
from http.client import HTTPException
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import urlopen
from collections.abc import Mapping

from tests.resource_requests import UnreadableRequestError, request_calls
from x_twitter_scraper._constants import DEFAULT_BASE_URL

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SPEC = "https://xquik.com/openapi.json"
EXCLUSIONS = "excluded-operations.json"
RESOURCES = Path("src/x_twitter_scraper/resources")
HTTP_METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")
OPERATION = re.compile(f"({'|'.join(method.upper() for method in HTTP_METHODS)}) /\\S*")
PLACEHOLDER = re.compile(r"\{[^{}/]*\}")
SPEC_FAILURE = (
    "Could not read the API spec from {source}. "
    f"Check network access, or set XQUIK_OPENAPI_SPEC to a local copy of {DEFAULT_SPEC}."
)


class CheckFailure(Exception):
    def __init__(self, *lines: str) -> None:
        super().__init__("\n".join(lines))
        self.lines = lines


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


def _spec_operations(spec: Mapping[str, object]) -> dict[str, str]:
    operations: dict[str, str] = {}
    for path, item in as_object(spec.get("paths")).items():
        path_item = as_object(item)
        if "$ref" in path_item:
            raise ValueError(f"The path item of {path} is a reference")
        for method in HTTP_METHODS:
            if method not in path_item:
                continue
            operation = as_object(path_item[method])
            absolute = server_path(operation.get("servers"), path_item.get("servers"), spec.get("servers")) + path
            operation_id = operation.get("operationId")
            label = f"{method.upper()} {absolute}" + (f" ({operation_id})" if isinstance(operation_id, str) else "")
            operations[operation_key(method.upper(), absolute)] = label
    return operations


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
        return as_object(json.loads(content))
    except (OSError, ValueError, HTTPException) as error:
        raise CheckFailure(SPEC_FAILURE.format(source=source)) from error


def read_spec(source: str) -> dict[str, str]:
    spec = load_spec(source)
    try:
        return _spec_operations(spec)
    except ValueError as error:
        raise CheckFailure(SPEC_FAILURE.format(source=source)) from error


def sdk_operations(root: Path) -> set[str]:
    base_path = urlsplit(DEFAULT_BASE_URL).path.rstrip("/")
    try:
        return {operation_key(call.method, base_path + call.template) for call in request_calls(root / RESOURCES)}
    except UnreadableRequestError as error:
        raise CheckFailure(
            f"{error.source.relative_to(root)}:{error.line} {error.reason}.",
            "Fix that line. Write each request path as a string or a path_template call, and pass cast_to.",
        ) from error


def _invalid(problem: str) -> CheckFailure:
    return CheckFailure(
        f"{EXCLUSIONS} is not valid. {problem}",
        f"Fix {EXCLUSIONS} in the format CONTRIBUTING.md shows under API coverage.",
    )


def read_exclusions(root: Path) -> dict[str, str]:
    try:
        groups: object = json.loads((root / EXCLUSIONS).read_bytes())
    except OSError as error:
        raise _invalid("The file cannot be read.") from error
    except json.JSONDecodeError as error:
        raise _invalid(f"Line {error.lineno} column {error.colno} breaks the JSON syntax.") from error
    except ValueError as error:
        raise _invalid("Its bytes are not valid text.") from error
    if not isinstance(groups, list):
        raise _invalid("It must be a list of groups, each with a reason and operations.")
    operations: dict[str, str] = {}
    for number, group in enumerate(cast(list[object], groups), 1):
        fields: Mapping[str, object] = cast(Mapping[str, object], group) if isinstance(group, Mapping) else {}
        if set(fields) != {"reason", "operations"}:
            raise _invalid(f"Group {number} must hold a reason and operations, and nothing else.")
        reason, listed = fields["reason"], fields["operations"]
        if not isinstance(reason, str) or not reason.strip():
            raise _invalid(f"Group {number} needs a non-empty reason.")
        if not isinstance(listed, list) or not listed:
            raise _invalid(f"Group {number} needs at least 1 operation.")
        for operation in cast(list[object], listed):
            if not isinstance(operation, str) or not OPERATION.fullmatch(operation):
                raise _invalid(
                    f"Group {number} lists {json.dumps(operation)}. "
                    "Write an upper case method, a space and a path, such as GET /api/v1/x/trends."
                )
            key = operation_key(*operation.split(" ", 1))
            if key in operations:
                raise _invalid(f"{operation} appears more than once.")
            operations[key] = operation
    return operations


def check(spec_source: str, root: Path) -> str:
    api = read_spec(spec_source)
    excluded = read_exclusions(root)
    sdk = sdk_operations(root)
    missing = [
        f"{label} is in the API but not in the SDK."
        for key, label in sorted(api.items(), key=lambda entry: entry[1])
        if key not in sdk and key not in excluded
    ]
    stale = [
        f"{EXCLUSIONS} lists {operation}, which the API no longer has. Remove it."
        if key not in api
        else f"{EXCLUSIONS} lists {operation}, which the SDK already implements. Remove it."
        for key, operation in excluded.items()
        if key not in api or key in sdk
    ]
    if missing:
        raise CheckFailure(
            *missing,
            *stale,
            f"Add each operation above to the SDK, or list it in {EXCLUSIONS} with a reason.",
        )
    if stale:
        raise CheckFailure(*stale, f"Remove each operation above from {EXCLUSIONS}.")
    covered = len(api.keys() & sdk)
    return (
        f"The SDK covers {covered} of {len(api)} API operations, and {EXCLUSIONS} lists the other {len(api) - covered}."
    )


def main(root: Path = ROOT) -> int:
    try:
        print(check(os.environ.get("XQUIK_OPENAPI_SPEC") or DEFAULT_SPEC, root))
    except CheckFailure as failure:
        print("\n".join(failure.lines), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
