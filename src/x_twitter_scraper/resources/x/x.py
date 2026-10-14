# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .dm import (
    DmResource,
    AsyncDmResource,
    DmResourceWithRawResponse,
    AsyncDmResourceWithRawResponse,
    DmResourceWithStreamingResponse,
    AsyncDmResourceWithStreamingResponse,
)
from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from .media import (
    MediaResource,
    AsyncMediaResource,
    MediaResourceWithRawResponse,
    AsyncMediaResourceWithRawResponse,
    MediaResourceWithStreamingResponse,
    AsyncMediaResourceWithStreamingResponse,
)
from .spaces import (
    SpacesResource,
    AsyncSpacesResource,
    SpacesResourceWithRawResponse,
    AsyncSpacesResourceWithRawResponse,
    SpacesResourceWithStreamingResponse,
    AsyncSpacesResourceWithStreamingResponse,
)
from ...types import (
    x_get_trends_params,
    x_get_article_params,
    x_get_hashflags_params,
    x_search_places_params,
    x_get_home_timeline_params,
    x_get_notifications_params,
    x_autocomplete_search_params,
    x_get_trend_locations_params,
)
from .profile import (
    ProfileResource,
    AsyncProfileResource,
    ProfileResourceWithRawResponse,
    AsyncProfileResourceWithRawResponse,
    ProfileResourceWithStreamingResponse,
    AsyncProfileResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .analysis import (
    AnalysisResource,
    AsyncAnalysisResource,
    AnalysisResourceWithRawResponse,
    AsyncAnalysisResourceWithRawResponse,
    AnalysisResourceWithStreamingResponse,
    AsyncAnalysisResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .bookmarks import (
    BookmarksResource,
    AsyncBookmarksResource,
    BookmarksResourceWithRawResponse,
    AsyncBookmarksResourceWithRawResponse,
    BookmarksResourceWithStreamingResponse,
    AsyncBookmarksResourceWithStreamingResponse,
)
from .followers import (
    FollowersResource,
    AsyncFollowersResource,
    FollowersResourceWithRawResponse,
    AsyncFollowersResourceWithRawResponse,
    FollowersResourceWithStreamingResponse,
    AsyncFollowersResourceWithStreamingResponse,
)
from .broadcasts import (
    BroadcastsResource,
    AsyncBroadcastsResource,
    BroadcastsResourceWithRawResponse,
    AsyncBroadcastsResourceWithRawResponse,
    BroadcastsResourceWithStreamingResponse,
    AsyncBroadcastsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .users.users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from .tweets.tweets import (
    TweetsResource,
    AsyncTweetsResource,
    TweetsResourceWithRawResponse,
    AsyncTweetsResourceWithRawResponse,
    TweetsResourceWithStreamingResponse,
    AsyncTweetsResourceWithStreamingResponse,
)
from .write_actions import (
    WriteActionsResource,
    AsyncWriteActionsResource,
    WriteActionsResourceWithRawResponse,
    AsyncWriteActionsResourceWithRawResponse,
    WriteActionsResourceWithStreamingResponse,
    AsyncWriteActionsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .communities.communities import (
    CommunitiesResource,
    AsyncCommunitiesResource,
    CommunitiesResourceWithRawResponse,
    AsyncCommunitiesResourceWithRawResponse,
    CommunitiesResourceWithStreamingResponse,
    AsyncCommunitiesResourceWithStreamingResponse,
)
from .account_connection_attempts import (
    AccountConnectionAttemptsResource,
    AsyncAccountConnectionAttemptsResource,
    AccountConnectionAttemptsResourceWithRawResponse,
    AsyncAccountConnectionAttemptsResourceWithRawResponse,
    AccountConnectionAttemptsResourceWithStreamingResponse,
    AsyncAccountConnectionAttemptsResourceWithStreamingResponse,
)
from ...types.x_get_trends_response import XGetTrendsResponse
from .account_connection_challenges import (
    AccountConnectionChallengesResource,
    AsyncAccountConnectionChallengesResource,
    AccountConnectionChallengesResourceWithRawResponse,
    AsyncAccountConnectionChallengesResourceWithRawResponse,
    AccountConnectionChallengesResourceWithStreamingResponse,
    AsyncAccountConnectionChallengesResourceWithStreamingResponse,
)
from ...types.x_get_article_response import XGetArticleResponse
from ...types.shared.paginated_tweets import PaginatedTweets
from ...types.x_get_hashflags_response import XGetHashflagsResponse
from ...types.x_search_places_response import XSearchPlacesResponse
from ...types.x_get_notifications_response import XGetNotificationsResponse
from ...types.x_autocomplete_search_response import XAutocompleteSearchResponse
from ...types.x_get_trend_locations_response import XGetTrendLocationsResponse

__all__ = ["XResource", "AsyncXResource"]


class XResource(SyncAPIResource):
    @cached_property
    def write_actions(self) -> WriteActionsResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return WriteActionsResource(self._client)

    @cached_property
    def analysis(self) -> AnalysisResource:
        """AI analysis of posts, at 2 credits per analyzed post"""
        return AnalysisResource(self._client)

    @cached_property
    def tweets(self) -> TweetsResource:
        return TweetsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def followers(self) -> FollowersResource:
        """Look up, search, and explore user profiles and relationships"""
        return FollowersResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        """Public X job listings, search and details"""
        return JobsResource(self._client)

    @cached_property
    def dm(self) -> DmResource:
        return DmResource(self._client)

    @cached_property
    def media(self) -> MediaResource:
        return MediaResource(self._client)

    @cached_property
    def profile(self) -> ProfileResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return ProfileResource(self._client)

    @cached_property
    def communities(self) -> CommunitiesResource:
        return CommunitiesResource(self._client)

    @cached_property
    def accounts(self) -> AccountsResource:
        """Connected X account management"""
        return AccountsResource(self._client)

    @cached_property
    def account_connection_challenges(self) -> AccountConnectionChallengesResource:
        """Connected X account management"""
        return AccountConnectionChallengesResource(self._client)

    @cached_property
    def account_connection_attempts(self) -> AccountConnectionAttemptsResource:
        """Connected X account management"""
        return AccountConnectionAttemptsResource(self._client)

    @cached_property
    def bookmarks(self) -> BookmarksResource:
        """Look up, search, and analyze individual tweets"""
        return BookmarksResource(self._client)

    @cached_property
    def lists(self) -> ListsResource:
        """X List search, details, followers, members, and tweets"""
        return ListsResource(self._client)

    @cached_property
    def broadcasts(self) -> BroadcastsResource:
        """X live video details, watch counts, and broadcaster"""
        return BroadcastsResource(self._client)

    @cached_property
    def spaces(self) -> SpacesResource:
        """X Space details, host, and speakers"""
        return SpacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> XResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return XResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> XResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return XResourceWithStreamingResponse(self)

    def autocomplete_search(
        self,
        *,
        q: str,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        types: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XAutocompleteSearchResponse:
        """
        Returns the accounts, topics, hashtags & cashtags X suggests while someone types
        a search. X may rank them differently per request. Costs 1 credit per
        suggestion.

        Args:
          q: Text typed so far. Start with # for hashtags or $ for cashtags. A # query
              returns hashtags & the accounts X suggests for it. Alias: query.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Most suggestions to return: 1 to 100, default 20. Accounts fill it first, then
              topics, hashtags & cashtags. Credits can return fewer. Aliases: pageSize, count,
              max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          types: Comma-separated suggestion types: users, topics, hashtags or cashtags. Omit for
              all. With only hashtags or only cashtags, the query gets its # or $ when it
              lacks one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/search/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                        "types": types,
                    },
                    x_autocomplete_search_params.XAutocompleteSearchParams,
                ),
            ),
            cast_to=XAutocompleteSearchResponse,
        )

    def get_article(
        self,
        tweet_id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetArticleResponse:
        """
        Retrieve the full content of an X Article (long-form post) by numeric tweet ID.
        Returns article_not_found when the tweet is valid but is not an X Article.

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
        if not tweet_id:
            raise ValueError(f"Expected a non-empty value for `tweet_id` but received {tweet_id!r}")
        return self._get(
            path_template("/x/articles/{tweet_id}", tweet_id=tweet_id),
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
                    x_get_article_params.XGetArticleParams,
                ),
            ),
            cast_to=XGetArticleResponse,
        )

    def get_hashflags(
        self,
        *,
        active_only: bool | Omit = omit,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        q: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetHashflagsResponse:
        """Returns X's hashflags, the custom emoji X shows after some hashtags.

        Lists the
        ones running now unless activeOnly is false. Each returned hashflag costs 1
        credit.

        Args:
          active_only: Keeps hashflags that run now. Send false to add ended & upcoming ones.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum hashflags to return. Omit it for every match. Credits can return fewer.
              Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          q: Text the hashtag contains, such as football. Case insensitive. A leading hash
              sign is ignored. Alias query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/hashflags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active_only": active_only,
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                        "q": q,
                    },
                    x_get_hashflags_params.XGetHashflagsParams,
                ),
            ),
            cast_to=XGetHashflagsResponse,
        )

    def get_home_timeline(
        self,
        *,
        cursor: str | Omit = omit,
        seen_tweet_ids: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns the home timeline of 1 of your connected X accounts, else 424
        `account_required`. A cursor reads the next page from the same account. Results
        exclude X ads.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          seen_tweet_ids: Comma-separated tweet IDs to exclude from results. Empty entries are ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/timeline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "seen_tweet_ids": seen_tweet_ids,
                    },
                    x_get_home_timeline_params.XGetHomeTimelineParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def get_notifications(
        self,
        *,
        cursor: str | Omit = omit,
        type: Literal["All", "Verified", "Mentions"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetNotificationsResponse:
        """
        Returns your X account's notifications, else 424 `account_required`.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          type: Notification type filter. Unrecognized values fall back to All.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "type": type,
                    },
                    x_get_notifications_params.XGetNotificationsParams,
                ),
            ),
            cast_to=XGetNotificationsResponse,
        )

    def get_trend_locations(
        self,
        *,
        country: str | Omit = omit,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        place_type: Literal["country", "town", "worldwide", "unknown"] | Omit = omit,
        q: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetTrendLocationsResponse:
        """Returns the places X offers trends for.

        Pass a location's woeid to /x/trends.
        Each returned location costs 1 credit.

        Args:
          country: Country name or 2-letter code, such as Turkey or TR. Case insensitive. Returns
              the country & its towns.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum locations to return. Omit it for every match. Credits can return fewer.
              Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          place_type: Kind of place. Case insensitive. X labels a few towns unknown.

          q: Text the location name contains, such as york. Case insensitive. Alias query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/trends/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                        "place_type": place_type,
                        "q": q,
                    },
                    x_get_trend_locations_params.XGetTrendLocationsParams,
                ),
            ),
            cast_to=XGetTrendLocationsResponse,
        )

    def get_trends(
        self,
        *,
        count: int | Omit = omit,
        country: str | Omit = omit,
        fields: str | Omit = omit,
        location: str | Omit = omit,
        omit: str | Omit = omit,
        woeid: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetTrendsResponse:
        """Returns X's current trends for a place you choose.

        Pick it by woeid, country or
        location name. Without one, trends are worldwide. Each request costs 1 credit,
        however many trends it returns.

        Args:
          count: Number of trending topics to return (1-50, default 30)

          country: Country to read trends for, by name or 2-letter code, such as Turkey or TR. Case
              insensitive.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          location: Town or country to read trends for, by name, such as Istanbul. Case insensitive.
              Add country when 2 towns share a name. /x/trends/locations lists every name.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          woeid: Region WOEID (1=Worldwide, 23424977=US, 23424975=UK, 23424969=Turkey). Wins over
              country & location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/trends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "count": count,
                        "country": country,
                        "fields": fields,
                        "location": location,
                        "omit": omit,
                        "woeid": woeid,
                    },
                    x_get_trends_params.XGetTrendsParams,
                ),
            ),
            cast_to=XGetTrendsResponse,
        )

    def search_places(
        self,
        *,
        q: str,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XSearchPlacesResponse:
        """Finds places on X by name.

        Pass a place's id as place to /x/tweets/search to
        read posts tagged there. X ranks the places, so their order can differ between
        requests. Each returned place costs 1 credit.

        Args:
          q: Place name to search for, such as istanbul. Alias query.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum places to return. Omit it for every place X finds. Credits can return
              fewer. Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/places/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                    },
                    x_search_places_params.XSearchPlacesParams,
                ),
            ),
            cast_to=XSearchPlacesResponse,
        )


class AsyncXResource(AsyncAPIResource):
    @cached_property
    def write_actions(self) -> AsyncWriteActionsResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncWriteActionsResource(self._client)

    @cached_property
    def analysis(self) -> AsyncAnalysisResource:
        """AI analysis of posts, at 2 credits per analyzed post"""
        return AsyncAnalysisResource(self._client)

    @cached_property
    def tweets(self) -> AsyncTweetsResource:
        return AsyncTweetsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def followers(self) -> AsyncFollowersResource:
        """Look up, search, and explore user profiles and relationships"""
        return AsyncFollowersResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        """Public X job listings, search and details"""
        return AsyncJobsResource(self._client)

    @cached_property
    def dm(self) -> AsyncDmResource:
        return AsyncDmResource(self._client)

    @cached_property
    def media(self) -> AsyncMediaResource:
        return AsyncMediaResource(self._client)

    @cached_property
    def profile(self) -> AsyncProfileResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncProfileResource(self._client)

    @cached_property
    def communities(self) -> AsyncCommunitiesResource:
        return AsyncCommunitiesResource(self._client)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Connected X account management"""
        return AsyncAccountsResource(self._client)

    @cached_property
    def account_connection_challenges(self) -> AsyncAccountConnectionChallengesResource:
        """Connected X account management"""
        return AsyncAccountConnectionChallengesResource(self._client)

    @cached_property
    def account_connection_attempts(self) -> AsyncAccountConnectionAttemptsResource:
        """Connected X account management"""
        return AsyncAccountConnectionAttemptsResource(self._client)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResource:
        """Look up, search, and analyze individual tweets"""
        return AsyncBookmarksResource(self._client)

    @cached_property
    def lists(self) -> AsyncListsResource:
        """X List search, details, followers, members, and tweets"""
        return AsyncListsResource(self._client)

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResource:
        """X live video details, watch counts, and broadcaster"""
        return AsyncBroadcastsResource(self._client)

    @cached_property
    def spaces(self) -> AsyncSpacesResource:
        """X Space details, host, and speakers"""
        return AsyncSpacesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncXResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncXResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncXResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncXResourceWithStreamingResponse(self)

    async def autocomplete_search(
        self,
        *,
        q: str,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        types: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XAutocompleteSearchResponse:
        """
        Returns the accounts, topics, hashtags & cashtags X suggests while someone types
        a search. X may rank them differently per request. Costs 1 credit per
        suggestion.

        Args:
          q: Text typed so far. Start with # for hashtags or $ for cashtags. A # query
              returns hashtags & the accounts X suggests for it. Alias: query.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Most suggestions to return: 1 to 100, default 20. Accounts fill it first, then
              topics, hashtags & cashtags. Credits can return fewer. Aliases: pageSize, count,
              max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          types: Comma-separated suggestion types: users, topics, hashtags or cashtags. Omit for
              all. With only hashtags or only cashtags, the query gets its # or $ when it
              lacks one.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/search/autocomplete",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                        "types": types,
                    },
                    x_autocomplete_search_params.XAutocompleteSearchParams,
                ),
            ),
            cast_to=XAutocompleteSearchResponse,
        )

    async def get_article(
        self,
        tweet_id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetArticleResponse:
        """
        Retrieve the full content of an X Article (long-form post) by numeric tweet ID.
        Returns article_not_found when the tweet is valid but is not an X Article.

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
        if not tweet_id:
            raise ValueError(f"Expected a non-empty value for `tweet_id` but received {tweet_id!r}")
        return await self._get(
            path_template("/x/articles/{tweet_id}", tweet_id=tweet_id),
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
                    x_get_article_params.XGetArticleParams,
                ),
            ),
            cast_to=XGetArticleResponse,
        )

    async def get_hashflags(
        self,
        *,
        active_only: bool | Omit = omit,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        q: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetHashflagsResponse:
        """Returns X's hashflags, the custom emoji X shows after some hashtags.

        Lists the
        ones running now unless activeOnly is false. Each returned hashflag costs 1
        credit.

        Args:
          active_only: Keeps hashflags that run now. Send false to add ended & upcoming ones.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum hashflags to return. Omit it for every match. Credits can return fewer.
              Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          q: Text the hashtag contains, such as football. Case insensitive. A leading hash
              sign is ignored. Alias query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/hashflags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active_only": active_only,
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                        "q": q,
                    },
                    x_get_hashflags_params.XGetHashflagsParams,
                ),
            ),
            cast_to=XGetHashflagsResponse,
        )

    async def get_home_timeline(
        self,
        *,
        cursor: str | Omit = omit,
        seen_tweet_ids: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """
        Returns the home timeline of 1 of your connected X accounts, else 424
        `account_required`. A cursor reads the next page from the same account. Results
        exclude X ads.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          seen_tweet_ids: Comma-separated tweet IDs to exclude from results. Empty entries are ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/timeline",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "seen_tweet_ids": seen_tweet_ids,
                    },
                    x_get_home_timeline_params.XGetHomeTimelineParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def get_notifications(
        self,
        *,
        cursor: str | Omit = omit,
        type: Literal["All", "Verified", "Mentions"] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetNotificationsResponse:
        """
        Returns your X account's notifications, else 424 `account_required`.

        Args:
          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          type: Notification type filter. Unrecognized values fall back to All.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "type": type,
                    },
                    x_get_notifications_params.XGetNotificationsParams,
                ),
            ),
            cast_to=XGetNotificationsResponse,
        )

    async def get_trend_locations(
        self,
        *,
        country: str | Omit = omit,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        place_type: Literal["country", "town", "worldwide", "unknown"] | Omit = omit,
        q: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetTrendLocationsResponse:
        """Returns the places X offers trends for.

        Pass a location's woeid to /x/trends.
        Each returned location costs 1 credit.

        Args:
          country: Country name or 2-letter code, such as Turkey or TR. Case insensitive. Returns
              the country & its towns.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum locations to return. Omit it for every match. Credits can return fewer.
              Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          place_type: Kind of place. Case insensitive. X labels a few towns unknown.

          q: Text the location name contains, such as york. Case insensitive. Alias query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/trends/locations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                        "place_type": place_type,
                        "q": q,
                    },
                    x_get_trend_locations_params.XGetTrendLocationsParams,
                ),
            ),
            cast_to=XGetTrendLocationsResponse,
        )

    async def get_trends(
        self,
        *,
        count: int | Omit = omit,
        country: str | Omit = omit,
        fields: str | Omit = omit,
        location: str | Omit = omit,
        omit: str | Omit = omit,
        woeid: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XGetTrendsResponse:
        """Returns X's current trends for a place you choose.

        Pick it by woeid, country or
        location name. Without one, trends are worldwide. Each request costs 1 credit,
        however many trends it returns.

        Args:
          count: Number of trending topics to return (1-50, default 30)

          country: Country to read trends for, by name or 2-letter code, such as Turkey or TR. Case
              insensitive.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          location: Town or country to read trends for, by name, such as Istanbul. Case insensitive.
              Add country when 2 towns share a name. /x/trends/locations lists every name.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          woeid: Region WOEID (1=Worldwide, 23424977=US, 23424975=UK, 23424969=Turkey). Wins over
              country & location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/trends",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "count": count,
                        "country": country,
                        "fields": fields,
                        "location": location,
                        "omit": omit,
                        "woeid": woeid,
                    },
                    x_get_trends_params.XGetTrendsParams,
                ),
            ),
            cast_to=XGetTrendsResponse,
        )

    async def search_places(
        self,
        *,
        q: str,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> XSearchPlacesResponse:
        """Finds places on X by name.

        Pass a place's id as place to /x/tweets/search to
        read posts tagged there. X ranks the places, so their order can differ between
        requests. Each returned place costs 1 credit.

        Args:
          q: Place name to search for, such as istanbul. Alias query.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum places to return. Omit it for every place X finds. Credits can return
              fewer. Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/places/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                    },
                    x_search_places_params.XSearchPlacesParams,
                ),
            ),
            cast_to=XSearchPlacesResponse,
        )


class XResourceWithRawResponse:
    def __init__(self, x: XResource) -> None:
        self._x = x

        self.autocomplete_search = to_raw_response_wrapper(
            x.autocomplete_search,
        )
        self.get_article = to_raw_response_wrapper(
            x.get_article,
        )
        self.get_hashflags = to_raw_response_wrapper(
            x.get_hashflags,
        )
        self.get_home_timeline = to_raw_response_wrapper(
            x.get_home_timeline,
        )
        self.get_notifications = to_raw_response_wrapper(
            x.get_notifications,
        )
        self.get_trend_locations = to_raw_response_wrapper(
            x.get_trend_locations,
        )
        self.get_trends = to_raw_response_wrapper(
            x.get_trends,
        )
        self.search_places = to_raw_response_wrapper(
            x.search_places,
        )

    @cached_property
    def write_actions(self) -> WriteActionsResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return WriteActionsResourceWithRawResponse(self._x.write_actions)

    @cached_property
    def analysis(self) -> AnalysisResourceWithRawResponse:
        """AI analysis of posts, at 2 credits per analyzed post"""
        return AnalysisResourceWithRawResponse(self._x.analysis)

    @cached_property
    def tweets(self) -> TweetsResourceWithRawResponse:
        return TweetsResourceWithRawResponse(self._x.tweets)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._x.users)

    @cached_property
    def followers(self) -> FollowersResourceWithRawResponse:
        """Look up, search, and explore user profiles and relationships"""
        return FollowersResourceWithRawResponse(self._x.followers)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        """Public X job listings, search and details"""
        return JobsResourceWithRawResponse(self._x.jobs)

    @cached_property
    def dm(self) -> DmResourceWithRawResponse:
        return DmResourceWithRawResponse(self._x.dm)

    @cached_property
    def media(self) -> MediaResourceWithRawResponse:
        return MediaResourceWithRawResponse(self._x.media)

    @cached_property
    def profile(self) -> ProfileResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return ProfileResourceWithRawResponse(self._x.profile)

    @cached_property
    def communities(self) -> CommunitiesResourceWithRawResponse:
        return CommunitiesResourceWithRawResponse(self._x.communities)

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        """Connected X account management"""
        return AccountsResourceWithRawResponse(self._x.accounts)

    @cached_property
    def account_connection_challenges(self) -> AccountConnectionChallengesResourceWithRawResponse:
        """Connected X account management"""
        return AccountConnectionChallengesResourceWithRawResponse(self._x.account_connection_challenges)

    @cached_property
    def account_connection_attempts(self) -> AccountConnectionAttemptsResourceWithRawResponse:
        """Connected X account management"""
        return AccountConnectionAttemptsResourceWithRawResponse(self._x.account_connection_attempts)

    @cached_property
    def bookmarks(self) -> BookmarksResourceWithRawResponse:
        """Look up, search, and analyze individual tweets"""
        return BookmarksResourceWithRawResponse(self._x.bookmarks)

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        """X List search, details, followers, members, and tweets"""
        return ListsResourceWithRawResponse(self._x.lists)

    @cached_property
    def broadcasts(self) -> BroadcastsResourceWithRawResponse:
        """X live video details, watch counts, and broadcaster"""
        return BroadcastsResourceWithRawResponse(self._x.broadcasts)

    @cached_property
    def spaces(self) -> SpacesResourceWithRawResponse:
        """X Space details, host, and speakers"""
        return SpacesResourceWithRawResponse(self._x.spaces)


class AsyncXResourceWithRawResponse:
    def __init__(self, x: AsyncXResource) -> None:
        self._x = x

        self.autocomplete_search = async_to_raw_response_wrapper(
            x.autocomplete_search,
        )
        self.get_article = async_to_raw_response_wrapper(
            x.get_article,
        )
        self.get_hashflags = async_to_raw_response_wrapper(
            x.get_hashflags,
        )
        self.get_home_timeline = async_to_raw_response_wrapper(
            x.get_home_timeline,
        )
        self.get_notifications = async_to_raw_response_wrapper(
            x.get_notifications,
        )
        self.get_trend_locations = async_to_raw_response_wrapper(
            x.get_trend_locations,
        )
        self.get_trends = async_to_raw_response_wrapper(
            x.get_trends,
        )
        self.search_places = async_to_raw_response_wrapper(
            x.search_places,
        )

    @cached_property
    def write_actions(self) -> AsyncWriteActionsResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncWriteActionsResourceWithRawResponse(self._x.write_actions)

    @cached_property
    def analysis(self) -> AsyncAnalysisResourceWithRawResponse:
        """AI analysis of posts, at 2 credits per analyzed post"""
        return AsyncAnalysisResourceWithRawResponse(self._x.analysis)

    @cached_property
    def tweets(self) -> AsyncTweetsResourceWithRawResponse:
        return AsyncTweetsResourceWithRawResponse(self._x.tweets)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._x.users)

    @cached_property
    def followers(self) -> AsyncFollowersResourceWithRawResponse:
        """Look up, search, and explore user profiles and relationships"""
        return AsyncFollowersResourceWithRawResponse(self._x.followers)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        """Public X job listings, search and details"""
        return AsyncJobsResourceWithRawResponse(self._x.jobs)

    @cached_property
    def dm(self) -> AsyncDmResourceWithRawResponse:
        return AsyncDmResourceWithRawResponse(self._x.dm)

    @cached_property
    def media(self) -> AsyncMediaResourceWithRawResponse:
        return AsyncMediaResourceWithRawResponse(self._x.media)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncProfileResourceWithRawResponse(self._x.profile)

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithRawResponse:
        return AsyncCommunitiesResourceWithRawResponse(self._x.communities)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        """Connected X account management"""
        return AsyncAccountsResourceWithRawResponse(self._x.accounts)

    @cached_property
    def account_connection_challenges(self) -> AsyncAccountConnectionChallengesResourceWithRawResponse:
        """Connected X account management"""
        return AsyncAccountConnectionChallengesResourceWithRawResponse(self._x.account_connection_challenges)

    @cached_property
    def account_connection_attempts(self) -> AsyncAccountConnectionAttemptsResourceWithRawResponse:
        """Connected X account management"""
        return AsyncAccountConnectionAttemptsResourceWithRawResponse(self._x.account_connection_attempts)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResourceWithRawResponse:
        """Look up, search, and analyze individual tweets"""
        return AsyncBookmarksResourceWithRawResponse(self._x.bookmarks)

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        """X List search, details, followers, members, and tweets"""
        return AsyncListsResourceWithRawResponse(self._x.lists)

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResourceWithRawResponse:
        """X live video details, watch counts, and broadcaster"""
        return AsyncBroadcastsResourceWithRawResponse(self._x.broadcasts)

    @cached_property
    def spaces(self) -> AsyncSpacesResourceWithRawResponse:
        """X Space details, host, and speakers"""
        return AsyncSpacesResourceWithRawResponse(self._x.spaces)


class XResourceWithStreamingResponse:
    def __init__(self, x: XResource) -> None:
        self._x = x

        self.autocomplete_search = to_streamed_response_wrapper(
            x.autocomplete_search,
        )
        self.get_article = to_streamed_response_wrapper(
            x.get_article,
        )
        self.get_hashflags = to_streamed_response_wrapper(
            x.get_hashflags,
        )
        self.get_home_timeline = to_streamed_response_wrapper(
            x.get_home_timeline,
        )
        self.get_notifications = to_streamed_response_wrapper(
            x.get_notifications,
        )
        self.get_trend_locations = to_streamed_response_wrapper(
            x.get_trend_locations,
        )
        self.get_trends = to_streamed_response_wrapper(
            x.get_trends,
        )
        self.search_places = to_streamed_response_wrapper(
            x.search_places,
        )

    @cached_property
    def write_actions(self) -> WriteActionsResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return WriteActionsResourceWithStreamingResponse(self._x.write_actions)

    @cached_property
    def analysis(self) -> AnalysisResourceWithStreamingResponse:
        """AI analysis of posts, at 2 credits per analyzed post"""
        return AnalysisResourceWithStreamingResponse(self._x.analysis)

    @cached_property
    def tweets(self) -> TweetsResourceWithStreamingResponse:
        return TweetsResourceWithStreamingResponse(self._x.tweets)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._x.users)

    @cached_property
    def followers(self) -> FollowersResourceWithStreamingResponse:
        """Look up, search, and explore user profiles and relationships"""
        return FollowersResourceWithStreamingResponse(self._x.followers)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        """Public X job listings, search and details"""
        return JobsResourceWithStreamingResponse(self._x.jobs)

    @cached_property
    def dm(self) -> DmResourceWithStreamingResponse:
        return DmResourceWithStreamingResponse(self._x.dm)

    @cached_property
    def media(self) -> MediaResourceWithStreamingResponse:
        return MediaResourceWithStreamingResponse(self._x.media)

    @cached_property
    def profile(self) -> ProfileResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return ProfileResourceWithStreamingResponse(self._x.profile)

    @cached_property
    def communities(self) -> CommunitiesResourceWithStreamingResponse:
        return CommunitiesResourceWithStreamingResponse(self._x.communities)

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        """Connected X account management"""
        return AccountsResourceWithStreamingResponse(self._x.accounts)

    @cached_property
    def account_connection_challenges(self) -> AccountConnectionChallengesResourceWithStreamingResponse:
        """Connected X account management"""
        return AccountConnectionChallengesResourceWithStreamingResponse(self._x.account_connection_challenges)

    @cached_property
    def account_connection_attempts(self) -> AccountConnectionAttemptsResourceWithStreamingResponse:
        """Connected X account management"""
        return AccountConnectionAttemptsResourceWithStreamingResponse(self._x.account_connection_attempts)

    @cached_property
    def bookmarks(self) -> BookmarksResourceWithStreamingResponse:
        """Look up, search, and analyze individual tweets"""
        return BookmarksResourceWithStreamingResponse(self._x.bookmarks)

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        """X List search, details, followers, members, and tweets"""
        return ListsResourceWithStreamingResponse(self._x.lists)

    @cached_property
    def broadcasts(self) -> BroadcastsResourceWithStreamingResponse:
        """X live video details, watch counts, and broadcaster"""
        return BroadcastsResourceWithStreamingResponse(self._x.broadcasts)

    @cached_property
    def spaces(self) -> SpacesResourceWithStreamingResponse:
        """X Space details, host, and speakers"""
        return SpacesResourceWithStreamingResponse(self._x.spaces)


class AsyncXResourceWithStreamingResponse:
    def __init__(self, x: AsyncXResource) -> None:
        self._x = x

        self.autocomplete_search = async_to_streamed_response_wrapper(
            x.autocomplete_search,
        )
        self.get_article = async_to_streamed_response_wrapper(
            x.get_article,
        )
        self.get_hashflags = async_to_streamed_response_wrapper(
            x.get_hashflags,
        )
        self.get_home_timeline = async_to_streamed_response_wrapper(
            x.get_home_timeline,
        )
        self.get_notifications = async_to_streamed_response_wrapper(
            x.get_notifications,
        )
        self.get_trend_locations = async_to_streamed_response_wrapper(
            x.get_trend_locations,
        )
        self.get_trends = async_to_streamed_response_wrapper(
            x.get_trends,
        )
        self.search_places = async_to_streamed_response_wrapper(
            x.search_places,
        )

    @cached_property
    def write_actions(self) -> AsyncWriteActionsResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncWriteActionsResourceWithStreamingResponse(self._x.write_actions)

    @cached_property
    def analysis(self) -> AsyncAnalysisResourceWithStreamingResponse:
        """AI analysis of posts, at 2 credits per analyzed post"""
        return AsyncAnalysisResourceWithStreamingResponse(self._x.analysis)

    @cached_property
    def tweets(self) -> AsyncTweetsResourceWithStreamingResponse:
        return AsyncTweetsResourceWithStreamingResponse(self._x.tweets)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._x.users)

    @cached_property
    def followers(self) -> AsyncFollowersResourceWithStreamingResponse:
        """Look up, search, and explore user profiles and relationships"""
        return AsyncFollowersResourceWithStreamingResponse(self._x.followers)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        """Public X job listings, search and details"""
        return AsyncJobsResourceWithStreamingResponse(self._x.jobs)

    @cached_property
    def dm(self) -> AsyncDmResourceWithStreamingResponse:
        return AsyncDmResourceWithStreamingResponse(self._x.dm)

    @cached_property
    def media(self) -> AsyncMediaResourceWithStreamingResponse:
        return AsyncMediaResourceWithStreamingResponse(self._x.media)

    @cached_property
    def profile(self) -> AsyncProfileResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncProfileResourceWithStreamingResponse(self._x.profile)

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithStreamingResponse:
        return AsyncCommunitiesResourceWithStreamingResponse(self._x.communities)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        """Connected X account management"""
        return AsyncAccountsResourceWithStreamingResponse(self._x.accounts)

    @cached_property
    def account_connection_challenges(self) -> AsyncAccountConnectionChallengesResourceWithStreamingResponse:
        """Connected X account management"""
        return AsyncAccountConnectionChallengesResourceWithStreamingResponse(self._x.account_connection_challenges)

    @cached_property
    def account_connection_attempts(self) -> AsyncAccountConnectionAttemptsResourceWithStreamingResponse:
        """Connected X account management"""
        return AsyncAccountConnectionAttemptsResourceWithStreamingResponse(self._x.account_connection_attempts)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResourceWithStreamingResponse:
        """Look up, search, and analyze individual tweets"""
        return AsyncBookmarksResourceWithStreamingResponse(self._x.bookmarks)

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        """X List search, details, followers, members, and tweets"""
        return AsyncListsResourceWithStreamingResponse(self._x.lists)

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResourceWithStreamingResponse:
        """X live video details, watch counts, and broadcaster"""
        return AsyncBroadcastsResourceWithStreamingResponse(self._x.broadcasts)

    @cached_property
    def spaces(self) -> AsyncSpacesResourceWithStreamingResponse:
        """X Space details, host, and speakers"""
        return AsyncSpacesResourceWithStreamingResponse(self._x.spaces)
