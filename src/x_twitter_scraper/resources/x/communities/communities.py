# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from .join import (
    JoinResource,
    AsyncJoinResource,
    JoinResourceWithRawResponse,
    AsyncJoinResourceWithRawResponse,
    JoinResourceWithStreamingResponse,
    AsyncJoinResourceWithStreamingResponse,
)
from .media import (
    MediaResource,
    AsyncMediaResource,
    MediaResourceWithRawResponse,
    AsyncMediaResourceWithRawResponse,
    MediaResourceWithStreamingResponse,
    AsyncMediaResourceWithStreamingResponse,
)
from .tweets import (
    TweetsResource,
    AsyncTweetsResource,
    TweetsResourceWithRawResponse,
    AsyncTweetsResourceWithRawResponse,
    TweetsResourceWithStreamingResponse,
    AsyncTweetsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.x import (
    community_find_params,
    community_create_params,
    community_delete_params,
    community_list_topics_params,
    community_list_popular_params,
    community_retrieve_info_params,
    community_list_suggested_params,
    community_search_members_params,
    community_retrieve_search_params,
    community_retrieve_members_params,
    community_retrieve_analytics_params,
    community_retrieve_moderators_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.shared.community_page import CommunityPage
from ....types.shared.paginated_users import PaginatedUsers
from ....types.shared.paginated_tweets import PaginatedTweets
from ....types.shared.community_analytics import CommunityAnalytics
from ....types.x.community_create_response import CommunityCreateResponse
from ....types.x.community_delete_response import CommunityDeleteResponse
from ....types.x.community_list_topics_response import CommunityListTopicsResponse
from ....types.x.community_retrieve_info_response import CommunityRetrieveInfoResponse
from ....types.x.community_list_suggested_response import CommunityListSuggestedResponse

__all__ = ["CommunitiesResource", "AsyncCommunitiesResource"]


class CommunitiesResource(SyncAPIResource):
    @cached_property
    def join(self) -> JoinResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return JoinResource(self._client)

    @cached_property
    def tweets(self) -> TweetsResource:
        """Find X Communities & read their info, members, posts & media"""
        return TweetsResource(self._client)

    @cached_property
    def media(self) -> MediaResource:
        """Find X Communities & read their info, members, posts & media"""
        return MediaResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommunitiesResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return CommunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return CommunitiesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account: str,
        name: str,
        idempotency_key: str,
        description: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityCreateResponse:
        """
        Creates an X Community through a connected account.

        Args:
          account: X account (@username or ID) creating the community

          name: Community name, 1 to 100 characters, as X takes it

          description: Community description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return self._post(
            "/x/communities",
            body=maybe_transform(
                {
                    "account": account,
                    "name": name,
                    "description": description,
                },
                community_create_params.CommunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityCreateResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account: str,
        community_name: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityDeleteResponse:
        """
        Deletes an owned X Community through a connected account.

        Args:
          account: X account (@username or ID) deleting the community

          community_name: Community name for confirmation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return self._delete(
            path_template("/x/communities/{id}", id=id),
            body=maybe_transform(
                {
                    "account": account,
                    "community_name": community_name,
                },
                community_delete_params.CommunityDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityDeleteResponse,
        )

    def find(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityPage:
        """Returns the communities X finds for a keyword, in X's order.

        Each community
        costs 1 credit. To search the tweets in Communities, use /x/communities/search.

        Args:
          q: Keyword to find communities by, such as ai. Alias query.

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
            "/x/communities/find",
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
                    community_find_params.CommunityFindParams,
                ),
            ),
            cast_to=CommunityPage,
        )

    def list_popular(
        self,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        topic: str | Omit = omit,
        topic_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityPage:
        """Returns the communities X ranks highest under a topic or subtopic.

        Name it by
        topicId or by topic name from /x/communities/topics. Each community costs 1
        credit. A missing or unknown topic returns invalid_community_topic & lists the
        topic names.

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

          topic: Topic or subtopic name in any case, such as technology. Send this or topicId.

          topic_id: Topic or subtopic ID from /x/communities/topics, such as 301. Wins over topic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/communities/popular",
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
                        "topic": topic,
                        "topic_id": topic_id,
                    },
                    community_list_popular_params.CommunityListPopularParams,
                ),
            ),
            cast_to=CommunityPage,
        )

    def list_suggested(
        self,
        *,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityListSuggestedResponse:
        """Returns the communities X suggests, with their full public fields.

        X picks them
        per request, so 2 calls can differ. If X suggests none, Xquik asks up to 2 more
        times. An empty list is free. Each community costs 1 credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum communities to return. Omit it for every suggestion. Credits can return
              fewer. Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/communities/suggested",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                    },
                    community_list_suggested_params.CommunityListSuggestedParams,
                ),
            ),
            cast_to=CommunityListSuggestedResponse,
        )

    def list_topics(
        self,
        *,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityListTopicsResponse:
        """Returns the community topics with their subtopics.

        Pass an ID as topicId, or a
        name as topic, to /x/communities/popular. Each top-level topic costs 1 credit,
        its subtopics included.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum topics to return. Omit it for every topic. Credits can return fewer.
              Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/communities/topics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                    },
                    community_list_topics_params.CommunityListTopicsParams,
                ),
            ),
            cast_to=CommunityListTopicsResponse,
        )

    def retrieve_analytics(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityAnalytics:
        """Returns community activity for X's latest period.

        Includes likes, new members, posts, replies & unique posters. Each metric has a
        count and a changePercent. Each request costs 1 credit.

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
            path_template("/x/communities/{id}/analytics", id=id),
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
                    community_retrieve_analytics_params.CommunityRetrieveAnalyticsParams,
                ),
            ),
            cast_to=CommunityAnalytics,
        )

    def retrieve_info(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityRetrieveInfoResponse:
        """
        Returns one community's public identity, rules, join question, search tags,
        membership counts, and the profiles of its creator, admin and previewed members.

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
            path_template("/x/communities/{id}/info", id=id),
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
                    community_retrieve_info_params.CommunityRetrieveInfoParams,
                ),
            ),
            cast_to=CommunityRetrieveInfoResponse,
        )

    def retrieve_members(
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
        Returns public member profiles for one community.

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

          page_size: Maximum user profiles per page (1-200, default 20).

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
            path_template("/x/communities/{id}/members", id=id),
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
                    community_retrieve_members_params.CommunityRetrieveMembersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_moderators(
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
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Returns public moderator profiles for one community.

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
            path_template("/x/communities/{id}/moderators", id=id),
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
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
                    },
                    community_retrieve_moderators_params.CommunityRetrieveModeratorsParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    def retrieve_search(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns one tweet page, not community records.

        Add communityId to search 1
        Community, or leave it out to search every Community. To find communities by
        keyword, use /x/communities/find.

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
            "/x/communities/search",
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
                    community_retrieve_search_params.CommunityRetrieveSearchParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    def search_members(
        self,
        id: str,
        *,
        q: str,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        business_email_only: bool | Omit = omit,
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
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Finds a community's members by name or username, as the search box on X's
        members page does. X checks up to 10 accounts that match, & the answer holds the
        members among them, each with its role. Each member costs 1 credit. An answer
        without members is free.

        Args:
          q: Name or username to find members by, such as marckohlbrugge. A leading @ is
              dropped. Alias query.

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
            path_template("/x/communities/{id}/members/search", id=id),
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
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
                    },
                    community_search_members_params.CommunitySearchMembersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )


class AsyncCommunitiesResource(AsyncAPIResource):
    @cached_property
    def join(self) -> AsyncJoinResource:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncJoinResource(self._client)

    @cached_property
    def tweets(self) -> AsyncTweetsResource:
        """Find X Communities & read their info, members, posts & media"""
        return AsyncTweetsResource(self._client)

    @cached_property
    def media(self) -> AsyncMediaResource:
        """Find X Communities & read their info, members, posts & media"""
        return AsyncMediaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommunitiesResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncCommunitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommunitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncCommunitiesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account: str,
        name: str,
        idempotency_key: str,
        description: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityCreateResponse:
        """
        Creates an X Community through a connected account.

        Args:
          account: X account (@username or ID) creating the community

          name: Community name, 1 to 100 characters, as X takes it

          description: Community description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return await self._post(
            "/x/communities",
            body=await async_maybe_transform(
                {
                    "account": account,
                    "name": name,
                    "description": description,
                },
                community_create_params.CommunityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityCreateResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account: str,
        community_name: str,
        idempotency_key: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityDeleteResponse:
        """
        Deletes an owned X Community through a connected account.

        Args:
          account: X account (@username or ID) deleting the community

          community_name: Community name for confirmation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or dict[str, str | Omit]())}
        return await self._delete(
            path_template("/x/communities/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "account": account,
                    "community_name": community_name,
                },
                community_delete_params.CommunityDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityDeleteResponse,
        )

    async def find(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityPage:
        """Returns the communities X finds for a keyword, in X's order.

        Each community
        costs 1 credit. To search the tweets in Communities, use /x/communities/search.

        Args:
          q: Keyword to find communities by, such as ai. Alias query.

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
            "/x/communities/find",
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
                    community_find_params.CommunityFindParams,
                ),
            ),
            cast_to=CommunityPage,
        )

    async def list_popular(
        self,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        topic: str | Omit = omit,
        topic_id: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityPage:
        """Returns the communities X ranks highest under a topic or subtopic.

        Name it by
        topicId or by topic name from /x/communities/topics. Each community costs 1
        credit. A missing or unknown topic returns invalid_community_topic & lists the
        topic names.

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

          topic: Topic or subtopic name in any case, such as technology. Send this or topicId.

          topic_id: Topic or subtopic ID from /x/communities/topics, such as 301. Wins over topic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/communities/popular",
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
                        "topic": topic,
                        "topic_id": topic_id,
                    },
                    community_list_popular_params.CommunityListPopularParams,
                ),
            ),
            cast_to=CommunityPage,
        )

    async def list_suggested(
        self,
        *,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityListSuggestedResponse:
        """Returns the communities X suggests, with their full public fields.

        X picks them
        per request, so 2 calls can differ. If X suggests none, Xquik asks up to 2 more
        times. An empty list is free. Each community costs 1 credit.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum communities to return. Omit it for every suggestion. Credits can return
              fewer. Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/communities/suggested",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                    },
                    community_list_suggested_params.CommunityListSuggestedParams,
                ),
            ),
            cast_to=CommunityListSuggestedResponse,
        )

    async def list_topics(
        self,
        *,
        fields: str | Omit = omit,
        limit: int | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityListTopicsResponse:
        """Returns the community topics with their subtopics.

        Pass an ID as topicId, or a
        name as topic, to /x/communities/popular. Each top-level topic costs 1 credit,
        its subtopics included.

        Args:
          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Maximum topics to return. Omit it for every topic. Credits can return fewer.
              Aliases pageSize, count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/communities/topics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "limit": limit,
                        "omit": omit,
                    },
                    community_list_topics_params.CommunityListTopicsParams,
                ),
            ),
            cast_to=CommunityListTopicsResponse,
        )

    async def retrieve_analytics(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityAnalytics:
        """Returns community activity for X's latest period.

        Includes likes, new members, posts, replies & unique posters. Each metric has a
        count and a changePercent. Each request costs 1 credit.

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
            path_template("/x/communities/{id}/analytics", id=id),
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
                    community_retrieve_analytics_params.CommunityRetrieveAnalyticsParams,
                ),
            ),
            cast_to=CommunityAnalytics,
        )

    async def retrieve_info(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityRetrieveInfoResponse:
        """
        Returns one community's public identity, rules, join question, search tags,
        membership counts, and the profiles of its creator, admin and previewed members.

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
            path_template("/x/communities/{id}/info", id=id),
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
                    community_retrieve_info_params.CommunityRetrieveInfoParams,
                ),
            ),
            cast_to=CommunityRetrieveInfoResponse,
        )

    async def retrieve_members(
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
        Returns public member profiles for one community.

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

          page_size: Maximum user profiles per page (1-200, default 20).

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
            path_template("/x/communities/{id}/members", id=id),
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
                    community_retrieve_members_params.CommunityRetrieveMembersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_moderators(
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
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Returns public moderator profiles for one community.

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
            path_template("/x/communities/{id}/moderators", id=id),
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
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
                    },
                    community_retrieve_moderators_params.CommunityRetrieveModeratorsParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )

    async def retrieve_search(
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
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTweets:
        """Returns one tweet page, not community records.

        Add communityId to search 1
        Community, or leave it out to search every Community. To find communities by
        keyword, use /x/communities/find.

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
            "/x/communities/search",
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
                    community_retrieve_search_params.CommunityRetrieveSearchParams,
                ),
            ),
            cast_to=PaginatedTweets,
        )

    async def search_members(
        self,
        id: str,
        *,
        q: str,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        business_email_only: bool | Omit = omit,
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
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedUsers:
        """
        Finds a community's members by name or username, as the search box on X's
        members page does. X checks up to 10 accounts that match, & the answer holds the
        members among them, each with its role. Each member costs 1 credit. An answer
        without members is free.

        Args:
          q: Name or username to find members by, such as marckohlbrugge. A leading @ is
              dropped. Alias query.

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
            path_template("/x/communities/{id}/members/search", id=id),
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
                        "username_contains": username_contains,
                        "verified_only": verified_only,
                        "verified_type": verified_type,
                    },
                    community_search_members_params.CommunitySearchMembersParams,
                ),
            ),
            cast_to=PaginatedUsers,
        )


class CommunitiesResourceWithRawResponse:
    def __init__(self, communities: CommunitiesResource) -> None:
        self._communities = communities

        self.create = to_raw_response_wrapper(
            communities.create,
        )
        self.delete = to_raw_response_wrapper(
            communities.delete,
        )
        self.find = to_raw_response_wrapper(
            communities.find,
        )
        self.list_popular = to_raw_response_wrapper(
            communities.list_popular,
        )
        self.list_suggested = to_raw_response_wrapper(
            communities.list_suggested,
        )
        self.list_topics = to_raw_response_wrapper(
            communities.list_topics,
        )
        self.retrieve_analytics = to_raw_response_wrapper(
            communities.retrieve_analytics,
        )
        self.retrieve_info = to_raw_response_wrapper(
            communities.retrieve_info,
        )
        self.retrieve_members = to_raw_response_wrapper(
            communities.retrieve_members,
        )
        self.retrieve_moderators = to_raw_response_wrapper(
            communities.retrieve_moderators,
        )
        self.retrieve_search = to_raw_response_wrapper(
            communities.retrieve_search,
        )
        self.search_members = to_raw_response_wrapper(
            communities.search_members,
        )

    @cached_property
    def join(self) -> JoinResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return JoinResourceWithRawResponse(self._communities.join)

    @cached_property
    def tweets(self) -> TweetsResourceWithRawResponse:
        """Find X Communities & read their info, members, posts & media"""
        return TweetsResourceWithRawResponse(self._communities.tweets)

    @cached_property
    def media(self) -> MediaResourceWithRawResponse:
        """Find X Communities & read their info, members, posts & media"""
        return MediaResourceWithRawResponse(self._communities.media)


class AsyncCommunitiesResourceWithRawResponse:
    def __init__(self, communities: AsyncCommunitiesResource) -> None:
        self._communities = communities

        self.create = async_to_raw_response_wrapper(
            communities.create,
        )
        self.delete = async_to_raw_response_wrapper(
            communities.delete,
        )
        self.find = async_to_raw_response_wrapper(
            communities.find,
        )
        self.list_popular = async_to_raw_response_wrapper(
            communities.list_popular,
        )
        self.list_suggested = async_to_raw_response_wrapper(
            communities.list_suggested,
        )
        self.list_topics = async_to_raw_response_wrapper(
            communities.list_topics,
        )
        self.retrieve_analytics = async_to_raw_response_wrapper(
            communities.retrieve_analytics,
        )
        self.retrieve_info = async_to_raw_response_wrapper(
            communities.retrieve_info,
        )
        self.retrieve_members = async_to_raw_response_wrapper(
            communities.retrieve_members,
        )
        self.retrieve_moderators = async_to_raw_response_wrapper(
            communities.retrieve_moderators,
        )
        self.retrieve_search = async_to_raw_response_wrapper(
            communities.retrieve_search,
        )
        self.search_members = async_to_raw_response_wrapper(
            communities.search_members,
        )

    @cached_property
    def join(self) -> AsyncJoinResourceWithRawResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncJoinResourceWithRawResponse(self._communities.join)

    @cached_property
    def tweets(self) -> AsyncTweetsResourceWithRawResponse:
        """Find X Communities & read their info, members, posts & media"""
        return AsyncTweetsResourceWithRawResponse(self._communities.tweets)

    @cached_property
    def media(self) -> AsyncMediaResourceWithRawResponse:
        """Find X Communities & read their info, members, posts & media"""
        return AsyncMediaResourceWithRawResponse(self._communities.media)


class CommunitiesResourceWithStreamingResponse:
    def __init__(self, communities: CommunitiesResource) -> None:
        self._communities = communities

        self.create = to_streamed_response_wrapper(
            communities.create,
        )
        self.delete = to_streamed_response_wrapper(
            communities.delete,
        )
        self.find = to_streamed_response_wrapper(
            communities.find,
        )
        self.list_popular = to_streamed_response_wrapper(
            communities.list_popular,
        )
        self.list_suggested = to_streamed_response_wrapper(
            communities.list_suggested,
        )
        self.list_topics = to_streamed_response_wrapper(
            communities.list_topics,
        )
        self.retrieve_analytics = to_streamed_response_wrapper(
            communities.retrieve_analytics,
        )
        self.retrieve_info = to_streamed_response_wrapper(
            communities.retrieve_info,
        )
        self.retrieve_members = to_streamed_response_wrapper(
            communities.retrieve_members,
        )
        self.retrieve_moderators = to_streamed_response_wrapper(
            communities.retrieve_moderators,
        )
        self.retrieve_search = to_streamed_response_wrapper(
            communities.retrieve_search,
        )
        self.search_members = to_streamed_response_wrapper(
            communities.search_members,
        )

    @cached_property
    def join(self) -> JoinResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return JoinResourceWithStreamingResponse(self._communities.join)

    @cached_property
    def tweets(self) -> TweetsResourceWithStreamingResponse:
        """Find X Communities & read their info, members, posts & media"""
        return TweetsResourceWithStreamingResponse(self._communities.tweets)

    @cached_property
    def media(self) -> MediaResourceWithStreamingResponse:
        """Find X Communities & read their info, members, posts & media"""
        return MediaResourceWithStreamingResponse(self._communities.media)


class AsyncCommunitiesResourceWithStreamingResponse:
    def __init__(self, communities: AsyncCommunitiesResource) -> None:
        self._communities = communities

        self.create = async_to_streamed_response_wrapper(
            communities.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            communities.delete,
        )
        self.find = async_to_streamed_response_wrapper(
            communities.find,
        )
        self.list_popular = async_to_streamed_response_wrapper(
            communities.list_popular,
        )
        self.list_suggested = async_to_streamed_response_wrapper(
            communities.list_suggested,
        )
        self.list_topics = async_to_streamed_response_wrapper(
            communities.list_topics,
        )
        self.retrieve_analytics = async_to_streamed_response_wrapper(
            communities.retrieve_analytics,
        )
        self.retrieve_info = async_to_streamed_response_wrapper(
            communities.retrieve_info,
        )
        self.retrieve_members = async_to_streamed_response_wrapper(
            communities.retrieve_members,
        )
        self.retrieve_moderators = async_to_streamed_response_wrapper(
            communities.retrieve_moderators,
        )
        self.retrieve_search = async_to_streamed_response_wrapper(
            communities.retrieve_search,
        )
        self.search_members = async_to_streamed_response_wrapper(
            communities.search_members,
        )

    @cached_property
    def join(self) -> AsyncJoinResourceWithStreamingResponse:
        """X write actions (tweets, likes, follows, DMs)"""
        return AsyncJoinResourceWithStreamingResponse(self._communities.join)

    @cached_property
    def tweets(self) -> AsyncTweetsResourceWithStreamingResponse:
        """Find X Communities & read their info, members, posts & media"""
        return AsyncTweetsResourceWithStreamingResponse(self._communities.tweets)

    @cached_property
    def media(self) -> AsyncMediaResourceWithStreamingResponse:
        """Find X Communities & read their info, members, posts & media"""
        return AsyncMediaResourceWithStreamingResponse(self._communities.media)
