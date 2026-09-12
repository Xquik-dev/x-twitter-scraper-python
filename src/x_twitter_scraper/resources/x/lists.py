# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import date
from typing_extensions import Literal

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
from ...types.shared.paginated_tweets import PaginatedTweets
from ...types.x.list_retrieve_members_response import ListRetrieveMembersResponse
from ...types.x.list_retrieve_followers_response import ListRetrieveFollowersResponse

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
    ) -> ListRetrieveFollowersResponse:
        """
        Returns List followers with resumable or standard pagination.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

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

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Follow next_cursor while the response reports more pages.

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
            ListRetrieveFollowersResponse,
            self._get(
                path_template("/x/lists/{id}/followers", id=id),
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
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        list_retrieve_followers_params.ListRetrieveFollowersParams,
                    ),
                ),
                cast_to=cast(
                    Any, ListRetrieveFollowersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_members(
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
    ) -> ListRetrieveMembersResponse:
        """
        Returns List members with resumable or standard pagination.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

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

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Follow next_cursor while the response reports more pages.

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
            ListRetrieveMembersResponse,
            self._get(
                path_template("/x/lists/{id}/members", id=id),
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
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        list_retrieve_members_params.ListRetrieveMembersParams,
                    ),
                ),
                cast_to=cast(
                    Any, ListRetrieveMembersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_tweets(
        self,
        id: str,
        *,
        any_words: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        cashtags: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        include_replies: bool | Omit = omit,
        language: str | Omit = omit,
        max_faves: int | Omit = omit,
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
        mode: Literal["standard", "coverage"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        page_size: int | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_time: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Omit mode for resumable maximum coverage.

        Pass next_cursor unchanged. Standard
        keeps legacy pagination.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          cashtags: Cashtags separated by spaces, commas, or lines.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_replies: Include reply tweets unless replies specifies another mode.

          language: Filter by language. Alias `lang` is accepted.

          max_faves: Maximum likes threshold. maxLikes is also accepted.

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

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          native_retweets: Only return native reposts.

          page_size: Automatic pages accept 1-300 Tweets. Standard pages keep 1-100. Default 20.
              Follow next_cursor while the response reports more pages. Deprecated aliases
              remain accepted.

          replies: Only when the caller requests a reply mode.

          retweets: Only when the caller requests a repost mode.

          since_date: Start date in YYYY-MM-DD format.

          since_time: Inclusive ISO bound for Tweet creation time.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Exclusive ISO bound for Tweet creation time.

          verified_only: Only return tweets from verified authors.

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
                        "any_words": any_words,
                        "blue_verified_only": blue_verified_only,
                        "cashtags": cashtags,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "include_replies": include_replies,
                        "language": language,
                        "max_faves": max_faves,
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
                        "mode": mode,
                        "native_retweets": native_retweets,
                        "page_size": page_size,
                        "replies": replies,
                        "retweets": retweets,
                        "since_date": since_date,
                        "since_time": since_time,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "verified_only": verified_only,
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
    ) -> ListRetrieveFollowersResponse:
        """
        Returns List followers with resumable or standard pagination.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

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

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Follow next_cursor while the response reports more pages.

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
            ListRetrieveFollowersResponse,
            await self._get(
                path_template("/x/lists/{id}/followers", id=id),
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
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        list_retrieve_followers_params.ListRetrieveFollowersParams,
                    ),
                ),
                cast_to=cast(
                    Any, ListRetrieveFollowersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_members(
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
    ) -> ListRetrieveMembersResponse:
        """
        Returns List members with resumable or standard pagination.

        Args:
          bio_contains: Match any comma-separated or line-separated bio term, ignoring case.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

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

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          page_size: Maximum user profiles: automatic 300; standard 200. Sources return fewer
              profiles. Follow next_cursor while the response reports more pages.

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
            ListRetrieveMembersResponse,
            await self._get(
                path_template("/x/lists/{id}/members", id=id),
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
                            "mode": mode,
                            "page_size": page_size,
                            "username_contains": username_contains,
                            "verified_only": verified_only,
                            "verified_type": verified_type,
                        },
                        list_retrieve_members_params.ListRetrieveMembersParams,
                    ),
                ),
                cast_to=cast(
                    Any, ListRetrieveMembersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_tweets(
        self,
        id: str,
        *,
        any_words: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        cashtags: str | Omit = omit,
        cursor: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        include_replies: bool | Omit = omit,
        language: str | Omit = omit,
        max_faves: int | Omit = omit,
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
        mode: Literal["standard", "coverage"] | Omit = omit,
        native_retweets: bool | Omit = omit,
        page_size: int | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_time: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: str | Omit = omit,
        verified_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Omit mode for resumable maximum coverage.

        Pass next_cursor unchanged. Standard
        keeps legacy pagination.

        Args:
          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines.

          blue_verified_only: Only return tweets from Blue-verified authors.

          cashtags: Cashtags separated by spaces, commas, or lines.

          cursor: Cursor from the previous response. Xquik cursors resume automatic coverage.
              Existing unprefixed cursors keep legacy standard behavior.

          exact_phrase: Match this literal phrase, including any hyphens.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.

          from_user: Filter by author username.

          hashtags: Hashtags separated by spaces, commas, or lines.

          include_replies: Include reply tweets unless replies specifies another mode.

          language: Filter by language. Alias `lang` is accepted.

          max_faves: Maximum likes threshold. maxLikes is also accepted.

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

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

          native_retweets: Only return native reposts.

          page_size: Automatic pages accept 1-300 Tweets. Standard pages keep 1-100. Default 20.
              Follow next_cursor while the response reports more pages. Deprecated aliases
              remain accepted.

          replies: Only when the caller requests a reply mode.

          retweets: Only when the caller requests a repost mode.

          since_date: Start date in YYYY-MM-DD format.

          since_time: Inclusive ISO bound for Tweet creation time.

          to_user: Filter replies sent to a username.

          until_date: End date in YYYY-MM-DD format.

          until_time: Exclusive ISO bound for Tweet creation time.

          verified_only: Only return tweets from verified authors.

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
                        "any_words": any_words,
                        "blue_verified_only": blue_verified_only,
                        "cashtags": cashtags,
                        "cursor": cursor,
                        "exact_phrase": exact_phrase,
                        "exclude_words": exclude_words,
                        "from_user": from_user,
                        "hashtags": hashtags,
                        "include_replies": include_replies,
                        "language": language,
                        "max_faves": max_faves,
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
                        "mode": mode,
                        "native_retweets": native_retweets,
                        "page_size": page_size,
                        "replies": replies,
                        "retweets": retweets,
                        "since_date": since_date,
                        "since_time": since_time,
                        "to_user": to_user,
                        "until_date": until_date,
                        "until_time": until_time,
                        "verified_only": verified_only,
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
