# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from typing import Dict, List, Callable

import httpx
import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.event import DataMonitorFollow
from x_twitter_scraper.types.event_detail import DataMonitorFollow as DetailMonitorFollow
from x_twitter_scraper.types.monitors.post_monitor import PostMonitor
from x_twitter_scraper.types.x_get_article_response import Article
from x_twitter_scraper.types.x.media_download_response import Item
from x_twitter_scraper.types.extraction_retrieve_response import Result


def write_record(action: str) -> Dict[str, object]:
    return {
        "id": "wa_1",
        "action": action,
        "billing": {"charged": False, "chargedCredits": "0", "plannedCredits": "1", "status": "not_charged"},
        "charged": False,
        "chargedCredits": "0",
        "object": "x_write_action",
        "request": {},
        "retryable": False,
        "safeToRetry": False,
        "sendDispatched": True,
        "status": "success",
        "statusUrl": "/x/write-actions/wa_1",
        "success": True,
        "terminal": True,
        "writeActionId": "wa_1",
    }


def assert_write_request(request: httpx.Request, path: str) -> None:
    assert request.url.path == path
    assert request.headers["Idempotency-Key"] == "key-1"
    assert json.loads(request.content) == {"account": "@elonmusk"}


def captured_request(call: Callable[[XTwitterScraper], object], payload: object) -> httpx.Request:
    requests: List[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=payload)

    with XTwitterScraper(
        api_key="isolated-test",
        http_client=httpx.Client(transport=httpx.MockTransport(respond)),
    ) as client:
        call(client)
    assert len(requests) == 1
    return requests[0]


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_bookmark_create_sends_the_account_and_key(asynchronous: bool) -> None:
    request, record = await send_with_mock_transport(
        lambda client: client.x.tweets.bookmark.create("7", account="@elonmusk", idempotency_key="key-1"),
        lambda client: client.x.tweets.bookmark.create("7", account="@elonmusk", idempotency_key="key-1"),
        write_record("bookmark"),
        asynchronous,
        "POST",
    )

    assert_write_request(request, "/api/v1/x/tweets/7/bookmark")
    assert record.action == "bookmark"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_bookmark_delete_sends_the_account_and_key(asynchronous: bool) -> None:
    request, record = await send_with_mock_transport(
        lambda client: client.x.tweets.bookmark.delete("7", account="@elonmusk", idempotency_key="key-1"),
        lambda client: client.x.tweets.bookmark.delete("7", account="@elonmusk", idempotency_key="key-1"),
        write_record("unbookmark"),
        asynchronous,
        "DELETE",
    )

    assert_write_request(request, "/api/v1/x/tweets/7/bookmark")
    assert record.action == "unbookmark"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_block_create_sends_the_account_and_key(asynchronous: bool) -> None:
    request, record = await send_with_mock_transport(
        lambda client: client.x.users.block.create("44", account="@elonmusk", idempotency_key="key-1"),
        lambda client: client.x.users.block.create("44", account="@elonmusk", idempotency_key="key-1"),
        write_record("block"),
        asynchronous,
        "POST",
    )

    assert_write_request(request, "/api/v1/x/users/44/block")
    assert record.action == "block"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_block_delete_sends_the_account_and_key(asynchronous: bool) -> None:
    request, record = await send_with_mock_transport(
        lambda client: client.x.users.block.delete("44", account="@elonmusk", idempotency_key="key-1"),
        lambda client: client.x.users.block.delete("44", account="@elonmusk", idempotency_key="key-1"),
        write_record("unblock"),
        asynchronous,
        "DELETE",
    )

    assert_write_request(request, "/api/v1/x/users/44/block")
    assert record.action == "unblock"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_mute_create_sends_the_account_and_key(asynchronous: bool) -> None:
    request, record = await send_with_mock_transport(
        lambda client: client.x.users.mute.create("44", account="@elonmusk", idempotency_key="key-1"),
        lambda client: client.x.users.mute.create("44", account="@elonmusk", idempotency_key="key-1"),
        write_record("mute"),
        asynchronous,
        "POST",
    )

    assert_write_request(request, "/api/v1/x/users/44/mute")
    assert record.action == "mute"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_mute_delete_sends_the_account_and_key(asynchronous: bool) -> None:
    request, record = await send_with_mock_transport(
        lambda client: client.x.users.mute.delete("44", account="@elonmusk", idempotency_key="key-1"),
        lambda client: client.x.users.mute.delete("44", account="@elonmusk", idempotency_key="key-1"),
        write_record("unmute"),
        asynchronous,
        "DELETE",
    )

    assert_write_request(request, "/api/v1/x/users/44/mute")
    assert record.action == "unmute"


def test_post_monitor_create_can_start_paused() -> None:
    request = captured_request(
        lambda client: client.monitors.posts.create(post="7", is_active=False),
        {"id": "1"},
    )

    assert json.loads(request.content) == {"post": "7", "isActive": False}


def test_tweet_search_runs_without_q() -> None:
    request = captured_request(
        lambda client: client.x.tweets.search(from_user="elonmusk"),
        {"tweets": []},
    )

    assert dict(request.url.params) == {"fromUser": "elonmusk"}


def test_post_monitor_reads_the_author_affiliate() -> None:
    monitor = PostMonitor.construct(
        authorAffiliate={"badgeUrl": "https://pbs.twimg.com/badge.jpg", "description": "X"},
    )

    assert monitor.author_affiliate is not None
    assert monitor.author_affiliate.badge_url == "https://pbs.twimg.com/badge.jpg"
    assert monitor.author_affiliate.description == "X"
    assert monitor.author_affiliate.url is None


def test_flat_extraction_rows_read_the_quoted_post_and_sensitive_flags() -> None:
    row = Result.construct(
        possiblySensitive=True,
        quotedPossiblySensitive=False,
        quotedPost={"id": "9", "text": "Hello", "author": {"userName": "nasa"}},
    )

    assert row.possibly_sensitive is True
    assert row.quoted_possibly_sensitive is False
    assert row.quoted_post is not None
    assert row.quoted_post.text == "Hello"
    assert row.quoted_post.author is not None
    assert row.quoted_post.author.user_name == "nasa"


def test_media_download_items_read_the_poster_and_mp4_sizes() -> None:
    item = Item.construct(
        posterUrl="https://pbs.twimg.com/poster.jpg",
        qualities=[{"bitrate": 832000, "height": 720, "url": "https://video.twimg.com/a.mp4", "width": 1280}],
    )

    assert item.poster_url == "https://pbs.twimg.com/poster.jpg"
    assert item.qualities[0].bitrate == 832000


def test_follow_events_say_why_an_account_is_back() -> None:
    assert DataMonitorFollow.construct(followKind="refollow").follow_kind == "refollow"
    assert DetailMonitorFollow.construct(followKind="return").follow_kind == "return"


def test_articles_say_which_counts_x_did_not_send() -> None:
    article = Article.construct(unknownCounts=["viewCount"])

    assert article.unknown_counts == ["viewCount"]


async def test_response_wrappers_reach_the_new_writes() -> None:
    with XTwitterScraper(api_key="isolated-test") as client:
        async with AsyncXTwitterScraper(api_key="isolated-test") as async_client:
            for tweets in (
                client.x.tweets.with_raw_response,
                client.x.tweets.with_streaming_response,
                async_client.x.tweets.with_raw_response,
                async_client.x.tweets.with_streaming_response,
            ):
                assert callable(tweets.bookmark.create)
                assert callable(tweets.bookmark.delete)

            for users in (
                client.x.users.with_raw_response,
                client.x.users.with_streaming_response,
                async_client.x.users.with_raw_response,
                async_client.x.users.with_streaming_response,
            ):
                assert callable(users.block.create)
                assert callable(users.block.delete)
                assert callable(users.mute.create)
                assert callable(users.mute.delete)


def test_extraction_rows_say_when_the_author_deleted_a_post() -> None:
    assert Result.construct(isDeleted=True).is_deleted is True


def test_user_insights_and_shadowban_send_limit() -> None:
    insights = captured_request(lambda client: client.x.users.retrieve_insights("nasa", limit=50), {})
    shadowban = captured_request(lambda client: client.x.users.retrieve_shadowban("nasa", limit=50), {})

    assert dict(insights.url.params) == {"limit": "50"}
    assert dict(shadowban.url.params) == {"limit": "50"}
