# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import copy
from pathlib import Path

import pytest

from tests.utils import json_dumps
from scripts.verify_codeql import main, validate
from x_twitter_scraper._utils import is_dict, is_list

RUN: dict[str, object] = {
    "tool": {"driver": {"notifications": [{"id": "py/diagnostics/extraction-warnings"}]}},
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
REPORT: dict[str, object] = {"version": "2.1.0", "runs": [RUN]}


def resolve(document: object, path: tuple[str | int, ...]) -> object:
    for key in path:
        if isinstance(key, int):
            assert is_list(document)
            document = document[key]
        else:
            assert is_dict(document)
            document = document[key]
    return document


def test_complete_codeql_report() -> None:
    validate(REPORT)


@pytest.mark.parametrize("report", [None, [], {}, {"version": "2.1.0", "runs": [None]}])
def test_invalid_codeql_structure(report: object) -> None:
    with pytest.raises(ValueError):
        validate(report)


@pytest.mark.parametrize(
    "path,value",
    [
        (("version",), "2.0.0"),
        (("runs",), [RUN, RUN]),
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
        (("runs", 0, "tool", "driver", "notifications"), [{"id": "py/diagnostics/successfully-extracted-files"}]),
        (("runs", 0, "tool"), None),
    ],
)
def test_incomplete_or_failed_codeql_report(path: tuple[str | int, ...], value: object) -> None:
    report = copy.deepcopy(REPORT)
    target = resolve(report, path[:-1])
    key = path[-1]
    if isinstance(key, int):
        assert is_list(target)
        target[key] = value
    else:
        assert is_dict(target)
        target[key] = value
    with pytest.raises(ValueError):
        validate(report)


def with_notifications(*notifications: dict[str, object]) -> dict[str, object]:
    report = copy.deepcopy(REPORT)
    existing = resolve(report, ("runs", 0, "invocations", 0, "toolExecutionNotifications"))
    assert is_list(existing)
    existing.extend(notifications)
    return report


def unread(file: str, line: int) -> dict[str, object]:
    return {
        "locations": [{"physicalLocation": {"artifactLocation": {"uri": file}, "region": {"startLine": line}}}],
        "message": {"text": f"Extraction failed in {file} with error Syntax Error"},
        "descriptor": {"id": "py/diagnostics/extraction-warnings"},
    }


SYNTAX_ERROR: dict[str, object] = {
    "locations": [{"physicalLocation": {"artifactLocation": {"uri": "src/x_twitter_scraper/_client.py"}}}],
    "message": {"text": "A parse error occurred while processing `src/x_twitter_scraper/_client.py`."},
    "descriptor": {"id": "py/diagnostics/syntax-error"},
}


def test_each_file_that_codeql_could_not_parse_is_named_once() -> None:
    report = with_notifications(
        unread("src/x_twitter_scraper/_client.py", 12),
        SYNTAX_ERROR,
        unread("src/x_twitter_scraper/_client.py", 12),
        unread("src/x_twitter_scraper/_files.py", 3),
    )
    with pytest.raises(ValueError) as error:
        validate(report)
    assert str(error.value) == (
        "CodeQL could not parse src/x_twitter_scraper/_client.py at line 12 and src/x_twitter_scraper/_files.py "
        "at line 3, so the scan is incomplete. Rewrite that syntax so CodeQL parses it, then rerun bin/check-local."
    )


def test_another_diagnostic_above_note_level_is_named_with_its_message() -> None:
    with pytest.raises(ValueError) as error:
        validate(with_notifications(SYNTAX_ERROR))
    assert str(error.value) == (
        'CodeQL diagnostic py/diagnostics/syntax-error needs review. It said "A parse error occurred while '
        'processing `src/x_twitter_scraper/_client.py`.". Fix the cause, then rerun bin/check-local.'
    )


def test_main_passes_a_complete_report(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (tmp_path / "report.sarif").write_text(json_dumps(REPORT))
    assert main([str(tmp_path / "report.sarif")]) == 0
    assert capsys.readouterr().out == "CodeQL completed without findings and extracted 1 Python entries.\n"


def test_main_prints_1_line_for_a_failed_report(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (tmp_path / "report.sarif").write_text(json_dumps(with_notifications(unread("src/x_twitter_scraper/_files.py", 3))))
    assert main([str(tmp_path / "report.sarif")]) == 1
    assert capsys.readouterr().err == (
        "CodeQL could not parse src/x_twitter_scraper/_files.py at line 3, so the scan is incomplete. "
        "Rewrite that syntax so CodeQL parses it, then rerun bin/check-local.\n"
    )
