# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
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
from ....types.x.tweet_search_response import TweetSearchResponse
from ....types.x.tweet_retrieve_response import TweetRetrieveResponse
from ....types.x.tweet_get_replies_response import TweetGetRepliesResponse

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
        bio_contains: str | Omit = omit,
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
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
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Pagination cursor for favoriters

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          page_size: Maximum user profiles requested from this page (20-200, default 200). Source,
              filters, or credits can return fewer profiles. Keep requesting next_cursor while
              has_next_page is true. Deprecated aliases remain accepted.

          username_contains: Match a username substring, ignoring case.

          verified_only: Only return verified profiles.

          verified_type: Match the verification type exactly, ignoring case.

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
                        "bio_contains": bio_contains,
                        "cursor": cursor,
                        "has_location": has_location,
                        "has_website": has_website,
                        "location_contains": location_contains,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_statuses": max_statuses,
                        "min_account_age_days": min_account_age_days,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_statuses": min_statuses,
                        "page_size": page_size,
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
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
        blue_verified_only: bool | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        include_replies: bool | Omit = omit,
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
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        page_size: int | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: str | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
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

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for quote tweets

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_replies: Include reply quotes (default false)

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          max_faves: Maximum likes threshold. maxLikes is also accepted.

          max_id: Return Tweets older than this Tweet ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          page_size: Maximum page items (1-100, default 20). Source, filters, or credits can reduce
              results. Continue while has_next_page is true. Deprecated limit and count
              aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Unix timestamp - return quotes posted after this time

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return quotes posted before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

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
                        "blue_verified_only": blue_verified_only,
                        "card_name": card_name,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_source": exclude_source,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "geocode": geocode,
                        "hashtags": hashtags,
                        "include_replies": include_replies,
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
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "native_retweets": native_retweets,
                        "near": near,
                        "news": news,
                        "page_size": page_size,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "safe": safe,
                        "since_date": since_date,
                        "since_id": since_id,
                        "since_time": since_time,
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
                        "within": within,
                        "within_time": within_time,
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
        blue_verified_only: bool | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_original_author: bool | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        has_media_only: bool | Omit = omit,
        include_original_post: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        max_depth: int | Omit = omit,
        max_faves: int | Omit = omit,
        max_id: str | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard", "complete"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        page_size: int | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        scope: Literal["all", "direct", "nested"] | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: str | Omit = omit,
        sort: Literal["relevance", "latest", "oldest", "likes"] | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetGetRepliesResponse:
        """Returns direct replies.

        Omit mode for automatic maximum coverage with resumable
        pagination. Complete mode returns nested replies, diagnostics, and 424 when
        direct coverage stays below 80%.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          exact_phrase: Exact phrase to match.

          exclude_original_author: Exclude replies written by the source-post author.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          has_media_only: Only return replies containing media.

          include_original_post: Include the source post and count it toward limit.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          limit: With mode=complete, maximum combined direct and nested reply rows (1-25000,
              default 25000). Automatic pages accept 1-300. Standard pages accept 1-100.
              Prefer pageSize outside complete mode.

          max_depth: Maximum reply depth from the source post.

          max_faves: Maximum likes threshold. maxLikes is also accepted.

          max_id: Return Tweets older than this Tweet ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Optional advanced override. Omit mode for automatic maximum direct reply
              coverage with pagination. Standard keeps legacy pagination. Complete returns
              direct and nested replies with diagnostics, scope, depth, sorting, and
              original-post controls.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          page_size: Automatic pages accept 1-300 Tweets. Standard pages keep 1-100. Default 20.
              Continue while has_next_page is true. Deprecated aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          scope: Select all replies, direct replies, or nested replies.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Unix timestamp - return replies posted after this time

          sort: Sort the selected replies before applying limit.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return replies posted before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

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
                        "blue_verified_only": blue_verified_only,
                        "card_name": card_name,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_original_author": exclude_original_author,
                        "exclude_source": exclude_source,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "geocode": geocode,
                        "hashtags": hashtags,
                        "has_media_only": has_media_only,
                        "include_original_post": include_original_post,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "limit": limit,
                        "max_depth": max_depth,
                        "max_faves": max_faves,
                        "max_id": max_id,
                        "max_quotes": max_quotes,
                        "max_replies": max_replies,
                        "max_retweets": max_retweets,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_bookmarks": min_bookmarks,
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "mode": mode,
                        "native_retweets": native_retweets,
                        "near": near,
                        "news": news,
                        "page_size": page_size,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "safe": safe,
                        "scope": scope,
                        "since_date": since_date,
                        "since_id": since_id,
                        "since_time": since_time,
                        "sort": sort,
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
                        "within": within,
                        "within_time": within_time,
                    },
                    tweet_get_replies_params.TweetGetRepliesParams,
                ),
            ),
            cast_to=TweetGetRepliesResponse,
        )

    def get_retweeters(
        self,
        id: str,
        *,
        bio_contains: str | Omit = omit,
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
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
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Pagination cursor for retweeters

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          page_size: Maximum user profiles requested from this page (20-200, default 200). Source,
              filters, or credits can return fewer profiles. Keep requesting next_cursor while
              has_next_page is true. Deprecated aliases remain accepted.

          username_contains: Match a username substring, ignoring case.

          verified_only: Only return verified profiles.

          verified_type: Match the verification type exactly, ignoring case.

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
                        "bio_contains": bio_contains,
                        "cursor": cursor,
                        "has_location": has_location,
                        "has_website": has_website,
                        "location_contains": location_contains,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_statuses": max_statuses,
                        "min_account_age_days": min_account_age_days,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_statuses": min_statuses,
                        "page_size": page_size,
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
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

          page_size: Maximum page items (1-100, default 20). Source, filters, or credits can reduce
              results. Continue while has_next_page is true. Deprecated limit and count
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
        blue_verified_only: bool | Omit = omit,
        bounding_box: str | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        max_faves: int | Omit = omit,
        max_id: str | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: str | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetSearchResponse:
        """No-mode search maximizes coverage.

        Args:
          q: Query, Tweet ID, or status URL.

        Valid inline bounds apply per page.

          advanced_query: Raw advanced search query appended as-is.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          limit: Result upper bound. Omit it for the existing 20-row page size. Explicit coverage
              defaults to 2000 and allows 10000. For paid requests, remaining credits can
              reduce results. Zero affordable results returns 402.

          list_id: Search within a list ID.

          max_faves: Maximum likes threshold. maxLikes is also accepted.

          max_id: Return Tweets older than this Tweet ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          place: Search within a place ID.

          place_country: Search within a country code.

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi.

          query_type: Sort order - Latest (chronological) or Top (engagement-ranked)

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Inclusive ISO bound.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Exclusive ISO bound.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TweetSearchResponse,
            self._get(
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
                            "blue_verified_only": blue_verified_only,
                            "bounding_box": bounding_box,
                            "card_name": card_name,
                            "cashtags": cashtags,
                            "conversation_id": conversation_id,
                            "cursor": cursor,
                            "exact_phrase": exact_phrase,
                            "exclude_source": exclude_source,
                            "exclude_words": exclude_words,
                            "from_user": from_user,
                            "geocode": geocode,
                            "hashtags": hashtags,
                            "in_reply_to_tweet_id": in_reply_to_tweet_id,
                            "language": language,
                            "limit": limit,
                            "list_id": list_id,
                            "max_faves": max_faves,
                            "max_id": max_id,
                            "max_quotes": max_quotes,
                            "max_replies": max_replies,
                            "max_retweets": max_retweets,
                            "media_type": media_type,
                            "mentioning": mentioning,
                            "min_bookmarks": min_bookmarks,
                            "min_faves": min_faves,
                            "min_quotes": min_quotes,
                            "min_replies": min_replies,
                            "min_retweets": min_retweets,
                            "min_views": min_views,
                            "mode": mode,
                            "native_retweets": native_retweets,
                            "near": near,
                            "news": news,
                            "place": place,
                            "place_country": place_country,
                            "point_radius": point_radius,
                            "query_type": query_type,
                            "quotes": quotes,
                            "quotes_of_tweet_id": quotes_of_tweet_id,
                            "replies": replies,
                            "retweets": retweets,
                            "retweets_of_tweet_id": retweets_of_tweet_id,
                            "safe": safe,
                            "since_date": since_date,
                            "since_id": since_id,
                            "since_time": since_time,
                            "source": source,
                            "to_user": to_user,
                            "until_date": until_date,
                            "until_time": until_time,
                            "url": url,
                            "verified_only": verified_only,
                            "within": within,
                            "within_time": within_time,
                        },
                        tweet_search_params.TweetSearchParams,
                    ),
                ),
                cast_to=cast(
                    Any, TweetSearchResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        bio_contains: str | Omit = omit,
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
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
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Pagination cursor for favoriters

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          page_size: Maximum user profiles requested from this page (20-200, default 200). Source,
              filters, or credits can return fewer profiles. Keep requesting next_cursor while
              has_next_page is true. Deprecated aliases remain accepted.

          username_contains: Match a username substring, ignoring case.

          verified_only: Only return verified profiles.

          verified_type: Match the verification type exactly, ignoring case.

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
                        "bio_contains": bio_contains,
                        "cursor": cursor,
                        "has_location": has_location,
                        "has_website": has_website,
                        "location_contains": location_contains,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_statuses": max_statuses,
                        "min_account_age_days": min_account_age_days,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_statuses": min_statuses,
                        "page_size": page_size,
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
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
        blue_verified_only: bool | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        include_replies: bool | Omit = omit,
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
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        page_size: int | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: str | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
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

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for quote tweets

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_replies: Include reply quotes (default false)

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          max_faves: Maximum likes threshold. maxLikes is also accepted.

          max_id: Return Tweets older than this Tweet ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          page_size: Maximum page items (1-100, default 20). Source, filters, or credits can reduce
              results. Continue while has_next_page is true. Deprecated limit and count
              aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Unix timestamp - return quotes posted after this time

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return quotes posted before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

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
                        "blue_verified_only": blue_verified_only,
                        "card_name": card_name,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_source": exclude_source,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "geocode": geocode,
                        "hashtags": hashtags,
                        "include_replies": include_replies,
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
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "native_retweets": native_retweets,
                        "near": near,
                        "news": news,
                        "page_size": page_size,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "safe": safe,
                        "since_date": since_date,
                        "since_id": since_id,
                        "since_time": since_time,
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
                        "within": within,
                        "within_time": within_time,
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
        blue_verified_only: bool | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_original_author: bool | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        has_media_only: bool | Omit = omit,
        include_original_post: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        max_depth: int | Omit = omit,
        max_faves: int | Omit = omit,
        max_id: str | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard", "complete"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        page_size: int | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        scope: Literal["all", "direct", "nested"] | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: str | Omit = omit,
        sort: Literal["relevance", "latest", "oldest", "likes"] | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetGetRepliesResponse:
        """Returns direct replies.

        Omit mode for automatic maximum coverage with resumable
        pagination. Complete mode returns nested replies, diagnostics, and 424 when
        direct coverage stays below 80%.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          exact_phrase: Exact phrase to match.

          exclude_original_author: Exclude replies written by the source-post author.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          has_media_only: Only return replies containing media.

          include_original_post: Include the source post and count it toward limit.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          limit: With mode=complete, maximum combined direct and nested reply rows (1-25000,
              default 25000). Automatic pages accept 1-300. Standard pages accept 1-100.
              Prefer pageSize outside complete mode.

          max_depth: Maximum reply depth from the source post.

          max_faves: Maximum likes threshold. maxLikes is also accepted.

          max_id: Return Tweets older than this Tweet ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Optional advanced override. Omit mode for automatic maximum direct reply
              coverage with pagination. Standard keeps legacy pagination. Complete returns
              direct and nested replies with diagnostics, scope, depth, sorting, and
              original-post controls.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          page_size: Automatic pages accept 1-300 Tweets. Standard pages keep 1-100. Default 20.
              Continue while has_next_page is true. Deprecated aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          scope: Select all replies, direct replies, or nested replies.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Unix timestamp - return replies posted after this time

          sort: Sort the selected replies before applying limit.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return replies posted before this time

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

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
                        "blue_verified_only": blue_verified_only,
                        "card_name": card_name,
                        "cashtags": cashtags,
                        "conversation_id": conversation_id,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_original_author": exclude_original_author,
                        "exclude_source": exclude_source,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "geocode": geocode,
                        "hashtags": hashtags,
                        "has_media_only": has_media_only,
                        "include_original_post": include_original_post,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "language": language,
                        "limit": limit,
                        "max_depth": max_depth,
                        "max_faves": max_faves,
                        "max_id": max_id,
                        "max_quotes": max_quotes,
                        "max_replies": max_replies,
                        "max_retweets": max_retweets,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_bookmarks": min_bookmarks,
                        "min_faves": min_faves,
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "mode": mode,
                        "native_retweets": native_retweets,
                        "near": near,
                        "news": news,
                        "page_size": page_size,
                        "quotes": quotes,
                        "quotes_of_tweet_id": quotes_of_tweet_id,
                        "replies": replies,
                        "retweets": retweets,
                        "retweets_of_tweet_id": retweets_of_tweet_id,
                        "safe": safe,
                        "scope": scope,
                        "since_date": since_date,
                        "since_id": since_id,
                        "since_time": since_time,
                        "sort": sort,
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "url": url,
                        "verified_only": verified_only,
                        "within": within,
                        "within_time": within_time,
                    },
                    tweet_get_replies_params.TweetGetRepliesParams,
                ),
            ),
            cast_to=TweetGetRepliesResponse,
        )

    async def get_retweeters(
        self,
        id: str,
        *,
        bio_contains: str | Omit = omit,
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
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
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Pagination cursor for retweeters

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          page_size: Maximum user profiles requested from this page (20-200, default 200). Source,
              filters, or credits can return fewer profiles. Keep requesting next_cursor while
              has_next_page is true. Deprecated aliases remain accepted.

          username_contains: Match a username substring, ignoring case.

          verified_only: Only return verified profiles.

          verified_type: Match the verification type exactly, ignoring case.

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
                        "bio_contains": bio_contains,
                        "cursor": cursor,
                        "has_location": has_location,
                        "has_website": has_website,
                        "location_contains": location_contains,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_statuses": max_statuses,
                        "min_account_age_days": min_account_age_days,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_statuses": min_statuses,
                        "page_size": page_size,
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
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

          page_size: Maximum page items (1-100, default 20). Source, filters, or credits can reduce
              results. Continue while has_next_page is true. Deprecated limit and count
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
        blue_verified_only: bool | Omit = omit,
        bounding_box: str | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        limit: int | Omit = omit,
        list_id: str | Omit = omit,
        max_faves: int | Omit = omit,
        max_id: str | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: str | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetSearchResponse:
        """No-mode search maximizes coverage.

        Args:
          q: Query, Tweet ID, or status URL.

        Valid inline bounds apply per page.

          advanced_query: Raw advanced search query appended as-is.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Language code filter, e.g. en or tr.

          limit: Result upper bound. Omit it for the existing 20-row page size. Explicit coverage
              defaults to 2000 and allows 10000. For paid requests, remaining credits can
              reduce results. Zero affordable results returns 402.

          list_id: Search within a list ID.

          max_faves: Maximum likes threshold. maxLikes is also accepted.

          max_id: Return Tweets older than this Tweet ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter by media type.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Minimum likes threshold.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          place: Search within a place ID.

          place_country: Search within a country code.

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi.

          query_type: Sort order - Latest (chronological) or Top (engagement-ranked)

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Inclusive ISO bound.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Exclusive ISO bound.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            TweetSearchResponse,
            await self._get(
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
                            "blue_verified_only": blue_verified_only,
                            "bounding_box": bounding_box,
                            "card_name": card_name,
                            "cashtags": cashtags,
                            "conversation_id": conversation_id,
                            "cursor": cursor,
                            "exact_phrase": exact_phrase,
                            "exclude_source": exclude_source,
                            "exclude_words": exclude_words,
                            "from_user": from_user,
                            "geocode": geocode,
                            "hashtags": hashtags,
                            "in_reply_to_tweet_id": in_reply_to_tweet_id,
                            "language": language,
                            "limit": limit,
                            "list_id": list_id,
                            "max_faves": max_faves,
                            "max_id": max_id,
                            "max_quotes": max_quotes,
                            "max_replies": max_replies,
                            "max_retweets": max_retweets,
                            "media_type": media_type,
                            "mentioning": mentioning,
                            "min_bookmarks": min_bookmarks,
                            "min_faves": min_faves,
                            "min_quotes": min_quotes,
                            "min_replies": min_replies,
                            "min_retweets": min_retweets,
                            "min_views": min_views,
                            "mode": mode,
                            "native_retweets": native_retweets,
                            "near": near,
                            "news": news,
                            "place": place,
                            "place_country": place_country,
                            "point_radius": point_radius,
                            "query_type": query_type,
                            "quotes": quotes,
                            "quotes_of_tweet_id": quotes_of_tweet_id,
                            "replies": replies,
                            "retweets": retweets,
                            "retweets_of_tweet_id": retweets_of_tweet_id,
                            "safe": safe,
                            "since_date": since_date,
                            "since_id": since_id,
                            "since_time": since_time,
                            "source": source,
                            "to_user": to_user,
                            "until_date": until_date,
                            "until_time": until_time,
                            "url": url,
                            "verified_only": verified_only,
                            "within": within,
                            "within_time": within_time,
                        },
                        tweet_search_params.TweetSearchParams,
                    ),
                ),
                cast_to=cast(
                    Any, TweetSearchResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
