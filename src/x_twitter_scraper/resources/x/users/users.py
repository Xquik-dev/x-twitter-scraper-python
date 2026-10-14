# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, Union, cast
from datetime import date
from typing_extensions import Literal

import httpx

from .follow import (
    FollowResource,
    AsyncFollowResource,
    FollowResourceWithRawResponse,
    AsyncFollowResourceWithRawResponse,
    FollowResourceWithStreamingResponse,
    AsyncFollowResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.x import (
    user_retrieve_params,
    user_retrieve_live_params,
    user_translate_bio_params,
    user_retrieve_batch_params,
    user_retrieve_likes_params,
    user_retrieve_lists_params,
    user_retrieve_media_params,
    user_remove_follower_params,
    user_retrieve_search_params,
    user_retrieve_tweets_params,
    user_retrieve_replies_params,
    user_retrieve_similar_params,
    user_retrieve_articles_params,
    user_retrieve_insights_params,
    user_retrieve_mentions_params,
    user_retrieve_followers_params,
    user_retrieve_following_params,
    user_retrieve_affiliates_params,
    user_retrieve_highlights_params,
    user_retrieve_batch_tweets_params,
    user_retrieve_follower_ids_params,
    user_retrieve_following_ids_params,
    user_retrieve_subscriptions_params,
    user_retrieve_list_memberships_params,
    user_retrieve_followers_you_know_params,
    user_retrieve_verified_followers_params,
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
from ....types.shared.user_profile import UserProfile
from ....types.shared.paginated_users import PaginatedUsers
from ....types.shared.paginated_tweets import PaginatedTweets
from ....types.x.user_retrieve_live_response import UserRetrieveLiveResponse
from ....types.x.user_translate_bio_response import UserTranslateBioResponse
from ....types.x.user_retrieve_batch_response import UserRetrieveBatchResponse
from ....types.x.user_retrieve_lists_response import UserRetrieveListsResponse
from ....types.x.user_remove_follower_response import UserRemoveFollowerResponse
from ....types.x.user_retrieve_insights_response import UserRetrieveInsightsResponse
from ....types.x.user_retrieve_followers_response import UserRetrieveFollowersResponse
from ....types.x.user_retrieve_following_response import UserRetrieveFollowingResponse
from ....types.x.user_retrieve_batch_tweets_response import UserRetrieveBatchTweetsResponse
from ....types.x.user_retrieve_follower_ids_response import UserRetrieveFollowerIdsResponse
from ....types.x.user_retrieve_following_ids_response import UserRetrieveFollowingIdsResponse
from ....types.x.user_retrieve_list_memberships_response import UserRetrieveListMembershipsResponse
from ....types.x.user_retrieve_verified_followers_response import UserRetrieveVerifiedFollowersResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def follow(self) -> FollowResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return FollowResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfile:
        """
        Returns one public profile with counts and verification details.

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
            path_template("/x/users/{id}", id=id),
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
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=UserProfile,
        )

    def remove_follower(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRemoveFollowerResponse:
        """
        Removes a follower from a connected X account.

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
        return self._post(
            path_template("/x/users/{id}/remove-follower", id=id),
            body=maybe_transform({"account": account}, user_remove_follower_params.UserRemoveFollowerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRemoveFollowerResponse,
        )

    def retrieve_affiliates(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """Returns the accounts an organization lists as its affiliates, in X's order.

        An
        account without affiliates returns an empty list.

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
            path_template("/x/users/{id}/affiliates", id=id),
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
                    user_retrieve_affiliates_params.UserRetrieveAffiliatesParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_articles(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns the posts on the user's Articles tab, newest first.

        Each post's
        `article` holds the Article's ID, title, preview, cover & dates. Read the full
        text with GET /x/articles/{tweetId}.

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
            path_template("/x/users/{id}/articles", id=id),
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
                    user_retrieve_articles_params.UserRetrieveArticlesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_batch(
        self,
        *,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        business_email_only: bool | Omit = omit,
        email_domains: str | Omit = omit,
        fields: str | Omit = omit,
        has_email: bool | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        ids: str | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        omit: str | Omit = omit,
        username_contains: str | Omit = omit,
        usernames: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveBatchResponse:
        """Returns public profiles for up to 100 user IDs, usernames or profile links.

        Send
        ids or usernames, not both. Each returned profile costs 1 credit.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

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

          ids: Comma-separated numeric user IDs (1-100 values). Duplicate IDs are ignored while
              preserving first-seen order.

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

          username_contains: Match a username substring, ignoring case.

          usernames: Comma-separated X usernames, with or without @, or profile links such as
              x.com/nasa (1-100 values), in place of ids. A name in another case is the same
              account.

          verified_only: Only return verified profiles.

          verified_type: Match the verification type exactly, ignoring case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/users/batch",
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
                        "email_domains": email_domains,
                        "fields": fields,
                        "has_email": has_email,
                        "has_location": has_location,
                        "has_website": has_website,
                        "ids": ids,
                        "location_contains": location_contains,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_statuses": max_statuses,
                        "min_account_age_days": min_account_age_days,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_statuses": min_statuses,
                        "omit": omit,
                        "username_contains": username_contains,
                        "usernames": usernames,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
                    },
                    user_retrieve_batch_params.UserRetrieveBatchParams,
                ),
            ),
            cast_to=UserRetrieveBatchResponse,
        )

    def retrieve_batch_tweets(
        self,
        *,
        fields: str | Omit = omit,
        ids: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        usernames: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveBatchTweetsResponse:
        """
        Returns the newest posts of up to 20 users, named by user ID, username or
        profile link, in the order named. Send ids or usernames, not both. Each post
        costs 1 credit. A user in unavailable_ids or unprocessed_ids costs nothing.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          ids: Comma-separated numeric user IDs (1-20 values). Duplicate IDs are ignored while
              preserving first-seen order.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Posts per user (1-20, default 20). Credits can return fewer. Aliases: limit,
              count, max_results, maxItems, max_items & per_page.

          usernames: Comma-separated X usernames, with or without @, or profile links such as
              x.com/nasa (1-20 values), in place of ids. A name in another case is the same
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/users/batch/tweets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "ids": ids,
                        "omit": omit,
                        "page_size": page_size,
                        "usernames": usernames,
                    },
                    user_retrieve_batch_tweets_params.UserRetrieveBatchTweetsParams,
                ),
            ),
            cast_to=UserRetrieveBatchTweetsResponse,
        )

    def retrieve_follower_ids(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveFollowerIdsResponse:
        """
        Returns the user IDs of the selected user's followers, newest first, up to 5,000
        a page. Use it when you need IDs only. Each ID costs 1 credit.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          page_size: User IDs to request from this page (1-5000, default 5000). Credits can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/follower-ids", id=id),
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
                    user_retrieve_follower_ids_params.UserRetrieveFollowerIdsParams,
                ),
            ),
            cast_to=UserRetrieveFollowerIdsResponse,
        )

    def retrieve_followers(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_scan: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveFollowersResponse:
        """Returns public follower profiles for the selected user, newest first.

        x.com puts
        some promoted followers first; Xquik doesn't.

        Args:
          after: Legacy cursor alias. Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

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

          limit: Legacy page-size alias outside coverage mode. Coverage accepts 1-10000. Prefer
              pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_scan: Most profiles 1 request reads, kept or dropped by the filters. A filter that
              keeps few profiles reads up to 65 s a request without it. The request then
              answers the profiles it kept, the count it dropped & the cursor to read on. Each
              request of a cursor may send its own value. Automatic mode only.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Up to 300 user profiles in automatic mode, 200 in standard. Sources can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

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
        return cast(
            UserRetrieveFollowersResponse,
            self._get(
                path_template("/x/users/{id}/followers", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "after": after,
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
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_scan": max_scan,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "omit": omit,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_followers_params.UserRetrieveFollowersParams,
                    ),
                ),
                cast_to=cast(Any, UserRetrieveFollowersResponse),
            ),
        )

    def retrieve_followers_you_know(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Mutuals your X account sees, else 424 `account_required`.

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
            path_template("/x/users/{id}/followers-you-know", id=id),
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
                    user_retrieve_followers_you_know_params.UserRetrieveFollowersYouKnowParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_following(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_scan: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveFollowingResponse:
        """
        Returns public profiles followed by the selected user.

        Args:
          after: Legacy cursor alias. Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

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

          limit: Legacy page-size alias outside coverage mode. Coverage accepts 1-10000. Prefer
              pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_scan: Most profiles 1 request reads, kept or dropped by the filters. A filter that
              keeps few profiles reads up to 65 s a request without it. The request then
              answers the profiles it kept, the count it dropped & the cursor to read on. Each
              request of a cursor may send its own value. Automatic mode only.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Up to 300 user profiles in automatic mode, 200 in standard. Sources can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

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
        return cast(
            UserRetrieveFollowingResponse,
            self._get(
                path_template("/x/users/{id}/following", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "after": after,
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
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_scan": max_scan,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "omit": omit,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_following_params.UserRetrieveFollowingParams,
                    ),
                ),
                cast_to=cast(Any, UserRetrieveFollowingResponse),
            ),
        )

    def retrieve_following_ids(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveFollowingIdsResponse:
        """
        Returns the user IDs of the accounts the selected user follows, newest first, up
        to 5,000 a page. Use it when you need IDs only. Each ID costs 1 credit.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          page_size: User IDs to request from this page (1-5000, default 5000). Credits can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/following-ids", id=id),
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
                    user_retrieve_following_ids_params.UserRetrieveFollowingIdsParams,
                ),
            ),
            cast_to=UserRetrieveFollowingIdsResponse,
        )

    def retrieve_highlights(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns the posts on the user's Highlights tab, in X's order.

        An account without
        highlights returns an empty list.

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
            path_template("/x/users/{id}/highlights", id=id),
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
                    user_retrieve_highlights_params.UserRetrieveHighlightsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_insights(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveInsightsResponse:
        """
        Returns engagement insights for one profile: engagement rate, averages per post
        and posting rate, from its counts and its last 20 posts. Reposts and the pinned
        post stay out of the averages. Each report costs 1 credit, whatever it reads.

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
            path_template("/x/users/{id}/insights", id=id),
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
                    user_retrieve_insights_params.UserRetrieveInsightsParams,
                ),
            ),
            cast_to=UserRetrieveInsightsResponse,
        )

    def retrieve_likes(
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
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
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Your X account's likes, else 424 `account_required`.

        Others' likes get 424
        `likes_unavailable`.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

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

          near: Match a place name.

          news: Only return news results.

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

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

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
            path_template("/x/users/{id}/likes", id=id),
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
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
                        "since_date": since_date,
                        "since_id": since_id,
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
                        "url": url,
                        "verified_only": verified_only,
                        "within": within,
                        "within_time": within_time,
                    },
                    user_retrieve_likes_params.UserRetrieveLikesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_list_memberships(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveListMembershipsResponse:
        """
        Returns the public X Lists that include the selected user, as the profile's List
        memberships page shows them. Each List costs 1 credit. A protected account
        answers 403.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/list-memberships", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "fields": fields,
                        "omit": omit,
                        "page_size": page_size,
                    },
                    user_retrieve_list_memberships_params.UserRetrieveListMembershipsParams,
                ),
            ),
            cast_to=UserRetrieveListMembershipsResponse,
        )

    def retrieve_lists(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveListsResponse:
        """
        Returns the public X Lists the selected user created, in X's order, as the
        profile's Lists tab shows them. Each List costs 1 credit. A protected account
        answers 403.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/x/users/{id}/lists", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "fields": fields,
                        "omit": omit,
                        "page_size": page_size,
                    },
                    user_retrieve_lists_params.UserRetrieveListsParams,
                ),
            ),
            cast_to=UserRetrieveListsResponse,
        )

    def retrieve_live(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveLiveResponse:
        """
        Says whether one user is broadcasting live video on X right now, with their
        latest broadcast, live or ended. Each check costs 1 credit.

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
            path_template("/x/users/{id}/live", id=id),
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
                    user_retrieve_live_params.UserRetrieveLiveParams,
                ),
            ),
            cast_to=UserRetrieveLiveResponse,
        )

    def retrieve_media(
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
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
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns public media posts from the selected user.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

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

          near: Match a place name.

          news: Only return news results.

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

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

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
            path_template("/x/users/{id}/media", id=id),
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
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
                        "since_date": since_date,
                        "since_id": since_id,
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
                        "url": url,
                        "verified_only": verified_only,
                        "within": within,
                        "within_time": within_time,
                    },
                    user_retrieve_media_params.UserRetrieveMediaParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_mentions(
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns public posts mentioning the selected user.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

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

          near: Match a place name.

          news: Only return news results.

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

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          since_time: Inclusive ISO bound for Tweet creation time, such as 2026-09-25T19:20:41Z. Unix
              seconds also work. A time without an offset is UTC.

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
            path_template("/x/users/{id}/mentions", id=id),
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
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
                    user_retrieve_mentions_params.UserRetrieveMentionsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_replies(
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
        include_parent_tweet: bool | Omit = omit,
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns target-authored posts & replies, without other authors' context.

        Omit
        mode for automatic maximum coverage. Pass next_cursor unchanged; unprefixed
        cursors are legacy. It never opens with the pinned tweet.

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

          include_parent_tweet: Include each reply's parent tweet as parentTweet on the reply. A reply whose
              parent X does not return comes without it. Search-only filters such as keywords
              do not apply with it.

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
            path_template("/x/users/{id}/replies", id=id),
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
                        "include_parent_tweet": include_parent_tweet,
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
                    user_retrieve_replies_params.UserRetrieveRepliesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_search(
        self,
        *,
        q: str,
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Returns public profiles matching a name or username.

        Args:
          q: User search query

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

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          username_contains: Match a username substring, ignoring case.

          verified_only: Only return verified profiles.

          verified_type: Match the verification type exactly, ignoring case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/users/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
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
                    user_retrieve_search_params.UserRetrieveSearchParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_similar(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Returns the public accounts X lists as similar to the selected user, in X's
        order. X can list slightly different accounts on each call. Each account costs 1
        credit.

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
            path_template("/x/users/{id}/similar", id=id),
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
                    user_retrieve_similar_params.UserRetrieveSimilarParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_subscriptions(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """Returns the creators the selected user subscribes to, in X's order.

        An account
        that hides its subscriptions returns an empty list.

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
            path_template("/x/users/{id}/subscriptions", id=id),
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
                    user_retrieve_subscriptions_params.UserRetrieveSubscriptionsParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_tweets(
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
        include_parent_tweet: bool | Omit = omit,
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """For the newest posts of 2 to 20 users, use getBatchUserTweets.

        For more, use
        createExtraction with tweet_search_extractor & targetUsernames. Omit mode for
        automatic maximum coverage. Pass next_cursor unchanged; unprefixed cursors are
        legacy. The first page opens with the pinned tweet, flagged isPinned, unless
        replies are included. Rows stay newest first. x.com's Posts tab groups
        self-threads & hides reposts; retweets=exclude drops reposts.

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

          include_parent_tweet: Include each reply's parent tweet as parentTweet on the reply. A reply whose
              parent X does not return comes without it. Search-only filters such as keywords
              do not apply with it.

          include_replies: Include reply tweets unless replies specifies another mode.

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
            path_template("/x/users/{id}/tweets", id=id),
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
                        "include_parent_tweet": include_parent_tweet,
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
                    user_retrieve_tweets_params.UserRetrieveTweetsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_verified_followers(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_scan: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveVerifiedFollowersResponse:
        """
        Returns verified public profiles following the selected user.

        Args:
          after: Legacy cursor alias. Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

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

          limit: Legacy page-size alias outside coverage mode. Coverage accepts 1-10000. Prefer
              pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_scan: Most profiles 1 request reads, kept or dropped by the filters. A filter that
              keeps few profiles reads up to 65 s a request without it. The request then
              answers the profiles it kept, the count it dropped & the cursor to read on. Each
              request of a cursor may send its own value. Automatic mode only.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Up to 300 user profiles in automatic mode, 200 in standard. Sources can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

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
        return cast(
            UserRetrieveVerifiedFollowersResponse,
            self._get(
                path_template("/x/users/{id}/verified-followers", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "after": after,
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
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_scan": max_scan,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "omit": omit,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_verified_followers_params.UserRetrieveVerifiedFollowersParams,
                    ),
                ),
                cast_to=cast(Any, UserRetrieveVerifiedFollowersResponse),
            ),
        )

    def translate_bio(
        self,
        id: str,
        *,
        language: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserTranslateBioResponse:
        """
        Returns X's own translation of one profile's bio into the language you pick,
        with the links, mentions, and tags X places in the translated text. A profile
        without a bio returns translation null & a message, free of charge.

        Args:
          language: Language code to translate into, such as `es`, `tr`, `pt-br`, or `zh-tw`. Upper
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
            path_template("/x/users/{id}/translation", id=id),
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
                    user_translate_bio_params.UserTranslateBioParams,
                ),
            ),
            cast_to=UserTranslateBioResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def follow(self) -> AsyncFollowResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncFollowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfile:
        """
        Returns one public profile with counts and verification details.

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
            path_template("/x/users/{id}", id=id),
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
                    user_retrieve_params.UserRetrieveParams,
                ),
            ),
            cast_to=UserProfile,
        )

    async def remove_follower(
        self,
        id: str,
        *,
        account: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRemoveFollowerResponse:
        """
        Removes a follower from a connected X account.

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
        return await self._post(
            path_template("/x/users/{id}/remove-follower", id=id),
            body=await async_maybe_transform(
                {"account": account}, user_remove_follower_params.UserRemoveFollowerParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRemoveFollowerResponse,
        )

    async def retrieve_affiliates(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """Returns the accounts an organization lists as its affiliates, in X's order.

        An
        account without affiliates returns an empty list.

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
            path_template("/x/users/{id}/affiliates", id=id),
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
                    user_retrieve_affiliates_params.UserRetrieveAffiliatesParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_articles(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns the posts on the user's Articles tab, newest first.

        Each post's
        `article` holds the Article's ID, title, preview, cover & dates. Read the full
        text with GET /x/articles/{tweetId}.

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
            path_template("/x/users/{id}/articles", id=id),
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
                    user_retrieve_articles_params.UserRetrieveArticlesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_batch(
        self,
        *,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        business_email_only: bool | Omit = omit,
        email_domains: str | Omit = omit,
        fields: str | Omit = omit,
        has_email: bool | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        ids: str | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        omit: str | Omit = omit,
        username_contains: str | Omit = omit,
        usernames: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveBatchResponse:
        """Returns public profiles for up to 100 user IDs, usernames or profile links.

        Send
        ids or usernames, not both. Each returned profile costs 1 credit.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

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

          ids: Comma-separated numeric user IDs (1-100 values). Duplicate IDs are ignored while
              preserving first-seen order.

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

          username_contains: Match a username substring, ignoring case.

          usernames: Comma-separated X usernames, with or without @, or profile links such as
              x.com/nasa (1-100 values), in place of ids. A name in another case is the same
              account.

          verified_only: Only return verified profiles.

          verified_type: Match the verification type exactly, ignoring case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/users/batch",
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
                        "email_domains": email_domains,
                        "fields": fields,
                        "has_email": has_email,
                        "has_location": has_location,
                        "has_website": has_website,
                        "ids": ids,
                        "location_contains": location_contains,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_statuses": max_statuses,
                        "min_account_age_days": min_account_age_days,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_statuses": min_statuses,
                        "omit": omit,
                        "username_contains": username_contains,
                        "usernames": usernames,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
                    },
                    user_retrieve_batch_params.UserRetrieveBatchParams,
                ),
            ),
            cast_to=UserRetrieveBatchResponse,
        )

    async def retrieve_batch_tweets(
        self,
        *,
        fields: str | Omit = omit,
        ids: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        usernames: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveBatchTweetsResponse:
        """
        Returns the newest posts of up to 20 users, named by user ID, username or
        profile link, in the order named. Send ids or usernames, not both. Each post
        costs 1 credit. A user in unavailable_ids or unprocessed_ids costs nothing.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          ids: Comma-separated numeric user IDs (1-20 values). Duplicate IDs are ignored while
              preserving first-seen order.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Posts per user (1-20, default 20). Credits can return fewer. Aliases: limit,
              count, max_results, maxItems, max_items & per_page.

          usernames: Comma-separated X usernames, with or without @, or profile links such as
              x.com/nasa (1-20 values), in place of ids. A name in another case is the same
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/users/batch/tweets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "ids": ids,
                        "omit": omit,
                        "page_size": page_size,
                        "usernames": usernames,
                    },
                    user_retrieve_batch_tweets_params.UserRetrieveBatchTweetsParams,
                ),
            ),
            cast_to=UserRetrieveBatchTweetsResponse,
        )

    async def retrieve_follower_ids(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveFollowerIdsResponse:
        """
        Returns the user IDs of the selected user's followers, newest first, up to 5,000
        a page. Use it when you need IDs only. Each ID costs 1 credit.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          page_size: User IDs to request from this page (1-5000, default 5000). Credits can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/follower-ids", id=id),
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
                    user_retrieve_follower_ids_params.UserRetrieveFollowerIdsParams,
                ),
            ),
            cast_to=UserRetrieveFollowerIdsResponse,
        )

    async def retrieve_followers(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_scan: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveFollowersResponse:
        """Returns public follower profiles for the selected user, newest first.

        x.com puts
        some promoted followers first; Xquik doesn't.

        Args:
          after: Legacy cursor alias. Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

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

          limit: Legacy page-size alias outside coverage mode. Coverage accepts 1-10000. Prefer
              pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_scan: Most profiles 1 request reads, kept or dropped by the filters. A filter that
              keeps few profiles reads up to 65 s a request without it. The request then
              answers the profiles it kept, the count it dropped & the cursor to read on. Each
              request of a cursor may send its own value. Automatic mode only.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Up to 300 user profiles in automatic mode, 200 in standard. Sources can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

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
        return cast(
            UserRetrieveFollowersResponse,
            await self._get(
                path_template("/x/users/{id}/followers", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "after": after,
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
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_scan": max_scan,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "omit": omit,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_followers_params.UserRetrieveFollowersParams,
                    ),
                ),
                cast_to=cast(Any, UserRetrieveFollowersResponse),
            ),
        )

    async def retrieve_followers_you_know(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Mutuals your X account sees, else 424 `account_required`.

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
            path_template("/x/users/{id}/followers-you-know", id=id),
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
                    user_retrieve_followers_you_know_params.UserRetrieveFollowersYouKnowParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_following(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_scan: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveFollowingResponse:
        """
        Returns public profiles followed by the selected user.

        Args:
          after: Legacy cursor alias. Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

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

          limit: Legacy page-size alias outside coverage mode. Coverage accepts 1-10000. Prefer
              pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_scan: Most profiles 1 request reads, kept or dropped by the filters. A filter that
              keeps few profiles reads up to 65 s a request without it. The request then
              answers the profiles it kept, the count it dropped & the cursor to read on. Each
              request of a cursor may send its own value. Automatic mode only.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Up to 300 user profiles in automatic mode, 200 in standard. Sources can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

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
        return cast(
            UserRetrieveFollowingResponse,
            await self._get(
                path_template("/x/users/{id}/following", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "after": after,
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
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_scan": max_scan,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "omit": omit,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_following_params.UserRetrieveFollowingParams,
                    ),
                ),
                cast_to=cast(Any, UserRetrieveFollowingResponse),
            ),
        )

    async def retrieve_following_ids(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveFollowingIdsResponse:
        """
        Returns the user IDs of the accounts the selected user follows, newest first, up
        to 5,000 a page. Use it when you need IDs only. Each ID costs 1 credit.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          page_size: User IDs to request from this page (1-5000, default 5000). Credits can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/following-ids", id=id),
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
                    user_retrieve_following_ids_params.UserRetrieveFollowingIdsParams,
                ),
            ),
            cast_to=UserRetrieveFollowingIdsResponse,
        )

    async def retrieve_highlights(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns the posts on the user's Highlights tab, in X's order.

        An account without
        highlights returns an empty list.

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
            path_template("/x/users/{id}/highlights", id=id),
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
                    user_retrieve_highlights_params.UserRetrieveHighlightsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_insights(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveInsightsResponse:
        """
        Returns engagement insights for one profile: engagement rate, averages per post
        and posting rate, from its counts and its last 20 posts. Reposts and the pinned
        post stay out of the averages. Each report costs 1 credit, whatever it reads.

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
            path_template("/x/users/{id}/insights", id=id),
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
                    user_retrieve_insights_params.UserRetrieveInsightsParams,
                ),
            ),
            cast_to=UserRetrieveInsightsResponse,
        )

    async def retrieve_likes(
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
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
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Your X account's likes, else 424 `account_required`.

        Others' likes get 424
        `likes_unavailable`.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

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

          near: Match a place name.

          news: Only return news results.

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

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

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
            path_template("/x/users/{id}/likes", id=id),
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
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
                        "since_date": since_date,
                        "since_id": since_id,
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
                        "url": url,
                        "verified_only": verified_only,
                        "within": within,
                        "within_time": within_time,
                    },
                    user_retrieve_likes_params.UserRetrieveLikesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_list_memberships(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveListMembershipsResponse:
        """
        Returns the public X Lists that include the selected user, as the profile's List
        memberships page shows them. Each List costs 1 credit. A protected account
        answers 403.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/list-memberships", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "fields": fields,
                        "omit": omit,
                        "page_size": page_size,
                    },
                    user_retrieve_list_memberships_params.UserRetrieveListMembershipsParams,
                ),
            ),
            cast_to=UserRetrieveListMembershipsResponse,
        )

    async def retrieve_lists(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveListsResponse:
        """
        Returns the public X Lists the selected user created, in X's order, as the
        profile's Lists tab shows them. Each List costs 1 credit. A protected account
        answers 403.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/x/users/{id}/lists", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "fields": fields,
                        "omit": omit,
                        "page_size": page_size,
                    },
                    user_retrieve_lists_params.UserRetrieveListsParams,
                ),
            ),
            cast_to=UserRetrieveListsResponse,
        )

    async def retrieve_live(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveLiveResponse:
        """
        Says whether one user is broadcasting live video on X right now, with their
        latest broadcast, live or ended. Each check costs 1 credit.

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
            path_template("/x/users/{id}/live", id=id),
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
                    user_retrieve_live_params.UserRetrieveLiveParams,
                ),
            ),
            cast_to=UserRetrieveLiveResponse,
        )

    async def retrieve_media(
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
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
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns public media posts from the selected user.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

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

          near: Match a place name.

          news: Only return news results.

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

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format, as a UTC day, inclusive, so its own posts count.

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
            path_template("/x/users/{id}/media", id=id),
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
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
                        "since_date": since_date,
                        "since_id": since_id,
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
                        "url": url,
                        "verified_only": verified_only,
                        "within": within,
                        "within_time": within_time,
                    },
                    user_retrieve_media_params.UserRetrieveMediaParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_mentions(
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
        fields: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns public posts mentioning the selected user.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          exact_phrase: Match this literal phrase, including any hyphens.

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

          near: Match a place name.

          news: Only return news results.

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

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format, as a UTC day.

          since_id: Return Tweets whose IDs exceed this ID.

          since_time: Inclusive ISO bound for Tweet creation time, such as 2026-09-25T19:20:41Z. Unix
              seconds also work. A time without an offset is UTC.

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
            path_template("/x/users/{id}/mentions", id=id),
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
                        "fields": fields,
                        "from_user": from_user,
                        "geocode": geocode,
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
                    user_retrieve_mentions_params.UserRetrieveMentionsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_replies(
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
        include_parent_tweet: bool | Omit = omit,
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns target-authored posts & replies, without other authors' context.

        Omit
        mode for automatic maximum coverage. Pass next_cursor unchanged; unprefixed
        cursors are legacy. It never opens with the pinned tweet.

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

          include_parent_tweet: Include each reply's parent tweet as parentTweet on the reply. A reply whose
              parent X does not return comes without it. Search-only filters such as keywords
              do not apply with it.

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
            path_template("/x/users/{id}/replies", id=id),
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
                        "include_parent_tweet": include_parent_tweet,
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
                    user_retrieve_replies_params.UserRetrieveRepliesParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_search(
        self,
        *,
        q: str,
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Returns public profiles matching a name or username.

        Args:
          q: User search query

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

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          username_contains: Match a username substring, ignoring case.

          verified_only: Only return verified profiles.

          verified_type: Match the verification type exactly, ignoring case.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/users/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
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
                    user_retrieve_search_params.UserRetrieveSearchParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_similar(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Returns the public accounts X lists as similar to the selected user, in X's
        order. X can list slightly different accounts on each call. Each account costs 1
        credit.

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
            path_template("/x/users/{id}/similar", id=id),
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
                    user_retrieve_similar_params.UserRetrieveSimilarParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_subscriptions(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """Returns the creators the selected user subscribes to, in X's order.

        An account
        that hides its subscriptions returns an empty list.

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
            path_template("/x/users/{id}/subscriptions", id=id),
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
                    user_retrieve_subscriptions_params.UserRetrieveSubscriptionsParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_tweets(
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
        include_parent_tweet: bool | Omit = omit,
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """For the newest posts of 2 to 20 users, use getBatchUserTweets.

        For more, use
        createExtraction with tweet_search_extractor & targetUsernames. Omit mode for
        automatic maximum coverage. Pass next_cursor unchanged; unprefixed cursors are
        legacy. The first page opens with the pinned tweet, flagged isPinned, unless
        replies are included. Rows stay newest first. x.com's Posts tab groups
        self-threads & hides reposts; retweets=exclude drops reposts.

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

          include_parent_tweet: Include each reply's parent tweet as parentTweet on the reply. A reply whose
              parent X does not return comes without it. Search-only filters such as keywords
              do not apply with it.

          include_replies: Include reply tweets unless replies specifies another mode.

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
            path_template("/x/users/{id}/tweets", id=id),
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
                        "include_parent_tweet": include_parent_tweet,
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
                    user_retrieve_tweets_params.UserRetrieveTweetsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_verified_followers(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_scan: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveVerifiedFollowersResponse:
        """
        Returns verified public profiles following the selected user.

        Args:
          after: Legacy cursor alias. Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          blue_verified_only: Only return profiles X marks as blue verified. X marks many business &
              government accounts blue too. Use verifiedType for 1 badge type.

          business_email_only: Only return profiles that publish an email outside free webmail, such as Gmail.

          cursor: Cursor from the previous response. Existing unprefixed cursors keep legacy
              standard behavior. Pages can be empty before more rows; follow next_cursor. Also
              read as next_cursor, next_token, pagination_token or continuation_token.

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

          limit: Legacy page-size alias outside coverage mode. Coverage accepts 1-10000. Prefer
              pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Profiles may follow at most this many accounts.

          max_scan: Most profiles 1 request reads, kept or dropped by the filters. A filter that
              keeps few profiles reads up to 65 s a request without it. The request then
              answers the profiles it kept, the count it dropped & the cursor to read on. Each
              request of a cursor may send its own value. Automatic mode only.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Profiles must follow at least this many accounts.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Up to 300 user profiles in automatic mode, 200 in standard. Sources can return
              fewer. Follow next_cursor for more pages. Aliases: limit, count, max_results,
              maxItems, max_items & per_page.

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
        return cast(
            UserRetrieveVerifiedFollowersResponse,
            await self._get(
                path_template("/x/users/{id}/verified-followers", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "after": after,
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
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_scan": max_scan,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "omit": omit,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_verified_followers_params.UserRetrieveVerifiedFollowersParams,
                    ),
                ),
                cast_to=cast(Any, UserRetrieveVerifiedFollowersResponse),
            ),
        )

    async def translate_bio(
        self,
        id: str,
        *,
        language: str,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserTranslateBioResponse:
        """
        Returns X's own translation of one profile's bio into the language you pick,
        with the links, mentions, and tags X places in the translated text. A profile
        without a bio returns translation null & a message, free of charge.

        Args:
          language: Language code to translate into, such as `es`, `tr`, `pt-br`, or `zh-tw`. Upper
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
            path_template("/x/users/{id}/translation", id=id),
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
                    user_translate_bio_params.UserTranslateBioParams,
                ),
            ),
            cast_to=UserTranslateBioResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.remove_follower = to_raw_response_wrapper(
            users.remove_follower,
        )
        self.retrieve_affiliates = to_raw_response_wrapper(
            users.retrieve_affiliates,
        )
        self.retrieve_articles = to_raw_response_wrapper(
            users.retrieve_articles,
        )
        self.retrieve_batch = to_raw_response_wrapper(
            users.retrieve_batch,
        )
        self.retrieve_batch_tweets = to_raw_response_wrapper(
            users.retrieve_batch_tweets,
        )
        self.retrieve_follower_ids = to_raw_response_wrapper(
            users.retrieve_follower_ids,
        )
        self.retrieve_followers = to_raw_response_wrapper(
            users.retrieve_followers,
        )
        self.retrieve_followers_you_know = to_raw_response_wrapper(
            users.retrieve_followers_you_know,
        )
        self.retrieve_following = to_raw_response_wrapper(
            users.retrieve_following,
        )
        self.retrieve_following_ids = to_raw_response_wrapper(
            users.retrieve_following_ids,
        )
        self.retrieve_highlights = to_raw_response_wrapper(
            users.retrieve_highlights,
        )
        self.retrieve_insights = to_raw_response_wrapper(
            users.retrieve_insights,
        )
        self.retrieve_likes = to_raw_response_wrapper(
            users.retrieve_likes,
        )
        self.retrieve_list_memberships = to_raw_response_wrapper(
            users.retrieve_list_memberships,
        )
        self.retrieve_lists = to_raw_response_wrapper(
            users.retrieve_lists,
        )
        self.retrieve_live = to_raw_response_wrapper(
            users.retrieve_live,
        )
        self.retrieve_media = to_raw_response_wrapper(
            users.retrieve_media,
        )
        self.retrieve_mentions = to_raw_response_wrapper(
            users.retrieve_mentions,
        )
        self.retrieve_replies = to_raw_response_wrapper(
            users.retrieve_replies,
        )
        self.retrieve_search = to_raw_response_wrapper(
            users.retrieve_search,
        )
        self.retrieve_similar = to_raw_response_wrapper(
            users.retrieve_similar,
        )
        self.retrieve_subscriptions = to_raw_response_wrapper(
            users.retrieve_subscriptions,
        )
        self.retrieve_tweets = to_raw_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = to_raw_response_wrapper(
            users.retrieve_verified_followers,
        )
        self.translate_bio = to_raw_response_wrapper(
            users.translate_bio,
        )

    @cached_property
    def follow(self) -> FollowResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return FollowResourceWithRawResponse(self._users.follow)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.remove_follower = async_to_raw_response_wrapper(
            users.remove_follower,
        )
        self.retrieve_affiliates = async_to_raw_response_wrapper(
            users.retrieve_affiliates,
        )
        self.retrieve_articles = async_to_raw_response_wrapper(
            users.retrieve_articles,
        )
        self.retrieve_batch = async_to_raw_response_wrapper(
            users.retrieve_batch,
        )
        self.retrieve_batch_tweets = async_to_raw_response_wrapper(
            users.retrieve_batch_tweets,
        )
        self.retrieve_follower_ids = async_to_raw_response_wrapper(
            users.retrieve_follower_ids,
        )
        self.retrieve_followers = async_to_raw_response_wrapper(
            users.retrieve_followers,
        )
        self.retrieve_followers_you_know = async_to_raw_response_wrapper(
            users.retrieve_followers_you_know,
        )
        self.retrieve_following = async_to_raw_response_wrapper(
            users.retrieve_following,
        )
        self.retrieve_following_ids = async_to_raw_response_wrapper(
            users.retrieve_following_ids,
        )
        self.retrieve_highlights = async_to_raw_response_wrapper(
            users.retrieve_highlights,
        )
        self.retrieve_insights = async_to_raw_response_wrapper(
            users.retrieve_insights,
        )
        self.retrieve_likes = async_to_raw_response_wrapper(
            users.retrieve_likes,
        )
        self.retrieve_list_memberships = async_to_raw_response_wrapper(
            users.retrieve_list_memberships,
        )
        self.retrieve_lists = async_to_raw_response_wrapper(
            users.retrieve_lists,
        )
        self.retrieve_live = async_to_raw_response_wrapper(
            users.retrieve_live,
        )
        self.retrieve_media = async_to_raw_response_wrapper(
            users.retrieve_media,
        )
        self.retrieve_mentions = async_to_raw_response_wrapper(
            users.retrieve_mentions,
        )
        self.retrieve_replies = async_to_raw_response_wrapper(
            users.retrieve_replies,
        )
        self.retrieve_search = async_to_raw_response_wrapper(
            users.retrieve_search,
        )
        self.retrieve_similar = async_to_raw_response_wrapper(
            users.retrieve_similar,
        )
        self.retrieve_subscriptions = async_to_raw_response_wrapper(
            users.retrieve_subscriptions,
        )
        self.retrieve_tweets = async_to_raw_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = async_to_raw_response_wrapper(
            users.retrieve_verified_followers,
        )
        self.translate_bio = async_to_raw_response_wrapper(
            users.translate_bio,
        )

    @cached_property
    def follow(self) -> AsyncFollowResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncFollowResourceWithRawResponse(self._users.follow)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.remove_follower = to_streamed_response_wrapper(
            users.remove_follower,
        )
        self.retrieve_affiliates = to_streamed_response_wrapper(
            users.retrieve_affiliates,
        )
        self.retrieve_articles = to_streamed_response_wrapper(
            users.retrieve_articles,
        )
        self.retrieve_batch = to_streamed_response_wrapper(
            users.retrieve_batch,
        )
        self.retrieve_batch_tweets = to_streamed_response_wrapper(
            users.retrieve_batch_tweets,
        )
        self.retrieve_follower_ids = to_streamed_response_wrapper(
            users.retrieve_follower_ids,
        )
        self.retrieve_followers = to_streamed_response_wrapper(
            users.retrieve_followers,
        )
        self.retrieve_followers_you_know = to_streamed_response_wrapper(
            users.retrieve_followers_you_know,
        )
        self.retrieve_following = to_streamed_response_wrapper(
            users.retrieve_following,
        )
        self.retrieve_following_ids = to_streamed_response_wrapper(
            users.retrieve_following_ids,
        )
        self.retrieve_highlights = to_streamed_response_wrapper(
            users.retrieve_highlights,
        )
        self.retrieve_insights = to_streamed_response_wrapper(
            users.retrieve_insights,
        )
        self.retrieve_likes = to_streamed_response_wrapper(
            users.retrieve_likes,
        )
        self.retrieve_list_memberships = to_streamed_response_wrapper(
            users.retrieve_list_memberships,
        )
        self.retrieve_lists = to_streamed_response_wrapper(
            users.retrieve_lists,
        )
        self.retrieve_live = to_streamed_response_wrapper(
            users.retrieve_live,
        )
        self.retrieve_media = to_streamed_response_wrapper(
            users.retrieve_media,
        )
        self.retrieve_mentions = to_streamed_response_wrapper(
            users.retrieve_mentions,
        )
        self.retrieve_replies = to_streamed_response_wrapper(
            users.retrieve_replies,
        )
        self.retrieve_search = to_streamed_response_wrapper(
            users.retrieve_search,
        )
        self.retrieve_similar = to_streamed_response_wrapper(
            users.retrieve_similar,
        )
        self.retrieve_subscriptions = to_streamed_response_wrapper(
            users.retrieve_subscriptions,
        )
        self.retrieve_tweets = to_streamed_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = to_streamed_response_wrapper(
            users.retrieve_verified_followers,
        )
        self.translate_bio = to_streamed_response_wrapper(
            users.translate_bio,
        )

    @cached_property
    def follow(self) -> FollowResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return FollowResourceWithStreamingResponse(self._users.follow)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.remove_follower = async_to_streamed_response_wrapper(
            users.remove_follower,
        )
        self.retrieve_affiliates = async_to_streamed_response_wrapper(
            users.retrieve_affiliates,
        )
        self.retrieve_articles = async_to_streamed_response_wrapper(
            users.retrieve_articles,
        )
        self.retrieve_batch = async_to_streamed_response_wrapper(
            users.retrieve_batch,
        )
        self.retrieve_batch_tweets = async_to_streamed_response_wrapper(
            users.retrieve_batch_tweets,
        )
        self.retrieve_follower_ids = async_to_streamed_response_wrapper(
            users.retrieve_follower_ids,
        )
        self.retrieve_followers = async_to_streamed_response_wrapper(
            users.retrieve_followers,
        )
        self.retrieve_followers_you_know = async_to_streamed_response_wrapper(
            users.retrieve_followers_you_know,
        )
        self.retrieve_following = async_to_streamed_response_wrapper(
            users.retrieve_following,
        )
        self.retrieve_following_ids = async_to_streamed_response_wrapper(
            users.retrieve_following_ids,
        )
        self.retrieve_highlights = async_to_streamed_response_wrapper(
            users.retrieve_highlights,
        )
        self.retrieve_insights = async_to_streamed_response_wrapper(
            users.retrieve_insights,
        )
        self.retrieve_likes = async_to_streamed_response_wrapper(
            users.retrieve_likes,
        )
        self.retrieve_list_memberships = async_to_streamed_response_wrapper(
            users.retrieve_list_memberships,
        )
        self.retrieve_lists = async_to_streamed_response_wrapper(
            users.retrieve_lists,
        )
        self.retrieve_live = async_to_streamed_response_wrapper(
            users.retrieve_live,
        )
        self.retrieve_media = async_to_streamed_response_wrapper(
            users.retrieve_media,
        )
        self.retrieve_mentions = async_to_streamed_response_wrapper(
            users.retrieve_mentions,
        )
        self.retrieve_replies = async_to_streamed_response_wrapper(
            users.retrieve_replies,
        )
        self.retrieve_search = async_to_streamed_response_wrapper(
            users.retrieve_search,
        )
        self.retrieve_similar = async_to_streamed_response_wrapper(
            users.retrieve_similar,
        )
        self.retrieve_subscriptions = async_to_streamed_response_wrapper(
            users.retrieve_subscriptions,
        )
        self.retrieve_tweets = async_to_streamed_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = async_to_streamed_response_wrapper(
            users.retrieve_verified_followers,
        )
        self.translate_bio = async_to_streamed_response_wrapper(
            users.translate_bio,
        )

    @cached_property
    def follow(self) -> AsyncFollowResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncFollowResourceWithStreamingResponse(self._users.follow)
