# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Tuple, TypeVar, Callable, Awaitable, get_args, get_type_hints
from datetime import datetime, timezone
from typing_extensions import Literal

import httpx
import pytest

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import XGetTrendsParams
from x_twitter_scraper.types.x import SpaceSearchParams

T = TypeVar("T")
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


async def send(
    sync_call: Callable[[XTwitterScraper], T],
    async_call: Callable[[AsyncXTwitterScraper], Awaitable[T]],
    payload: object,
    asynchronous: bool,
) -> Tuple[httpx.Request, T]:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=payload)

    transport = httpx.MockTransport(respond)
    if asynchronous:
        async with AsyncXTwitterScraper(
            api_key="isolated-test",
            http_client=httpx.AsyncClient(transport=transport),
            _strict_response_validation=True,
        ) as client:
            result = await async_call(client)
    else:
        with XTwitterScraper(
            api_key="isolated-test",
            http_client=httpx.Client(transport=transport),
            _strict_response_validation=True,
        ) as sync_client:
            result = sync_call(sync_client)
    assert len(requests) == 1
    assert requests[0].method == "GET"
    return requests[0], result


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_trends_at_a_past_time_read_the_stored_list_times(asynchronous: bool) -> None:
    arguments: XGetTrendsParams = {"at": "2026-10-13T14:00:00Z", "location": "Istanbul", "count": 30}
    request, trends = await send(
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
    request, trends = await send(
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
    request, page = await send(
        lambda client: client.x.spaces.search(**arguments),
        lambda client: client.x.spaces.search(**arguments),
        SPACES,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/spaces/search"
    assert dict(request.url.params) == {"q": "solana", "pageSize": "20", "queryType": query_type}
    space = page.spaces[0]
    assert (space.id, space.title, space.state) == ("1OGwblLjnQMKB", "Extending the Network to the Edge", "Ended")
    assert space.started_at == datetime(2026, 3, 11, 17, 0, 26, 227000, tzinfo=timezone.utc)
    assert (space.total_live_listeners, space.total_replay_watched) == (841, 609)
    assert space.admins[0].username == "solana"
    assert (page.has_next_page, page.next_cursor) == (True, "DAACCgACGRElMJcAAA")


def test_spaces_search_types_every_query_type_of_the_spec() -> None:
    query_type = get_type_hints(SpaceSearchParams, include_extras=True)["query_type"]
    assert get_args(get_args(query_type)[0]) == ("Latest", "Top", "Live", "Upcoming")
