# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import activity_list_params, activity_export_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.activity_record import ActivityRecord
from ..types.activity_list_response import ActivityListResponse

__all__ = ["ActivityResource", "AsyncActivityResource"]


class ActivityResource(SyncAPIResource):
    """Account activity log"""

    @cached_property
    def with_raw_response(self) -> ActivityResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return ActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return ActivityResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        category: str | Omit = omit,
        format: Literal["json"] | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActivityListResponse:
        """
        Returns the account's activity log, newest first, with the Activity page's
        filters. It covers write actions, extractions, monitor changes and events,
        webhooks, giveaways, media, support, API keys, X account connections and
        billing.

        Args:
          category: Activity group, like the Activity page's tabs. `all` by default, or `actions`,
              `extractions`, `monitors`, `webhooks` or `billing`.

          format: Leave it out or pass json to get the rows. Use export for a file.

          limit: Most rows to return, from 1 to 100,000. 100 by default.

          q: Search text.

          since: Oldest time, ISO 8601.

          status: Comma-separated statuses.

          until: Newest time, ISO 8601.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "format": format,
                        "limit": limit,
                        "q": q,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    activity_list_params.ActivityListParams,
                ),
            ),
            cast_to=ActivityListResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActivityRecord:
        """
        Returns 1 activity of the account with its full technical record. It covers
        every kind of activity the Activity log shows. The record holds the request,
        the caller, the charge, every timestamp in UTC and related activity. It never
        holds an API key value, a webhook secret or another account's data. Only a
        signed-in dashboard session sees an `api_key` record, so an API key or an OAuth
        app gets 404 for its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/activity/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActivityRecord,
        )

    def export(
        self,
        *,
        format: Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"],
        category: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Downloads the activity log rows as a CSV, Excel, JSON, Markdown, PDF or text
        file, with the same filters as list.

        Args:
          format: File format. PDF stops at 10,000 rows.

          category: Activity group, like the Activity page's tabs. `all` by default, or `actions`,
              `extractions`, `monitors`, `webhooks` or `billing`.

          limit: Most rows to return, from 1 to 100,000. 100 by default.

          q: Search text.

          since: Oldest time, ISO 8601.

          status: Comma-separated statuses.

          until: Newest time, ISO 8601.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or dict[str, str | Omit]())}
        return self._get(
            "/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "category": category,
                        "limit": limit,
                        "q": q,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    activity_export_params.ActivityExportParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncActivityResource(AsyncAPIResource):
    """Account activity log"""

    @cached_property
    def with_raw_response(self) -> AsyncActivityResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncActivityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncActivityResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        category: str | Omit = omit,
        format: Literal["json"] | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActivityListResponse:
        """
        Returns the account's activity log, newest first, with the Activity page's
        filters. It covers write actions, extractions, monitor changes and events,
        webhooks, giveaways, media, support, API keys, X account connections and
        billing.

        Args:
          category: Activity group, like the Activity page's tabs. `all` by default, or `actions`,
              `extractions`, `monitors`, `webhooks` or `billing`.

          format: Leave it out or pass json to get the rows. Use export for a file.

          limit: Most rows to return, from 1 to 100,000. 100 by default.

          q: Search text.

          since: Oldest time, ISO 8601.

          status: Comma-separated statuses.

          until: Newest time, ISO 8601.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "format": format,
                        "limit": limit,
                        "q": q,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    activity_list_params.ActivityListParams,
                ),
            ),
            cast_to=ActivityListResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActivityRecord:
        """
        Returns 1 activity of the account with its full technical record. It covers
        every kind of activity the Activity log shows. The record holds the request,
        the caller, the charge, every timestamp in UTC and related activity. It never
        holds an API key value, a webhook secret or another account's data. Only a
        signed-in dashboard session sees an `api_key` record, so an API key or an OAuth
        app gets 404 for its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/activity/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActivityRecord,
        )

    async def export(
        self,
        *,
        format: Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"],
        category: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Downloads the activity log rows as a CSV, Excel, JSON, Markdown, PDF or text
        file, with the same filters as list.

        Args:
          format: File format. PDF stops at 10,000 rows.

          category: Activity group, like the Activity page's tabs. `all` by default, or `actions`,
              `extractions`, `monitors`, `webhooks` or `billing`.

          limit: Most rows to return, from 1 to 100,000. 100 by default.

          q: Search text.

          since: Oldest time, ISO 8601.

          status: Comma-separated statuses.

          until: Newest time, ISO 8601.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or dict[str, str | Omit]())}
        return await self._get(
            "/activity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "category": category,
                        "limit": limit,
                        "q": q,
                        "since": since,
                        "status": status,
                        "until": until,
                    },
                    activity_export_params.ActivityExportParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ActivityResourceWithRawResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.list = to_raw_response_wrapper(
            activity.list,
        )
        self.retrieve = to_raw_response_wrapper(
            activity.retrieve,
        )
        self.export = to_custom_raw_response_wrapper(
            activity.export,
            BinaryAPIResponse,
        )


class AsyncActivityResourceWithRawResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.list = async_to_raw_response_wrapper(
            activity.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            activity.retrieve,
        )
        self.export = async_to_custom_raw_response_wrapper(
            activity.export,
            AsyncBinaryAPIResponse,
        )


class ActivityResourceWithStreamingResponse:
    def __init__(self, activity: ActivityResource) -> None:
        self._activity = activity

        self.list = to_streamed_response_wrapper(
            activity.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            activity.retrieve,
        )
        self.export = to_custom_streamed_response_wrapper(
            activity.export,
            StreamedBinaryAPIResponse,
        )


class AsyncActivityResourceWithStreamingResponse:
    def __init__(self, activity: AsyncActivityResource) -> None:
        self._activity = activity

        self.list = async_to_streamed_response_wrapper(
            activity.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            activity.retrieve,
        )
        self.export = async_to_custom_streamed_response_wrapper(
            activity.export,
            AsyncStreamedBinaryAPIResponse,
        )
