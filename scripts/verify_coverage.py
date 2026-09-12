#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import json
from typing import cast
from pathlib import Path
from fractions import Fraction
from collections.abc import Mapping

import pytest
from _pytest.terminal import TerminalReporter

METRICS = (
    ("Statement", "covered_lines", "num_statements"),
    ("Branch", "covered_branches", "num_branches"),
)


def _integer(mapping: Mapping[str, object], key: str) -> int:
    value = mapping.get(key)
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"Coverage report field {key!r} must be an integer. Regenerate coverage.")
    return value


def verify_coverage(report_path: Path) -> bool:
    report = _mapping(json.loads(report_path.read_text(encoding="utf-8")), "root must be an object")
    totals = _mapping(report.get("totals"), "lacks totals")

    for label, covered_key, total_key in METRICS:
        covered = _integer(totals, covered_key)
        total = _integer(totals, total_key)
        if total <= 0:
            raise ValueError("Coverage report has no measurable items. Regenerate coverage.")
        if not 0 <= covered <= total:
            raise ValueError(f"Coverage report field {covered_key!r} is outside its total. Regenerate coverage.")
        percent = covered * 100 / total
        print(f"{label} coverage: {covered}/{total} ({percent:.2f}%)")
    return True


def _mapping(value: object, message: str = "requires an object") -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise ValueError(f"Coverage report {message}. Regenerate coverage.")
    return cast(Mapping[str, object], value)


def coverage_metrics(report_path: Path) -> dict[str, Fraction]:
    report = _mapping(json.loads(report_path.read_text(encoding="utf-8")))
    totals = _mapping(report.get("totals"))
    counts = {name: (_integer(totals, covered), _integer(totals, total)) for name, covered, total in METRICS}
    covered_functions = total_functions = declarations = 0
    files = _mapping(report.get("files"))
    if not files:
        raise ValueError("Coverage report lacks files. Regenerate coverage.")
    for file in files.values():
        for name, function in _mapping(_mapping(file).get("functions")).items():
            if not name:
                continue
            summary = _mapping(_mapping(function).get("summary"))
            covered = _integer(summary, "covered_lines")
            total = _integer(summary, "num_statements")
            if not 0 <= covered <= total:
                raise ValueError("Function coverage is outside its total. Regenerate coverage.")
            declarations += total == 0
            total_functions += total > 0
            covered_functions += covered > 0
    counts["Function"] = (covered_functions, total_functions)
    counts["Line"] = counts["Statement"]
    print(f"Function declarations without executable statements: {declarations}")
    metrics: dict[str, Fraction] = {}
    for name, (covered, total) in counts.items():
        if total <= 0 or not 0 <= covered <= total:
            raise ValueError(f"Invalid {name} coverage counts. Regenerate coverage.")
        metrics[name] = Fraction(covered * 100, total)
    return metrics


def verify_non_regression(report_path: Path, parent_path: Path) -> bool:
    metadata = [
        _mapping(_mapping(json.loads(path.read_text(encoding="utf-8"))).get("meta"))
        for path in (report_path, parent_path)
    ]
    if any(meta.get("branch_coverage") is not True or meta.get("format") != 3 for meta in metadata):
        raise ValueError("Coverage requires format 3 with branch measurements. Regenerate both reports.")
    version = metadata[0].get("version")
    if not isinstance(version, str) or not version or version != metadata[1].get("version"):
        raise ValueError("Coverage provider versions differ or are missing. Regenerate both reports.")
    current, parent = coverage_metrics(report_path), coverage_metrics(parent_path)
    passed = True
    for name, value in current.items():
        required = parent[name]
        print(f"{name}: {float(parent[name]):.4f}% -> {float(value):.4f}%; required {float(required):.4f}%")
        passed = value >= required and passed
    return passed


def pytest_sessionfinish(session: pytest.Session) -> None:
    reporter = session.config.pluginmanager.get_plugin("terminalreporter")
    if not isinstance(reporter, TerminalReporter):
        raise RuntimeError("Test results are unavailable. Enable pytest terminal reporting.")
    if any(reporter.stats.get(outcome) for outcome in ("skipped", "deselected", "xfailed", "xpassed")):
        reporter.write_sep("=", "Skipped, deselected, xfailed, or xpassed tests prevent release validation")
        if session.exitstatus == pytest.ExitCode.OK:
            session.exitstatus = pytest.ExitCode.TESTS_FAILED


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: verify_coverage.py COVERAGE_JSON PARENT_COVERAGE_JSON", file=sys.stderr)
        raise SystemExit(2)
    passed = verify_coverage(Path(sys.argv[1]))
    preserved = verify_non_regression(Path(sys.argv[1]), Path(sys.argv[2]))
    raise SystemExit(0 if passed and preserved else 1)
