# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import List, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.monitors import post_list_params, post_create_params, post_update_params, post_retrieve_metrics_params
from ...types.monitors.post_monitor import PostMonitor, PostEventType, PostMonitorMetrics
from ...types.monitors.post_list_response import PostListResponse
from ...types.monitors.post_delete_response import PostDeleteResponse

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    """Post monitoring with replies, quotes, edits, deletion & 6 metrics"""

    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return PostsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        post: str,
        event_types: List[PostEventType] | Omit = omit,
        name: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostMonitor:
        """
        Creates a monitor for 1 X post. It tracks replies, quotes, edits, deletion & 6
        metrics, for 30 credits an hour with events & webhook deliveries included. That
        hourly price is a monitor's only charge. Creation needs the credits of the first
        hour & reads the post once.

        Args:
          post: Post link or ID. x.com, twitter.com, mobile & /i/web/status/ links work
              with any query string.

          event_types: Post event types to send. Without it, a monitor sends new replies,
              new quotes, like & retweet changes, edits & deletion.

          name: Your own label for the post monitor. Its events carry it as monitorName.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/monitors/posts",
            body=maybe_transform(
                {
                    "post": post,
                    "event_types": event_types,
                    "name": name,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostMonitor,
        )

    def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostMonitor:
        """
        Returns 1 post monitor with its post & the 6 metrics, each with its current
        value & gain since tracking began.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/monitors/posts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostMonitor,
        )

    def update(
        self,
        id: str,
        *,
        event_types: List[PostEventType] | Omit = omit,
        is_active: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostMonitor:
        """
        Updates a post monitor's label, event types or active state. Turning a paused
        monitor on reads the post first, & answers 409 while X hides it.

        Args:
          event_types: Post event types to send. Without it, a monitor sends new replies,
              new quotes, like & retweet changes, edits & deletion.

          is_active: Turns the monitor on or off.

          name: New label for the post monitor. Send null to remove it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/monitors/posts/{id}", id=id),
            body=maybe_transform(
                {
                    "event_types": event_types,
                    "is_active": is_active,
                    "name": name,
                },
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostMonitor,
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
    ) -> PostListResponse:
        """
        Returns post monitors with each post's 6 metrics, their current values & gains
        since tracking began.

        Args:
          cursor: Previous nextCursor. The after alias also works. Offset pagination is
              not supported.

          limit: Maximum items per page, from 1 to 200. Default 200. Pass nextCursor as
              cursor for the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/monitors/posts",
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
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostDeleteResponse:
        """
        Stops 1 post monitor, then removes its stored events & metric history in bounded
        batches. Poll statusUrl until the monitor returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/monitors/posts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostDeleteResponse,
        )

    def retrieve_metrics(
        self,
        id: str,
        *,
        hours: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostMonitorMetrics:
        """
        Returns 1 bucket per hour with each metric's value at the hour's end & its gain
        over that hour. The last bucket is the current hour. Hours before tracking began
        carry the starting values with a gain of 0.

        Args:
          hours: Hours to return, from 1 to 720.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/monitors/posts/{id}/metrics", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "hours": hours,
                    },
                    post_retrieve_metrics_params.PostRetrieveMetricsParams,
                ),
            ),
            cast_to=PostMonitorMetrics,
        )


class AsyncPostsResource(AsyncAPIResource):
    """Post monitoring with replies, quotes, edits, deletion & 6 metrics"""

    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncPostsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        post: str,
        event_types: List[PostEventType] | Omit = omit,
        name: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostMonitor:
        """
        Creates a monitor for 1 X post. It tracks replies, quotes, edits, deletion & 6
        metrics, for 30 credits an hour with events & webhook deliveries included. That
        hourly price is a monitor's only charge. Creation needs the credits of the first
        hour & reads the post once.

        Args:
          post: Post link or ID. x.com, twitter.com, mobile & /i/web/status/ links work
              with any query string.

          event_types: Post event types to send. Without it, a monitor sends new replies,
              new quotes, like & retweet changes, edits & deletion.

          name: Your own label for the post monitor. Its events carry it as monitorName.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/monitors/posts",
            body=await async_maybe_transform(
                {
                    "post": post,
                    "event_types": event_types,
                    "name": name,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostMonitor,
        )

    async def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostMonitor:
        """
        Returns 1 post monitor with its post & the 6 metrics, each with its current
        value & gain since tracking began.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/monitors/posts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostMonitor,
        )

    async def update(
        self,
        id: str,
        *,
        event_types: List[PostEventType] | Omit = omit,
        is_active: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostMonitor:
        """
        Updates a post monitor's label, event types or active state. Turning a paused
        monitor on reads the post first, & answers 409 while X hides it.

        Args:
          event_types: Post event types to send. Without it, a monitor sends new replies,
              new quotes, like & retweet changes, edits & deletion.

          is_active: Turns the monitor on or off.

          name: New label for the post monitor. Send null to remove it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/monitors/posts/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "event_types": event_types,
                    "is_active": is_active,
                    "name": name,
                },
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostMonitor,
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
    ) -> PostListResponse:
        """
        Returns post monitors with each post's 6 metrics, their current values & gains
        since tracking began.

        Args:
          cursor: Previous nextCursor. The after alias also works. Offset pagination is
              not supported.

          limit: Maximum items per page, from 1 to 200. Default 200. Pass nextCursor as
              cursor for the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/monitors/posts",
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
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostDeleteResponse:
        """
        Stops 1 post monitor, then removes its stored events & metric history in bounded
        batches. Poll statusUrl until the monitor returns 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/monitors/posts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostDeleteResponse,
        )

    async def retrieve_metrics(
        self,
        id: str,
        *,
        hours: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostMonitorMetrics:
        """
        Returns 1 bucket per hour with each metric's value at the hour's end & its gain
        over that hour. The last bucket is the current hour. Hours before tracking began
        carry the starting values with a gain of 0.

        Args:
          hours: Hours to return, from 1 to 720.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/monitors/posts/{id}/metrics", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "hours": hours,
                    },
                    post_retrieve_metrics_params.PostRetrieveMetricsParams,
                ),
            ),
            cast_to=PostMonitorMetrics,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_raw_response_wrapper(
            posts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            posts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            posts.update,
        )
        self.list = to_raw_response_wrapper(
            posts.list,
        )
        self.delete = to_raw_response_wrapper(
            posts.delete,
        )
        self.retrieve_metrics = to_raw_response_wrapper(
            posts.retrieve_metrics,
        )


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_raw_response_wrapper(
            posts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            posts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            posts.update,
        )
        self.list = async_to_raw_response_wrapper(
            posts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            posts.delete,
        )
        self.retrieve_metrics = async_to_raw_response_wrapper(
            posts.retrieve_metrics,
        )


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_streamed_response_wrapper(
            posts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            posts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            posts.update,
        )
        self.list = to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = to_streamed_response_wrapper(
            posts.delete,
        )
        self.retrieve_metrics = to_streamed_response_wrapper(
            posts.retrieve_metrics,
        )


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_streamed_response_wrapper(
            posts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            posts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            posts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            posts.delete,
        )
        self.retrieve_metrics = async_to_streamed_response_wrapper(
            posts.retrieve_metrics,
        )
