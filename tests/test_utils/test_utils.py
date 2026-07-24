# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import date, datetime, timezone

import pytest

from x_twitter_scraper._types import Omit
from x_twitter_scraper._utils import (
    json_safe,
    coerce_float,
    removeprefix,
    removesuffix,
    coerce_boolean,
    coerce_integer,
    maybe_coerce_float,
    get_required_header,
    maybe_coerce_boolean,
    maybe_coerce_integer,
)
from x_twitter_scraper._utils._utils import human_join


class HeaderBag:
    def __init__(self, values: dict[str, str]) -> None:
        self.values = values

    def get(self, key: str) -> str | None:
        return self.values.get(key)


def test_human_join() -> None:
    assert human_join([]) == ""
    assert human_join(["one"]) == "one"
    assert human_join(["one", "two"]) == "one or two"
    assert human_join(["one", "two", "three"], delim="; ", final="and") == "one; two and three"


def test_numeric_coercion() -> None:
    assert coerce_integer("42") == 42
    assert coerce_float("4.2") == 4.2
    assert maybe_coerce_integer(None) is None
    assert maybe_coerce_integer("42") == 42
    assert maybe_coerce_float(None) is None
    assert maybe_coerce_float("4.2") == 4.2


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("true", True),
        ("1", True),
        ("on", True),
        ("false", False),
    ],
)
def test_boolean_coercion(value: str, expected: bool) -> None:
    assert coerce_boolean(value) is expected
    assert maybe_coerce_boolean(value) is expected
    assert maybe_coerce_boolean(None) is None


def test_remove_prefix_and_suffix() -> None:
    assert removeprefix("prefix-value", "prefix-") == "value"
    assert removeprefix("value", "prefix-") == "value"
    assert removesuffix("value-suffix", "-suffix") == "value"
    assert removesuffix("value", "-suffix") == "value"


def test_get_required_header_from_mapping() -> None:
    assert get_required_header({"X-Request-ID": "request-id"}, "x-request-id") == "request-id"
    with pytest.raises(ValueError, match="Could not find x-request-id header"):
        get_required_header({"X-Request-ID": Omit()}, "x-request-id")


def test_get_required_header_normalizes_protocol_keys() -> None:
    assert get_required_header(HeaderBag({"X-TRACE-ID": "trace-id"}), "x-trace-id") == "trace-id"
    assert get_required_header(HeaderBag({"Stainless-Event-Id": "event-id"}), "stainless-event-id") == "event-id"


def test_get_required_header_rejects_missing_header() -> None:
    with pytest.raises(ValueError, match="Could not find x-trace-id header"):
        get_required_header(HeaderBag({}), "x-trace-id")


def test_json_safe_recursively_serializes_values() -> None:
    moment = datetime(2026, 7, 23, 12, 30, tzinfo=timezone.utc)
    day = date(2026, 7, 23)
    data = {
        "moments": (moment, day),
        "bytes": b"raw",
        "plain": 42,
    }

    assert json_safe(data) == {
        "moments": [moment.isoformat(), day.isoformat()],
        "bytes": b"raw",
        "plain": 42,
    }
