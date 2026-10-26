# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import re
import sys
import json
from typing import Callable, cast
from pathlib import Path
from datetime import date, timedelta
from collections.abc import Mapping

# json.loads declares Any, and without an object hook it returns only JSON values. https://docs.python.org/3/library/json.html#json-to-py-table
load_json: Callable[[str], object] = json.loads

REASONS = ("build-time only", "peer dependency provided by the host")
MAX_RECHECK = timedelta(days=30)
REQUIREMENT = re.compile(r"^([A-Za-z0-9][A-Za-z0-9._-]*)==")


def normalize(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def requirement_names(text: str) -> set[str]:
    return {normalize(match.group(1)) for match in map(REQUIREMENT.match, text.splitlines()) if match}


def _mapping(value: object, message: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        raise ValueError(message)
    return cast(Mapping[str, object], value)


def _list(value: object, message: str) -> list[object]:
    if not isinstance(value, list):
        raise ValueError(message)
    return cast(list[object], value)


def _strings(value: object, message: str) -> list[str]:
    items = _list(value, message)
    if not all(isinstance(item, str) and item for item in items):
        raise ValueError(message)
    return cast(list[str], items)


def load_exceptions(document: object, today: date) -> dict[tuple[str, str], date]:
    entries = _list(
        _mapping(document, "audit-exceptions.json must be an object.").get("exceptions"),
        "audit-exceptions.json needs an exceptions list.",
    )
    listed: dict[tuple[str, str], date] = {}
    for item in entries:
        entry = _mapping(item, "Each audit exception must be an object.")
        advisory, path, reason, recheck = (entry.get(key) for key in ("id", "package", "reason", "recheck"))
        if not isinstance(advisory, str) or not advisory or not isinstance(path, str) or not path.strip():
            raise ValueError("Each audit exception needs an advisory id and a package path.")
        if reason not in REASONS:
            raise ValueError(f"Exception {advisory} needs reason {REASONS[0]!r} or {REASONS[1]!r}.")
        try:
            recheck_date = date.fromisoformat(cast(str, recheck))
        except (TypeError, ValueError):
            raise ValueError(f"Exception {advisory} needs a recheck date as YYYY-MM-DD.") from None
        if recheck_date - today > MAX_RECHECK:
            raise ValueError(f"Exception {advisory} rechecks more than 30 days out. Pick an earlier date.")
        listed[(advisory, normalize(path.split(">")[-1].strip()))] = recheck_date
    return listed


def blocking_findings(
    report: object,
    audited: set[str],
    runtime: set[str],
    listed: Mapping[tuple[str, str], date],
    today: date,
) -> list[str]:
    dependencies = _list(
        _mapping(report, "pip-audit returned no JSON object.").get("dependencies"),
        "The pip-audit report lacks its dependency list.",
    )
    blocking: list[str] = []
    seen: set[str] = set()
    for item in dependencies:
        dependency = _mapping(item, "The pip-audit report lists an invalid dependency.")
        name, version = dependency.get("name"), dependency.get("version")
        if not isinstance(name, str) or not isinstance(version, str):
            raise ValueError("The pip-audit report lists a dependency without a name or version.")
        package = normalize(name)
        seen.add(package)
        if "skip_reason" in dependency:
            blocking.append(f"pip-audit skipped {name} {version}: {dependency['skip_reason']}")
            continue
        for vulnerability in _list(dependency.get("vulns"), f"pip-audit lists invalid findings for {name}."):
            finding = _mapping(vulnerability, f"pip-audit lists an invalid finding for {name}.")
            advisory = finding.get("id")
            if not isinstance(advisory, str) or not advisory:
                raise ValueError(f"pip-audit lists a finding without an ID for {name}.")
            aliases = _strings(finding.get("aliases", []), f"pip-audit lists invalid aliases for {advisory}.")
            fixes = _strings(finding.get("fix_versions", []), f"pip-audit lists invalid fixes for {advisory}.")
            label = f"{name} {version} {advisory}"
            recheck = min(
                (listed[(key, package)] for key in (advisory, *aliases) if (key, package) in listed), default=None
            )
            if package in runtime:
                blocking.append(f"{label} affects a shipped runtime dependency. Upgrade it in uv.lock.")
            elif fixes:
                blocking.append(f"{label} is fixed in {', '.join(fixes)}. Upgrade it in uv.lock.")
            elif recheck is None:
                blocking.append(f"{label} has no fix. Review it and list it in audit-exceptions.json.")
            elif today >= recheck:
                blocking.append(f"{label} reached its recheck date {recheck}. Review it again.")
            else:
                print(f"Allowed until {recheck}: {label}, development only, no fix yet.")
    missing = sorted(audited - seen)
    if missing:
        blocking.append(f"pip-audit did not report {', '.join(missing)}. Rerun scripts/audit.")
    return blocking


def main(arguments: list[str], today: date) -> int:
    if len(arguments) != 4:
        print(
            "Usage: verify_audit.py REPORT_JSON AUDITED_REQUIREMENTS RUNTIME_REQUIREMENTS EXCEPTIONS_JSON",
            file=sys.stderr,
        )
        return 2
    report_path, audited_path, runtime_path, exceptions_path = map(Path, arguments)
    try:
        report = load_json(report_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        print("pip-audit wrote no report. Fix the error above, then rerun.", file=sys.stderr)
        return 1
    try:
        exceptions = load_json(exceptions_path.read_text(encoding="utf-8"))
        blocking = blocking_findings(
            report,
            requirement_names(audited_path.read_text(encoding="utf-8")),
            requirement_names(runtime_path.read_text(encoding="utf-8")),
            load_exceptions(exceptions, today),
            today,
        )
    except (OSError, ValueError) as error:
        print(f"Dependency audit failed: {error}", file=sys.stderr)
        return 1
    for line in blocking:
        print(line, file=sys.stderr)
    if blocking:
        return 1
    print("Dependency audit passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:], date.today()))
