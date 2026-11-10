# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import List, Optional

import httpx

from .posts import (
    PostsResource,
    AsyncPostsResource,
    PostsResourceWithRawResponse,
    AsyncPostsResourceWithRawResponse,
    PostsResourceWithStreamingResponse,
    AsyncPostsResourceWithStreamingResponse,
)
from ...types import (
    monitor_list_params,
    monitor_create_params,
    monitor_update_params,
    monitor_upsert_by_username_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .keywords import (
    KeywordsResource,
    AsyncKeywordsResource,
    KeywordsResourceWithRawResponse,
    AsyncKeywordsResourceWithRawResponse,
    KeywordsResourceWithStreamingResponse,
    AsyncKeywordsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.monitor import Monitor
from ...types.shared.event_type import EventType
from ...types.monitor_list_response import MonitorListResponse
from ...types.monitor_create_response import MonitorCreateResponse
from ...types.monitor_deactivate_response import MonitorDeactivateResponse
from ...types.monitor_upsert_by_username_response import MonitorUpsertByUsernameResponse

__all__ = ["MonitorsResource", "AsyncMonitorsResource"]


class MonitorsResource(SyncAPIResource):
    """X account monitoring with 1-second checks"""

    @cached_property
    def keywords(self) -> KeywordsResource:
        """X account monitoring with 1-second checks"""
        return KeywordsResource(self._client)

    @cached_property
    def posts(self) -> PostsResource:
        """Post monitoring with replies, quotes, edits, deletion & 6 metrics"""
        return PostsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MonitorsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return MonitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return MonitorsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        event_types: List[EventType],
        username: str,
        name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorCreateResponse:
        """Creates an account monitor, with no count limit.

        Active monitors check every
        second for 30 credits an hour, events & webhook deliveries included. That hourly
        price is a monitor's only charge. Creation needs the credits of the first hour.

        Args:
          event_types: Array of event types to subscribe to.

          username: X username to monitor, with or without @

          name: Your label for the monitor. Its events carry it as monitorName. Whitespace is
              normalized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/monitors",
            body=maybe_transform(
                {
                    "event_types": event_types,
                    "username": username,
                    "name": name,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Returns configuration and status for one account monitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/monitors/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    def update(
        self,
        id: str,
        *,
        event_types: List[EventType] | Omit = omit,
        is_active: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Updates mutable settings for an existing account monitor.

        Args:
          event_types: Array of event types to subscribe to.

          name: New label for the account monitor. Send null to remove the label.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/monitors/{id}", id=id),
            body=maybe_transform(
                {
                    "event_types": event_types,
                    "is_active": is_active,
                    "name": name,
                },
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
        """
        Returns account monitors with their current operating states.

        Args:
          cursor: Previous nextCursor. The after alias also works. Offset pagination is not
              supported.

          limit: Maximum items per page: 1 to 200, default 200. Pass nextCursor as cursor for the
              next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    monitor_list_params.MonitorListParams,
                ),
            ),
            cast_to=MonitorListResponse,
        )

    def deactivate(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorDeactivateResponse:
        """
        Stops one account monitor, then removes its stored events in bounded batches.
        Poll statusUrl until the monitor returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/monitors/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorDeactivateResponse,
        )

    def upsert_by_username(
        self,
        username: str,
        *,
        event_types: List[EventType],
        name: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorUpsertByUsernameResponse:
        """Creates the monitor if it does not exist, or updates it if it does.

        Send the same
        call twice & you still have 1 monitor. A new monitor answers 201 & an update
        answers 200. Both carry `created`, so you know which one ran. Creating needs the
        credits of the first hour, then costs 30 credits an hour. A stopped monitor
        turns back on & counts as created. Updating is free & replaces the event types.
        It changes the name only when you send one.

        Args:
          username: The account's X username, with or without @, or its numeric user ID. A number
              is a user ID, so this call matches the account even after a rename.

          event_types: Array of event types to subscribe to.

          name: Your label for the monitor. Its events carry it as monitorName. Leave it out to
              keep the current label, or send null to remove it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._put(
            path_template("/monitors/username/{username}", username=username),
            body=maybe_transform(
                {
                    "event_types": event_types,
                    "name": name,
                },
                monitor_upsert_by_username_params.MonitorUpsertByUsernameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorUpsertByUsernameResponse,
        )


class AsyncMonitorsResource(AsyncAPIResource):
    """X account monitoring with 1-second checks"""

    @cached_property
    def keywords(self) -> AsyncKeywordsResource:
        """X account monitoring with 1-second checks"""
        return AsyncKeywordsResource(self._client)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        """Post monitoring with replies, quotes, edits, deletion & 6 metrics"""
        return AsyncPostsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMonitorsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncMonitorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncMonitorsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        event_types: List[EventType],
        username: str,
        name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorCreateResponse:
        """Creates an account monitor, with no count limit.

        Active monitors check every
        second for 30 credits an hour, events & webhook deliveries included. That hourly
        price is a monitor's only charge. Creation needs the credits of the first hour.

        Args:
          event_types: Array of event types to subscribe to.

          username: X username to monitor, with or without @

          name: Your label for the monitor. Its events carry it as monitorName. Whitespace is
              normalized.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/monitors",
            body=await async_maybe_transform(
                {
                    "event_types": event_types,
                    "username": username,
                    "name": name,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Returns configuration and status for one account monitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/monitors/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    async def update(
        self,
        id: str,
        *,
        event_types: List[EventType] | Omit = omit,
        is_active: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Updates mutable settings for an existing account monitor.

        Args:
          event_types: Array of event types to subscribe to.

          name: New label for the account monitor. Send null to remove the label.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/monitors/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "event_types": event_types,
                    "is_active": is_active,
                    "name": name,
                },
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorListResponse:
        """
        Returns account monitors with their current operating states.

        Args:
          cursor: Previous nextCursor. The after alias also works. Offset pagination is not
              supported.

          limit: Maximum items per page: 1 to 200, default 200. Pass nextCursor as cursor for the
              next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    monitor_list_params.MonitorListParams,
                ),
            ),
            cast_to=MonitorListResponse,
        )

    async def deactivate(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorDeactivateResponse:
        """
        Stops one account monitor, then removes its stored events in bounded batches.
        Poll statusUrl until the monitor returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/monitors/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorDeactivateResponse,
        )

    async def upsert_by_username(
        self,
        username: str,
        *,
        event_types: List[EventType],
        name: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitorUpsertByUsernameResponse:
        """Creates the monitor if it does not exist, or updates it if it does.

        Send the same
        call twice & you still have 1 monitor. A new monitor answers 201 & an update
        answers 200. Both carry `created`, so you know which one ran. Creating needs the
        credits of the first hour, then costs 30 credits an hour. A stopped monitor
        turns back on & counts as created. Updating is free & replaces the event types.
        It changes the name only when you send one.

        Args:
          username: The account's X username, with or without @, or its numeric user ID. A number
              is a user ID, so this call matches the account even after a rename.

          event_types: Array of event types to subscribe to.

          name: Your label for the monitor. Its events carry it as monitorName. Leave it out to
              keep the current label, or send null to remove it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._put(
            path_template("/monitors/username/{username}", username=username),
            body=await async_maybe_transform(
                {
                    "event_types": event_types,
                    "name": name,
                },
                monitor_upsert_by_username_params.MonitorUpsertByUsernameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorUpsertByUsernameResponse,
        )


class MonitorsResourceWithRawResponse:
    def __init__(self, monitors: MonitorsResource) -> None:
        self._monitors = monitors

        self.create = to_raw_response_wrapper(
            monitors.create,
        )
        self.retrieve = to_raw_response_wrapper(
            monitors.retrieve,
        )
        self.update = to_raw_response_wrapper(
            monitors.update,
        )
        self.list = to_raw_response_wrapper(
            monitors.list,
        )
        self.deactivate = to_raw_response_wrapper(
            monitors.deactivate,
        )
        self.upsert_by_username = to_raw_response_wrapper(
            monitors.upsert_by_username,
        )

    @cached_property
    def keywords(self) -> KeywordsResourceWithRawResponse:
        """X account monitoring with 1-second checks"""
        return KeywordsResourceWithRawResponse(self._monitors.keywords)

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        """Post monitoring with replies, quotes, edits, deletion & 6 metrics"""
        return PostsResourceWithRawResponse(self._monitors.posts)


class AsyncMonitorsResourceWithRawResponse:
    def __init__(self, monitors: AsyncMonitorsResource) -> None:
        self._monitors = monitors

        self.create = async_to_raw_response_wrapper(
            monitors.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            monitors.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            monitors.update,
        )
        self.list = async_to_raw_response_wrapper(
            monitors.list,
        )
        self.deactivate = async_to_raw_response_wrapper(
            monitors.deactivate,
        )
        self.upsert_by_username = async_to_raw_response_wrapper(
            monitors.upsert_by_username,
        )

    @cached_property
    def keywords(self) -> AsyncKeywordsResourceWithRawResponse:
        """X account monitoring with 1-second checks"""
        return AsyncKeywordsResourceWithRawResponse(self._monitors.keywords)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        """Post monitoring with replies, quotes, edits, deletion & 6 metrics"""
        return AsyncPostsResourceWithRawResponse(self._monitors.posts)


class MonitorsResourceWithStreamingResponse:
    def __init__(self, monitors: MonitorsResource) -> None:
        self._monitors = monitors

        self.create = to_streamed_response_wrapper(
            monitors.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            monitors.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            monitors.update,
        )
        self.list = to_streamed_response_wrapper(
            monitors.list,
        )
        self.deactivate = to_streamed_response_wrapper(
            monitors.deactivate,
        )
        self.upsert_by_username = to_streamed_response_wrapper(
            monitors.upsert_by_username,
        )

    @cached_property
    def keywords(self) -> KeywordsResourceWithStreamingResponse:
        """X account monitoring with 1-second checks"""
        return KeywordsResourceWithStreamingResponse(self._monitors.keywords)

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        """Post monitoring with replies, quotes, edits, deletion & 6 metrics"""
        return PostsResourceWithStreamingResponse(self._monitors.posts)


class AsyncMonitorsResourceWithStreamingResponse:
    def __init__(self, monitors: AsyncMonitorsResource) -> None:
        self._monitors = monitors

        self.create = async_to_streamed_response_wrapper(
            monitors.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            monitors.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            monitors.update,
        )
        self.list = async_to_streamed_response_wrapper(
            monitors.list,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            monitors.deactivate,
        )
        self.upsert_by_username = async_to_streamed_response_wrapper(
            monitors.upsert_by_username,
        )

    @cached_property
    def keywords(self) -> AsyncKeywordsResourceWithStreamingResponse:
        """X account monitoring with 1-second checks"""
        return AsyncKeywordsResourceWithStreamingResponse(self._monitors.keywords)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        """Post monitoring with replies, quotes, edits, deletion & 6 metrics"""
        return AsyncPostsResourceWithStreamingResponse(self._monitors.posts)
