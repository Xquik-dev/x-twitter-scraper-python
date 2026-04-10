# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import radar_retrieve_trending_topics_params
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
from ..types.radar_retrieve_trending_topics_response import RadarRetrieveTrendingTopicsResponse

__all__ = ["RadarResource", "AsyncRadarResource"]


class RadarResource(SyncAPIResource):
    """AI tweet composition, drafts, writing styles, and radar"""

    @cached_property
    def with_raw_response(self) -> RadarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return RadarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RadarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return RadarResourceWithStreamingResponse(self)

    def retrieve_trending_topics(
        self,
        *,
        category: str | Omit = omit,
        count: int | Omit = omit,
        hours: int | Omit = omit,
        region: str | Omit = omit,
        source: Literal["github", "google_trends", "hacker_news", "polymarket", "reddit", "trustmrr", "wikipedia"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RadarRetrieveTrendingTopicsResponse:
        """
        Get trending topics from curated sources

        Args:
          category: Filter by category (general, tech, dev, etc.)

          count: Number of items to return

          hours: Lookback window in hours

          region: Region filter (us, global, etc.)

          source: Source filter. One of: github, google_trends, hacker_news, polymarket, reddit,
              trustmrr, wikipedia

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "count": count,
                        "hours": hours,
                        "region": region,
                        "source": source,
                    },
                    radar_retrieve_trending_topics_params.RadarRetrieveTrendingTopicsParams,
                ),
            ),
            cast_to=RadarRetrieveTrendingTopicsResponse,
        )


class AsyncRadarResource(AsyncAPIResource):
    """AI tweet composition, drafts, writing styles, and radar"""

    @cached_property
    def with_raw_response(self) -> AsyncRadarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRadarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRadarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncRadarResourceWithStreamingResponse(self)

    async def retrieve_trending_topics(
        self,
        *,
        category: str | Omit = omit,
        count: int | Omit = omit,
        hours: int | Omit = omit,
        region: str | Omit = omit,
        source: Literal["github", "google_trends", "hacker_news", "polymarket", "reddit", "trustmrr", "wikipedia"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RadarRetrieveTrendingTopicsResponse:
        """
        Get trending topics from curated sources

        Args:
          category: Filter by category (general, tech, dev, etc.)

          count: Number of items to return

          hours: Lookback window in hours

          region: Region filter (us, global, etc.)

          source: Source filter. One of: github, google_trends, hacker_news, polymarket, reddit,
              trustmrr, wikipedia

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "count": count,
                        "hours": hours,
                        "region": region,
                        "source": source,
                    },
                    radar_retrieve_trending_topics_params.RadarRetrieveTrendingTopicsParams,
                ),
            ),
            cast_to=RadarRetrieveTrendingTopicsResponse,
        )


class RadarResourceWithRawResponse:
    def __init__(self, radar: RadarResource) -> None:
        self._radar = radar

        self.retrieve_trending_topics = to_raw_response_wrapper(
            radar.retrieve_trending_topics,
        )


class AsyncRadarResourceWithRawResponse:
    def __init__(self, radar: AsyncRadarResource) -> None:
        self._radar = radar

        self.retrieve_trending_topics = async_to_raw_response_wrapper(
            radar.retrieve_trending_topics,
        )


class RadarResourceWithStreamingResponse:
    def __init__(self, radar: RadarResource) -> None:
        self._radar = radar

        self.retrieve_trending_topics = to_streamed_response_wrapper(
            radar.retrieve_trending_topics,
        )


class AsyncRadarResourceWithStreamingResponse:
    def __init__(self, radar: AsyncRadarResource) -> None:
        self._radar = radar

        self.retrieve_trending_topics = async_to_streamed_response_wrapper(
            radar.retrieve_trending_topics,
        )
