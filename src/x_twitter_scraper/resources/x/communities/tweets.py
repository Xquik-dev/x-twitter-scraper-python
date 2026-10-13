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
    """Find X Communities & read their info, members, posts & media"""

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
        q: str,
        any_words: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        cashtags: str | Omit = omit,
        community_id: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        max_faves: int | Omit = omit,
        max_id: str | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """One resumable page.

        Add communityId to search 1 Community, or leave it out to
        search every Community.

        Args:
          q: Search query

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          cashtags: Cashtags separated by spaces, commas, or lines.

          community_id: Numeric ID of the Community whose posts to search. Leave it out to search posts
              across every Community.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for community search. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Filter by language. Alias `lang` is accepted.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          native_retweets: Only return native reposts.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          query_type: Sort order (Latest or Top)

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within_time: Keeps Tweets from a recent window, such as 90m or 7d. Use a whole number & s, m,
              h or d.

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
                        "q": q,
                        "any_words": any_words,
                        "blue_verified_only": blue_verified_only,
                        "cashtags": cashtags,
                        "community_id": community_id,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "fields": fields,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "max_faves": max_faves,
                        "max_id": max_id,
                        "max_quotes": max_quotes,
                        "max_replies": max_replies,
                        "max_retweets": max_retweets,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_bookmarks": min_bookmarks,
                        "min_likes": min_likes,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "native_retweets": native_retweets,
                        "omit": omit,
                        "page_size": page_size,
                        "query_type": query_type,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_id": since_id,
                        "to_user": to_user,
                        "until_date": until_date,
                        "url": url,
                        "verified_only": verified_only,
                        "within_time": within_time,
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
        any_words: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        max_faves: int | Omit = omit,
        max_id: str | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns public tweets posted within one community, newest first by default.

        Send
        queryType=Top for the posts X ranks highest. The first page opens with the tweet
        the community pinned, flagged isPinned, as x.com shows it. Each tweet costs 1
        credit.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Filter by language. Alias `lang` is accepted.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          native_retweets: Only return native reposts.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          query_type: Latest for newest first, or Top for the posts X ranks highest. Any case. Aliases
              ranking & sort, which also take Recency & Relevance. Send the same value with
              each cursor.

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within_time: Keeps Tweets from a recent window, such as 90m or 7d. Use a whole number & s, m,
              h or d.

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
                        "any_words": any_words,
                        "blue_verified_only": blue_verified_only,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "fields": fields,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "max_faves": max_faves,
                        "max_id": max_id,
                        "max_quotes": max_quotes,
                        "max_replies": max_replies,
                        "max_retweets": max_retweets,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_bookmarks": min_bookmarks,
                        "min_likes": min_likes,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "native_retweets": native_retweets,
                        "omit": omit,
                        "page_size": page_size,
                        "query_type": query_type,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_id": since_id,
                        "to_user": to_user,
                        "until_date": until_date,
                        "url": url,
                        "verified_only": verified_only,
                        "within_time": within_time,
                    },
                    tweet_list_by_community_params.TweetListByCommunityParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )


class AsyncTweetsResource(AsyncAPIResource):
    """Find X Communities & read their info, members, posts & media"""

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
        q: str,
        any_words: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        cashtags: str | Omit = omit,
        community_id: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        max_faves: int | Omit = omit,
        max_id: str | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """One resumable page.

        Add communityId to search 1 Community, or leave it out to
        search every Community.

        Args:
          q: Search query

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          cashtags: Cashtags separated by spaces, commas, or lines.

          community_id: Numeric ID of the Community whose posts to search. Leave it out to search posts
              across every Community.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for community search. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Filter by language. Alias `lang` is accepted.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          native_retweets: Only return native reposts.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          query_type: Sort order (Latest or Top)

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within_time: Keeps Tweets from a recent window, such as 90m or 7d. Use a whole number & s, m,
              h or d.

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
                        "q": q,
                        "any_words": any_words,
                        "blue_verified_only": blue_verified_only,
                        "cashtags": cashtags,
                        "community_id": community_id,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "fields": fields,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "max_faves": max_faves,
                        "max_id": max_id,
                        "max_quotes": max_quotes,
                        "max_replies": max_replies,
                        "max_retweets": max_retweets,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_bookmarks": min_bookmarks,
                        "min_likes": min_likes,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "native_retweets": native_retweets,
                        "omit": omit,
                        "page_size": page_size,
                        "query_type": query_type,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_id": since_id,
                        "to_user": to_user,
                        "until_date": until_date,
                        "url": url,
                        "verified_only": verified_only,
                        "within_time": within_time,
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
        any_words: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        max_faves: int | Omit = omit,
        max_id: str | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns public tweets posted within one community, newest first by default.

        Send
        queryType=Top for the posts X ranks highest. The first page opens with the tweet
        the community pinned, flagged isPinned, as x.com shows it. Each tweet costs 1
        credit.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Filter by language. Alias `lang` is accepted.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          native_retweets: Only return native reposts.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          query_type: Latest for newest first, or Top for the posts X ranks highest. Any case. Aliases
              ranking & sort, which also take Recency & Relevance. Send the same value with
              each cursor.

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within_time: Keeps Tweets from a recent window, such as 90m or 7d. Use a whole number & s, m,
              h or d.

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
                        "any_words": any_words,
                        "blue_verified_only": blue_verified_only,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "fields": fields,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "max_faves": max_faves,
                        "max_id": max_id,
                        "max_quotes": max_quotes,
                        "max_replies": max_replies,
                        "max_retweets": max_retweets,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_bookmarks": min_bookmarks,
                        "min_likes": min_likes,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "native_retweets": native_retweets,
                        "omit": omit,
                        "page_size": page_size,
                        "query_type": query_type,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "since_date": since_date,
                        "since_id": since_id,
                        "to_user": to_user,
                        "until_date": until_date,
                        "url": url,
                        "verified_only": verified_only,
                        "within_time": within_time,
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
