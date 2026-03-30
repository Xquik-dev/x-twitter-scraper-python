# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .like import (
    LikeResource,
    AsyncLikeResource,
    LikeResourceWithRawResponse,
    AsyncLikeResourceWithRawResponse,
    LikeResourceWithStreamingResponse,
    AsyncLikeResourceWithStreamingResponse,
)
from .retweet import (
    RetweetResource,
    AsyncRetweetResource,
    RetweetResourceWithRawResponse,
    AsyncRetweetResourceWithRawResponse,
    RetweetResourceWithStreamingResponse,
    AsyncRetweetResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.x import (
    tweet_list_params,
    tweet_create_params,
    tweet_delete_params,
    tweet_search_params,
    tweet_get_quotes_params,
    tweet_get_thread_params,
    tweet_get_replies_params,
    tweet_get_favoriters_params,
    tweet_get_retweeters_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.shared.paginated_users import PaginatedUsers
from ....types.shared.paginated_tweets import PaginatedTweets
from ....types.x.tweet_create_response import TweetCreateResponse
from ....types.x.tweet_delete_response import TweetDeleteResponse
from ....types.x.tweet_retrieve_response import TweetRetrieveResponse

__all__ = ["TweetsResource", "AsyncTweetsResource"]


class TweetsResource(SyncAPIResource):
    @cached_property
    def like(self) -> LikeResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return LikeResource(self._client)

    @cached_property
    def retweet(self) -> RetweetResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return RetweetResource(self._client)

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

    def create(
        self,
        *,
        account: str,
        text: str,
        attachment_url: str | Omit = omit,
        community_id: str | Omit = omit,
        is_note_tweet: bool | Omit = omit,
        media_ids: SequenceNotStr[str] | Omit = omit,
        reply_to_tweet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetCreateResponse:
        """
        Create tweet

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/x/tweets",
            body=maybe_transform(
                {
                    "account": account,
                    "text": text,
                    "attachment_url": attachment_url,
                    "community_id": community_id,
                    "is_note_tweet": is_note_tweet,
                    "media_ids": media_ids,
                    "reply_to_tweet_id": reply_to_tweet_id,
                },
                tweet_create_params.TweetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TweetCreateResponse,
        )

    def retrieve(
        self,
        tweet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetRetrieveResponse:
        """
        Look up tweet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tweet_id:
            raise ValueError(f"Expected a non-empty value for `tweet_id` but received {tweet_id!r}")
        return self._get(
            path_template("/x/tweets/{tweet_id}", tweet_id=tweet_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TweetRetrieveResponse,
        )

    def list(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get multiple tweets by IDs

        Args:
          ids: Comma-separated tweet IDs (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/x/tweets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, tweet_list_params.TweetListParams),
            ),
            cast_to=NoneType,
        )

    def delete(
        self,
        tweet_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetDeleteResponse:
        """
        Delete tweet

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tweet_id:
            raise ValueError(f"Expected a non-empty value for `tweet_id` but received {tweet_id!r}")
        return self._delete(
            path_template("/x/tweets/{tweet_id}", tweet_id=tweet_id),
            body=maybe_transform({"account": account}, tweet_delete_params.TweetDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TweetDeleteResponse,
        )

    def get_favoriters(
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
        Get users who liked a tweet

        Args:
          cursor: Pagination cursor from previous response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}/favoriters", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, tweet_get_favoriters_params.TweetGetFavoritersParams),
            ),
            cast_to=PaginatedUsers,
        )

    def get_quotes(
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
        Get quote tweets of a tweet

        Args:
          cursor: Pagination cursor

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
            path_template("/x/tweets/{id}/quotes", id=id),
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
                    tweet_get_quotes_params.TweetGetQuotesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def get_replies(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
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
        Get replies to a tweet

        Args:
          cursor: Pagination cursor

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
            path_template("/x/tweets/{id}/replies", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "since_time": since_time,
                        "until_time": until_time,
                    },
                    tweet_get_replies_params.TweetGetRepliesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def get_retweeters(
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
        Get users who retweeted a tweet

        Args:
          cursor: Pagination cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}/retweeters", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, tweet_get_retweeters_params.TweetGetRetweetersParams),
            ),
            cast_to=PaginatedUsers,
        )

    def get_thread(
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
    ) -> PaginatedTweets:
        """
        Get thread context for a tweet

        Args:
          cursor: Pagination cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}/thread", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, tweet_get_thread_params.TweetGetThreadParams),
            ),
            cast_to=PaginatedTweets,
        )

    def search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
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
        Search tweets

        Args:
          q: Search query (keywords,

          cursor: Pagination cursor from previous response

          limit: Deprecated — use cursor-based pagination instead

          query_type: Sort order — Latest (chronological) or Top (engagement-ranked)

          since_time: ISO 8601 timestamp — only return tweets after this time

          until_time: ISO 8601 timestamp — only return tweets before this time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/tweets/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "limit": limit,
                        "query_type": query_type,
                        "since_time": since_time,
                        "until_time": until_time,
                    },
                    tweet_search_params.TweetSearchParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )


class AsyncTweetsResource(AsyncAPIResource):
    @cached_property
    def like(self) -> AsyncLikeResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncLikeResource(self._client)

    @cached_property
    def retweet(self) -> AsyncRetweetResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncRetweetResource(self._client)

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

    async def create(
        self,
        *,
        account: str,
        text: str,
        attachment_url: str | Omit = omit,
        community_id: str | Omit = omit,
        is_note_tweet: bool | Omit = omit,
        media_ids: SequenceNotStr[str] | Omit = omit,
        reply_to_tweet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetCreateResponse:
        """
        Create tweet

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/x/tweets",
            body=await async_maybe_transform(
                {
                    "account": account,
                    "text": text,
                    "attachment_url": attachment_url,
                    "community_id": community_id,
                    "is_note_tweet": is_note_tweet,
                    "media_ids": media_ids,
                    "reply_to_tweet_id": reply_to_tweet_id,
                },
                tweet_create_params.TweetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TweetCreateResponse,
        )

    async def retrieve(
        self,
        tweet_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetRetrieveResponse:
        """
        Look up tweet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tweet_id:
            raise ValueError(f"Expected a non-empty value for `tweet_id` but received {tweet_id!r}")
        return await self._get(
            path_template("/x/tweets/{tweet_id}", tweet_id=tweet_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TweetRetrieveResponse,
        )

    async def list(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get multiple tweets by IDs

        Args:
          ids: Comma-separated tweet IDs (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/x/tweets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, tweet_list_params.TweetListParams),
            ),
            cast_to=NoneType,
        )

    async def delete(
        self,
        tweet_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetDeleteResponse:
        """
        Delete tweet

        Args:
          account: X account (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tweet_id:
            raise ValueError(f"Expected a non-empty value for `tweet_id` but received {tweet_id!r}")
        return await self._delete(
            path_template("/x/tweets/{tweet_id}", tweet_id=tweet_id),
            body=await async_maybe_transform({"account": account}, tweet_delete_params.TweetDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TweetDeleteResponse,
        )

    async def get_favoriters(
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
        Get users who liked a tweet

        Args:
          cursor: Pagination cursor from previous response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}/favoriters", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, tweet_get_favoriters_params.TweetGetFavoritersParams
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def get_quotes(
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
        Get quote tweets of a tweet

        Args:
          cursor: Pagination cursor

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
            path_template("/x/tweets/{id}/quotes", id=id),
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
                    tweet_get_quotes_params.TweetGetQuotesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def get_replies(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
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
        Get replies to a tweet

        Args:
          cursor: Pagination cursor

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
            path_template("/x/tweets/{id}/replies", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "since_time": since_time,
                        "until_time": until_time,
                    },
                    tweet_get_replies_params.TweetGetRepliesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def get_retweeters(
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
        Get users who retweeted a tweet

        Args:
          cursor: Pagination cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}/retweeters", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, tweet_get_retweeters_params.TweetGetRetweetersParams
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def get_thread(
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
    ) -> PaginatedTweets:
        """
        Get thread context for a tweet

        Args:
          cursor: Pagination cursor

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}/thread", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cursor": cursor}, tweet_get_thread_params.TweetGetThreadParams),
            ),
            cast_to=PaginatedTweets,
        )

    async def search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
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
        Search tweets

        Args:
          q: Search query (keywords,

          cursor: Pagination cursor from previous response

          limit: Deprecated — use cursor-based pagination instead

          query_type: Sort order — Latest (chronological) or Top (engagement-ranked)

          since_time: ISO 8601 timestamp — only return tweets after this time

          until_time: ISO 8601 timestamp — only return tweets before this time

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/tweets/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "limit": limit,
                        "query_type": query_type,
                        "since_time": since_time,
                        "until_time": until_time,
                    },
                    tweet_search_params.TweetSearchParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )


class TweetsResourceWithRawResponse:
    def __init__(self, tweets: TweetsResource) -> None:
        self._tweets = tweets

        self.create = to_raw_response_wrapper(
            tweets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tweets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tweets.list,
        )
        self.delete = to_raw_response_wrapper(
            tweets.delete,
        )
        self.get_favoriters = to_raw_response_wrapper(
            tweets.get_favoriters,
        )
        self.get_quotes = to_raw_response_wrapper(
            tweets.get_quotes,
        )
        self.get_replies = to_raw_response_wrapper(
            tweets.get_replies,
        )
        self.get_retweeters = to_raw_response_wrapper(
            tweets.get_retweeters,
        )
        self.get_thread = to_raw_response_wrapper(
            tweets.get_thread,
        )
        self.search = to_raw_response_wrapper(
            tweets.search,
        )

    @cached_property
    def like(self) -> LikeResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return LikeResourceWithRawResponse(self._tweets.like)

    @cached_property
    def retweet(self) -> RetweetResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return RetweetResourceWithRawResponse(self._tweets.retweet)


class AsyncTweetsResourceWithRawResponse:
    def __init__(self, tweets: AsyncTweetsResource) -> None:
        self._tweets = tweets

        self.create = async_to_raw_response_wrapper(
            tweets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tweets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tweets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tweets.delete,
        )
        self.get_favoriters = async_to_raw_response_wrapper(
            tweets.get_favoriters,
        )
        self.get_quotes = async_to_raw_response_wrapper(
            tweets.get_quotes,
        )
        self.get_replies = async_to_raw_response_wrapper(
            tweets.get_replies,
        )
        self.get_retweeters = async_to_raw_response_wrapper(
            tweets.get_retweeters,
        )
        self.get_thread = async_to_raw_response_wrapper(
            tweets.get_thread,
        )
        self.search = async_to_raw_response_wrapper(
            tweets.search,
        )

    @cached_property
    def like(self) -> AsyncLikeResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncLikeResourceWithRawResponse(self._tweets.like)

    @cached_property
    def retweet(self) -> AsyncRetweetResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncRetweetResourceWithRawResponse(self._tweets.retweet)


class TweetsResourceWithStreamingResponse:
    def __init__(self, tweets: TweetsResource) -> None:
        self._tweets = tweets

        self.create = to_streamed_response_wrapper(
            tweets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tweets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tweets.list,
        )
        self.delete = to_streamed_response_wrapper(
            tweets.delete,
        )
        self.get_favoriters = to_streamed_response_wrapper(
            tweets.get_favoriters,
        )
        self.get_quotes = to_streamed_response_wrapper(
            tweets.get_quotes,
        )
        self.get_replies = to_streamed_response_wrapper(
            tweets.get_replies,
        )
        self.get_retweeters = to_streamed_response_wrapper(
            tweets.get_retweeters,
        )
        self.get_thread = to_streamed_response_wrapper(
            tweets.get_thread,
        )
        self.search = to_streamed_response_wrapper(
            tweets.search,
        )

    @cached_property
    def like(self) -> LikeResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return LikeResourceWithStreamingResponse(self._tweets.like)

    @cached_property
    def retweet(self) -> RetweetResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return RetweetResourceWithStreamingResponse(self._tweets.retweet)


class AsyncTweetsResourceWithStreamingResponse:
    def __init__(self, tweets: AsyncTweetsResource) -> None:
        self._tweets = tweets

        self.create = async_to_streamed_response_wrapper(
            tweets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tweets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tweets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tweets.delete,
        )
        self.get_favoriters = async_to_streamed_response_wrapper(
            tweets.get_favoriters,
        )
        self.get_quotes = async_to_streamed_response_wrapper(
            tweets.get_quotes,
        )
        self.get_replies = async_to_streamed_response_wrapper(
            tweets.get_replies,
        )
        self.get_retweeters = async_to_streamed_response_wrapper(
            tweets.get_retweeters,
        )
        self.get_thread = async_to_streamed_response_wrapper(
            tweets.get_thread,
        )
        self.search = async_to_streamed_response_wrapper(
            tweets.search,
        )

    @cached_property
    def like(self) -> AsyncLikeResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncLikeResourceWithStreamingResponse(self._tweets.like)

    @cached_property
    def retweet(self) -> AsyncRetweetResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncRetweetResourceWithStreamingResponse(self._tweets.retweet)
