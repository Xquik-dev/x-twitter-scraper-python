# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import broadcast_retrieve_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.broadcast_retrieve_response import BroadcastRetrieveResponse

__all__ = ["BroadcastsResource", "AsyncBroadcastsResource"]


class BroadcastsResource(SyncAPIResource):
    """X live video details, watch counts, and broadcaster"""

    @cached_property
    def with_raw_response(self) -> BroadcastsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return BroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return BroadcastsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastRetrieveResponse:
        """
        Returns one X broadcast, the live video X hosts at x.com/i/broadcasts, live or
        ended. Accepts the broadcast ID or the URL-encoded broadcast URL. Reading a
        broadcast adds no view to it.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/broadcasts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    broadcast_retrieve_params.BroadcastRetrieveParams,
                ),
            ),
            cast_to=BroadcastRetrieveResponse,
        )


class AsyncBroadcastsResource(AsyncAPIResource):
    """X live video details, watch counts, and broadcaster"""

    @cached_property
    def with_raw_response(self) -> AsyncBroadcastsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncBroadcastsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBroadcastsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncBroadcastsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BroadcastRetrieveResponse:
        """
        Returns one X broadcast, the live video X hosts at x.com/i/broadcasts, live or
        ended. Accepts the broadcast ID or the URL-encoded broadcast URL. Reading a
        broadcast adds no view to it.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/broadcasts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    broadcast_retrieve_params.BroadcastRetrieveParams,
                ),
            ),
            cast_to=BroadcastRetrieveResponse,
        )


class BroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.retrieve = to_raw_response_wrapper(
            broadcasts.retrieve,
        )


class AsyncBroadcastsResourceWithRawResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.retrieve = async_to_raw_response_wrapper(
            broadcasts.retrieve,
        )


class BroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: BroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.retrieve = to_streamed_response_wrapper(
            broadcasts.retrieve,
        )


class AsyncBroadcastsResourceWithStreamingResponse:
    def __init__(self, broadcasts: AsyncBroadcastsResource) -> None:
        self._broadcasts = broadcasts

        self.retrieve = async_to_streamed_response_wrapper(
            broadcasts.retrieve,
        )
