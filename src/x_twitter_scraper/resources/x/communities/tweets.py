# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.x.communities import tweet_list_params, tweet_list_by_community_params
from ....types.shared.paginated_tweets import PaginatedTweets

__all__ = ["TweetsResource", "AsyncTweetsResource"]


class TweetsResource(SyncAPIResource):
    """X Community info, members, and tweets"""

    @cached_property
    def with_raw_response(self) -> TweetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return TweetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TweetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return TweetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        community_id: str,
        q: str,
        cursor: str | Omit = omit,
        language: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        min_likes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        page_size: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """One resumable page.

        Requires a Community ID and query.

        Args:
          community_id: Numeric ID of the community whose posts to search

          q: Search query

          cursor: Pagination cursor for community search

          language: Filter by language. Alias `lang` is accepted.

          media_type: Filter media. Aliases: has_video, has_media.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          page_size: Maximum page items (1-100, default 20). Source, filters, or credits can reduce
              results. Follow next_cursor while the response reports more pages. Deprecated
              limit and count aliases remain accepted.

          query_type: Sort order (Latest or Top)

          since_date: Start date in YYYY-MM-DD format.

          until_date: End date in YYYY-MM-DD format.

          verified_only: Only return tweets from verified authors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/communities/tweets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "community_id": community_id,
                        "q": q,
                        "cursor": cursor,
                        "language": language,
                        "media_type": media_type,
                        "min_likes": min_likes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "page_size": page_size,
                        "query_type": query_type,
                        "since_date": since_date,
                        "until_date": until_date,
                        "verified_only": verified_only,
                    },
                    tweet_list_params.TweetListParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def list_by_community(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        language: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        min_likes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        page_size: int | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns public tweets posted within one community.

        Args:
          cursor: Pagination cursor for collection results.

          language: Filter by language. Alias `lang` is accepted.

          media_type: Filter media. Aliases: has_video, has_media.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          page_size: Maximum page items (1-100, default 20). Source, filters, or credits can reduce
              results. Follow next_cursor while the response reports more pages. Deprecated
              limit and count aliases remain accepted.

          since_date: Start date in YYYY-MM-DD format.

          until_date: End date in YYYY-MM-DD format.

          verified_only: Only return tweets from verified authors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/communities/{id}/tweets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "language": language,
                        "media_type": media_type,
                        "min_likes": min_likes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "page_size": page_size,
                        "since_date": since_date,
                        "until_date": until_date,
                        "verified_only": verified_only,
                    },
                    tweet_list_by_community_params.TweetListByCommunityParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )


class AsyncTweetsResource(AsyncAPIResource):
    """X Community info, members, and tweets"""

    @cached_property
    def with_raw_response(self) -> AsyncTweetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTweetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTweetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncTweetsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        community_id: str,
        q: str,
        cursor: str | Omit = omit,
        language: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        min_likes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        page_size: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """One resumable page.

        Requires a Community ID and query.

        Args:
          community_id: Numeric ID of the community whose posts to search

          q: Search query

          cursor: Pagination cursor for community search

          language: Filter by language. Alias `lang` is accepted.

          media_type: Filter media. Aliases: has_video, has_media.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          page_size: Maximum page items (1-100, default 20). Source, filters, or credits can reduce
              results. Follow next_cursor while the response reports more pages. Deprecated
              limit and count aliases remain accepted.

          query_type: Sort order (Latest or Top)

          since_date: Start date in YYYY-MM-DD format.

          until_date: End date in YYYY-MM-DD format.

          verified_only: Only return tweets from verified authors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/communities/tweets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "community_id": community_id,
                        "q": q,
                        "cursor": cursor,
                        "language": language,
                        "media_type": media_type,
                        "min_likes": min_likes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "page_size": page_size,
                        "query_type": query_type,
                        "since_date": since_date,
                        "until_date": until_date,
                        "verified_only": verified_only,
                    },
                    tweet_list_params.TweetListParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def list_by_community(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        language: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        min_likes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        page_size: int | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns public tweets posted within one community.

        Args:
          cursor: Pagination cursor for collection results.

          language: Filter by language. Alias `lang` is accepted.

          media_type: Filter media. Aliases: has_video, has_media.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          page_size: Maximum page items (1-100, default 20). Source, filters, or credits can reduce
              results. Follow next_cursor while the response reports more pages. Deprecated
              limit and count aliases remain accepted.

          since_date: Start date in YYYY-MM-DD format.

          until_date: End date in YYYY-MM-DD format.

          verified_only: Only return tweets from verified authors.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/communities/{id}/tweets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "language": language,
                        "media_type": media_type,
                        "min_likes": min_likes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "page_size": page_size,
                        "since_date": since_date,
                        "until_date": until_date,
                        "verified_only": verified_only,
                    },
                    tweet_list_by_community_params.TweetListByCommunityParams,
                ),
            ),
            cast_to=PaginatedTweets,
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
