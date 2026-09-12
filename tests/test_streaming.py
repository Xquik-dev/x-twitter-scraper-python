# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Iterator, AsyncIterator

import httpx
import pytest

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper._streaming import Stream, SSEDecoder, AsyncStream, ServerSentEvent


@pytest.mark.asyncio
@pytest.mark.parametrize("sync", [True, False], ids=["sync", "async"])
@pytest.mark.parametrize(
    ("chunks", "expected"),
    [
        pytest.param(
            [b"event: completion\n", b'data: {"foo":true}\n', b"\n"], [("completion", {"foo": True}, None)], id="basic"
        ),
        pytest.param([b'data: {"foo":true}\n', b"\n"], [(None, {"foo": True}, None)], id="data_missing_event"),
        pytest.param([b"event: ping\n", b"\n"], [("ping", None, "")], id="event_missing_data"),
        pytest.param(
            [b"event: ping\n", b"\n", b"event: completion\n", b"\n"],
            [("ping", None, ""), ("completion", None, "")],
            id="multiple_events",
        ),
        pytest.param(
            [b"event: ping\n", b'data: {"foo":true}\n', b"\n", b"event: completion\n", b'data: {"bar":false}\n', b"\n"],
            [("ping", {"foo": True}, None), ("completion", {"bar": False}, None)],
            id="multiple_events_with_data",
        ),
        pytest.param(
            [b"event: ping\n", b"data: {\n", b'data: "foo":\n', b"data: \n", b"data:\n", b"data: true}\n", b"\n\n"],
            [("ping", {"foo": True}, '{\n"foo":\n\n\ntrue}')],
            id="multiple_data_lines_with_empty_line",
        ),
        pytest.param(
            [b"event: ping\n", b'data: {"foo": "my long\\n\\ncontent"}', b"\n\n"],
            [("ping", {"foo": "my long\n\ncontent"}, None)],
            id="data_json_escaped_double_new_line",
        ),
        pytest.param(
            [b"event: ping\n", b"data: {\n", b'data: "foo":\n', b"data: true}\n", b"\n\n"],
            [("ping", {"foo": True}, None)],
            id="multiple_data_lines",
        ),
        pytest.param(
            [
                b'data: {"content":" culpa"}\n',
                b"\n",
                b'data: {"content":" \xe2\x80\xa8"}\n',
                b"\n",
                b'data: {"content":"foo"}\n',
                b"\n",
            ],
            [
                (None, {"content": " culpa"}, None),
                (None, {"content": " \u2028"}, None),
                (None, {"content": "foo"}, None),
            ],
            id="special_new_line_character",
        ),
        pytest.param(
            [
                b'data: {"content":"',
                b"\xd0",
                b"\xb8\xd0\xb7\xd0",
                b"\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xbd\xd0\xb8",
                b'"}\n',
                b"\n",
            ],
            [(None, {"content": "известни"}, None)],
            id="multi_byte_character_multiple_chunks",
        ),
    ],
)
async def test_stream_events(
    sync: bool,
    chunks: list[bytes],
    expected: list[tuple[str | None, object, str | None]],
    client: XTwitterScraper,
    async_client: AsyncXTwitterScraper,
) -> None:
    iterator = make_event_iterator(content=iter(chunks), sync=sync, client=client, async_client=async_client)
    for event, json_data, raw_data in expected:
        sse = await iter_next(iterator)
        assert sse.event == event
        if json_data is not None:
            assert sse.json() == json_data
        if raw_data is not None:
            assert sse.data == raw_data
    await assert_empty_iter(iterator)


def test_decoder_handles_comments_ids_retries_and_unknown_fields() -> None:
    decoder = SSEDecoder()
    assert decoder.decode(": keep-alive") is None
    assert decoder.decode("id: event-id") is None
    assert decoder.decode("id: ignored\0value") is None
    assert decoder.decode("retry: 250") is None
    assert decoder.decode("unknown: ignored") is None
    assert decoder.decode("data: payload") is None

    event = decoder.decode("")
    assert event is not None
    assert event.id == "event-id"
    assert event.retry == 250
    assert event.data == "payload"


def test_decoder_ignores_invalid_retry_and_empty_events() -> None:
    decoder = SSEDecoder()
    assert decoder.decode("retry: invalid") is None
    assert decoder.decode("") is None


async def to_aiter(iter: Iterator[bytes]) -> AsyncIterator[bytes]:
    for chunk in iter:
        yield chunk


async def iter_next(iter: Iterator[ServerSentEvent] | AsyncIterator[ServerSentEvent]) -> ServerSentEvent:
    event = await iter.__anext__() if isinstance(iter, AsyncIterator) else next(iter)
    assert isinstance(event, ServerSentEvent)
    return event


async def assert_empty_iter(iter: Iterator[ServerSentEvent] | AsyncIterator[ServerSentEvent]) -> None:
    with pytest.raises((StopAsyncIteration, RuntimeError)):
        await iter_next(iter)


def make_event_iterator(
    content: Iterator[bytes],
    *,
    sync: bool,
    client: XTwitterScraper,
    async_client: AsyncXTwitterScraper,
) -> Iterator[ServerSentEvent] | AsyncIterator[ServerSentEvent]:
    if sync:
        return Stream(cast_to=object, client=client, response=httpx.Response(200, content=content))._iter_events()

    return AsyncStream(
        cast_to=object, client=async_client, response=httpx.Response(200, content=to_aiter(content))
    )._iter_events()
