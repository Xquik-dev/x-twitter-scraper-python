# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx
import pytest
from respx import MockRouter

from tests.conftest import base_url
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper

STREAM_BODY = (
    b": connected\n\n"
    b"id: 41\n"
    b"event: tweet.new\n"
    b'data: {"id":"41","type":"tweet.new","monitorId":"7","monitorType":"account",'
    b'"occurredAt":"2026-10-13T12:00:00.000Z","data":{}}\n\n'
    b": idle\n\n"
    b"id: 42\n"
    b"event: follower.gained\n"
    b'data: {"id":"42","type":"follower.gained","monitorId":"7","monitorType":"account",'
    b'"occurredAt":"2026-10-13T12:00:15.000Z","data":{}}\n\n'
)


def stream_response() -> httpx.Response:
    return httpx.Response(200, content=STREAM_BODY, headers={"Content-Type": "text/event-stream"})


@pytest.mark.respx(base_url=base_url)
def test_event_stream_yields_each_event(respx_mock: MockRouter) -> None:
    route = respx_mock.get("/events/stream").mock(return_value=stream_response())

    with XTwitterScraper(base_url=base_url, api_key="My API Key", _strict_response_validation=False) as client:
        stream = client.events.stream(last_event_id="40")
        events = list(stream)

    assert [(event.id, event.type, event.monitor_id) for event in events] == [
        ("41", "tweet.new", "7"),
        ("42", "follower.gained", "7"),
    ]
    assert stream.response.is_closed
    request = route.calls.last.request
    assert request.headers["Accept"] == "text/event-stream"
    assert request.headers["Last-Event-ID"] == "40"


@pytest.mark.respx(base_url=base_url)
async def test_async_event_stream_yields_each_event(respx_mock: MockRouter) -> None:
    route = respx_mock.get("/events/stream").mock(return_value=stream_response())

    async with AsyncXTwitterScraper(
        base_url=base_url, api_key="My API Key", _strict_response_validation=False
    ) as client:
        stream = await client.events.stream()
        events = [event async for event in stream]

    assert [event.id for event in events] == ["41", "42"]
    assert stream.response.is_closed
    request = route.calls.last.request
    assert request.headers["Accept"] == "text/event-stream"
    assert "Last-Event-ID" not in request.headers
