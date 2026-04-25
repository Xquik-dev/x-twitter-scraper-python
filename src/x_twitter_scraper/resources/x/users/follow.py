# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.x.users import follow_create_params, follow_delete_all_params
from ....types.x.users.follow_create_response import FollowCreateResponse
from ....types.x.users.follow_delete_all_response import FollowDeleteAllResponse

__all__ = ["FollowResource", "AsyncFollowResource"]


class FollowResource(SyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> FollowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return FollowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FollowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return FollowResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowCreateResponse:
        """
        Follow user

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/x/users/{id}/follow", id=id),
            body=maybe_transform({"account": account}, follow_create_params.FollowCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowCreateResponse,
        )

    def delete_all(
        self,
        id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowDeleteAllResponse:
        """
        Unfollow user

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/x/users/{id}/follow", id=id),
            body=maybe_transform({"account": account}, follow_delete_all_params.FollowDeleteAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowDeleteAllResponse,
        )


class AsyncFollowResource(AsyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> AsyncFollowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFollowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFollowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncFollowResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowCreateResponse:
        """
        Follow user

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/x/users/{id}/follow", id=id),
            body=await async_maybe_transform({"account": account}, follow_create_params.FollowCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowCreateResponse,
        )

    async def delete_all(
        self,
        id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowDeleteAllResponse:
        """
        Unfollow user

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/x/users/{id}/follow", id=id),
            body=await async_maybe_transform({"account": account}, follow_delete_all_params.FollowDeleteAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FollowDeleteAllResponse,
        )


class FollowResourceWithRawResponse:
    def __init__(self, follow: FollowResource) -> None:
        self._follow = follow

        self.create = to_raw_response_wrapper(
            follow.create,
        )
        self.delete_all = to_raw_response_wrapper(
            follow.delete_all,
        )


class AsyncFollowResourceWithRawResponse:
    def __init__(self, follow: AsyncFollowResource) -> None:
        self._follow = follow

        self.create = async_to_raw_response_wrapper(
            follow.create,
        )
        self.delete_all = async_to_raw_response_wrapper(
            follow.delete_all,
        )


class FollowResourceWithStreamingResponse:
    def __init__(self, follow: FollowResource) -> None:
        self._follow = follow

        self.create = to_streamed_response_wrapper(
            follow.create,
        )
        self.delete_all = to_streamed_response_wrapper(
            follow.delete_all,
        )


class AsyncFollowResourceWithStreamingResponse:
    def __init__(self, follow: AsyncFollowResource) -> None:
        self._follow = follow

        self.create = async_to_streamed_response_wrapper(
            follow.create,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            follow.delete_all,
        )
