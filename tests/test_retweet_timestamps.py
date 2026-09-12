# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime, timezone

import httpx
import pytest

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper, omit


@pytest.mark.parametrize("enabled", [None, False, True])
@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retweet_timestamps(enabled: bool | None, asynchronous: bool) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "users": [
                    {"id": "1", "name": "One", "username": "one", "retweetedAt": "2026-09-11T20:24:45.000Z"},
                    {"id": "2", "name": "Two", "username": "two", "retweetedAt": None},
                ],
                "has_next_page": True,
                "next_cursor": "next-page",
            },
        )

    transport = httpx.MockTransport(respond)
    flag = omit if enabled is None else enabled
    if asynchronous:
        async with AsyncXTwitterScraper(
            api_key="isolated-test", http_client=httpx.AsyncClient(transport=transport)
        ) as client:
            result = await client.x.tweets.get_retweeters("123", cursor="previous-page", include_retweet_timestamp=flag)
    else:
        with XTwitterScraper(api_key="isolated-test", http_client=httpx.Client(transport=transport)) as sync_client:
            result = sync_client.x.tweets.get_retweeters("123", cursor="previous-page", include_retweet_timestamp=flag)
    assert len(requests) == 1
    assert requests[0].url.path == "/api/v1/x/tweets/123/retweeters"
    assert requests[0].url.params.get("includeRetweetTimestamp") == (None if enabled is None else str(enabled).lower())
    assert requests[0].url.params["cursor"] == "previous-page"
    assert result.users[0].retweeted_at == datetime(2026, 9, 11, 20, 24, 45, tzinfo=timezone.utc)
    assert result.users[1].retweeted_at is None
    assert result.has_next_page is True
    assert result.next_cursor == "next-page"
