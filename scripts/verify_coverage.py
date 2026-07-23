#!/usr/bin/env python3

from __future__ import annotations

import sys
import json
from typing import cast
from pathlib import Path
from collections.abc import Mapping, Sequence

STATEMENT_MINIMUM = 90
BRANCH_MINIMUM = 80


def _integer(mapping: Mapping[str, object], key: str) -> int:
    value = mapping.get(key)
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"Coverage report field {key!r} must be an integer")
    return value


def coverage_percent(covered: int, total: int) -> float:
    if total <= 0:
        raise ValueError("Coverage report must contain measurable items")
    return covered * 100 / total


def coverage_passes(covered: int, total: int, minimum: int) -> bool:
    return covered * 100 >= total * minimum


def verify_coverage(report_path: Path) -> bool:
    payload = cast(object, json.loads(report_path.read_text(encoding="utf-8")))
    if not isinstance(payload, dict):
        raise ValueError("Coverage report root must be an object")
    report = cast(dict[str, object], payload)
    totals_value = report.get("totals")
    if not isinstance(totals_value, dict):
        raise ValueError("Coverage report must contain totals")
    totals = cast(dict[str, object], totals_value)

    metrics = (
        (
            "Statement",
            _integer(totals, "covered_lines"),
            _integer(totals, "num_statements"),
            STATEMENT_MINIMUM,
        ),
        (
            "Branch",
            _integer(totals, "covered_branches"),
            _integer(totals, "num_branches"),
            BRANCH_MINIMUM,
        ),
    )

    passed = True
    for label, covered, total, minimum in metrics:
        percent = coverage_percent(covered, total)
        print(f"{label} coverage: {covered}/{total} ({percent:.2f}%); minimum {minimum:.2f}%")
        passed = coverage_passes(covered, total, minimum) and passed
    return passed


def main(argv: Sequence[str]) -> int:
    if len(argv) != 2:
        print("usage: verify_coverage.py COVERAGE_JSON", file=sys.stderr)
        return 2
    return 0 if verify_coverage(Path(argv[1])) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
