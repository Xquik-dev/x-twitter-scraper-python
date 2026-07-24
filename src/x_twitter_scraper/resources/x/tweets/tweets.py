# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
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
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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

    def create(
        self,
        *,
        account: str,
        idempotency_key: str,
        community_id: str | Omit = omit,
        is_note_tweet: bool | Omit = omit,
        media: SequenceNotStr[str] | Omit = omit,
        reply_to_tweet_id: str | Omit = omit,
        text: str | Omit = omit,
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

          media: Array of public media URLs to attach. Supports up to 4 images or exactly 1 MP4
              video up to 100 MB. Each URL must be publicly reachable. Attached media adds 2
              credits per started MB across all files.

          text: Tweet text (optional when media is provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            "/x/tweets",
            body=maybe_transform(
                {
                    "account": account,
                    "community_id": community_id,
                    "is_note_tweet": is_note_tweet,
                    "media": media,
                    "reply_to_tweet_id": reply_to_tweet_id,
                    "text": text,
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
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetRetrieveResponse:
        """
        Get tweet with full text, author, metrics and media

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}", id=id),
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
    ) -> PaginatedTweets:
        """
        Get multiple tweets by IDs

        Args:
          ids: Comma-separated tweet IDs (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/tweets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, tweet_list_params.TweetListParams),
            ),
            cast_to=PaginatedTweets,
        )

    def delete(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
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
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._delete(
            path_template("/x/tweets/{id}", id=id),
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
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """Returns liker profiles that X makes visible for the post.

        X can withhold liker
        identities even when the post reports likes. In that case this endpoint returns
        424 `favoriters_unavailable` instead of a misleading empty success.

        Args:
          cursor: Pagination cursor for favoriters

          page_size: Maximum user profiles requested from this page (20-200, default 200). The
              response can contain fewer profiles because the source returned fewer or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true. The deprecated limit and count aliases remain accepted.

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
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    tweet_get_favoriters_params.TweetGetFavoritersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def get_quotes(
        self,
        id: str,
        *,
        any_words: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        include_replies: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        page_size: int | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_time: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List quote tweets of a tweet

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for quote tweets

          exact_phrase: Exact phrase to match.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_replies: Include reply quotes (default false)

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          page_size: Maximum items requested from this page (1-100, default 20). The response can
              contain fewer items because the source returned fewer, filters removed items, or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true, even when a page is empty. The deprecated limit and count
              aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format.

          since_time: Unix timestamp - return quotes posted after this time

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return quotes posted before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

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
                        "any_words": any_words,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "include_replies": include_replies,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "page_size": page_size,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_time": since_time,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
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
        any_words: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        page_size: int | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_time: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns visible replies.

        For an unfiltered first page, Xquik compares a terminal
        page with the post's reported reply count. If the page is visibly incomplete,
        the endpoint returns 424 `replies_incomplete` instead of presenting partial
        coverage as complete. Use tweet search with a `conversation_id:{id}` query as
        the broader fallback.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for tweet replies

          exact_phrase: Exact phrase to match.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          page_size: Maximum items requested from this page (1-100, default 20). The response can
              contain fewer items because the source returned fewer, filters removed items, or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true, even when a page is empty. The deprecated limit and count
              aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format.

          since_time: Unix timestamp - return replies posted after this time

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return replies posted before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

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
                        "any_words": any_words,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "page_size": page_size,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_time": since_time,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
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
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List users who retweeted a tweet

        Args:
          cursor: Pagination cursor for retweeters

          page_size: Maximum user profiles requested from this page (20-200, default 200). The
              response can contain fewer profiles because the source returned fewer or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true. The deprecated limit and count aliases remain accepted.

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
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    tweet_get_retweeters_params.TweetGetRetweetersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def get_thread(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Get full conversation thread for a tweet

        Args:
          cursor: Pagination cursor for thread tweets

          page_size: Maximum items requested from this page (1-100, default 20). The response can
              contain fewer items because the source returned fewer, filters removed items, or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true, even when a page is empty. The deprecated limit and count
              aliases remain accepted.

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
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    tweet_get_thread_params.TweetGetThreadParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def search(
        self,
        *,
        q: str,
        advanced_query: str | Omit = omit,
        any_words: str | Omit = omit,
        bounding_box: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_time: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Search tweets by query, Tweet ID, X status URL, or account date window

        Args:
          q: Search query (keywords,

          advanced_query: Raw advanced search query appended as-is.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor from previous response

          exact_phrase: Exact phrase to match.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          limit: Max tweets to return (server paginates internally). Omit for single page (~20).
              This is an upper bound for paid authenticated calls: remaining credits can
              reduce the returned page size, and zero affordable results returns 402
              insufficient_credits.

          list_id: Search within a list ID.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          place: Search within a place ID.

          place_country: Search within a country code.

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi.

          query_type: Sort order - Latest (chronological) or Top (engagement-ranked)

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format.

          since_time: ISO 8601 timestamp - only return tweets after this time

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: ISO 8601 timestamp - only return tweets before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

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
                        "advanced_query": advanced_query,
                        "any_words": any_words,
                        "bounding_box": bounding_box,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "limit": limit,
                        "list_id": list_id,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "place": place,
                        "place_country": place_country,
                        "point_radius": point_radius,
                        "query_type": query_type,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_time": since_time,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
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

    async def create(
        self,
        *,
        account: str,
        idempotency_key: str,
        community_id: str | Omit = omit,
        is_note_tweet: bool | Omit = omit,
        media: SequenceNotStr[str] | Omit = omit,
        reply_to_tweet_id: str | Omit = omit,
        text: str | Omit = omit,
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

          media: Array of public media URLs to attach. Supports up to 4 images or exactly 1 MP4
              video up to 100 MB. Each URL must be publicly reachable. Attached media adds 2
              credits per started MB across all files.

          text: Tweet text (optional when media is provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            "/x/tweets",
            body=await async_maybe_transform(
                {
                    "account": account,
                    "community_id": community_id,
                    "is_note_tweet": is_note_tweet,
                    "media": media,
                    "reply_to_tweet_id": reply_to_tweet_id,
                    "text": text,
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
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetRetrieveResponse:
        """
        Get tweet with full text, author, metrics and media

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}", id=id),
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
    ) -> PaginatedTweets:
        """
        Get multiple tweets by IDs

        Args:
          ids: Comma-separated tweet IDs (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/tweets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, tweet_list_params.TweetListParams),
            ),
            cast_to=PaginatedTweets,
        )

    async def delete(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
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
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._delete(
            path_template("/x/tweets/{id}", id=id),
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
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """Returns liker profiles that X makes visible for the post.

        X can withhold liker
        identities even when the post reports likes. In that case this endpoint returns
        424 `favoriters_unavailable` instead of a misleading empty success.

        Args:
          cursor: Pagination cursor for favoriters

          page_size: Maximum user profiles requested from this page (20-200, default 200). The
              response can contain fewer profiles because the source returned fewer or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true. The deprecated limit and count aliases remain accepted.

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
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    tweet_get_favoriters_params.TweetGetFavoritersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def get_quotes(
        self,
        id: str,
        *,
        any_words: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        include_replies: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        page_size: int | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_time: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        List quote tweets of a tweet

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for quote tweets

          exact_phrase: Exact phrase to match.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_replies: Include reply quotes (default false)

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          page_size: Maximum items requested from this page (1-100, default 20). The response can
              contain fewer items because the source returned fewer, filters removed items, or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true, even when a page is empty. The deprecated limit and count
              aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format.

          since_time: Unix timestamp - return quotes posted after this time

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return quotes posted before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

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
                        "any_words": any_words,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "include_replies": include_replies,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "page_size": page_size,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_time": since_time,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
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
        any_words: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        page_size: int | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_time: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns visible replies.

        For an unfiltered first page, Xquik compares a terminal
        page with the post's reported reply count. If the page is visibly incomplete,
        the endpoint returns 424 `replies_incomplete` instead of presenting partial
        coverage as complete. Use tweet search with a `conversation_id:{id}` query as
        the broader fallback.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for tweet replies

          exact_phrase: Exact phrase to match.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          page_size: Maximum items requested from this page (1-100, default 20). The response can
              contain fewer items because the source returned fewer, filters removed items, or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true, even when a page is empty. The deprecated limit and count
              aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format.

          since_time: Unix timestamp - return replies posted after this time

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return replies posted before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

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
                        "any_words": any_words,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "page_size": page_size,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_time": since_time,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
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
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        List users who retweeted a tweet

        Args:
          cursor: Pagination cursor for retweeters

          page_size: Maximum user profiles requested from this page (20-200, default 200). The
              response can contain fewer profiles because the source returned fewer or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true. The deprecated limit and count aliases remain accepted.

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
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    tweet_get_retweeters_params.TweetGetRetweetersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def get_thread(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Get full conversation thread for a tweet

        Args:
          cursor: Pagination cursor for thread tweets

          page_size: Maximum items requested from this page (1-100, default 20). The response can
              contain fewer items because the source returned fewer, filters removed items, or
              remaining credits cover fewer results. Keep requesting next_cursor while
              has_next_page is true, even when a page is empty. The deprecated limit and count
              aliases remain accepted.

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
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    tweet_get_thread_params.TweetGetThreadParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def search(
        self,
        *,
        q: str,
        advanced_query: str | Omit = omit,
        any_words: str | Omit = omit,
        bounding_box: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_time: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Search tweets by query, Tweet ID, X status URL, or account date window

        Args:
          q: Search query (keywords,

          advanced_query: Raw advanced search query appended as-is.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor from previous response

          exact_phrase: Exact phrase to match.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          limit: Max tweets to return (server paginates internally). Omit for single page (~20).
              This is an upper bound for paid authenticated calls: remaining credits can
              reduce the returned page size, and zero affordable results returns 402
              insufficient_credits.

          list_id: Search within a list ID.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          place: Search within a place ID.

          place_country: Search within a country code.

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi.

          query_type: Sort order - Latest (chronological) or Top (engagement-ranked)

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format.

          since_time: ISO 8601 timestamp - only return tweets after this time

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: ISO 8601 timestamp - only return tweets before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

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
                        "advanced_query": advanced_query,
                        "any_words": any_words,
                        "bounding_box": bounding_box,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "limit": limit,
                        "list_id": list_id,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "place": place,
                        "place_country": place_country,
                        "point_radius": point_radius,
                        "query_type": query_type,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_time": since_time,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
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
