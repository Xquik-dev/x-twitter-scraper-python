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
from ...types.monitors import keyword_list_params, keyword_create_params, keyword_update_params
from ...types.shared.event_type import EventType
from ...types.monitors.keyword_list_response import KeywordListResponse
from ...types.monitors.keyword_create_response import KeywordCreateResponse
from ...types.monitors.keyword_update_response import KeywordUpdateResponse
from ...types.monitors.keyword_retrieve_response import KeywordRetrieveResponse
from ...types.monitors.keyword_deactivate_response import KeywordDeactivateResponse

__all__ = ["KeywordsResource", "AsyncKeywordsResource"]


class KeywordsResource(SyncAPIResource):
    """X account monitoring with 1-second checks"""

    @cached_property
    def with_raw_response(self) -> KeywordsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return KeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return KeywordsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        event_types: List[EventType],
        query: str,
        name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordCreateResponse:
        """Creates a keyword monitor, with no count limit.

        Active monitors check every
        second for 30 credits an hour, events & webhook deliveries included. That hourly
        price is a monitor's only charge. Creation needs the credits of the first hour.

        Args:
          event_types: Array of event types to subscribe to.

          query: X search query to monitor. Whitespace is normalized.

          name: Your own label for the keyword monitor. Its events carry it as monitorName.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/monitors/keywords",
            body=maybe_transform(
                {
                    "event_types": event_types,
                    "query": query,
                    "name": name,
                },
                keyword_create_params.KeywordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordRetrieveResponse:
        """
        Returns configuration and status for one keyword monitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/monitors/keywords/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordRetrieveResponse,
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
    ) -> KeywordUpdateResponse:
        """
        Updates mutable settings for an existing keyword monitor.

        Args:
          event_types: Array of event types to subscribe to.

          name: New label for the keyword monitor. Send null to remove it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/monitors/keywords/{id}", id=id),
            body=maybe_transform(
                {
                    "event_types": event_types,
                    "is_active": is_active,
                    "name": name,
                },
                keyword_update_params.KeywordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordUpdateResponse,
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
    ) -> KeywordListResponse:
        """
        Returns keyword monitors with their current operating states.

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
            "/monitors/keywords",
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
                    keyword_list_params.KeywordListParams,
                ),
            ),
            cast_to=KeywordListResponse,
        )

    def deactivate(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordDeactivateResponse:
        """
        Stops one keyword monitor, then removes its stored events in bounded batches.
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
            path_template("/monitors/keywords/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordDeactivateResponse,
        )


class AsyncKeywordsResource(AsyncAPIResource):
    """X account monitoring with 1-second checks"""

    @cached_property
    def with_raw_response(self) -> AsyncKeywordsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncKeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncKeywordsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        event_types: List[EventType],
        query: str,
        name: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordCreateResponse:
        """Creates a keyword monitor, with no count limit.

        Active monitors check every
        second for 30 credits an hour, events & webhook deliveries included. That hourly
        price is a monitor's only charge. Creation needs the credits of the first hour.

        Args:
          event_types: Array of event types to subscribe to.

          query: X search query to monitor. Whitespace is normalized.

          name: Your own label for the keyword monitor. Its events carry it as monitorName.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/monitors/keywords",
            body=await async_maybe_transform(
                {
                    "event_types": event_types,
                    "query": query,
                    "name": name,
                },
                keyword_create_params.KeywordCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordRetrieveResponse:
        """
        Returns configuration and status for one keyword monitor.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/monitors/keywords/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordRetrieveResponse,
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
    ) -> KeywordUpdateResponse:
        """
        Updates mutable settings for an existing keyword monitor.

        Args:
          event_types: Array of event types to subscribe to.

          name: New label for the keyword monitor. Send null to remove it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/monitors/keywords/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "event_types": event_types,
                    "is_active": is_active,
                    "name": name,
                },
                keyword_update_params.KeywordUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordUpdateResponse,
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
    ) -> KeywordListResponse:
        """
        Returns keyword monitors with their current operating states.

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
            "/monitors/keywords",
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
                    keyword_list_params.KeywordListParams,
                ),
            ),
            cast_to=KeywordListResponse,
        )

    async def deactivate(
        self,
        id: str,
        *,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeywordDeactivateResponse:
        """
        Stops one keyword monitor, then removes its stored events in bounded batches.
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
            path_template("/monitors/keywords/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordDeactivateResponse,
        )


class KeywordsResourceWithRawResponse:
    def __init__(self, keywords: KeywordsResource) -> None:
        self._keywords = keywords

        self.create = to_raw_response_wrapper(
            keywords.create,
        )
        self.retrieve = to_raw_response_wrapper(
            keywords.retrieve,
        )
        self.update = to_raw_response_wrapper(
            keywords.update,
        )
        self.list = to_raw_response_wrapper(
            keywords.list,
        )
        self.deactivate = to_raw_response_wrapper(
            keywords.deactivate,
        )


class AsyncKeywordsResourceWithRawResponse:
    def __init__(self, keywords: AsyncKeywordsResource) -> None:
        self._keywords = keywords

        self.create = async_to_raw_response_wrapper(
            keywords.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            keywords.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            keywords.update,
        )
        self.list = async_to_raw_response_wrapper(
            keywords.list,
        )
        self.deactivate = async_to_raw_response_wrapper(
            keywords.deactivate,
        )


class KeywordsResourceWithStreamingResponse:
    def __init__(self, keywords: KeywordsResource) -> None:
        self._keywords = keywords

        self.create = to_streamed_response_wrapper(
            keywords.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            keywords.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            keywords.update,
        )
        self.list = to_streamed_response_wrapper(
            keywords.list,
        )
        self.deactivate = to_streamed_response_wrapper(
            keywords.deactivate,
        )


class AsyncKeywordsResourceWithStreamingResponse:
    def __init__(self, keywords: AsyncKeywordsResource) -> None:
        self._keywords = keywords

        self.create = async_to_streamed_response_wrapper(
            keywords.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            keywords.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            keywords.update,
        )
        self.list = async_to_streamed_response_wrapper(
            keywords.list,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            keywords.deactivate,
        )
