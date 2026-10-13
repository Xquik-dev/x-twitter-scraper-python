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
from ...types.x import (
    list_retrieve_params,
    list_retrieve_search_params,
    list_retrieve_tweets_params,
    list_retrieve_members_params,
    list_retrieve_followers_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.paginated_tweets import PaginatedTweets
from ...types.x.list_retrieve_response import ListRetrieveResponse
from ...types.x.list_retrieve_search_response import ListRetrieveSearchResponse
from ...types.x.list_retrieve_members_response import ListRetrieveMembersResponse
from ...types.x.list_retrieve_followers_response import ListRetrieveFollowersResponse

__all__ = ["ListsResource", "AsyncListsResource"]


class ListsResource(SyncAPIResource):
    """X List search, details, followers, members, and tweets"""

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
    ) -> ListRetrieveResponse:
        """Returns one public X List as its page on X shows it.

        Accepts the List ID or the
        URL-encoded List URL, such as x.com/i/lists/4143408. A private List answers 404
        list_not_found.

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
            path_template("/x/lists/{id}", id=id),
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
                    list_retrieve_params.ListRetrieveParams,
                ),
            ),
            cast_to=ListRetrieveResponse,
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
        fields: str | Omit = omit,
        has_email: bool | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveFollowersResponse:
        """Returns a public List's followers with resumable or standard pagination.

        A
        private List answers 404 list_not_found.

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
                            "after": after,
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
        after: str | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveMembersResponse:
        """Returns a public List's members with resumable or standard pagination.

        A private
        List answers 404 list_not_found.

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
                            "after": after,
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
                        list_retrieve_members_params.ListRetrieveMembersParams,
                    ),
                ),
                cast_to=cast(
                    Any, ListRetrieveMembersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveSearchResponse:
        """Returns one page of public Lists with member counts, banners & owner profiles.

        X
        may rank the Lists differently per request. Pass next_cursor as cursor for the
        next page.

        Args:
          q: Keywords to find Lists by, such as a topic. Alias query.

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
        return self._get(
            "/x/lists/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "fields": fields,
                        "omit": omit,
                        "page_size": page_size,
                    },
                    list_retrieve_search_params.ListRetrieveSearchParams,
                ),
            ),
            cast_to=ListRetrieveSearchResponse,
        )

    def retrieve_tweets(
        self,
        id: str,
        *,
        advanced_query: str | Omit = omit,
        after: str | Omit = omit,
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
        mode: Literal["standard", "coverage"] | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Omit mode for resumable maximum coverage.

        Pass next_cursor unchanged. Standard
        keeps legacy pagination. A private List answers 404 list_not_found.

        Args:
          advanced_query: Raw advanced search query appended as-is.

          after: Legacy cursor alias. Prefer cursor.

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

          include_replies: Include reply tweets unless replies specifies another mode.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          keywords: Words the Tweets must match, in X search syntax.

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

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

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
            path_template("/x/lists/{id}/tweets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "advanced_query": advanced_query,
                        "after": after,
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
                    list_retrieve_tweets_params.ListRetrieveTweetsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )


class AsyncListsResource(AsyncAPIResource):
    """X List search, details, followers, members, and tweets"""

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
    ) -> ListRetrieveResponse:
        """Returns one public X List as its page on X shows it.

        Accepts the List ID or the
        URL-encoded List URL, such as x.com/i/lists/4143408. A private List answers 404
        list_not_found.

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
            path_template("/x/lists/{id}", id=id),
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
                    list_retrieve_params.ListRetrieveParams,
                ),
            ),
            cast_to=ListRetrieveResponse,
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
        fields: str | Omit = omit,
        has_email: bool | Omit = omit,
        has_location: bool | Omit = omit,
        has_website: bool | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveFollowersResponse:
        """Returns a public List's followers with resumable or standard pagination.

        A
        private List answers 404 list_not_found.

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
                            "after": after,
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
        after: str | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveMembersResponse:
        """Returns a public List's members with resumable or standard pagination.

        A private
        List answers 404 list_not_found.

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
                            "after": after,
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
                        list_retrieve_members_params.ListRetrieveMembersParams,
                    ),
                ),
                cast_to=cast(
                    Any, ListRetrieveMembersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ListRetrieveSearchResponse:
        """Returns one page of public Lists with member counts, banners & owner profiles.

        X
        may rank the Lists differently per request. Pass next_cursor as cursor for the
        next page.

        Args:
          q: Keywords to find Lists by, such as a topic. Alias query.

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
        return await self._get(
            "/x/lists/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "cursor": cursor,
                        "fields": fields,
                        "omit": omit,
                        "page_size": page_size,
                    },
                    list_retrieve_search_params.ListRetrieveSearchParams,
                ),
            ),
            cast_to=ListRetrieveSearchResponse,
        )

    async def retrieve_tweets(
        self,
        id: str,
        *,
        advanced_query: str | Omit = omit,
        after: str | Omit = omit,
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
        mode: Literal["standard", "coverage"] | Omit = omit,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Omit mode for resumable maximum coverage.

        Pass next_cursor unchanged. Standard
        keeps legacy pagination. A private List answers 404 list_not_found.

        Args:
          advanced_query: Raw advanced search query appended as-is.

          after: Legacy cursor alias. Prefer cursor.

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

          include_replies: Include reply tweets unless replies specifies another mode.

          in_reply_to_tweet_id: Only replies to this tweet ID.

          keywords: Words the Tweets must match, in X search syntax.

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

          mode: Omit mode for resumable maximum coverage. Standard keeps legacy pagination.
              Coverage returns diagnostics once and rejects cursors.

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
            path_template("/x/lists/{id}/tweets", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "advanced_query": advanced_query,
                        "after": after,
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
                    list_retrieve_tweets_params.ListRetrieveTweetsParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )


class ListsResourceWithRawResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.retrieve = to_raw_response_wrapper(
            lists.retrieve,
        )
        self.retrieve_followers = to_raw_response_wrapper(
            lists.retrieve_followers,
        )
        self.retrieve_members = to_raw_response_wrapper(
            lists.retrieve_members,
        )
        self.retrieve_search = to_raw_response_wrapper(
            lists.retrieve_search,
        )
        self.retrieve_tweets = to_raw_response_wrapper(
            lists.retrieve_tweets,
        )


class AsyncListsResourceWithRawResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.retrieve = async_to_raw_response_wrapper(
            lists.retrieve,
        )
        self.retrieve_followers = async_to_raw_response_wrapper(
            lists.retrieve_followers,
        )
        self.retrieve_members = async_to_raw_response_wrapper(
            lists.retrieve_members,
        )
        self.retrieve_search = async_to_raw_response_wrapper(
            lists.retrieve_search,
        )
        self.retrieve_tweets = async_to_raw_response_wrapper(
            lists.retrieve_tweets,
        )


class ListsResourceWithStreamingResponse:
    def __init__(self, lists: ListsResource) -> None:
        self._lists = lists

        self.retrieve = to_streamed_response_wrapper(
            lists.retrieve,
        )
        self.retrieve_followers = to_streamed_response_wrapper(
            lists.retrieve_followers,
        )
        self.retrieve_members = to_streamed_response_wrapper(
            lists.retrieve_members,
        )
        self.retrieve_search = to_streamed_response_wrapper(
            lists.retrieve_search,
        )
        self.retrieve_tweets = to_streamed_response_wrapper(
            lists.retrieve_tweets,
        )


class AsyncListsResourceWithStreamingResponse:
    def __init__(self, lists: AsyncListsResource) -> None:
        self._lists = lists

        self.retrieve = async_to_streamed_response_wrapper(
            lists.retrieve,
        )
        self.retrieve_followers = async_to_streamed_response_wrapper(
            lists.retrieve_followers,
        )
        self.retrieve_members = async_to_streamed_response_wrapper(
            lists.retrieve_members,
        )
        self.retrieve_search = async_to_streamed_response_wrapper(
            lists.retrieve_search,
        )
        self.retrieve_tweets = async_to_streamed_response_wrapper(
            lists.retrieve_tweets,
        )
