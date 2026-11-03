# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Dict, List

import httpx

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from tests.test_activity import CSV, ROWS, RECORD
from tests.test_football import ROSTER, GAME_POSTS, PLAYER_PROPS
from tests.test_shadowban import ACTIVE

PAYLOADS: Dict[str, object] = {
    "/api/v1/activity": ROWS,
    "/api/v1/activity/naF3xqHLWDTs": RECORD,
    "/api/v1/x/users/NASA/shadowban": ACTIVE,
    "/api/v1/x/sports/nfl/games/1/roster": ROSTER,
    "/api/v1/x/sports/nfl/games/1/player-props": PLAYER_PROPS,
    "/api/v1/x/sports/nfl/games/1/posts": GAME_POSTS,
}
EXPORTS = ["/api/v1/activity", "/api/v1/activity"]


def transport(requests: List[httpx.Request]) -> httpx.MockTransport:
    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if "format" in request.url.params:
            return httpx.Response(200, content=CSV, headers={"Content-Type": "text/csv"})
        return httpx.Response(200, json=PAYLOADS[request.url.path])

    return httpx.MockTransport(respond)


def test_raw_responses_reach_each_new_read() -> None:
    requests: List[httpx.Request] = []
    with XTwitterScraper(api_key="isolated-test", http_client=httpx.Client(transport=transport(requests))) as client:
        rows = client.activity.with_raw_response.list().parse()
        record = client.activity.with_raw_response.retrieve("naF3xqHLWDTs").parse()
        report = client.x.users.with_raw_response.retrieve_shadowban("NASA").parse()
        roster = client.x.sports.with_raw_response.retrieve_roster("1", league="nfl").parse()
        props = client.x.sports.with_raw_response.retrieve_player_props("1", league="nfl").parse()
        posts = client.x.sports.with_raw_response.list_posts("1", league="nfl").parse()
        exported = client.activity.with_raw_response.export(format="csv").read()
        with client.activity.with_streaming_response.export(format="csv") as streamed:
            streamed_file = streamed.read()
        with client.activity.with_streaming_response.list() as response:
            streamed_rows = response.parse()
        with client.activity.with_streaming_response.retrieve("naF3xqHLWDTs") as response:
            streamed_record = response.parse()
        with client.x.users.with_streaming_response.retrieve_shadowban("NASA") as response:
            streamed_report = response.parse()
        with client.x.sports.with_streaming_response.retrieve_roster("1", league="nfl") as response:
            streamed_roster = response.parse()
        with client.x.sports.with_streaming_response.retrieve_player_props("1", league="nfl") as response:
            streamed_props = response.parse()
        with client.x.sports.with_streaming_response.list_posts("1", league="nfl") as response:
            streamed_posts = response.parse()

    assert [request.url.path for request in requests] == [*PAYLOADS, *EXPORTS, *PAYLOADS]
    assert [request.headers["Accept"] for request in requests[6:8]] == ["application/octet-stream"] * 2
    assert streamed_rows[0].id == streamed_record.id == "naF3xqHLWDTs"
    assert streamed_report.user_id == "11348282"
    assert streamed_roster.rosters[0].team_id == "689566294702555136"
    assert streamed_props.id == "2055084502741929984"
    assert streamed_posts.has_next_page is True
    assert rows[0].id == "naF3xqHLWDTs"
    assert record.id == "naF3xqHLWDTs"
    assert report.user_id == "11348282"
    assert roster.rosters[0].team_id == "689566294702555136"
    assert props.id == "2055084502741929984"
    assert posts.has_next_page is True
    assert exported == streamed_file == CSV


async def test_async_raw_responses_reach_each_new_read() -> None:
    requests: List[httpx.Request] = []
    async with AsyncXTwitterScraper(
        api_key="isolated-test", http_client=httpx.AsyncClient(transport=transport(requests))
    ) as client:
        rows = await (await client.activity.with_raw_response.list()).parse()
        record = await (await client.activity.with_raw_response.retrieve("naF3xqHLWDTs")).parse()
        report = await (await client.x.users.with_raw_response.retrieve_shadowban("NASA")).parse()
        roster = await (await client.x.sports.with_raw_response.retrieve_roster("1", league="nfl")).parse()
        props = await (await client.x.sports.with_raw_response.retrieve_player_props("1", league="nfl")).parse()
        posts = await (await client.x.sports.with_raw_response.list_posts("1", league="nfl")).parse()
        exported = await (await client.activity.with_raw_response.export(format="csv")).read()
        async with client.activity.with_streaming_response.export(format="csv") as streamed:
            streamed_file = await streamed.read()
        async with client.activity.with_streaming_response.list() as response:
            streamed_rows = await response.parse()
        async with client.activity.with_streaming_response.retrieve("naF3xqHLWDTs") as response:
            streamed_record = await response.parse()
        async with client.x.users.with_streaming_response.retrieve_shadowban("NASA") as response:
            streamed_report = await response.parse()
        async with client.x.sports.with_streaming_response.retrieve_roster("1", league="nfl") as response:
            streamed_roster = await response.parse()
        async with client.x.sports.with_streaming_response.retrieve_player_props("1", league="nfl") as response:
            streamed_props = await response.parse()
        async with client.x.sports.with_streaming_response.list_posts("1", league="nfl") as response:
            streamed_posts = await response.parse()

    assert [request.url.path for request in requests] == [*PAYLOADS, *EXPORTS, *PAYLOADS]
    assert [request.headers["Accept"] for request in requests[6:8]] == ["application/octet-stream"] * 2
    assert streamed_rows[0].id == streamed_record.id == "naF3xqHLWDTs"
    assert streamed_report.user_id == "11348282"
    assert streamed_roster.rosters[0].team_id == "689566294702555136"
    assert streamed_props.id == "2055084502741929984"
    assert streamed_posts.has_next_page is True
    assert rows[0].id == "naF3xqHLWDTs"
    assert record.id == "naF3xqHLWDTs"
    assert report.user_id == "11348282"
    assert roster.rosters[0].team_id == "689566294702555136"
    assert props.id == "2055084502741929984"
    assert posts.has_next_page is True
    assert exported == streamed_file == CSV
