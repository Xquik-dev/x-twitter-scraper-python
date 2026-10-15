# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import re
from pathlib import Path

from scripts.api_spec import (
    ROOT,
    METHOD_PATTERN,
    Operation,
    CheckFailure,
    ReviewedList,
    run,
    load_spec,
    request_key,
    spec_source,
    operation_key,
    spec_operations,
    unexpected_spec,
    read_request_calls,
)

RESOURCES = Path("src/x_twitter_scraper/resources")
EXCLUSIONS = ReviewedList(
    file="excluded-operations.json",
    entry="operation",
    section="API coverage",
    pattern=re.compile(f"({METHOD_PATTERN}) /\\S*"),
    example="Write an upper case method, a space and a path, such as GET /api/v1/x/trends.",
    key=lambda operation: operation_key(*operation.split(" ", 1)),
)


def _label(operation: Operation) -> str:
    operation_id = operation.spec.get("operationId")
    return f"{operation.label} ({operation_id})" if isinstance(operation_id, str) else operation.label


def read_spec(source: str) -> dict[str, str]:
    document = load_spec(source)
    try:
        return {operation.key: _label(operation) for operation in spec_operations(document)}
    except ValueError as error:
        raise unexpected_spec(source) from error


def check(spec: str, root: Path) -> str:
    api = read_spec(spec)
    excluded = EXCLUSIONS.read(root)
    sdk = {request_key(call) for call in read_request_calls(root, root / RESOURCES)}
    missing = [
        f"{label} is in the API but not in the SDK."
        for key, label in sorted(api.items(), key=lambda entry: entry[1])
        if key not in sdk and key not in excluded
    ]
    stale = [
        f"{EXCLUSIONS.file} lists {operation}, which the API no longer has. Remove it."
        if key not in api
        else f"{EXCLUSIONS.file} lists {operation}, which the SDK already implements. Remove it."
        for key, operation in excluded.items()
        if key not in api or key in sdk
    ]
    if missing:
        raise CheckFailure(
            *missing,
            *stale,
            f"Add each operation above to the SDK, or list it in {EXCLUSIONS.file} with a reason.",
        )
    if stale:
        raise CheckFailure(*stale, f"Remove each operation above from {EXCLUSIONS.file}.")
    covered = len(api.keys() & sdk)
    return (
        f"The SDK covers {covered} of {len(api)} API operations, "
        f"and {EXCLUSIONS.file} lists the other {len(api) - covered}."
    )


def main(root: Path = ROOT) -> int:
    return run(lambda: check(spec_source(), root))


if __name__ == "__main__":
    raise SystemExit(main())
