# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import style_update_params, style_analyze_params, style_compare_params
from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.style_profile import StyleProfile
from ..types.style_list_response import StyleListResponse
from ..types.style_compare_response import StyleCompareResponse
from ..types.style_get_performance_response import StyleGetPerformanceResponse

__all__ = ["StylesResource", "AsyncStylesResource"]


class StylesResource(SyncAPIResource):
    """Tweet composition, drafts, writing styles & radar"""

    @cached_property
    def with_raw_response(self) -> StylesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return StylesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StylesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return StylesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleProfile:
        """
        Get cached style profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            path_template("/styles/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleProfile,
        )

    def update(
        self,
        username: str,
        *,
        label: str,
        tweets: Iterable[style_update_params.Tweet],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleProfile:
        """
        Save style profile with custom tweets

        Args:
          label: Display label for the style

          tweets: Array of tweet objects

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._put(
            path_template("/styles/{username}", username=username),
            body=maybe_transform(
                {
                    "label": label,
                    "tweets": tweets,
                },
                style_update_params.StyleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleProfile,
        )

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

    def delete(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a style profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/styles/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> StyleProfile:
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
            cast_to=StyleProfile,
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

    def get_performance(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleGetPerformanceResponse:
        """
        Get engagement metrics for style tweets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            path_template("/styles/{username}/performance", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleGetPerformanceResponse,
        )


class AsyncStylesResource(AsyncAPIResource):
    """Tweet composition, drafts, writing styles & radar"""

    @cached_property
    def with_raw_response(self) -> AsyncStylesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStylesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStylesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncStylesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleProfile:
        """
        Get cached style profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            path_template("/styles/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleProfile,
        )

    async def update(
        self,
        username: str,
        *,
        label: str,
        tweets: Iterable[style_update_params.Tweet],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleProfile:
        """
        Save style profile with custom tweets

        Args:
          label: Display label for the style

          tweets: Array of tweet objects

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._put(
            path_template("/styles/{username}", username=username),
            body=await async_maybe_transform(
                {
                    "label": label,
                    "tweets": tweets,
                },
                style_update_params.StyleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleProfile,
        )

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

    async def delete(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a style profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/styles/{username}", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> StyleProfile:
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
            cast_to=StyleProfile,
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

    async def get_performance(
        self,
        username: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleGetPerformanceResponse:
        """
        Get engagement metrics for style tweets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            path_template("/styles/{username}/performance", username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StyleGetPerformanceResponse,
        )


class StylesResourceWithRawResponse:
    def __init__(self, styles: StylesResource) -> None:
        self._styles = styles

        self.retrieve = to_raw_response_wrapper(
            styles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            styles.update,
        )
        self.list = to_raw_response_wrapper(
            styles.list,
        )
        self.delete = to_raw_response_wrapper(
            styles.delete,
        )
        self.analyze = to_raw_response_wrapper(
            styles.analyze,
        )
        self.compare = to_raw_response_wrapper(
            styles.compare,
        )
        self.get_performance = to_raw_response_wrapper(
            styles.get_performance,
        )


class AsyncStylesResourceWithRawResponse:
    def __init__(self, styles: AsyncStylesResource) -> None:
        self._styles = styles

        self.retrieve = async_to_raw_response_wrapper(
            styles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            styles.update,
        )
        self.list = async_to_raw_response_wrapper(
            styles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            styles.delete,
        )
        self.analyze = async_to_raw_response_wrapper(
            styles.analyze,
        )
        self.compare = async_to_raw_response_wrapper(
            styles.compare,
        )
        self.get_performance = async_to_raw_response_wrapper(
            styles.get_performance,
        )


class StylesResourceWithStreamingResponse:
    def __init__(self, styles: StylesResource) -> None:
        self._styles = styles

        self.retrieve = to_streamed_response_wrapper(
            styles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            styles.update,
        )
        self.list = to_streamed_response_wrapper(
            styles.list,
        )
        self.delete = to_streamed_response_wrapper(
            styles.delete,
        )
        self.analyze = to_streamed_response_wrapper(
            styles.analyze,
        )
        self.compare = to_streamed_response_wrapper(
            styles.compare,
        )
        self.get_performance = to_streamed_response_wrapper(
            styles.get_performance,
        )


class AsyncStylesResourceWithStreamingResponse:
    def __init__(self, styles: AsyncStylesResource) -> None:
        self._styles = styles

        self.retrieve = async_to_streamed_response_wrapper(
            styles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            styles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            styles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            styles.delete,
        )
        self.analyze = async_to_streamed_response_wrapper(
            styles.analyze,
        )
        self.compare = async_to_streamed_response_wrapper(
            styles.compare,
        )
        self.get_performance = async_to_streamed_response_wrapper(
            styles.get_performance,
        )
