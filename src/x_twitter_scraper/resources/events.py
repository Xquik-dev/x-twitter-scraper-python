# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx

from ..types import event_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from ..types.event import Event
from .._base_client import make_request_options
from ..types.event_detail import EventDetail
from ..types.shared.event_type import EventType
from ..types.event_list_response import EventListResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    """Activity events from monitored accounts"""

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDetail:
        """
        Returns one monitor event owned by the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/events/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDetail,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        event_type: EventType | Omit = omit,
        keyword_monitor_id: str | Omit = omit,
        limit: int | Omit = omit,
        monitor_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventListResponse:
        """
        Returns monitor events with cursor pagination and filters.

        Args:
          cursor: Previous nextCursor. The after alias also works. Offset pagination is not
              supported.

          event_type: Filter events by type

          keyword_monitor_id: Keyword monitor ID. The keyword_monitor_id alias also works.

          limit: Maximum items per page: 1 to 100, default 50. Credits can reduce paid results.
              With none affordable, it returns 402 insufficient_credits.

          monitor_id: Account monitor ID. The monitor_id alias also works.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_type": event_type,
                        "keyword_monitor_id": keyword_monitor_id,
                        "limit": limit,
                        "monitor_id": monitor_id,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            cast_to=EventListResponse,
        )

    def stream(
        self,
        *,
        last_event_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[Event]:
        """
        Streams the account's monitor events as server-sent events, each named by its
        event type and numbered by its event ID. A reconnect that sends Last-Event-ID
        first gets every event after that one from the last 30 days, then each new
        event. A connection lasts up to 30 minutes and sends a comment every 15 seconds
        while idle. Keep up to 5 streams open per account. Events and streams cost no
        credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or dict[str, str | Omit]())}
        extra_headers = {
            **strip_not_given({"Last-Event-ID": last_event_id}),
            **(extra_headers or dict[str, str | Omit]()),
        }
        return self._get(
            "/events/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Event,
            stream=True,
            stream_cls=Stream[Event],
        )


class AsyncEventsResource(AsyncAPIResource):
    """Activity events from monitored accounts"""

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventDetail:
        """
        Returns one monitor event owned by the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/events/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventDetail,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        event_type: EventType | Omit = omit,
        keyword_monitor_id: str | Omit = omit,
        limit: int | Omit = omit,
        monitor_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventListResponse:
        """
        Returns monitor events with cursor pagination and filters.

        Args:
          cursor: Previous nextCursor. The after alias also works. Offset pagination is not
              supported.

          event_type: Filter events by type

          keyword_monitor_id: Keyword monitor ID. The keyword_monitor_id alias also works.

          limit: Maximum items per page: 1 to 100, default 50. Credits can reduce paid results.
              With none affordable, it returns 402 insufficient_credits.

          monitor_id: Account monitor ID. The monitor_id alias also works.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "event_type": event_type,
                        "keyword_monitor_id": keyword_monitor_id,
                        "limit": limit,
                        "monitor_id": monitor_id,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            cast_to=EventListResponse,
        )

    async def stream(
        self,
        *,
        last_event_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[Event]:
        """
        Streams the account's monitor events as server-sent events, each named by its
        event type and numbered by its event ID. A reconnect that sends Last-Event-ID
        first gets every event after that one from the last 30 days, then each new
        event. A connection lasts up to 30 minutes and sends a comment every 15 seconds
        while idle. Keep up to 5 streams open per account. Events and streams cost no
        credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or dict[str, str | Omit]())}
        extra_headers = {
            **strip_not_given({"Last-Event-ID": last_event_id}),
            **(extra_headers or dict[str, str | Omit]()),
        }
        return await self._get(
            "/events/stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Event,
            stream=True,
            stream_cls=AsyncStream[Event],
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.retrieve = to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.stream = to_raw_response_wrapper(
            events.stream,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.retrieve = async_to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.stream = async_to_raw_response_wrapper(
            events.stream,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.retrieve = to_streamed_response_wrapper(
            events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.stream = to_streamed_response_wrapper(
            events.stream,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.retrieve = async_to_streamed_response_wrapper(
            events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.stream = async_to_streamed_response_wrapper(
            events.stream,
        )
