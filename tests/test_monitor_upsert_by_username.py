# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from typing import Any, Dict, List

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.shared.event_type import EventType

MONITOR: Dict[str, object] = {
    "created": True,
    "id": "42",
    "username": "elonmusk",
    "xUserId": "1234567890",
    "name": "Launch watch",
    "eventTypes": ["tweet.new", "tweet.reply"],
    "isActive": True,
    "createdAt": "2025-01-15T12:00:00Z",
    "nextBillingAt": "2025-01-15T12:00:00Z",
}
EVENT_TYPES: List[EventType] = ["tweet.new", "tweet.reply"]


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    ("arguments", "expected"),
    [
        ({}, {"eventTypes": EVENT_TYPES}),
        ({"name": "Launch watch"}, {"eventTypes": EVENT_TYPES, "name": "Launch watch"}),
        ({"name": None}, {"eventTypes": EVENT_TYPES, "name": None}),
    ],
)
async def test_upsert_puts_the_body_and_reads_created(
    arguments: Dict[str, Any],
    expected: object,
    asynchronous: bool,
) -> None:
    request, monitor = await send_with_mock_transport(
        lambda client: client.monitors.upsert_by_username("elonmusk", event_types=EVENT_TYPES, **arguments),
        lambda client: client.monitors.upsert_by_username("elonmusk", event_types=EVENT_TYPES, **arguments),
        MONITOR,
        asynchronous,
        "PUT",
    )

    assert request.method == "PUT"
    assert request.url.path.endswith("/monitors/username/elonmusk")
    assert json.loads(request.content) == expected
    assert monitor.created is True
    assert monitor.id == "42"
    assert monitor.x_user_id == "1234567890"


def test_upsert_refuses_an_empty_username() -> None:
    client = XTwitterScraper(api_key="isolated-test")
    with pytest.raises(ValueError, match="username"):
        client.monitors.upsert_by_username("", event_types=[])


async def test_async_upsert_refuses_an_empty_username() -> None:
    client = AsyncXTwitterScraper(api_key="isolated-test")
    with pytest.raises(ValueError, match="username"):
        await client.monitors.upsert_by_username("", event_types=[])


def test_the_raw_and_streaming_wrappers_expose_the_upsert() -> None:
    client = XTwitterScraper(api_key="isolated-test")
    assert callable(client.monitors.with_raw_response.upsert_by_username)
    assert callable(client.monitors.with_streaming_response.upsert_by_username)
    asynchronous = AsyncXTwitterScraper(api_key="isolated-test")
    assert callable(asynchronous.monitors.with_raw_response.upsert_by_username)
    assert callable(asynchronous.monitors.with_streaming_response.upsert_by_username)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_media_download_returns_the_posts_it_had_no_time_to_read(asynchronous: bool) -> None:
    _, result = await send_with_mock_transport(
        lambda client: client.x.media.download(tweet_ids=["7", "8"]),
        lambda client: client.x.media.download(tweet_ids=["7", "8"]),
        {"unprocessedTweetIds": ["8"]},
        asynchronous,
        "POST",
    )

    assert result.unprocessed_tweet_ids == ["8"]
