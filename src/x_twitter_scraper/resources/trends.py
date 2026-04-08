# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import trend_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.trend_list_response import TrendListResponse

__all__ = ["TrendsResource", "AsyncTrendsResource"]


class TrendsResource(SyncAPIResource):
    """Trending topics by region"""

    @cached_property
    def with_raw_response(self) -> TrendsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return TrendsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrendsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return TrendsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        count: int | Omit = omit,
        woeid: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrendListResponse:
        """
        Get regional trending topics

        Args:
          count: Number of trending topics to return (1-50, default 30)

          woeid: Region WOEID (1=Worldwide, 23424977=US, 23424975=UK, 23424969=Turkey)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/trends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "count": count,
                        "woeid": woeid,
                    },
                    trend_list_params.TrendListParams,
                ),
            ),
            cast_to=TrendListResponse,
        )


class AsyncTrendsResource(AsyncAPIResource):
    """Trending topics by region"""

    @cached_property
    def with_raw_response(self) -> AsyncTrendsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrendsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrendsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncTrendsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        count: int | Omit = omit,
        woeid: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrendListResponse:
        """
        Get regional trending topics

        Args:
          count: Number of trending topics to return (1-50, default 30)

          woeid: Region WOEID (1=Worldwide, 23424977=US, 23424975=UK, 23424969=Turkey)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/trends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "count": count,
                        "woeid": woeid,
                    },
                    trend_list_params.TrendListParams,
                ),
            ),
            cast_to=TrendListResponse,
        )


class TrendsResourceWithRawResponse:
    def __init__(self, trends: TrendsResource) -> None:
        self._trends = trends

        self.list = to_raw_response_wrapper(
            trends.list,
        )


class AsyncTrendsResourceWithRawResponse:
    def __init__(self, trends: AsyncTrendsResource) -> None:
        self._trends = trends

        self.list = async_to_raw_response_wrapper(
            trends.list,
        )


class TrendsResourceWithStreamingResponse:
    def __init__(self, trends: TrendsResource) -> None:
        self._trends = trends

        self.list = to_streamed_response_wrapper(
            trends.list,
        )


class AsyncTrendsResourceWithStreamingResponse:
    def __init__(self, trends: AsyncTrendsResource) -> None:
        self._trends = trends

        self.list = async_to_streamed_response_wrapper(
            trends.list,
        )
