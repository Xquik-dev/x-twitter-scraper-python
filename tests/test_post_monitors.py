# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from datetime import datetime, timezone

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper import XTwitterScraper
from x_twitter_scraper.types.monitors import PostMonitor, PostListResponse, PostDeleteResponse, PostMonitorMetrics

POST_MONITOR = {
    "id": "31",
    "name": "Launch post",
    "postId": "2104984505677430978",
    "postUrl": "https://x.com/xquik/status/2104984505677430978",
    "authorId": "1661816432185823232",
    "authorUsername": "xquik",
    "authorName": "Xquik",
    "text": "We shipped post monitors.",
    "postedAt": "2026-09-29T17:19:49.000Z",
    "eventTypes": ["post.reply.new", "post.quote.new", "post.likes.changed"],
    "isActive": True,
    "createdAt": "2025-01-15T12:00:00Z",
    "nextBillingAt": "2026-10-22T12:00:00Z",
    "pausedReason": "x_post_deleted",
    "pausedAt": "2026-10-22T12:00:00Z",
    "metrics": {
        "views": {"current": 1885, "gain": 12},
        "likes": {"current": 1885, "gain": 12},
        "retweets": {"current": 1885, "gain": 12},
        "replies": {"current": 1885, "gain": 12},
        "quotes": {"current": 1885, "gain": 12},
        "bookmarks": {"current": 1885, "gain": 12},
    },
}

METRICS = {
    "hours": 12,
    "buckets": [
        {
            "at": "2026-10-22T11:00:00.000Z",
            "metrics": {
                "views": {"value": 541600, "gain": 500},
                "likes": {"value": 1890, "gain": 5},
                "retweets": {"value": 112, "gain": 0},
                "replies": {"value": 86, "gain": 1},
                "quotes": {"value": 87, "gain": 0},
                "bookmarks": {"value": 471, "gain": 1},
            },
        }
    ],
}


def _expect_monitor(monitor: object) -> None:
    assert isinstance(monitor, PostMonitor)
    assert monitor.id == "31"
    assert monitor.name == "Launch post"
    assert monitor.post_url == "https://x.com/xquik/status/2104984505677430978"
    assert monitor.posted_at == datetime(2026, 9, 29, 17, 19, 49, tzinfo=timezone.utc)
    assert monitor.event_types == ["post.reply.new", "post.quote.new", "post.likes.changed"]
    assert monitor.paused_reason == "x_post_deleted"
    assert monitor.metrics.views.current == 1885
    assert monitor.metrics.bookmarks.gain == 12


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_create_sends_the_post_label_and_event_types(asynchronous: bool) -> None:
    request, monitor = await send_with_mock_transport(
        lambda client: client.monitors.posts.create(
            post="https://x.com/xquik/status/2104984505677430978",
            name="Launch post",
            event_types=["post.reply.new", "post.likes.changed"],
        ),
        lambda client: client.monitors.posts.create(
            post="https://x.com/xquik/status/2104984505677430978",
            name="Launch post",
            event_types=["post.reply.new", "post.likes.changed"],
        ),
        POST_MONITOR,
        asynchronous,
        method="POST",
    )

    assert request.method == "POST"
    assert request.url.path == "/api/v1/monitors/posts"
    assert json.loads(request.content) == {
        "post": "https://x.com/xquik/status/2104984505677430978",
        "name": "Launch post",
        "eventTypes": ["post.reply.new", "post.likes.changed"],
    }
    _expect_monitor(monitor)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_reads_1_monitor(asynchronous: bool) -> None:
    request, monitor = await send_with_mock_transport(
        lambda client: client.monitors.posts.retrieve("31"),
        lambda client: client.monitors.posts.retrieve("31"),
        POST_MONITOR,
        asynchronous,
    )

    assert request.method == "GET"
    assert request.url.path == "/api/v1/monitors/posts/31"
    _expect_monitor(monitor)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_update_sends_null_to_remove_the_label(asynchronous: bool) -> None:
    request, monitor = await send_with_mock_transport(
        lambda client: client.monitors.posts.update("31", is_active=False, name=None),
        lambda client: client.monitors.posts.update("31", is_active=False, name=None),
        POST_MONITOR,
        asynchronous,
        method="PATCH",
    )

    assert request.method == "PATCH"
    assert request.url.path == "/api/v1/monitors/posts/31"
    assert json.loads(request.content) == {"isActive": False, "name": None}
    _expect_monitor(monitor)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_list_passes_the_cursor_and_limit(asynchronous: bool) -> None:
    request, page = await send_with_mock_transport(
        lambda client: client.monitors.posts.list(cursor="abc123", limit=20),
        lambda client: client.monitors.posts.list(cursor="abc123", limit=20),
        {"monitors": [POST_MONITOR], "total": 1, "hasMore": True, "nextCursor": "abc123"},
        asynchronous,
    )

    assert request.method == "GET"
    assert request.url.path == "/api/v1/monitors/posts"
    assert dict(request.url.params) == {"cursor": "abc123", "limit": "20"}
    assert isinstance(page, PostListResponse)
    assert page.total == 1
    assert page.has_more is True
    assert page.next_cursor == "abc123"
    _expect_monitor(page.monitors[0])


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_delete_returns_the_status_url(asynchronous: bool) -> None:
    request, deletion = await send_with_mock_transport(
        lambda client: client.monitors.posts.delete("31"),
        lambda client: client.monitors.posts.delete("31"),
        {"deletionStatus": "deleting", "statusUrl": "/api/v1/monitors/posts/31", "success": True},
        asynchronous,
        method="DELETE",
    )

    assert request.method == "DELETE"
    assert request.url.path == "/api/v1/monitors/posts/31"
    assert isinstance(deletion, PostDeleteResponse)
    assert deletion.deletion_status == "deleting"
    assert deletion.status_url == "/api/v1/monitors/posts/31"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_metrics_passes_hours_and_reads_buckets(asynchronous: bool) -> None:
    request, metrics = await send_with_mock_transport(
        lambda client: client.monitors.posts.retrieve_metrics("31", hours=12),
        lambda client: client.monitors.posts.retrieve_metrics("31", hours=12),
        METRICS,
        asynchronous,
    )

    assert request.method == "GET"
    assert request.url.path == "/api/v1/monitors/posts/31/metrics"
    assert dict(request.url.params) == {"hours": "12"}
    assert isinstance(metrics, PostMonitorMetrics)
    assert metrics.hours == 12
    bucket = metrics.buckets[0]
    assert bucket.at == datetime(2026, 10, 22, 11, tzinfo=timezone.utc)
    assert (bucket.metrics.views.value, bucket.metrics.views.gain) == (541600, 500)
    assert bucket.metrics.bookmarks.value == 471


@pytest.mark.parametrize("method", ["retrieve", "update", "delete", "retrieve_metrics"])
def test_an_empty_id_raises_before_any_request(client: XTwitterScraper, method: str) -> None:
    with pytest.raises(ValueError, match="`id`"):
        getattr(client.monitors.posts, method)("")


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_events_filter_by_post_monitor_and_carry_the_post(asynchronous: bool) -> None:
    request, page = await send_with_mock_transport(
        lambda client: client.events.list(post_monitor_id="31"),
        lambda client: client.events.list(post_monitor_id="31"),
        {
            "events": [
                {
                    "id": "9001",
                    "type": "post.reply.new",
                    "monitorId": "31",
                    "monitorType": "post",
                    "monitorName": "Launch post",
                    "occurredAt": "2026-10-22T11:05:00.000Z",
                    "postId": "2104984505677430978",
                    "postUrl": "https://x.com/xquik/status/2104984505677430978",
                    "authorId": "1661816432185823232",
                    "authorUsername": "xquik",
                    "data": {"replyId": "2104990000000000000"},
                }
            ],
            "hasMore": False,
        },
        asynchronous,
    )

    assert request.url.path == "/api/v1/events"
    assert dict(request.url.params) == {"postMonitorId": "31"}
    event = page.events[0]
    assert event.monitor_type == "post"
    assert event.type == "post.reply.new"
    assert event.post_id == "2104984505677430978"
    assert event.post_url == "https://x.com/xquik/status/2104984505677430978"
    assert event.author_id == "1661816432185823232"
    assert event.author_username == "xquik"


@pytest.mark.parametrize(
    "data, field, value",
    [
        ({"metric": "likes", "previous": 17096, "current": 17200, "change": 104}, "metric", "likes"),
        (
            {
                "previousText": "We cut costs by 20%.",
                "text": "We cut costs by 25%.",
                "versionId": "2082577277246973001",
            },
            "version_id",
            "2082577277246973001",
        ),
    ],
)
async def test_post_event_data_reads_metric_changes_and_edits(data: dict[str, object], field: str, value: str) -> None:
    _, page = await send_with_mock_transport(
        lambda client: client.events.list(event_type="post.likes.changed"),
        lambda client: client.events.list(event_type="post.likes.changed"),
        {
            "events": [
                {
                    "id": "9002",
                    "type": "post.likes.changed",
                    "monitorId": "31",
                    "monitorType": "post",
                    "occurredAt": "2026-10-22T11:05:00.000Z",
                    "data": data,
                }
            ],
            "hasMore": False,
        },
        False,
    )

    assert getattr(page.events[0].data, field) == value
