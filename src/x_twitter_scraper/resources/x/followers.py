# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import follower_check_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.follower_check_response import FollowerCheckResponse

__all__ = ["FollowersResource", "AsyncFollowersResource"]


class FollowersResource(SyncAPIResource):
    """X data lookups (subscription required)"""

    @cached_property
    def with_raw_response(self) -> FollowersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return FollowersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FollowersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return FollowersResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        source: str,
        target: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowerCheckResponse:
        """
        Check follow relationship

        Args:
          source: Username to check (without @)

          target: Target username (without @)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/followers/check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "source": source,
                        "target": target,
                    },
                    follower_check_params.FollowerCheckParams,
                ),
            ),
            cast_to=FollowerCheckResponse,
        )


class AsyncFollowersResource(AsyncAPIResource):
    """X data lookups (subscription required)"""

    @cached_property
    def with_raw_response(self) -> AsyncFollowersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFollowersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFollowersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncFollowersResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        source: str,
        target: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowerCheckResponse:
        """
        Check follow relationship

        Args:
          source: Username to check (without @)

          target: Target username (without @)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/followers/check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "source": source,
                        "target": target,
                    },
                    follower_check_params.FollowerCheckParams,
                ),
            ),
            cast_to=FollowerCheckResponse,
        )


class FollowersResourceWithRawResponse:
    def __init__(self, followers: FollowersResource) -> None:
        self._followers = followers

        self.check = to_raw_response_wrapper(
            followers.check,
        )


class AsyncFollowersResourceWithRawResponse:
    def __init__(self, followers: AsyncFollowersResource) -> None:
        self._followers = followers

        self.check = async_to_raw_response_wrapper(
            followers.check,
        )


class FollowersResourceWithStreamingResponse:
    def __init__(self, followers: FollowersResource) -> None:
        self._followers = followers

        self.check = to_streamed_response_wrapper(
            followers.check,
        )


class AsyncFollowersResourceWithStreamingResponse:
    def __init__(self, followers: AsyncFollowersResource) -> None:
        self._followers = followers

        self.check = async_to_streamed_response_wrapper(
            followers.check,
        )
