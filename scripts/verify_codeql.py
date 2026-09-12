# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import json
from typing import cast
from pathlib import Path
from collections.abc import Mapping


def _mapping(value: object) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise ValueError("CodeQL metadata must be an object.")
    return cast(Mapping[str, object], value)


def _objects(value: object) -> list[Mapping[str, object]]:
    if not isinstance(value, list) or not value:
        raise ValueError("CodeQL analysis metadata is missing.")
    return [_mapping(item) for item in cast(list[object], value)]


def validate(report: object) -> None:
    data = _mapping(report)
    runs = _objects(data.get("runs"))
    if data.get("version") != "2.1.0" or len(runs) != 1:
        raise ValueError("Expected one SARIF 2.1.0 run.")
    run = runs[0]
    if run.get("results") != []:
        raise ValueError("CodeQL findings or incomplete analysis prevent release.")
    extracted = 0
    for invocation in _objects(run.get("invocations")):
        if invocation.get("executionSuccessful") is not True:
            raise ValueError("CodeQL invocation failed.")
        for notification in _objects(invocation.get("toolExecutionNotifications")):
            if notification.get("level") not in ("none", "note"):
                raise ValueError("CodeQL diagnostic requires review.")
            descriptor = _mapping(notification.get("descriptor"))
            extracted += descriptor.get("id") == "py/diagnostics/successfully-extracted-files"
    if not extracted:
        raise ValueError("CodeQL did not confirm extracted Python files.")
    print(f"CodeQL completed without findings; extracted Python entries: {extracted}")


if __name__ == "__main__":
    validate(json.loads(Path(sys.argv[1]).read_text()))
