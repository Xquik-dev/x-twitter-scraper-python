# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from typing import Any, Dict, Callable, cast

import pytest

from x_twitter_scraper.types import Event, EventDetail
from x_twitter_scraper._models import validate_type, construct_type_unchecked

POST = json.loads(
    """{
      "id": "1900000000000000001",
      "text": "Launch day",
      "likeCount": 42,
      "retweetCount": 5,
      "replyCount": 3,
      "quoteCount": 1,
      "viewCount": 1500,
      "bookmarkCount": 2,
      "retweetedAt": "2026-09-11T20:24:45.000Z",
      "cashtagAttachments": [
        {"cashtag": "$XQK", "startTime": "2026-10-09T13:30:00.000Z", "endTime": "2026-10-09T20:00:00.123Z"}
      ],
      "author": {"id": "44196397", "username": "xquik", "name": "Xquik"}
    }"""
)
PROFILE_CHANGE = json.loads(
    """{
      "field": "bio",
      "userId": "44196397",
      "username": "xquik",
      "previous": "Old bio",
      "current": "New bio"
    }"""
)
LEGACY_POST = json.loads(
    """{
      "id": "1900000000000000002",
      "text": "Stored post",
      "quoted_tweet": {"id": "1900000000000000003"},
      "legacyScore": 7
    }"""
)

DATA_CASES = [
    pytest.param(
        POST, "DataMonitorPost", ["text", "likeCount", "author", "retweetedAt", "cashtagAttachments"], id="post"
    ),
    pytest.param(PROFILE_CHANGE, "DataMonitorProfileChange", ["field", "userId", "current"], id="profile-change"),
    pytest.param(LEGACY_POST, "DataMonitorLegacyPost", ["text", "quoted_tweet", "legacyScore"], id="legacy-post"),
]
EVENT_CASES = [
    pytest.param(Event, "Event.data", id="event"),
    pytest.param(EventDetail, "EventDetail.data", id="event-detail"),
]
PARSERS = [
    pytest.param(construct_type_unchecked, id="loose"),
    pytest.param(validate_type, id="strict"),
]


def event_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "id": "42",
        "type": "tweet.new",
        "monitorId": "7",
        "monitorType": "account",
        "occurredAt": "2026-10-13T12:00:00.000Z",
        "data": data,
    }


@pytest.mark.parametrize("parse", PARSERS)
@pytest.mark.parametrize(("model", "owner"), EVENT_CASES)
@pytest.mark.parametrize(("data", "data_type", "keys"), DATA_CASES)
def test_event_data_keeps_dict_access(
    parse: Callable[..., Any],
    model: type[Event | EventDetail],
    owner: str,
    data: Dict[str, Any],
    data_type: str,
    keys: list[str],
) -> None:
    event = cast("Event | EventDetail", parse(type_=model, value=event_payload(data)))
    assert type(event.data).__name__ == data_type
    message = rf"Dict access on {owner} is deprecated & goes away in a later minor version\. Use attribute access or to_dict\(\)\."

    for key in keys:
        with pytest.warns(DeprecationWarning, match=message) as record:
            assert event.data[key] == data[key]
        assert record[0].filename == __file__
        with pytest.warns(DeprecationWarning, match=message):
            assert event.data.get(key) == data.get(key)
        with pytest.warns(DeprecationWarning, match=message):
            assert key in event.data

    with pytest.warns(DeprecationWarning, match=message):
        assert event.data.get("missing", "fallback") == "fallback"
    with pytest.warns(DeprecationWarning, match=message):
        assert event.data.get("missing") is None
    with pytest.warns(DeprecationWarning, match=message):
        assert "missing" not in event.data
    with pytest.warns(DeprecationWarning, match=message), pytest.raises(KeyError, match="missing"):
        event.data["missing"]
