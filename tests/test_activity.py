# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from datetime import datetime, timezone

import httpx
import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import ActivityLogRow, ActivityRecord

ROWS = [
    {
        "time": "2026-10-28T20:22:13.481Z",
        "category": "monitor_change",
        "type": "pause",
        "activity": "Account monitor for @elonmusk paused",
        "status": "completed",
        "source": "elonmusk",
        "target": "",
        "results": "",
        "credits": "",
        "details": "",
        "id": "naF3xqHLWDTs",
        "link": "",
    },
    {
        "time": "2026-10-28T19:02:40.120Z",
        "category": "extraction",
        "type": "reply_extractor",
        "activity": "Reply extraction for @elonmusk",
        "status": "completed",
        "source": "elonmusk",
        "target": "1846000000000000001",
        "results": 12,
        "credits": 1000,
        "details": "200",
        "id": "Q7wErTyUiOpA",
        "link": "https://x.com/elonmusk/status/1846000000000000001",
    },
]

RECORD = {
    "object": "activity",
    "id": "naF3xqHLWDTs",
    "kind": "monitor_change",
    "type": "pause",
    "status": "completed",
    "url": "https://dashboard.xquik.com/activity/naF3xqHLWDTs",
    "requestId": "9f2c1d7e4b8a4c55a1e0d3b2c6f7a8e9",
    "timestamps": {"createdAt": "2026-10-28T20:22:13.481Z"},
    "request": {
        "method": "PATCH",
        "path": "/api/v1/monitors/42",
        "httpStatus": 200,
        "durationMs": 37,
        "ipAddress": "203.0.113.9",
        "userAgent": "my-agent/1.0",
        "at": "2026-10-28T20:22:13.519Z",
    },
    "caller": {"authMethod": "api_key", "apiKey": {"name": "Production", "prefix": "xq_ab12"}, "oauthClient": None},
    "charge": None,
    "details": {
        "monitorKind": "account",
        "monitorId": "42",
        "subjectUsername": "elonmusk",
        "subjectQuery": None,
        "subjectName": None,
        "subjectXId": "44196397",
        "subjectAvatar": None,
        "surface": "rest",
    },
    "related": [
        {
            "id": "Q7wErTyUiOpA",
            "type": "create",
            "status": "completed",
            "createdAt": "2026-10-21T09:12:40.002Z",
            "url": "https://dashboard.xquik.com/activity/Q7wErTyUiOpA",
        }
    ],
}

CHARGED_RECORD = {
    **RECORD,
    "kind": "extraction",
    "type": "reply_extractor",
    "timestamps": {"createdAt": "2026-10-28T20:22:13.481Z", "completedAt": "2026-10-28T20:22:13.950Z"},
    "caller": {"authMethod": "oauth", "apiKey": None, "oauthClient": {"id": "claude", "name": "Claude"}},
    "charge": {"credits": 1300, "balanceAfter": 898700, "at": "2026-10-28T20:22:13.900Z"},
    "related": [],
}

CSV = (
    b"time,category,type,activity,status,source,target,results,credits,details,id,link\n"
    b"2026-10-28T20:22:13.481Z,monitor_change,pause,Account monitor for @elonmusk paused,completed,elonmusk,,,,,naF3xqHLWDTs,\n"
)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_list_sends_the_filters_and_reads_the_rows(asynchronous: bool) -> None:
    since = datetime(2026, 10, 21, tzinfo=timezone.utc)
    request, rows = await send_with_mock_transport(
        lambda client: client.activity.list(category="monitors", limit=50, since=since, status="failed,running"),
        lambda client: client.activity.list(category="monitors", limit=50, since=since, status="failed,running"),
        ROWS,
        asynchronous,
    )

    assert request.url.path == "/api/v1/activity"
    assert dict(request.url.params) == {
        "category": "monitors",
        "limit": "50",
        "since": "2026-10-21T00:00:00+00:00",
        "status": "failed,running",
    }
    assert all(isinstance(row, ActivityLogRow) for row in rows)
    assert [row.id for row in rows] == ["naF3xqHLWDTs", "Q7wErTyUiOpA"]
    assert (rows[0].activity, rows[0].results, rows[0].credits) == ("Account monitor for @elonmusk paused", "", "")
    assert (rows[1].results, rows[1].credits) == (12, 1000)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_reads_the_request_caller_and_related_activity(asynchronous: bool) -> None:
    request, record = await send_with_mock_transport(
        lambda client: client.activity.retrieve("naF3xqHLWDTs"),
        lambda client: client.activity.retrieve("naF3xqHLWDTs"),
        RECORD,
        asynchronous,
    )

    assert request.url.path == "/api/v1/activity/naF3xqHLWDTs"
    assert isinstance(record, ActivityRecord)
    assert (record.kind, record.type, record.status) == ("monitor_change", "pause", "completed")
    assert record.timestamps.created_at == datetime(2026, 10, 28, 20, 22, 13, 481000, tzinfo=timezone.utc)
    assert record.timestamps.completed_at is None
    assert record.request is not None
    assert (record.request.method, record.request.http_status, record.request.duration_ms) == ("PATCH", 200, 37)
    assert record.caller.api_key is not None and record.caller.api_key.prefix == "xq_ab12"
    assert record.caller.oauth_client is None
    assert record.charge is None
    assert record.details["monitorKind"] == "account"
    assert record.details["subjectQuery"] is None
    assert record.related[0].created_at == datetime(2026, 10, 21, 9, 12, 40, 2000, tzinfo=timezone.utc)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_retrieve_reads_the_charge_and_oauth_caller(asynchronous: bool) -> None:
    _, record = await send_with_mock_transport(
        lambda client: client.activity.retrieve("naF3xqHLWDTs"),
        lambda client: client.activity.retrieve("naF3xqHLWDTs"),
        CHARGED_RECORD,
        asynchronous,
    )

    assert record.charge is not None
    assert (record.charge.credits, record.charge.balance_after) == (1300, 898700)
    assert record.caller.auth_method == "oauth"
    assert record.caller.oauth_client is not None and record.caller.oauth_client.name == "Claude"
    assert record.timestamps.completed_at == datetime(2026, 10, 28, 20, 22, 13, 950000, tzinfo=timezone.utc)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_export_sends_the_format_and_returns_the_file(asynchronous: bool) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, content=CSV, headers={"Content-Type": "text/csv"})

    transport = httpx.MockTransport(respond)
    if asynchronous:
        async with AsyncXTwitterScraper(
            api_key="isolated-test", http_client=httpx.AsyncClient(transport=transport)
        ) as async_client:
            async_file = await async_client.activity.export(format="csv", status="failed,running")
            content = await async_file.read()
    else:
        with XTwitterScraper(api_key="isolated-test", http_client=httpx.Client(transport=transport)) as client:
            content = client.activity.export(format="csv", status="failed,running").read()

    assert content == CSV
    assert len(requests) == 1
    assert requests[0].url.path == "/api/v1/activity"
    assert dict(requests[0].url.params) == {"format": "csv", "status": "failed,running"}
    assert requests[0].headers["Accept"] == "application/octet-stream"


def test_an_empty_id_raises_before_any_request(client: XTwitterScraper) -> None:
    with pytest.raises(ValueError, match="`id`"):
        client.activity.retrieve("")


async def test_an_async_empty_id_raises_before_any_request(async_client: AsyncXTwitterScraper) -> None:
    with pytest.raises(ValueError, match="`id`"):
        await async_client.activity.retrieve("")
