# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
    user_retrieve_batch_params,
    user_retrieve_likes_params,
    user_retrieve_media_params,
    user_remove_follower_params,
    user_retrieve_search_params,
    user_retrieve_tweets_params,
    user_retrieve_replies_params,
    user_retrieve_mentions_params,
    user_retrieve_followers_params,
    user_retrieve_following_params,
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
from ....types.shared.user_profile import UserProfile
from ....types.shared.paginated_users import PaginatedUsers
from ....types.shared.paginated_tweets import PaginatedTweets
from ....types.x.user_retrieve_batch_response import UserRetrieveBatchResponse
from ....types.x.user_remove_follower_response import UserRemoveFollowerResponse
from ....types.x.user_retrieve_followers_response import UserRetrieveFollowersResponse
from ....types.x.user_retrieve_following_response import UserRetrieveFollowingResponse
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
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfile:
        """
        Get user profile with follower counts and verification

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserProfile,
        )

    def remove_follower(
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
    ) -> UserRemoveFollowerResponse:
        """
        Remove follower

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
        return self._post(
            path_template("/x/users/{id}/remove-follower", id=id),
            body=maybe_transform({"account": account}, user_remove_follower_params.UserRemoveFollowerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRemoveFollowerResponse,
        )

    def retrieve_batch(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveBatchResponse:
        """
        Look up multiple users by IDs in one call

        Args:
          ids: Comma-separated numeric user IDs (1-100 values). Duplicate IDs are ignored while
              preserving first-seen order.

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
                query=maybe_transform({"ids": ids}, user_retrieve_batch_params.UserRetrieveBatchParams),
            ),
            cast_to=UserRetrieveBatchResponse,
        )

    def retrieve_followers(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        bio_contains: str | Omit = omit,
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
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
    ) -> UserRetrieveFollowersResponse:
        """List followers of a user

        Args:
          after: Legacy cursor alias.

        Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          limit: Legacy page-size alias outside explicit coverage mode. Coverage accepts 1-10000.
              Prefer pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Continue with has_next_page.

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
                            "cursor": cursor,
                            "has_location": has_location,
                            "has_website": has_website,
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_followers_params.UserRetrieveFollowersParams,
                    ),
                ),
                cast_to=cast(
                    Any, UserRetrieveFollowersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_followers_you_know(
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
        List mutual followers between you and a user

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Pagination cursor for followers-you-know

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
            path_template("/x/users/{id}/followers-you-know", id=id),
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
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
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
    ) -> UserRetrieveFollowingResponse:
        """List accounts a user follows

        Args:
          after: Deprecated following cursor alias.

        Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          limit: Legacy page-size alias outside explicit coverage mode. Coverage accepts 1-10000.
              Prefer pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Continue with has_next_page.

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
                            "cursor": cursor,
                            "has_location": has_location,
                            "has_website": has_website,
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_following_params.UserRetrieveFollowingParams,
                    ),
                ),
                cast_to=cast(
                    Any, UserRetrieveFollowingResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
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
        List tweets liked by a user

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for liked tweets

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

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

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

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
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
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
        List media tweets posted by a user

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for media tweets

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

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

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

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
        List tweets mentioning a user

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for mentions

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

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

          since_time: Unix timestamp - return mentions after this time

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return mentions before this time

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
                    user_retrieve_mentions_params.UserRetrieveMentionsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def retrieve_replies(
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
        include_parent_tweet: bool | Omit = omit,
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
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
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
        """Returns target-authored posts and replies.

        Omit mode for automatic maximum
        coverage. Pass next_cursor unchanged. Unprefixed cursors stay legacy. Excludes
        other-author context.

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

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_parent_tweet: Include each reply's parent tweet.

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

          page_size: Automatic pages accept 1-300 Tweets. Standard pages keep 1-100. Default 20.
              Continue while has_next_page is true. Deprecated aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

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
            path_template("/x/users/{id}/replies", id=id),
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
                        "include_parent_tweet": include_parent_tweet,
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
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
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
        Search users by name or username

        Args:
          q: User search query

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Pagination cursor for user search

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
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
                    },
                    user_retrieve_search_params.UserRetrieveSearchParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_tweets(
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
        include_parent_tweet: bool | Omit = omit,
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
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
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
        """Omit mode for automatic maximum coverage.

        Pass next_cursor unchanged. Unprefixed
        cursors use legacy pagination. Shape and billing stay the same.

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

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_parent_tweet: Include parent tweet for replies

          include_replies: Include reply tweets

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

          page_size: Automatic pages accept 1-300 Tweets. Standard pages keep 1-100. Default 20.
              Continue while has_next_page is true. Deprecated aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

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
            path_template("/x/users/{id}/tweets", id=id),
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
                        "include_parent_tweet": include_parent_tweet,
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
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
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
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
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
    ) -> UserRetrieveVerifiedFollowersResponse:
        """List verified followers of a user

        Args:
          after: Legacy cursor alias.

        Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          limit: Legacy page-size alias outside explicit coverage mode. Coverage accepts 1-10000.
              Prefer pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Continue with has_next_page.

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
                            "cursor": cursor,
                            "has_location": has_location,
                            "has_website": has_website,
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_verified_followers_params.UserRetrieveVerifiedFollowersParams,
                    ),
                ),
                cast_to=cast(
                    Any, UserRetrieveVerifiedFollowersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def follow(self) -> AsyncFollowResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncFollowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfile:
        """
        Get user profile with follower counts and verification

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserProfile,
        )

    async def remove_follower(
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
    ) -> UserRemoveFollowerResponse:
        """
        Remove follower

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

    async def retrieve_batch(
        self,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveBatchResponse:
        """
        Look up multiple users by IDs in one call

        Args:
          ids: Comma-separated numeric user IDs (1-100 values). Duplicate IDs are ignored while
              preserving first-seen order.

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
                query=await async_maybe_transform({"ids": ids}, user_retrieve_batch_params.UserRetrieveBatchParams),
            ),
            cast_to=UserRetrieveBatchResponse,
        )

    async def retrieve_followers(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        bio_contains: str | Omit = omit,
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
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
    ) -> UserRetrieveFollowersResponse:
        """List followers of a user

        Args:
          after: Legacy cursor alias.

        Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          limit: Legacy page-size alias outside explicit coverage mode. Coverage accepts 1-10000.
              Prefer pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Continue with has_next_page.

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
                            "cursor": cursor,
                            "has_location": has_location,
                            "has_website": has_website,
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_followers_params.UserRetrieveFollowersParams,
                    ),
                ),
                cast_to=cast(
                    Any, UserRetrieveFollowersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_followers_you_know(
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
        List mutual followers between you and a user

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Pagination cursor for followers-you-know

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
            path_template("/x/users/{id}/followers-you-know", id=id),
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
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
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
    ) -> UserRetrieveFollowingResponse:
        """List accounts a user follows

        Args:
          after: Deprecated following cursor alias.

        Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          limit: Legacy page-size alias outside explicit coverage mode. Coverage accepts 1-10000.
              Prefer pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Continue with has_next_page.

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
                            "cursor": cursor,
                            "has_location": has_location,
                            "has_website": has_website,
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_following_params.UserRetrieveFollowingParams,
                    ),
                ),
                cast_to=cast(
                    Any, UserRetrieveFollowingResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
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
        List tweets liked by a user

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for liked tweets

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

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

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

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
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
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
        List media tweets posted by a user

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for media tweets

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

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

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

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
        List tweets mentioning a user

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter.

          cursor: Pagination cursor for mentions

          exact_phrase: Exact phrase to match.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

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

          since_time: Unix timestamp - return mentions after this time

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Unix timestamp - return mentions before this time

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
                    user_retrieve_mentions_params.UserRetrieveMentionsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def retrieve_replies(
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
        include_parent_tweet: bool | Omit = omit,
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
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
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
        """Returns target-authored posts and replies.

        Omit mode for automatic maximum
        coverage. Pass next_cursor unchanged. Unprefixed cursors stay legacy. Excludes
        other-author context.

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

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_parent_tweet: Include each reply's parent tweet.

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

          page_size: Automatic pages accept 1-300 Tweets. Standard pages keep 1-100. Default 20.
              Continue while has_next_page is true. Deprecated aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

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
            path_template("/x/users/{id}/replies", id=id),
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
                        "include_parent_tweet": include_parent_tweet,
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
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
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
        Search users by name or username

        Args:
          q: User search query

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Pagination cursor for user search

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
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
                    },
                    user_retrieve_search_params.UserRetrieveSearchParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_tweets(
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
        include_parent_tweet: bool | Omit = omit,
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
        source: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
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
        """Omit mode for automatic maximum coverage.

        Pass next_cursor unchanged. Unprefixed
        cursors use legacy pagination. Shape and billing stay the same.

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

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_parent_tweet: Include parent tweet for replies

          include_replies: Include reply tweets

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

          page_size: Automatic pages accept 1-300 Tweets. Standard pages keep 1-100. Default 20.
              Continue while has_next_page is true. Deprecated aliases remain accepted.

          quotes: Quote mode.

          quotes_of_tweet_id: Only quotes of this tweet ID.

          replies: Reply mode.

          retweets: Retweet mode.

          retweets_of_tweet_id: Only retweets of this tweet ID.

          safe: Enable the safe-search filter.

          since_date: Start date in YYYY-MM-DD format.

          since_id: Return Tweets newer than this Tweet ID.

          source: Match the source application.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

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
            path_template("/x/users/{id}/tweets", id=id),
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
                        "include_parent_tweet": include_parent_tweet,
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
                        "source": source,
                        "to_user": to_user,
                        "until_date": until_date,
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
        cursor: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
        limit: int | Omit = omit,
        location_contains: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_statuses: int | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_statuses: int | Omit = omit,
        mode: Literal["standard", "coverage"] | Omit = omit,
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
    ) -> UserRetrieveVerifiedFollowersResponse:
        """List verified followers of a user

        Args:
          after: Legacy cursor alias.

        Prefer cursor.

          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          has_location: Only return profiles with a location.

          has_website: Only return profiles with a website.

          limit: Legacy page-size alias outside explicit coverage mode. Coverage accepts 1-10000.
              Prefer pageSize.

          location_contains: Match a location substring, ignoring case.

          max_followers: Maximum follower count. Missing counts pass this maximum.

          max_following: Maximum following count.

          max_statuses: Maximum post count. maxPosts is also accepted.

          min_account_age_days: Minimum account age in whole days.

          min_followers: Minimum follower count. Filtering happens before billing.

          min_following: Minimum following count.

          min_statuses: Minimum post count. minPosts is also accepted.

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Continue with has_next_page.

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
                            "cursor": cursor,
                            "has_location": has_location,
                            "has_website": has_website,
                            "limit": limit,
                            "location_contains": location_contains,
                            "max_followers": max_followers,
                            "max_following": max_following,
                            "max_statuses": max_statuses,
                            "min_account_age_days": min_account_age_days,
                            "min_followers": min_followers,
                            "min_following": min_following,
                            "min_statuses": min_statuses,
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        user_retrieve_verified_followers_params.UserRetrieveVerifiedFollowersParams,
                    ),
                ),
                cast_to=cast(
                    Any, UserRetrieveVerifiedFollowersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
        self.retrieve_batch = to_raw_response_wrapper(
            users.retrieve_batch,
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
        self.retrieve_likes = to_raw_response_wrapper(
            users.retrieve_likes,
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
        self.retrieve_tweets = to_raw_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = to_raw_response_wrapper(
            users.retrieve_verified_followers,
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
        self.retrieve_batch = async_to_raw_response_wrapper(
            users.retrieve_batch,
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
        self.retrieve_likes = async_to_raw_response_wrapper(
            users.retrieve_likes,
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
        self.retrieve_tweets = async_to_raw_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = async_to_raw_response_wrapper(
            users.retrieve_verified_followers,
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
        self.retrieve_batch = to_streamed_response_wrapper(
            users.retrieve_batch,
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
        self.retrieve_likes = to_streamed_response_wrapper(
            users.retrieve_likes,
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
        self.retrieve_tweets = to_streamed_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = to_streamed_response_wrapper(
            users.retrieve_verified_followers,
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
        self.retrieve_batch = async_to_streamed_response_wrapper(
            users.retrieve_batch,
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
        self.retrieve_likes = async_to_streamed_response_wrapper(
            users.retrieve_likes,
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
        self.retrieve_tweets = async_to_streamed_response_wrapper(
            users.retrieve_tweets,
        )
        self.retrieve_verified_followers = async_to_streamed_response_wrapper(
            users.retrieve_verified_followers,
        )

    @cached_property
    def follow(self) -> AsyncFollowResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncFollowResourceWithStreamingResponse(self._users.follow)
