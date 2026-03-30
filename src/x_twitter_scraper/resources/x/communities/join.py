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
from ....types.x.communities import join_create_params, join_delete_all_params
from ....types.x.community_action_result import CommunityActionResult

__all__ = ["JoinResource", "AsyncJoinResource"]


class JoinResource(SyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> JoinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return JoinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JoinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return JoinResourceWithStreamingResponse(self)

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
    ) -> CommunityActionResult:
        """
        Join community

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/x/communities/{id}/join", id=id),
            body=maybe_transform({"account": account}, join_create_params.JoinCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityActionResult,
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
    ) -> CommunityActionResult:
        """
        Leave community

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/x/communities/{id}/join", id=id),
            body=maybe_transform({"account": account}, join_delete_all_params.JoinDeleteAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityActionResult,
        )


class AsyncJoinResource(AsyncAPIResource):
    """X write actions (tweets, likes, follows, DMs)"""

    @cached_property
    def with_raw_response(self) -> AsyncJoinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJoinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJoinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncJoinResourceWithStreamingResponse(self)

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
    ) -> CommunityActionResult:
        """
        Join community

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/x/communities/{id}/join", id=id),
            body=await async_maybe_transform({"account": account}, join_create_params.JoinCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityActionResult,
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
    ) -> CommunityActionResult:
        """
        Leave community

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/x/communities/{id}/join", id=id),
            body=await async_maybe_transform({"account": account}, join_delete_all_params.JoinDeleteAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityActionResult,
        )


class JoinResourceWithRawResponse:
    def __init__(self, join: JoinResource) -> None:
        self._join = join

        self.create = to_raw_response_wrapper(
            join.create,
        )
        self.delete_all = to_raw_response_wrapper(
            join.delete_all,
        )


class AsyncJoinResourceWithRawResponse:
    def __init__(self, join: AsyncJoinResource) -> None:
        self._join = join

        self.create = async_to_raw_response_wrapper(
            join.create,
        )
        self.delete_all = async_to_raw_response_wrapper(
            join.delete_all,
        )


class JoinResourceWithStreamingResponse:
    def __init__(self, join: JoinResource) -> None:
        self._join = join

        self.create = to_streamed_response_wrapper(
            join.create,
        )
        self.delete_all = to_streamed_response_wrapper(
            join.delete_all,
        )


class AsyncJoinResourceWithStreamingResponse:
    def __init__(self, join: AsyncJoinResource) -> None:
        self._join = join

        self.create = async_to_streamed_response_wrapper(
            join.create,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            join.delete_all,
        )
