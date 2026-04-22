# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import list_retrieve_tweets_params, list_retrieve_members_params, list_retrieve_followers_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.paginated_users import PaginatedUsers
from ...types.shared.paginated_tweets import PaginatedTweets

__all__ = ["ListsResource", "AsyncListsResource"]


class ListsResource(SyncAPIResource):
    """X List followers, members, and tweets"""

    @cached_property
    def with_raw_response(self) -> ListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return ListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return ListsResourceWithStreamingResponse(self)

    def retrieve_followers(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List followers of an X List

        Args:
          cursor: Pagination cursor for list followers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/lists/{id}/followers", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, list_retrieve_followers_params.ListRetrieveFollowersParams),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_members(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List members of an X List

        Args:
          cursor: Pagination cursor for list members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/lists/{id}/members", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, list_retrieve_members_params.ListRetrieveMembersParams),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_tweets(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        include_replies: bool | Omit = omit,
        since_time: str | Omit = omit,
        until_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List tweets from an X List

        Args:
          cursor: Pagination cursor for list tweets

          include_replies: Include replies (default false)

          since_time: Unix timestamp - filter after

          until_time: Unix timestamp - filter before

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/lists/{id}/tweets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_replies": include_replies,
                        "since_time": since_time,
                        "until_time": until_time,
                    },
                    list_retrieve_tweets_params.ListRetrieveTweetsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )


class AsyncListsResource(AsyncAPIResource):
    """X List followers, members, and tweets"""

    @cached_property
    def with_raw_response(self) -> AsyncListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncListsResourceWithStreamingResponse(self)

    async def retrieve_followers(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List followers of an X List

        Args:
          cursor: Pagination cursor for list followers

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/lists/{id}/followers", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, list_retrieve_followers_params.ListRetrieveFollowersParams
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_members(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List members of an X List

        Args:
          cursor: Pagination cursor for list members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/lists/{id}/members", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, list_retrieve_members_params.ListRetrieveMembersParams
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_tweets(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        include_replies: bool | Omit = omit,
        since_time: str | Omit = omit,
        until_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List tweets from an X List

        Args:
          cursor: Pagination cursor for list tweets

          include_replies: Include replies (default false)

          since_time: Unix timestamp - filter after

          until_time: Unix timestamp - filter before

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/lists/{id}/tweets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "include_replies": include_replies,
                        "since_time": since_time,
                        "until_time": until_time,
                    },
                    list_retrieve_tweets_params.ListRetrieveTweetsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )


class ListsResourceWithRawResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.retrieve_followers = to_raw_response_wrapper(
            lists.retrieve_followers,
        )
        self.retrieve_members = to_raw_response_wrapper(
            lists.retrieve_members,
        )
        self.retrieve_tweets = to_raw_response_wrapper(
            lists.retrieve_tweets,
        )


class AsyncListsResourceWithRawResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.retrieve_followers = async_to_raw_response_wrapper(
            lists.retrieve_followers,
        )
        self.retrieve_members = async_to_raw_response_wrapper(
            lists.retrieve_members,
        )
        self.retrieve_tweets = async_to_raw_response_wrapper(
            lists.retrieve_tweets,
        )


class ListsResourceWithStreamingResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.retrieve_followers = to_streamed_response_wrapper(
            lists.retrieve_followers,
        )
        self.retrieve_members = to_streamed_response_wrapper(
            lists.retrieve_members,
        )
        self.retrieve_tweets = to_streamed_response_wrapper(
            lists.retrieve_tweets,
        )


class AsyncListsResourceWithStreamingResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.retrieve_followers = async_to_streamed_response_wrapper(
            lists.retrieve_followers,
        )
        self.retrieve_members = async_to_streamed_response_wrapper(
            lists.retrieve_members,
        )
        self.retrieve_tweets = async_to_streamed_response_wrapper(
            lists.retrieve_tweets,
        )
