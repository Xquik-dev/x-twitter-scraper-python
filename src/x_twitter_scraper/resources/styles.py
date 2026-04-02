# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import style_analyze_params, style_compare_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.style_list_response import StyleListResponse
from ..types.style_analyze_response import StyleAnalyzeResponse
from ..types.style_compare_response import StyleCompareResponse

__all__ = ["StylesResource", "AsyncStylesResource"]


class StylesResource(SyncAPIResource):
    """Tweet composition, drafts, writing styles & radar"""

    @cached_property
    def with_raw_response(self) -> StylesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return StylesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StylesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return StylesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleListResponse:
        """List cached style profiles"""
        return self._get(
            "/styles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleListResponse,
        )

    def analyze(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleAnalyzeResponse:
        """
        Analyze writing style from recent tweets

        Args:
          username: X username to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/styles",
            body=maybe_transform({"username": username}, style_analyze_params.StyleAnalyzeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleAnalyzeResponse,
        )

    def compare(
        self,
        *,
        username1: str,
        username2: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleCompareResponse:
        """
        Compare two style profiles

        Args:
          username1: First username to compare

          username2: Second username to compare

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/styles/compare",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "username1": username1,
                        "username2": username2,
                    },
                    style_compare_params.StyleCompareParams,
                ),
            ),
            cast_to=StyleCompareResponse,
        )


class AsyncStylesResource(AsyncAPIResource):
    """Tweet composition, drafts, writing styles & radar"""

    @cached_property
    def with_raw_response(self) -> AsyncStylesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStylesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStylesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncStylesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleListResponse:
        """List cached style profiles"""
        return await self._get(
            "/styles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleListResponse,
        )

    async def analyze(
        self,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleAnalyzeResponse:
        """
        Analyze writing style from recent tweets

        Args:
          username: X username to analyze

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/styles",
            body=await async_maybe_transform({"username": username}, style_analyze_params.StyleAnalyzeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleAnalyzeResponse,
        )

    async def compare(
        self,
        *,
        username1: str,
        username2: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleCompareResponse:
        """
        Compare two style profiles

        Args:
          username1: First username to compare

          username2: Second username to compare

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/styles/compare",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "username1": username1,
                        "username2": username2,
                    },
                    style_compare_params.StyleCompareParams,
                ),
            ),
            cast_to=StyleCompareResponse,
        )


class StylesResourceWithRawResponse:
    def __init__(self, styles: StylesResource) -> None:
        self._styles = styles

        self.list = to_raw_response_wrapper(
            styles.list,
        )
        self.analyze = to_raw_response_wrapper(
            styles.analyze,
        )
        self.compare = to_raw_response_wrapper(
            styles.compare,
        )


class AsyncStylesResourceWithRawResponse:
    def __init__(self, styles: AsyncStylesResource) -> None:
        self._styles = styles

        self.list = async_to_raw_response_wrapper(
            styles.list,
        )
        self.analyze = async_to_raw_response_wrapper(
            styles.analyze,
        )
        self.compare = async_to_raw_response_wrapper(
            styles.compare,
        )


class StylesResourceWithStreamingResponse:
    def __init__(self, styles: StylesResource) -> None:
        self._styles = styles

        self.list = to_streamed_response_wrapper(
            styles.list,
        )
        self.analyze = to_streamed_response_wrapper(
            styles.analyze,
        )
        self.compare = to_streamed_response_wrapper(
            styles.compare,
        )


class AsyncStylesResourceWithStreamingResponse:
    def __init__(self, styles: AsyncStylesResource) -> None:
        self._styles = styles

        self.list = async_to_streamed_response_wrapper(
            styles.list,
        )
        self.analyze = async_to_streamed_response_wrapper(
            styles.analyze,
        )
        self.compare = async_to_streamed_response_wrapper(
            styles.compare,
        )
