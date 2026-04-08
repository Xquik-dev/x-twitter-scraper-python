# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.x.communities import tweet_list_params, tweet_list_by_community_params
from ....types.shared.paginated_tweets import PaginatedTweets

__all__ = ["TweetsResource", "AsyncTweetsResource"]


class TweetsResource(SyncAPIResource):
    """X data lookups (subscription required)"""

    @cached_property
    def with_raw_response(self) -> TweetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return TweetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TweetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return TweetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        query_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PaginatedTweets]:
        """
        Search tweets across all communities

        Args:
          q: Search query for cross-community tweets

          cursor: Pagination cursor for cross-community results

          query_type: Sort order for cross-community results (Latest or Top)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/x/communities/tweets",
            page=SyncCursorPage[PaginatedTweets],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "query_type": query_type,
                    },
                    tweet_list_params.TweetListParams,
                ),
            ),
            model=PaginatedTweets,
        )

    def list_by_community(
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
    ) -> SyncCursorPage[PaginatedTweets]:
        """
        Get community tweets

        Args:
          cursor: Pagination cursor for community tweets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/x/communities/{id}/tweets", id=id),
            page=SyncCursorPage[PaginatedTweets],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, tweet_list_by_community_params.TweetListByCommunityParams),
            ),
            model=PaginatedTweets,
        )


class AsyncTweetsResource(AsyncAPIResource):
    """X data lookups (subscription required)"""

    @cached_property
    def with_raw_response(self) -> AsyncTweetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTweetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTweetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncTweetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        query_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaginatedTweets, AsyncCursorPage[PaginatedTweets]]:
        """
        Search tweets across all communities

        Args:
          q: Search query for cross-community tweets

          cursor: Pagination cursor for cross-community results

          query_type: Sort order for cross-community results (Latest or Top)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/x/communities/tweets",
            page=AsyncCursorPage[PaginatedTweets],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "query_type": query_type,
                    },
                    tweet_list_params.TweetListParams,
                ),
            ),
            model=PaginatedTweets,
        )

    def list_by_community(
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
    ) -> AsyncPaginator[PaginatedTweets, AsyncCursorPage[PaginatedTweets]]:
        """
        Get community tweets

        Args:
          cursor: Pagination cursor for community tweets

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/x/communities/{id}/tweets", id=id),
            page=AsyncCursorPage[PaginatedTweets],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, tweet_list_by_community_params.TweetListByCommunityParams),
            ),
            model=PaginatedTweets,
        )


class TweetsResourceWithRawResponse:
    def __init__(self, tweets: TweetsResource) -> None:
        self._tweets = tweets

        self.list = to_raw_response_wrapper(
            tweets.list,
        )
        self.list_by_community = to_raw_response_wrapper(
            tweets.list_by_community,
        )


class AsyncTweetsResourceWithRawResponse:
    def __init__(self, tweets: AsyncTweetsResource) -> None:
        self._tweets = tweets

        self.list = async_to_raw_response_wrapper(
            tweets.list,
        )
        self.list_by_community = async_to_raw_response_wrapper(
            tweets.list_by_community,
        )


class TweetsResourceWithStreamingResponse:
    def __init__(self, tweets: TweetsResource) -> None:
        self._tweets = tweets

        self.list = to_streamed_response_wrapper(
            tweets.list,
        )
        self.list_by_community = to_streamed_response_wrapper(
            tweets.list_by_community,
        )


class AsyncTweetsResourceWithStreamingResponse:
    def __init__(self, tweets: AsyncTweetsResource) -> None:
        self._tweets = tweets

        self.list = async_to_streamed_response_wrapper(
            tweets.list,
        )
        self.list_by_community = async_to_streamed_response_wrapper(
            tweets.list_by_community,
        )
