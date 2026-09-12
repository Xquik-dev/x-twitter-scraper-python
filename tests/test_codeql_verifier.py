# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import copy
from typing import Any

import pytest

from scripts.verify_codeql import validate

REPORT: dict[str, Any] = {
    "version": "2.1.0",
    "runs": [
        {
            "results": [],
            "invocations": [
                {
                    "executionSuccessful": True,
                    "toolExecutionNotifications": [
                        {
                            "level": "none",
                            "descriptor": {"id": "py/diagnostics/successfully-extracted-files"},
                        }
                    ],
                }
            ],
        }
    ],
}


def test_complete_codeql_report() -> None:
    assert validate(REPORT) is None


@pytest.mark.parametrize("report", [None, [], {}, {"version": "2.1.0", "runs": [None]}])
def test_invalid_codeql_structure(report: object) -> None:
    with pytest.raises(ValueError):
        validate(report)


@pytest.mark.parametrize(
    "path,value",
    [
        (("version",), "2.0.0"),
        (("runs",), [REPORT["runs"][0], REPORT["runs"][0]]),
        (("runs", 0, "results"), [{"ruleId": "py/unsafe-deserialization"}]),
        (("runs", 0, "results"), None),
        (("runs", 0, "invocations"), []),
        (("runs", 0, "invocations", 0, "executionSuccessful"), False),
        (("runs", 0, "invocations", 0, "executionSuccessful"), 1),
        (("runs", 0, "invocations", 0, "toolExecutionNotifications"), []),
        (("runs", 0, "invocations", 0, "toolExecutionNotifications", 0, "level"), "warning"),
        (("runs", 0, "invocations", 0, "toolExecutionNotifications", 0, "level"), "error"),
        (("runs", 0, "invocations", 0, "toolExecutionNotifications", 0, "level"), None),
        (("runs", 0, "invocations", 0, "toolExecutionNotifications", 0, "descriptor"), {}),
    ],
)
def test_incomplete_or_failed_codeql_report(path: tuple[str | int, ...], value: object) -> None:
    report = copy.deepcopy(REPORT)
    target: Any = report
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value
    with pytest.raises(ValueError):
        validate(report)
