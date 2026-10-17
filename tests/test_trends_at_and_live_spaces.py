# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import get_args, get_type_hints
from datetime import datetime, timezone
from typing_extensions import Literal

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper.types import XGetTrendsParams
from x_twitter_scraper.types.x import Space, SpaceParticipant, SpaceSearchParams

QueryType = Literal["Latest", "Top", "Live", "Upcoming"]
QUERY_TYPES: list[QueryType] = ["Latest", "Top", "Live", "Upcoming"]

TRENDS = {
    "trends": [
        {
            "name": "#AI",
            "description": "Artificial intelligence discussions",
            "promotedContent": None,
            "query": "%23AI",
            "rank": 1,
            "tweetVolume": 250000,
            "url": "https://x.com/search?q=%23AI",
        }
    ],
    "count": 30,
    "woeid": 1,
    "location": {
        "woeid": 2344116,
        "name": "Istanbul",
        "country": "Turkey",
        "countryCode": "TR",
        "placeType": "Town",
        "placeTypeCode": 7,
        "parentWoeid": 23424969,
        "url": "http://where.yahooapis.com/v1/place/2344116",
    },
    "capturedAt": "2026-10-13T14:00:26.000Z",
    "requestedAt": "2026-10-13T14:00:00.000Z",
}

SPACE = {
    "space": {
        "id": "1OGwblLjnQMKB",
        "title": "Extending the Network to the Edge",
        "state": "Ended",
        "startedAt": "2026-03-11T17:00:26.227Z",
        "endedAt": "2026-03-11T17:49:29.190Z",
        "totalLiveListeners": 841,
        "totalReplayWatched": 609,
        "creator": {"id": "951329744804392960", "username": "solana", "name": "Solana"},
        "admins": [{"id": "951329744804392960", "username": "solana", "name": "Solana"}],
        "speakers": [],
        "listeners": [],
    }
}

SPACES = {
    "spaces": [
        {
            "id": "1OGwblLjnQMKB",
            "title": "Extending the Network to the Edge",
            "state": "Ended",
            "startedAt": "2026-03-11T17:00:26.227Z",
            "endedAt": "2026-03-11T17:49:29.190Z",
            "totalLiveListeners": 841,
            "totalReplayWatched": 609,
            "admins": [{"id": "951329744804392960", "username": "solana", "name": "Solana"}],
            "speakers": [],
            "listeners": [],
        }
    ],
    "has_next_page": True,
    "next_cursor": "DAACCgACGRElMJcAAA",
}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_trends_at_a_past_time_read_the_stored_list_times(asynchronous: bool) -> None:
    arguments: XGetTrendsParams = {"at": "2026-10-13T14:00:00Z", "location": "Istanbul", "count": 30}
    request, trends = await send_with_mock_transport(
        lambda client: client.x.get_trends(**arguments),
        lambda client: client.x.get_trends(**arguments),
        TRENDS,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/trends"
    assert dict(request.url.params) == {"at": "2026-10-13T14:00:00Z", "location": "Istanbul", "count": "30"}
    assert trends.captured_at == datetime(2026, 10, 13, 14, 0, 26, tzinfo=timezone.utc)
    assert trends.requested_at == datetime(2026, 10, 13, 14, 0, tzinfo=timezone.utc)
    assert (trends.count, trends.woeid) == (30, 1)
    assert trends.trends[0].name == "#AI"
    assert trends.trends[0].tweet_volume == 250000
    assert trends.location is not None
    assert (trends.location.woeid, trends.location.name, trends.location.parent_woeid) == (
        2344116,
        "Istanbul",
        23424969,
    )


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_current_trends_leave_the_requested_time_out(asynchronous: bool) -> None:
    payload = {key: value for key, value in TRENDS.items() if key != "requestedAt"}
    request, trends = await send_with_mock_transport(
        lambda client: client.x.get_trends(),
        lambda client: client.x.get_trends(),
        payload,
        asynchronous,
    )

    assert request.url.query == b""
    assert trends.captured_at == datetime(2026, 10, 13, 14, 0, 26, tzinfo=timezone.utc)
    assert trends.requested_at is None


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("query_type", QUERY_TYPES)
async def test_spaces_search_sends_each_query_type(query_type: QueryType, asynchronous: bool) -> None:
    arguments: SpaceSearchParams = {"q": "solana", "page_size": 20, "query_type": query_type}
    request, page = await send_with_mock_transport(
        lambda client: client.x.spaces.search(**arguments),
        lambda client: client.x.spaces.search(**arguments),
        SPACES,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/spaces/search"
    assert dict(request.url.params) == {"q": "solana", "pageSize": "20", "queryType": query_type}
    assert page.spaces[0].id == "1OGwblLjnQMKB"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_spaces_search_reads_the_spec_example(asynchronous: bool) -> None:
    _, page = await send_with_mock_transport(
        lambda client: client.x.spaces.search(q="from:solana", query_type="Upcoming"),
        lambda client: client.x.spaces.search(q="from:solana", query_type="Upcoming"),
        SPACES,
        asynchronous,
    )

    space = page.spaces[0]
    assert (space.id, space.title, space.state) == ("1OGwblLjnQMKB", "Extending the Network to the Edge", "Ended")
    assert space.started_at == datetime(2026, 3, 11, 17, 0, 26, 227000, tzinfo=timezone.utc)
    assert space.ended_at == datetime(2026, 3, 11, 17, 49, 29, 190000, tzinfo=timezone.utc)
    assert (space.total_live_listeners, space.total_replay_watched) == (841, 609)
    assert (space.admins[0].id, space.admins[0].username, space.admins[0].name) == (
        "951329744804392960",
        "solana",
        "Solana",
    )
    assert (space.speakers, space.listeners) == ([], [])
    assert (page.has_next_page, page.next_cursor) == (True, "DAACCgACGRElMJcAAA")


def test_spaces_search_types_every_query_type_of_the_spec() -> None:
    query_type = get_type_hints(SpaceSearchParams, include_extras=True)["query_type"]
    assert get_args(get_args(query_type)[0]) == ("Latest", "Top", "Live", "Upcoming")


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_space_operations_return_the_same_model(asynchronous: bool) -> None:
    _, retrieved = await send_with_mock_transport(
        lambda client: client.x.spaces.retrieve("1OGwblLjnQMKB"),
        lambda client: client.x.spaces.retrieve("1OGwblLjnQMKB"),
        SPACE,
        asynchronous,
    )
    _, searched = await send_with_mock_transport(
        lambda client: client.x.spaces.search(q="from:solana"),
        lambda client: client.x.spaces.search(q="from:solana"),
        SPACES,
        asynchronous,
    )

    spaces: list[Space] = [retrieved.space, searched.spaces[0]]
    assert type(spaces[0]) is type(spaces[1]) is Space
    assert spaces[0].id == spaces[1].id == "1OGwblLjnQMKB"
    assert type(spaces[0].admins[0]) is type(spaces[1].admins[0]) is SpaceParticipant
