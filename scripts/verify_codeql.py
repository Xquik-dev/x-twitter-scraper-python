# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import json
from typing import Callable, cast
from pathlib import Path
from collections.abc import Mapping

# json.loads declares Any, and without an object hook it returns only JSON values. https://docs.python.org/3/library/json.html#json-to-py-table
load_json: Callable[[str], object] = json.loads

EXTRACTION_DIAGNOSTIC = "py/diagnostics/extraction-warnings"


def _mapping(value: object) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise ValueError("CodeQL metadata must be an object.")
    return cast(Mapping[str, object], value)


def _objects(value: object) -> list[Mapping[str, object]]:
    if not isinstance(value, list) or not value:
        raise ValueError("CodeQL analysis metadata is missing.")
    return [_mapping(item) for item in cast(list[object], value)]


def _diagnostic(notification: Mapping[str, object]) -> object:
    return _mapping(notification.get("descriptor")).get("id")


def _place(notification: Mapping[str, object]) -> str:
    location = _mapping(_objects(notification.get("locations"))[0].get("physicalLocation"))
    file = _mapping(location.get("artifactLocation")).get("uri")
    line = _mapping(location.get("region")).get("startLine")
    return f"{file} at line {line}"


def validate(report: object) -> None:
    data = _mapping(report)
    runs = _objects(data.get("runs"))
    if data.get("version") != "2.1.0" or len(runs) != 1:
        raise ValueError("Expected one SARIF 2.1.0 run.")
    run = runs[0]
    if run.get("results") != []:
        raise ValueError("CodeQL findings or incomplete analysis prevent release.")
    scanner = _mapping(_mapping(run.get("tool")).get("driver"))
    if EXTRACTION_DIAGNOSTIC not in [query.get("id") for query in _objects(scanner.get("notifications"))]:
        raise ValueError(
            f"The CodeQL scan lacks {EXTRACTION_DIAGNOSTIC}, so it cannot show that it read every file. "
            "Make the suite in scripts/codeql-security run that diagnostic query."
        )
    invocations = _objects(run.get("invocations"))
    if any(invocation.get("executionSuccessful") is not True for invocation in invocations):
        raise ValueError("CodeQL invocation failed.")
    notifications = [
        notification
        for invocation in invocations
        for notification in _objects(invocation.get("toolExecutionNotifications"))
    ]
    unread = [_place(n) for n in notifications if _diagnostic(n) == EXTRACTION_DIAGNOSTIC]
    if unread:
        raise ValueError(
            f"CodeQL could not parse {' and '.join(dict.fromkeys(unread))}, so the scan is incomplete. "
            "Rewrite that syntax so CodeQL parses it, then rerun bin/check-local."
        )
    for notification in notifications:
        if notification.get("level") not in ("none", "note"):
            said = _mapping(notification.get("message")).get("text")
            raise ValueError(
                f'CodeQL diagnostic {_diagnostic(notification)} needs review. It said "{said}". '
                "Fix the cause, then rerun bin/check-local."
            )
    extracted = [_diagnostic(n) for n in notifications].count("py/diagnostics/successfully-extracted-files")
    if not extracted:
        raise ValueError("CodeQL did not confirm extracted Python files.")
    print(f"CodeQL completed without findings and extracted {extracted} Python entries.")


def main(arguments: list[str]) -> int:
    try:
        validate(load_json(Path(arguments[0]).read_text()))
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
