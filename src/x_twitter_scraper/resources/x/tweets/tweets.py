# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

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
    tweet_embed_params,
    tweet_create_params,
    tweet_delete_params,
    tweet_search_params,
    tweet_list_top_params,
    tweet_retrieve_params,
    tweet_translate_params,
    tweet_get_quotes_params,
    tweet_get_thread_params,
    tweet_get_replies_params,
    tweet_check_repost_params,
    tweet_get_insights_params,
    tweet_get_subtitles_params,
    tweet_resolve_links_params,
    tweet_get_favoriters_params,
    tweet_get_retweeters_params,
    tweet_get_retweeter_ids_params,
    tweet_get_hidden_replies_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ...._deprecated_keywords import min_likes_or_min_faves
from ....types.x.tweet_list_response import TweetListResponse
from ....types.shared.paginated_users import PaginatedUsers
from ....types.x.tweet_embed_response import TweetEmbedResponse
from ....types.shared.paginated_tweets import PaginatedTweets
from ....types.x.tweet_create_response import TweetCreateResponse
from ....types.x.tweet_delete_response import TweetDeleteResponse
from ....types.x.tweet_search_response import TweetSearchResponse
from ....types.x.tweet_retrieve_response import TweetRetrieveResponse
from ....types.x.tweet_translate_response import TweetTranslateResponse
from ....types.x.tweet_get_replies_response import TweetGetRepliesResponse
from ....types.x.tweet_check_repost_response import TweetCheckRepostResponse
from ....types.x.tweet_get_insights_response import TweetGetInsightsResponse
from ....types.x.tweet_get_subtitles_response import TweetGetSubtitlesResponse
from ....types.x.tweet_resolve_links_response import TweetResolveLinksResponse
from ....types.x.tweet_get_retweeter_ids_response import TweetGetRetweeterIdsResponse

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
        Publishes a post through a connected X account.

        Args:
          account: X account (@username or account ID)

          community_id: The Community to post into, from 1 to 19 digits. The account must be a member.
              Xquik picks the Community in X's composer, checks the post request names it &
              reads the post after. A post X puts outside the Community is deleted & fails
              uncharged. Not with `reply_to_tweet_id`, since X keeps replies public.

          media: Publicly reachable URLs of up to 4 images or exactly 1 MP4 video up to 100 MB.
              Media adds 2 credits per started MB across all files.

          reply_to_tweet_id: The post to reply to. Any X post ID works, from 1 to 19 digits.

          text: Tweet text (optional when media is provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
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
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetRetrieveResponse:
        """
        Returns one public tweet with author, metrics, and media.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_retrieve_params.TweetRetrieveParams,
                ),
            ),
            cast_to=TweetRetrieveResponse,
        )

    def list(
        self,
        *,
        ids: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetListResponse:
        """
        Returns public tweet records for the requested IDs.

        Args:
          ids: 1 to 100 posts, separated by commas. Each is a tweet ID or a tweet URL, such as
              x.com/nasa/status/20. A post named twice is read once. Any other entry is
              skipped & listed under `skipped` with why. A batch without 1 post gets 400
              `invalid_tweet_id`.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

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
                query=maybe_transform(
                    {
                        "ids": ids,
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_list_params.TweetListParams,
                ),
            ),
            cast_to=TweetListResponse,
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
        Deletes an authored post through a connected X account.

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return self._delete(
            path_template("/x/tweets/{id}", id=id),
            body=maybe_transform({"account": account}, tweet_delete_params.TweetDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TweetDeleteResponse,
        )

    def check_repost(
        self,
        id: str,
        *,
        user: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetCheckRepostResponse:
        """Returns whether 1 account reposted the post, read from its newest posts.

        A
        repost older than the posts read returns false with complete false. Each check
        costs 1 credit.

        Args:
          user: User ID, username with or without @, or profile URL.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}/retweeters/check", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "user": user,
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_check_repost_params.TweetCheckRepostParams,
                ),
            ),
            cast_to=TweetCheckRepostResponse,
        )

    def embed(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        hide_media: bool | Omit = omit,
        hide_thread: bool | Omit = omit,
        omit: str | Omit = omit,
        omit_script: bool | Omit = omit,
        theme: Literal["light", "dark"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetEmbedResponse:
        """
        Returns the HTML that X gives websites to embed one public tweet, with the
        tweet's link and author.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          hide_media: Set `true` to leave photos, videos, and link cards out.

          hide_thread: Set `true` to leave the tweet this one replies to out.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          omit_script: Set `true` to leave the widget script tag out, for pages that load it once
              themselves.

          theme: Color theme of the embed. X uses light when left out.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}/embed", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "hide_media": hide_media,
                        "hide_thread": hide_thread,
                        "omit": omit,
                        "omit_script": omit_script,
                        "theme": theme,
                    },
                    tweet_embed_params.TweetEmbedParams,
                ),
            ),
            cast_to=TweetEmbedResponse,
        )

    def get_favoriters(
        self,
        id: str,
        *,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        business_email_only: bool | Omit = omit,
        cursor: str | Omit = omit,
        email_domains: str | Omit = omit,
        fields: str | Omit = omit,
        has_email: bool | Omit = omit,
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
        omit: str | Omit = omit,
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
        """Likers your X account sees, else 424 `account_required`.

        X shows likers only to
        the post author.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          email_domains: Only return profiles with an email at one of these domains. Separate domains
              with commas. Subdomains match.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          has_email: Only return profiles that publish an email.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Profiles to request from this page (1-200, default 200). Source, filters or
              credits can return fewer. Follow next_cursor for more pages. Aliases: limit,
              count, max_results, maxItems, max_items & per_page.

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
                        "blue_verified_only": blue_verified_only,
                        "business_email_only": business_email_only,
                        "cursor": cursor,
                        "email_domains": email_domains,
                        "fields": fields,
                        "has_email": has_email,
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
                        "omit": omit,
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

    def get_hidden_replies(
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
        """
        Returns the replies the post's author hid, oldest first, with the replies to
        them. A post without hidden replies returns an empty list.

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
            path_template("/x/tweets/{id}/hidden-replies", id=id),
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
                    tweet_get_hidden_replies_params.TweetGetHiddenRepliesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def get_insights(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetGetInsightsResponse:
        """
        Returns engagement insights for one tweet: engagements per hour since it went
        up, per view and per follower of its author, and how far it spread. Each report
        costs 1 credit, whatever it reads.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}/insights", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_get_insights_params.TweetGetInsightsParams,
                ),
            ),
            cast_to=TweetGetInsightsResponse,
        )

    def get_quotes(
        self,
        id: str,
        *,
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        include_replies: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        keywords: str | Omit = omit,
        language: str | Omit = omit,
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
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
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
    ) -> PaginatedTweets:
        """Returns public posts quoting the tweet, newest first, replies included.

        Drop
        them with replies=exclude. Send queryType=Top for the quotes X ranks highest.

        Args:
          advanced_query: Raw advanced search query appended as-is.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8.

          card_name: Keep only Tweets with this card type, such as poll2choice_text_only. Tweet
              search checks each Tweet's card.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_source: X search no longer supports excludeSource. A Tweet search with it answers 424 &
              charges nothing.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          geocode: X search no longer supports geocode. A Tweet search with it answers 424 &
              charges nothing.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_replies: Keep replies that quote the post. Automatic pages keep them unless this is
              false. Standard pages keep them only when it is true. Explicit replies takes
              precedence.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          keywords: Words the Tweets must match, in X search syntax.

          language: Filter by language. Alias `lang` is accepted.

          list_id: Search within a list ID.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Deprecated name of min_likes. Use min_likes.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Optional legacy pagination override. Search-only filters such as keywords apply
              only without it.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: X no longer searches filter:news.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Automatic pages accept 1-300 Tweets, standard pages 1-100. Default 20. Follow
              next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          place: Search within a place ID.

          place_country: Search within a country code.

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi.

          query_type: Latest for newest first, or Top for the quotes X ranks highest. Top is X's
              ranking, not a count order, & a later page can hold a quote X ranks higher. Any
              case. Alias sort, which also takes Recency & Relevance. Send the same value with
              each cursor. Standard pages list Latest.

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          since_time: Inclusive ISO bound for Tweet creation time, such as 2026-09-25T19:20:41Z. Unix
              seconds also work. A time without an offset is UTC.

          source: X search no longer supports source. A Tweet search with it answers 424 & charges
              nothing.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

          until_time: Exclusive ISO bound for Tweet creation time. Unix seconds also work. A time
              without an offset is UTC.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: X search no longer supports within. A Tweet search with it answers 424 & charges
              nothing. Use near alone.

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
            path_template("/x/tweets/{id}/quotes", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
                        "hashtags": hashtags,
                        "include_replies": include_replies,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "keywords": keywords,
                        "language": language,
                        "list_id": list_id,
                        "max_faves": max_faves,
                        "max_id": max_id,
                        "max_quotes": max_quotes,
                        "max_replies": max_replies,
                        "max_retweets": max_retweets,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_bookmarks": min_bookmarks,
                        "min_likes": min_likes_or_min_faves(min_likes, min_faves),
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "mode": mode,
                        "native_retweets": native_retweets,
                        "near": near,
                        "news": news,
                        "omit": omit,
                        "page_size": page_size,
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
                    tweet_get_quotes_params.TweetGetQuotesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def get_replies(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        has_media_only: bool | Omit = omit,
        include_hidden: bool | Omit = omit,
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
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard", "complete"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        omit: str | Omit = omit,
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
        """Returns direct replies with automatic maximum coverage and pagination.

        A retweet
        ID returns replies to the original post. Complete mode adds nested replies,
        diagnostics, and a 424 below 80% coverage. A fully read time window returns 200.

        Args:
          after: Legacy cursor alias. Prefer cursor.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_original_author: Exclude replies written by the source-post author.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          has_media_only: Only return replies containing media.

          include_hidden: Complete mode only. Adds the replies the post's author hid, each with
              hiddenByAuthor true. They count toward limit like any reply. A paged read
              answers 400. Get its hidden replies from GET /x/tweets/{id}/hidden-replies.

          include_original_post: Include the source post and count it toward limit.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Filter by language. Alias `lang` is accepted.

          limit: Complete mode defaults to 25,000 combined direct & nested replies; set another
              total with limit. Automatic pages accept 1-300, standard pages 1-100.

          max_depth: Maximum reply depth from the source post.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Deprecated name of min_likes. Use min_likes.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Override automatic coverage. Standard uses legacy pagination. Complete adds
              nested replies, diagnostics, scope, depth, and original-post controls.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Automatic pages accept 1-300 Tweets, standard pages 1-100. Default 20. Follow
              next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          scope: Select all replies, direct replies, or nested replies.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          since_time: Inclusive ISO bound for Tweet creation time, such as 2026-09-25T19:20:41Z. Unix
              seconds also work. A time without an offset is UTC.

          sort: Sorts the selected replies before limit applies. Complete mode defaults to
              relevance. Automatic pages list the newest first unless you set sort; standard
              pages ignore it. With likes, each page is sorted by likes. A later page can hold
              a reply with more likes. The order is final on the last page. Latest & oldest
              sort every row by date. They read the whole thread first, for up to 20 s. An
              answer that stopped before every reply X shows sets orderPartial.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

          until_time: Exclusive ISO bound for Tweet creation time. Unix seconds also work. A time
              without an offset is UTC.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: Set the radius for the near filter.

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
            path_template("/x/tweets/{id}/replies", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
                        "hashtags": hashtags,
                        "has_media_only": has_media_only,
                        "include_hidden": include_hidden,
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
                        "min_likes": min_likes_or_min_faves(min_likes, min_faves),
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "mode": mode,
                        "native_retweets": native_retweets,
                        "near": near,
                        "news": news,
                        "omit": omit,
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

    def get_retweeter_ids(
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
    ) -> TweetGetRetweeterIdsResponse:
        """
        Returns the user IDs of a post's reposters, in the order & pages of
        /x/tweets/{id}/retweeters. Use it when you need IDs only. Each ID costs 1
        credit. A post nobody reposted returns an empty list for free.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          page_size: Profiles to request from this page (1-200, default 200). Source, filters or
              credits can return fewer. Follow next_cursor for more pages. Aliases: limit,
              count, max_results, maxItems, max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}/retweeter-ids", id=id),
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
                    tweet_get_retweeter_ids_params.TweetGetRetweeterIdsParams,
                ),
            ),
            cast_to=TweetGetRetweeterIdsResponse,
        )

    def get_retweeters(
        self,
        id: str,
        *,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        business_email_only: bool | Omit = omit,
        cursor: str | Omit = omit,
        email_domains: str | Omit = omit,
        enrich_profiles: bool | Omit = omit,
        fields: str | Omit = omit,
        has_email: bool | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        include_retweet_timestamp: bool | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        omit: str | Omit = omit,
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
        """Lists reposters.

        includeRetweetTimestamp adds retweeted_at in Unix seconds. Null
        means no matching repost on the newest profile page or lookup failure. The
        created field means account creation. Timestamp lookups add latency.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          email_domains: Only return profiles with an email at one of these domains. Separate domains
              with commas. Subdomains match.

          enrich_profiles: Add each row's full profile, as GET /x/users/{id} returns it. Pages take several
              seconds longer.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          has_email: Only return profiles that publish an email.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          include_retweet_timestamp: Look up repost event times.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Profiles to request from this page (1-200, default 200). Source, filters or
              credits can return fewer. Follow next_cursor for more pages. Aliases: limit,
              count, max_results, maxItems, max_items & per_page.

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
                        "blue_verified_only": blue_verified_only,
                        "business_email_only": business_email_only,
                        "cursor": cursor,
                        "email_domains": email_domains,
                        "enrich_profiles": enrich_profiles,
                        "fields": fields,
                        "has_email": has_email,
                        "has_location": has_location,
                        "has_website": has_website,
                        "include_retweet_timestamp": include_retweet_timestamp,
                        "location_contains": location_contains,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_statuses": max_statuses,
                        "min_account_age_days": min_account_age_days,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_statuses": min_statuses,
                        "omit": omit,
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

    def get_subtitles(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetGetSubtitlesResponse:
        """
        Returns the caption tracks of one public tweet's videos, as X's player reads
        them. Each track has its language, name, timed cues, and full text. A tweet
        without video, or a video without captions, returns no track and costs nothing.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}/subtitles", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_get_subtitles_params.TweetGetSubtitlesParams,
                ),
            ),
            cast_to=TweetGetSubtitlesResponse,
        )

    def get_thread(
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
        min_faves: int | Omit = omit,
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
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
        """Returns visible posts from the selected conversation thread.

        Results exclude X
        ads.

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

          min_faves: Deprecated name of min_likes. Use min_likes.

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
            path_template("/x/tweets/{id}/thread", id=id),
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
                        "min_likes": min_likes_or_min_faves(min_likes, min_faves),
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "native_retweets": native_retweets,
                        "omit": omit,
                        "page_size": page_size,
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
                    tweet_get_thread_params.TweetGetThreadParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def list_top(
        self,
        *,
        country: str | Omit = omit,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        language: str | Omit = omit,
        metric: Literal["likes", "replies", "quotes", "bookmarks", "shares", "views"] | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        window: Literal["day", "week", "month"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns the tweets X ranks highest by one metric over the last day, week or
        month, as x.com's Inspiration page shows them. Covers all of X unless you pick a
        country or a language. Pages hold up to 20 tweets, and the list ends at 100.
        Each tweet costs 1 credit.

        Args:
          country: Only tweets from one country, as a 2- or 3-letter ISO 3166 code, such as US or
              USA. Send country or language, not both.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          language: Only tweets in one language, as a 2-letter code, such as en. Send country or
              language, not both.

          metric: What to rank tweets by. Defaults to likes. Singular names work too, such as
              like.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          window: How far back to look. Defaults to day. Also takes 24h, 7d, 30d, daily, weekly
              and monthly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/tweets/top",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "cursor": cursor,
                        "fields": fields,
                        "language": language,
                        "metric": metric,
                        "omit": omit,
                        "page_size": page_size,
                        "window": window,
                    },
                    tweet_list_top_params.TweetListTopParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def resolve_links(
        self,
        *,
        urls: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetResolveLinksResponse:
        """Returns where each t.co link leads, as X's own redirect says.

        Xquik reads the
        redirect and never visits the target site. A link t.co does not have comes back
        without `resolvedUrl` and costs nothing. A link X does not answer for in time
        comes back in `unprocessedUrls`, free. Each resolved link costs 1 credit.

        Args:
          urls: 1 to 100 links of the form `https://t.co/Xe1nm2pkSX`, separated by commas. Any
              other link is refused.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/links/resolve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "urls": urls,
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_resolve_links_params.TweetResolveLinksParams,
                ),
            ),
            cast_to=TweetResolveLinksResponse,
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        keywords: str | Omit = omit,
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
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        omit: str | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: str | Omit = omit,
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
        """Tweets include authors, like counts, media, URLs & cursors.

        Omit mode for
        maximum coverage. Reuse next_cursor with unchanged filters.

        Args:
          q: Query, Tweet ID, or URL. Alias query. Hyphens negate terms. Use exactPhrase for
              literals. Valid bounds apply per page. `since:` & `until:` dates are UTC days,
              written YYYY-MM-DD. 25/12/2026 & 12/25/2026 also work, since each has 1 reading.
              04/01/2026 has 2 & answers 424 with the form to write. `since_time:` &
              `until_time:` take Unix seconds or an ISO 8601 time. `list:` takes a public
              List's ID. A private List answers 404 list_not_found. X searches up to 512
              characters. A longer query answers 424 before any read, unless a term of its
              first OR group fits alone.

          advanced_query: Raw advanced search query appended as-is.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8.

          card_name: Keep only Tweets with this card type, such as poll2choice_text_only. Tweet
              search checks each Tweet's card.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_source: X search no longer supports excludeSource. A Tweet search with it answers 424 &
              charges nothing.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          geocode: X search no longer supports geocode. A Tweet search with it answers 424 &
              charges nothing.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          keywords: Words the Tweets must match, in X search syntax.

          language: Filter by language. Alias `lang` is accepted.

          limit: Most unique matches to return after filtering. Default 20; explicit coverage
              defaults to 2000. At the deadline it returns kept rows & diagnostics. Only
              returned rows are billed; credits can cut results, & 0 affordable rows returns
              402. Aliases: pageSize, count, max_results, maxItems, max_items & per_page.

          list_id: Search within a list ID.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Deprecated name of min_likes. Use min_likes.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: X no longer searches filter:news.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          place: Search within a place ID.

          place_country: Search within a country code.

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi.

          query_type: Latest lists posts newest first. Top keeps X's engagement ranking within each
              read. Xquik reads several of X's views, so a later page can hold a post X ranks
              higher. Top skips posts X shows above a ranked reply that cannot match the
              query. They cost nothing. Any case works. Photos, Videos & Media read Latest
              with mediaType images, videos or media, unless mediaType is set. People & Lists
              answer 400 & point to /x/users/search & /x/lists/search. Aliases result_type,
              sort_order, type, search_type, product, category & section.

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date as a UTC day, written YYYY-MM-DD. 25/12/2026 & 12/25/2026 also work,
              since each has 1 reading. A date that fits both orders reads month first, so
              04/01/2026 is 1 April.

          since_id: Return Tweets whose IDs exceed this ID.

          since_time: Inclusive ISO bound for Tweet creation time, such as 2026-09-25T19:20:41Z. Unix
              seconds also work. A time without an offset is UTC.

          source: X search no longer supports source. A Tweet search with it answers 424 & charges
              nothing.

          to_user: Filter replies sent to a username.

          until_date: End date as a UTC day, inclusive, so its own posts count. It takes the same date
              forms as sinceDate.

          until_time: Exclusive ISO bound for Tweet creation time. Unix seconds also work. A time
              without an offset is UTC.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: X search no longer supports within. A Tweet search with it answers 424 & charges
              nothing. Use near alone.

          within_time: Keeps Tweets from a recent window, such as 90m or 7d. Use a whole number & s, m,
              h or d.

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
                            "fields": fields,
                            "from_user": from_user,
                            "geocode": geocode,
                            "hashtags": hashtags,
                            "in_reply_to_tweet_id": in_reply_to_tweet_id,
                            "keywords": keywords,
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
                            "min_likes": min_likes_or_min_faves(min_likes, min_faves),
                            "min_quotes": min_quotes,
                            "min_replies": min_replies,
                            "min_retweets": min_retweets,
                            "min_views": min_views,
                            "mode": mode,
                            "native_retweets": native_retweets,
                            "near": near,
                            "news": news,
                            "omit": omit,
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

    def translate(
        self,
        id: str,
        *,
        language: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetTranslateResponse:
        """
        Returns X's own translation of one public tweet into the language you pick, with
        the links, mentions, and tags X places in the translated text.

        Args:
          language: Language code to translate into, such as `en`, `tr`, `pt-br`, or `zh-tw`. Upper
              and lower case both work.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/tweets/{id}/translation", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_translate_params.TweetTranslateParams,
                ),
            ),
            cast_to=TweetTranslateResponse,
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
        Publishes a post through a connected X account.

        Args:
          account: X account (@username or account ID)

          community_id: The Community to post into, from 1 to 19 digits. The account must be a member.
              Xquik picks the Community in X's composer, checks the post request names it &
              reads the post after. A post X puts outside the Community is deleted & fails
              uncharged. Not with `reply_to_tweet_id`, since X keeps replies public.

          media: Publicly reachable URLs of up to 4 images or exactly 1 MP4 video up to 100 MB.
              Media adds 2 credits per started MB across all files.

          reply_to_tweet_id: The post to reply to. Any X post ID works, from 1 to 19 digits.

          text: Tweet text (optional when media is provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
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
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetRetrieveResponse:
        """
        Returns one public tweet with author, metrics, and media.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_retrieve_params.TweetRetrieveParams,
                ),
            ),
            cast_to=TweetRetrieveResponse,
        )

    async def list(
        self,
        *,
        ids: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetListResponse:
        """
        Returns public tweet records for the requested IDs.

        Args:
          ids: 1 to 100 posts, separated by commas. Each is a tweet ID or a tweet URL, such as
              x.com/nasa/status/20. A post named twice is read once. Any other entry is
              skipped & listed under `skipped` with why. A batch without 1 post gets 400
              `invalid_tweet_id`.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

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
                query=await async_maybe_transform(
                    {
                        "ids": ids,
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_list_params.TweetListParams,
                ),
            ),
            cast_to=TweetListResponse,
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
        Deletes an authored post through a connected X account.

        Args:
          account: X account identifier (@username or account ID)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return await self._delete(
            path_template("/x/tweets/{id}", id=id),
            body=await async_maybe_transform({"account": account}, tweet_delete_params.TweetDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TweetDeleteResponse,
        )

    async def check_repost(
        self,
        id: str,
        *,
        user: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetCheckRepostResponse:
        """Returns whether 1 account reposted the post, read from its newest posts.

        A
        repost older than the posts read returns false with complete false. Each check
        costs 1 credit.

        Args:
          user: User ID, username with or without @, or profile URL.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}/retweeters/check", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "user": user,
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_check_repost_params.TweetCheckRepostParams,
                ),
            ),
            cast_to=TweetCheckRepostResponse,
        )

    async def embed(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        hide_media: bool | Omit = omit,
        hide_thread: bool | Omit = omit,
        omit: str | Omit = omit,
        omit_script: bool | Omit = omit,
        theme: Literal["light", "dark"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetEmbedResponse:
        """
        Returns the HTML that X gives websites to embed one public tweet, with the
        tweet's link and author.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          hide_media: Set `true` to leave photos, videos, and link cards out.

          hide_thread: Set `true` to leave the tweet this one replies to out.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          omit_script: Set `true` to leave the widget script tag out, for pages that load it once
              themselves.

          theme: Color theme of the embed. X uses light when left out.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}/embed", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "hide_media": hide_media,
                        "hide_thread": hide_thread,
                        "omit": omit,
                        "omit_script": omit_script,
                        "theme": theme,
                    },
                    tweet_embed_params.TweetEmbedParams,
                ),
            ),
            cast_to=TweetEmbedResponse,
        )

    async def get_favoriters(
        self,
        id: str,
        *,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        business_email_only: bool | Omit = omit,
        cursor: str | Omit = omit,
        email_domains: str | Omit = omit,
        fields: str | Omit = omit,
        has_email: bool | Omit = omit,
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
        omit: str | Omit = omit,
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
        """Likers your X account sees, else 424 `account_required`.

        X shows likers only to
        the post author.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          email_domains: Only return profiles with an email at one of these domains. Separate domains
              with commas. Subdomains match.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          has_email: Only return profiles that publish an email.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Profiles to request from this page (1-200, default 200). Source, filters or
              credits can return fewer. Follow next_cursor for more pages. Aliases: limit,
              count, max_results, maxItems, max_items & per_page.

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
                        "blue_verified_only": blue_verified_only,
                        "business_email_only": business_email_only,
                        "cursor": cursor,
                        "email_domains": email_domains,
                        "fields": fields,
                        "has_email": has_email,
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
                        "omit": omit,
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

    async def get_hidden_replies(
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
        """
        Returns the replies the post's author hid, oldest first, with the replies to
        them. A post without hidden replies returns an empty list.

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
            path_template("/x/tweets/{id}/hidden-replies", id=id),
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
                    tweet_get_hidden_replies_params.TweetGetHiddenRepliesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def get_insights(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetGetInsightsResponse:
        """
        Returns engagement insights for one tweet: engagements per hour since it went
        up, per view and per follower of its author, and how far it spread. Each report
        costs 1 credit, whatever it reads.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}/insights", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_get_insights_params.TweetGetInsightsParams,
                ),
            ),
            cast_to=TweetGetInsightsResponse,
        )

    async def get_quotes(
        self,
        id: str,
        *,
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        include_replies: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        keywords: str | Omit = omit,
        language: str | Omit = omit,
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
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
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
    ) -> PaginatedTweets:
        """Returns public posts quoting the tweet, newest first, replies included.

        Drop
        them with replies=exclude. Send queryType=Top for the quotes X ranks highest.

        Args:
          advanced_query: Raw advanced search query appended as-is.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8.

          card_name: Keep only Tweets with this card type, such as poll2choice_text_only. Tweet
              search checks each Tweet's card.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_source: X search no longer supports excludeSource. A Tweet search with it answers 424 &
              charges nothing.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          geocode: X search no longer supports geocode. A Tweet search with it answers 424 &
              charges nothing.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_replies: Keep replies that quote the post. Automatic pages keep them unless this is
              false. Standard pages keep them only when it is true. Explicit replies takes
              precedence.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          keywords: Words the Tweets must match, in X search syntax.

          language: Filter by language. Alias `lang` is accepted.

          list_id: Search within a list ID.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Deprecated name of min_likes. Use min_likes.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Optional legacy pagination override. Search-only filters such as keywords apply
              only without it.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: X no longer searches filter:news.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Automatic pages accept 1-300 Tweets, standard pages 1-100. Default 20. Follow
              next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          place: Search within a place ID.

          place_country: Search within a country code.

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi.

          query_type: Latest for newest first, or Top for the quotes X ranks highest. Top is X's
              ranking, not a count order, & a later page can hold a quote X ranks higher. Any
              case. Alias sort, which also takes Recency & Relevance. Send the same value with
              each cursor. Standard pages list Latest.

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          since_time: Inclusive ISO bound for Tweet creation time, such as 2026-09-25T19:20:41Z. Unix
              seconds also work. A time without an offset is UTC.

          source: X search no longer supports source. A Tweet search with it answers 424 & charges
              nothing.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

          until_time: Exclusive ISO bound for Tweet creation time. Unix seconds also work. A time
              without an offset is UTC.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: X search no longer supports within. A Tweet search with it answers 424 & charges
              nothing. Use near alone.

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
            path_template("/x/tweets/{id}/quotes", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
                        "hashtags": hashtags,
                        "include_replies": include_replies,
                        "in_reply_to_tweet_id": in_reply_to_tweet_id,
                        "keywords": keywords,
                        "language": language,
                        "list_id": list_id,
                        "max_faves": max_faves,
                        "max_id": max_id,
                        "max_quotes": max_quotes,
                        "max_replies": max_replies,
                        "max_retweets": max_retweets,
                        "media_type": media_type,
                        "mentioning": mentioning,
                        "min_bookmarks": min_bookmarks,
                        "min_likes": min_likes_or_min_faves(min_likes, min_faves),
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "mode": mode,
                        "native_retweets": native_retweets,
                        "near": near,
                        "news": news,
                        "omit": omit,
                        "page_size": page_size,
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
                    tweet_get_quotes_params.TweetGetQuotesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def get_replies(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        has_media_only: bool | Omit = omit,
        include_hidden: bool | Omit = omit,
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
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard", "complete"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        omit: str | Omit = omit,
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
        """Returns direct replies with automatic maximum coverage and pagination.

        A retweet
        ID returns replies to the original post. Complete mode adds nested replies,
        diagnostics, and a 424 below 80% coverage. A fully read time window returns 200.

        Args:
          after: Legacy cursor alias. Prefer cursor.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_original_author: Exclude replies written by the source-post author.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          has_media_only: Only return replies containing media.

          include_hidden: Complete mode only. Adds the replies the post's author hid, each with
              hiddenByAuthor true. They count toward limit like any reply. A paged read
              answers 400. Get its hidden replies from GET /x/tweets/{id}/hidden-replies.

          include_original_post: Include the source post and count it toward limit.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          language: Filter by language. Alias `lang` is accepted.

          limit: Complete mode defaults to 25,000 combined direct & nested replies; set another
              total with limit. Automatic pages accept 1-300, standard pages 1-100.

          max_depth: Maximum reply depth from the source post.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Deprecated name of min_likes. Use min_likes.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Override automatic coverage. Standard uses legacy pagination. Complete adds
              nested replies, diagnostics, scope, depth, and original-post controls.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Automatic pages accept 1-300 Tweets, standard pages 1-100. Default 20. Follow
              next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          scope: Select all replies, direct replies, or nested replies.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          since_time: Inclusive ISO bound for Tweet creation time, such as 2026-09-25T19:20:41Z. Unix
              seconds also work. A time without an offset is UTC.

          sort: Sorts the selected replies before limit applies. Complete mode defaults to
              relevance. Automatic pages list the newest first unless you set sort; standard
              pages ignore it. With likes, each page is sorted by likes. A later page can hold
              a reply with more likes. The order is final on the last page. Latest & oldest
              sort every row by date. They read the whole thread first, for up to 20 s. An
              answer that stopped before every reply X shows sets orderPartial.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

          until_time: Exclusive ISO bound for Tweet creation time. Unix seconds also work. A time
              without an offset is UTC.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: Set the radius for the near filter.

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
            path_template("/x/tweets/{id}/replies", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
                        "hashtags": hashtags,
                        "has_media_only": has_media_only,
                        "include_hidden": include_hidden,
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
                        "min_likes": min_likes_or_min_faves(min_likes, min_faves),
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "mode": mode,
                        "native_retweets": native_retweets,
                        "near": near,
                        "news": news,
                        "omit": omit,
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

    async def get_retweeter_ids(
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
    ) -> TweetGetRetweeterIdsResponse:
        """
        Returns the user IDs of a post's reposters, in the order & pages of
        /x/tweets/{id}/retweeters. Use it when you need IDs only. Each ID costs 1
        credit. A post nobody reposted returns an empty list for free.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          page_size: Profiles to request from this page (1-200, default 200). Source, filters or
              credits can return fewer. Follow next_cursor for more pages. Aliases: limit,
              count, max_results, maxItems, max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}/retweeter-ids", id=id),
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
                    tweet_get_retweeter_ids_params.TweetGetRetweeterIdsParams,
                ),
            ),
            cast_to=TweetGetRetweeterIdsResponse,
        )

    async def get_retweeters(
        self,
        id: str,
        *,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        business_email_only: bool | Omit = omit,
        cursor: str | Omit = omit,
        email_domains: str | Omit = omit,
        enrich_profiles: bool | Omit = omit,
        fields: str | Omit = omit,
        has_email: bool | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        include_retweet_timestamp: bool | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        omit: str | Omit = omit,
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
        """Lists reposters.

        includeRetweetTimestamp adds retweeted_at in Unix seconds. Null
        means no matching repost on the newest profile page or lookup failure. The
        created field means account creation. Timestamp lookups add latency.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          email_domains: Only return profiles with an email at one of these domains. Separate domains
              with commas. Subdomains match.

          enrich_profiles: Add each row's full profile, as GET /x/users/{id} returns it. Pages take several
              seconds longer.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          has_email: Only return profiles that publish an email.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          include_retweet_timestamp: Look up repost event times.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Profiles to request from this page (1-200, default 200). Source, filters or
              credits can return fewer. Follow next_cursor for more pages. Aliases: limit,
              count, max_results, maxItems, max_items & per_page.

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
                        "blue_verified_only": blue_verified_only,
                        "business_email_only": business_email_only,
                        "cursor": cursor,
                        "email_domains": email_domains,
                        "enrich_profiles": enrich_profiles,
                        "fields": fields,
                        "has_email": has_email,
                        "has_location": has_location,
                        "has_website": has_website,
                        "include_retweet_timestamp": include_retweet_timestamp,
                        "location_contains": location_contains,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_statuses": max_statuses,
                        "min_account_age_days": min_account_age_days,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_statuses": min_statuses,
                        "omit": omit,
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

    async def get_subtitles(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetGetSubtitlesResponse:
        """
        Returns the caption tracks of one public tweet's videos, as X's player reads
        them. Each track has its language, name, timed cues, and full text. A tweet
        without video, or a video without captions, returns no track and costs nothing.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}/subtitles", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_get_subtitles_params.TweetGetSubtitlesParams,
                ),
            ),
            cast_to=TweetGetSubtitlesResponse,
        )

    async def get_thread(
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
        min_faves: int | Omit = omit,
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
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
        """Returns visible posts from the selected conversation thread.

        Results exclude X
        ads.

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

          min_faves: Deprecated name of min_likes. Use min_likes.

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
            path_template("/x/tweets/{id}/thread", id=id),
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
                        "min_likes": min_likes_or_min_faves(min_likes, min_faves),
                        "min_quotes": min_quotes,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "native_retweets": native_retweets,
                        "omit": omit,
                        "page_size": page_size,
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
                    tweet_get_thread_params.TweetGetThreadParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def list_top(
        self,
        *,
        country: str | Omit = omit,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        language: str | Omit = omit,
        metric: Literal["likes", "replies", "quotes", "bookmarks", "shares", "views"] | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        window: Literal["day", "week", "month"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns the tweets X ranks highest by one metric over the last day, week or
        month, as x.com's Inspiration page shows them. Covers all of X unless you pick a
        country or a language. Pages hold up to 20 tweets, and the list ends at 100.
        Each tweet costs 1 credit.

        Args:
          country: Only tweets from one country, as a 2- or 3-letter ISO 3166 code, such as US or
              USA. Send country or language, not both.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          language: Only tweets in one language, as a 2-letter code, such as en. Send country or
              language, not both.

          metric: What to rank tweets by. Defaults to likes. Singular names work too, such as
              like.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          window: How far back to look. Defaults to day. Also takes 24h, 7d, 30d, daily, weekly
              and monthly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/tweets/top",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "cursor": cursor,
                        "fields": fields,
                        "language": language,
                        "metric": metric,
                        "omit": omit,
                        "page_size": page_size,
                        "window": window,
                    },
                    tweet_list_top_params.TweetListTopParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def resolve_links(
        self,
        *,
        urls: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetResolveLinksResponse:
        """Returns where each t.co link leads, as X's own redirect says.

        Xquik reads the
        redirect and never visits the target site. A link t.co does not have comes back
        without `resolvedUrl` and costs nothing. A link X does not answer for in time
        comes back in `unprocessedUrls`, free. Each resolved link costs 1 credit.

        Args:
          urls: 1 to 100 links of the form `https://t.co/Xe1nm2pkSX`, separated by commas. Any
              other link is refused.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/links/resolve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "urls": urls,
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_resolve_links_params.TweetResolveLinksParams,
                ),
            ),
            cast_to=TweetResolveLinksResponse,
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        keywords: str | Omit = omit,
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
        min_likes: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        omit: str | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: str | Omit = omit,
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
        """Tweets include authors, like counts, media, URLs & cursors.

        Omit mode for
        maximum coverage. Reuse next_cursor with unchanged filters.

        Args:
          q: Query, Tweet ID, or URL. Alias query. Hyphens negate terms. Use exactPhrase for
              literals. Valid bounds apply per page. `since:` & `until:` dates are UTC days,
              written YYYY-MM-DD. 25/12/2026 & 12/25/2026 also work, since each has 1 reading.
              04/01/2026 has 2 & answers 424 with the form to write. `since_time:` &
              `until_time:` take Unix seconds or an ISO 8601 time. `list:` takes a public
              List's ID. A private List answers 404 list_not_found. X searches up to 512
              characters. A longer query answers 424 before any read, unless a term of its
              first OR group fits alone.

          advanced_query: Raw advanced search query appended as-is.

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8.

          card_name: Keep only Tweets with this card type, such as poll2choice_text_only. Tweet
              search checks each Tweet's card.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_source: X search no longer supports excludeSource. A Tweet search with it answers 424 &
              charges nothing.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          from_user: Filter by author username.

          geocode: X search no longer supports geocode. A Tweet search with it answers 424 &
              charges nothing.

          hashtags: Hashtags separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          keywords: Words the Tweets must match, in X search syntax.

          language: Filter by language. Alias `lang` is accepted.

          limit: Most unique matches to return after filtering. Default 20; explicit coverage
              defaults to 2000. At the deadline it returns kept rows & diagnostics. Only
              returned rows are billed; credits can cut results, & 0 affordable rows returns
              402. Aliases: pageSize, count, max_results, maxItems, max_items & per_page.

          list_id: Search within a list ID.

          max_faves: Maximum likes threshold. maxLikes & max_likes also work.

          max_id: Return Tweets at or below this ID.

          max_quotes: Maximum quotes threshold.

          max_replies: Maximum replies threshold.

          max_retweets: Maximum retweets threshold.

          media_type: Filter media. Aliases: has_video, has_media.

          mentioning: Filter tweets mentioning a username.

          min_bookmarks: Minimum bookmark count threshold.

          min_faves: Deprecated name of min_likes. Use min_likes.

          min_likes: Minimum likes. Aliases: minFaves, min_likes, min_faves.

          min_quotes: Minimum quote count threshold.

          min_replies: Minimum replies threshold.

          min_retweets: Minimum retweets threshold.

          min_views: Minimum view count threshold.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: X no longer searches filter:news.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          place: Search within a place ID.

          place_country: Search within a country code.

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi.

          query_type: Latest lists posts newest first. Top keeps X's engagement ranking within each
              read. Xquik reads several of X's views, so a later page can hold a post X ranks
              higher. Top skips posts X shows above a ranked reply that cannot match the
              query. They cost nothing. Any case works. Photos, Videos & Media read Latest
              with mediaType images, videos or media, unless mediaType is set. People & Lists
              answer 400 & point to /x/users/search & /x/lists/search. Aliases result_type,
              sort_order, type, search_type, product, category & section.

          quotes: Only when the caller requests a quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode. Exclude keeps own-thread replies.

          retweets: Only when the caller requests a repost mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date as a UTC day, written YYYY-MM-DD. 25/12/2026 & 12/25/2026 also work,
              since each has 1 reading. A date that fits both orders reads month first, so
              04/01/2026 is 1 April.

          since_id: Return Tweets whose IDs exceed this ID.

          since_time: Inclusive ISO bound for Tweet creation time, such as 2026-09-25T19:20:41Z. Unix
              seconds also work. A time without an offset is UTC.

          source: X search no longer supports source. A Tweet search with it answers 424 & charges
              nothing.

          to_user: Filter replies sent to a username.

          until_date: End date as a UTC day, inclusive, so its own posts count. It takes the same date
              forms as sinceDate.

          until_time: Exclusive ISO bound for Tweet creation time. Unix seconds also work. A time
              without an offset is UTC.

          url: URL substring or domain filter.

          verified_only: Only return tweets from verified authors.

          within: X search no longer supports within. A Tweet search with it answers 424 & charges
              nothing. Use near alone.

          within_time: Keeps Tweets from a recent window, such as 90m or 7d. Use a whole number & s, m,
              h or d.

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
                            "fields": fields,
                            "from_user": from_user,
                            "geocode": geocode,
                            "hashtags": hashtags,
                            "in_reply_to_tweet_id": in_reply_to_tweet_id,
                            "keywords": keywords,
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
                            "min_likes": min_likes_or_min_faves(min_likes, min_faves),
                            "min_quotes": min_quotes,
                            "min_replies": min_replies,
                            "min_retweets": min_retweets,
                            "min_views": min_views,
                            "mode": mode,
                            "native_retweets": native_retweets,
                            "near": near,
                            "news": news,
                            "omit": omit,
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

    async def translate(
        self,
        id: str,
        *,
        language: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TweetTranslateResponse:
        """
        Returns X's own translation of one public tweet into the language you pick, with
        the links, mentions, and tags X places in the translated text.

        Args:
          language: Language code to translate into, such as `en`, `tr`, `pt-br`, or `zh-tw`. Upper
              and lower case both work.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/tweets/{id}/translation", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "fields": fields,
                        "omit": omit,
                    },
                    tweet_translate_params.TweetTranslateParams,
                ),
            ),
            cast_to=TweetTranslateResponse,
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
        self.check_repost = to_raw_response_wrapper(
            tweets.check_repost,
        )
        self.embed = to_raw_response_wrapper(
            tweets.embed,
        )
        self.get_favoriters = to_raw_response_wrapper(
            tweets.get_favoriters,
        )
        self.get_hidden_replies = to_raw_response_wrapper(
            tweets.get_hidden_replies,
        )
        self.get_insights = to_raw_response_wrapper(
            tweets.get_insights,
        )
        self.get_quotes = to_raw_response_wrapper(
            tweets.get_quotes,
        )
        self.get_replies = to_raw_response_wrapper(
            tweets.get_replies,
        )
        self.get_retweeter_ids = to_raw_response_wrapper(
            tweets.get_retweeter_ids,
        )
        self.get_retweeters = to_raw_response_wrapper(
            tweets.get_retweeters,
        )
        self.get_subtitles = to_raw_response_wrapper(
            tweets.get_subtitles,
        )
        self.get_thread = to_raw_response_wrapper(
            tweets.get_thread,
        )
        self.list_top = to_raw_response_wrapper(
            tweets.list_top,
        )
        self.resolve_links = to_raw_response_wrapper(
            tweets.resolve_links,
        )
        self.search = to_raw_response_wrapper(
            tweets.search,
        )
        self.translate = to_raw_response_wrapper(
            tweets.translate,
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
        self.check_repost = async_to_raw_response_wrapper(
            tweets.check_repost,
        )
        self.embed = async_to_raw_response_wrapper(
            tweets.embed,
        )
        self.get_favoriters = async_to_raw_response_wrapper(
            tweets.get_favoriters,
        )
        self.get_hidden_replies = async_to_raw_response_wrapper(
            tweets.get_hidden_replies,
        )
        self.get_insights = async_to_raw_response_wrapper(
            tweets.get_insights,
        )
        self.get_quotes = async_to_raw_response_wrapper(
            tweets.get_quotes,
        )
        self.get_replies = async_to_raw_response_wrapper(
            tweets.get_replies,
        )
        self.get_retweeter_ids = async_to_raw_response_wrapper(
            tweets.get_retweeter_ids,
        )
        self.get_retweeters = async_to_raw_response_wrapper(
            tweets.get_retweeters,
        )
        self.get_subtitles = async_to_raw_response_wrapper(
            tweets.get_subtitles,
        )
        self.get_thread = async_to_raw_response_wrapper(
            tweets.get_thread,
        )
        self.list_top = async_to_raw_response_wrapper(
            tweets.list_top,
        )
        self.resolve_links = async_to_raw_response_wrapper(
            tweets.resolve_links,
        )
        self.search = async_to_raw_response_wrapper(
            tweets.search,
        )
        self.translate = async_to_raw_response_wrapper(
            tweets.translate,
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
        self.check_repost = to_streamed_response_wrapper(
            tweets.check_repost,
        )
        self.embed = to_streamed_response_wrapper(
            tweets.embed,
        )
        self.get_favoriters = to_streamed_response_wrapper(
            tweets.get_favoriters,
        )
        self.get_hidden_replies = to_streamed_response_wrapper(
            tweets.get_hidden_replies,
        )
        self.get_insights = to_streamed_response_wrapper(
            tweets.get_insights,
        )
        self.get_quotes = to_streamed_response_wrapper(
            tweets.get_quotes,
        )
        self.get_replies = to_streamed_response_wrapper(
            tweets.get_replies,
        )
        self.get_retweeter_ids = to_streamed_response_wrapper(
            tweets.get_retweeter_ids,
        )
        self.get_retweeters = to_streamed_response_wrapper(
            tweets.get_retweeters,
        )
        self.get_subtitles = to_streamed_response_wrapper(
            tweets.get_subtitles,
        )
        self.get_thread = to_streamed_response_wrapper(
            tweets.get_thread,
        )
        self.list_top = to_streamed_response_wrapper(
            tweets.list_top,
        )
        self.resolve_links = to_streamed_response_wrapper(
            tweets.resolve_links,
        )
        self.search = to_streamed_response_wrapper(
            tweets.search,
        )
        self.translate = to_streamed_response_wrapper(
            tweets.translate,
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
        self.check_repost = async_to_streamed_response_wrapper(
            tweets.check_repost,
        )
        self.embed = async_to_streamed_response_wrapper(
            tweets.embed,
        )
        self.get_favoriters = async_to_streamed_response_wrapper(
            tweets.get_favoriters,
        )
        self.get_hidden_replies = async_to_streamed_response_wrapper(
            tweets.get_hidden_replies,
        )
        self.get_insights = async_to_streamed_response_wrapper(
            tweets.get_insights,
        )
        self.get_quotes = async_to_streamed_response_wrapper(
            tweets.get_quotes,
        )
        self.get_replies = async_to_streamed_response_wrapper(
            tweets.get_replies,
        )
        self.get_retweeter_ids = async_to_streamed_response_wrapper(
            tweets.get_retweeter_ids,
        )
        self.get_retweeters = async_to_streamed_response_wrapper(
            tweets.get_retweeters,
        )
        self.get_subtitles = async_to_streamed_response_wrapper(
            tweets.get_subtitles,
        )
        self.get_thread = async_to_streamed_response_wrapper(
            tweets.get_thread,
        )
        self.list_top = async_to_streamed_response_wrapper(
            tweets.list_top,
        )
        self.resolve_links = async_to_streamed_response_wrapper(
            tweets.resolve_links,
        )
        self.search = async_to_streamed_response_wrapper(
            tweets.search,
        )
        self.translate = async_to_streamed_response_wrapper(
            tweets.translate,
        )

    @cached_property
    def like(self) -> AsyncLikeResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncLikeResourceWithStreamingResponse(self._tweets.like)

    @cached_property
    def retweet(self) -> AsyncRetweetResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncRetweetResourceWithStreamingResponse(self._tweets.retweet)
