# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..types import (
    extraction_run_params,
    extraction_list_params,
    extraction_retrieve_params,
    extraction_estimate_cost_params,
    extraction_export_results_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.extraction_run_response import ExtractionRunResponse
from ..types.extraction_list_response import ExtractionListResponse
from ..types.extraction_retrieve_response import ExtractionRetrieveResponse
from ..types.extraction_estimate_cost_response import ExtractionEstimateCostResponse

__all__ = ["ExtractionsResource", "AsyncExtractionsResource"]


class ExtractionsResource(SyncAPIResource):
    """Bulk data extraction (23 tool types)"""

    @cached_property
    def with_raw_response(self) -> ExtractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return ExtractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return ExtractionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        field_style: Literal["source", "camelCase", "snake_case"] | Omit = omit,
        include_raw: bool | Omit = omit,
        limit: int | Omit = omit,
        output_mode: Literal["compact", "full", "raw"] | Omit = omit,
        output_preset: Literal["nested", "flat"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionRetrieveResponse:
        """
        Get extraction results

        Args:
          cursor: Previous nextCursor.

          field_style: Preserve source keys or convert result field names.

          include_raw: Use outputMode=raw instead.

          limit: Maximum number of results to return (1-1000, default 100)

          output_mode: Select compact, full, or raw-compatible result fields.

          output_preset: Keep enrichment nested or merge it into each result.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/extractions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "field_style": field_style,
                        "include_raw": include_raw,
                        "limit": limit,
                        "output_mode": output_mode,
                        "output_preset": output_preset,
                    },
                    extraction_retrieve_params.ExtractionRetrieveParams,
                ),
            ),
            cast_to=ExtractionRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        tool_type: Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
            "favoriters",
            "follower_explorer",
            "following_explorer",
            "list_follower_explorer",
            "list_member_extractor",
            "list_post_extractor",
            "mention_extractor",
            "people_search",
            "post_extractor",
            "quote_extractor",
            "reply_extractor",
            "repost_extractor",
            "space_explorer",
            "thread_extractor",
            "tweet_search_extractor",
            "user_likes",
            "user_media",
            "verified_follower_explorer",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionListResponse:
        """
        List extraction jobs

        Args:
          cursor: Previous nextCursor.

          limit: Maximum number of items to return (1-100, default 50). For paid per-result
              endpoints, the returned count may be lower when remaining credits cannot cover
              the requested page. If zero paid results are affordable, the endpoint returns
              402 insufficient_credits.

          status: Filter by job status

          tool_type: Filter by extraction tool type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/extractions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "tool_type": tool_type,
                    },
                    extraction_list_params.ExtractionListParams,
                ),
            ),
            cast_to=ExtractionListResponse,
        )

    def estimate_cost(
        self,
        *,
        tool_type: Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
            "favoriters",
            "follower_explorer",
            "following_explorer",
            "list_follower_explorer",
            "list_member_extractor",
            "list_post_extractor",
            "mention_extractor",
            "people_search",
            "post_extractor",
            "quote_extractor",
            "reply_extractor",
            "repost_extractor",
            "space_explorer",
            "thread_extractor",
            "tweet_search_extractor",
            "user_likes",
            "user_media",
            "verified_follower_explorer",
        ],
        advanced_query: str | Omit = omit,
        any_words: str | Omit = omit,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        bounding_box: str | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        collection_strategy: Literal["auto", "complete", "direct", "search", "thread"] | Omit = omit,
        conversation_id: str | Omit = omit,
        dedupe_across_targets: bool | Omit = omit,
        dedupe_mode: Literal["none", "first", "merge"] | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_original_author: bool | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_media_only: bool | Omit = omit,
        has_website: bool | Omit = omit,
        include_original_post: bool | Omit = omit,
        include_search_terms: bool | Omit = omit,
        include_target_metadata: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        list_id: str | Omit = omit,
        location_contains: str | Omit = omit,
        max_depth: int | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_id: str | Omit = omit,
        max_items_per_target: int | Omit = omit,
        max_likes: int | Omit = omit,
        max_pages_per_target: int | Omit = omit,
        max_posts: int | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_faves: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_posts: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        overlap_mode: bool | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: Literal["Latest", "Top", "Both"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        relation_targets: Iterable[extraction_estimate_cost_params.RelationTarget] | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        results_limit: int | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        scope: Literal["all", "direct", "nested"] | Omit = omit,
        search_queries: SequenceNotStr[str] | Omit = omit,
        search_query: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: Union[Union[str, datetime], int] | Omit = omit,
        sort: Literal["relevance", "latest", "oldest", "likes"] | Omit = omit,
        source: str | Omit = omit,
        start_cursor: str | Omit = omit,
        target_community_id: str | Omit = omit,
        target_community_ids: SequenceNotStr[str] | Omit = omit,
        target_list_id: str | Omit = omit,
        target_list_ids: SequenceNotStr[str] | Omit = omit,
        targets: SequenceNotStr[extraction_estimate_cost_params.Target] | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_tweet_ids: SequenceNotStr[str] | Omit = omit,
        target_username: str | Omit = omit,
        target_usernames: SequenceNotStr[str] | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: Union[Union[str, datetime], int] | Omit = omit,
        url: str | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionEstimateCostResponse:
        """
        Estimate extraction cost

        Args:
          tool_type: Identifier for the extraction tool used to run a job.

          advanced_query: Raw advanced search query appended as-is (tweet_search_extractor)

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines. (tweet_search_extractor)

          bio_contains: Bio terms separated by commas or lines.

          blue_verified_only: Return only Blue-verified Tweet authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8 (tweet_search_extractor)

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          collection_strategy: Reply collection strategy.

          conversation_id: Conversation ID filter (tweet_search_extractor)

          dedupe_across_targets: Merge duplicate results across collection targets.

          dedupe_mode: Keep target duplicates, first rows, or merged overlap.

          exact_phrase: Exact phrase to match (tweet_search_extractor)

          exclude_original_author: Exclude replies from the source author.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.
              (tweet_search_extractor)

          from_user: Filter by author username (tweet_search_extractor)

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          has_location: Require a profile location.

          has_media_only: Return only replies with media.

          has_website: Require a profile website.

          include_original_post: Include the source post in reply results.

          include_search_terms: Add matching search terms to collection metadata.

          include_target_metadata: Add source target metadata to each result.

          in_reply_to_tweet_id: Only replies to this tweet ID (tweet_search_extractor)

          language: Language code filter (tweet_search_extractor)

          list_id: Search within a list ID (tweet_search_extractor)

          location_contains: Required profile location text.

          max_depth: Maximum nested reply depth.

          max_followers: Maximum follower count for profile results.

          max_following: Maximum following count for profile results.

          max_id: Return Tweets older than this Tweet ID.

          max_items_per_target: Maximum results collected for each target.

          max_likes: Maximum Tweet like count.

          max_pages_per_target: Reply pages collected for each target.

          max_posts: Maximum post count for profile results.

          max_quotes: Maximum Tweet quote count.

          max_replies: Maximum Tweet reply count.

          max_retweets: Maximum Tweet repost count.

          media_type: Media type filter (tweet_search_extractor)

          mentioning: Filter tweets mentioning a username (tweet_search_extractor)

          min_account_age_days: Minimum profile age in days.

          min_bookmarks: Minimum Tweet bookmark count.

          min_faves: Minimum likes threshold (tweet_search_extractor)

          min_followers: Minimum follower count for profile results.

          min_following: Minimum following count for profile results.

          min_posts: Minimum post count for profile results.

          min_quotes: Minimum quote count threshold (tweet_search_extractor)

          min_replies: Minimum replies threshold (tweet_search_extractor)

          min_retweets: Minimum retweets threshold (tweet_search_extractor)

          min_views: Minimum Tweet view count.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          overlap_mode: Shortcut for dedupeMode=merge.

          place: Search within a place ID (tweet_search_extractor)

          place_country: Search within a country code (tweet_search_extractor)

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi (tweet_search_extractor)

          query_type: Search ranking applied to every query.

          quotes: Quote mode (tweet_search_extractor)

          quotes_of_tweet_id: Only quotes of this tweet ID (tweet_search_extractor)

          relation_targets: Profile relations processed within one job.

          replies: Reply mode (tweet_search_extractor)

          results_limit: Maximum number of results to extract. When set, the extraction stops after
              reaching this limit.

          retweets: Retweet mode (tweet_search_extractor)

          retweets_of_tweet_id: Only retweets of this tweet ID (tweet_search_extractor)

          safe: Enable the safe-search filter.

          scope: Reply depth scope.

          search_queries: Search queries processed as one collection job.

          search_query: Required for tweet_search_extractor & community_search.

          since_date: Start date YYYY-MM-DD (tweet_search_extractor)

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Reply start time as ISO 8601 or Unix seconds.

          sort: Reply result order.

          source: Match the source application.

          start_cursor: Resume one reply target from this cursor.

          target_community_id: Required for community_post_extractor & community_search.

          target_community_ids: Community IDs processed as one collection job.

          target_list_id: Required for list_follower_explorer, list_member_extractor &
              list_post_extractor.

          target_list_ids: List IDs processed as one collection job.

          targets: Mixed targets auto-routed within one job.

          target_space_id: Required for space_explorer.

          target_tweet_ids: Tweet IDs processed as one collection job.

          target_usernames: Usernames processed as one collection job.

          to_user: Filter replies sent to a username (tweet_search_extractor)

          until_date: End date YYYY-MM-DD (tweet_search_extractor)

          until_time: Reply end time as ISO 8601 or Unix seconds.

          url: URL substring or domain filter (tweet_search_extractor)

          username_contains: Required username text.

          verified_only: Only verified authors (tweet_search_extractor)

          verified_type: Exact profile verification type.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extractions/estimate",
            body=maybe_transform(
                {
                    "tool_type": tool_type,
                    "advanced_query": advanced_query,
                    "any_words": any_words,
                    "bio_contains": bio_contains,
                    "blue_verified_only": blue_verified_only,
                    "bounding_box": bounding_box,
                    "card_name": card_name,
                    "cashtags": cashtags,
                    "collection_strategy": collection_strategy,
                    "conversation_id": conversation_id,
                    "dedupe_across_targets": dedupe_across_targets,
                    "dedupe_mode": dedupe_mode,
                    "exact_phrase": exact_phrase,
                    "exclude_original_author": exclude_original_author,
                    "exclude_source": exclude_source,
                    "exclude_words": exclude_words,
                    "from_user": from_user,
                    "geocode": geocode,
                    "hashtags": hashtags,
                    "has_location": has_location,
                    "has_media_only": has_media_only,
                    "has_website": has_website,
                    "include_original_post": include_original_post,
                    "include_search_terms": include_search_terms,
                    "include_target_metadata": include_target_metadata,
                    "in_reply_to_tweet_id": in_reply_to_tweet_id,
                    "language": language,
                    "list_id": list_id,
                    "location_contains": location_contains,
                    "max_depth": max_depth,
                    "max_followers": max_followers,
                    "max_following": max_following,
                    "max_id": max_id,
                    "max_items_per_target": max_items_per_target,
                    "max_likes": max_likes,
                    "max_pages_per_target": max_pages_per_target,
                    "max_posts": max_posts,
                    "max_quotes": max_quotes,
                    "max_replies": max_replies,
                    "max_retweets": max_retweets,
                    "media_type": media_type,
                    "mentioning": mentioning,
                    "min_account_age_days": min_account_age_days,
                    "min_bookmarks": min_bookmarks,
                    "min_faves": min_faves,
                    "min_followers": min_followers,
                    "min_following": min_following,
                    "min_posts": min_posts,
                    "min_quotes": min_quotes,
                    "min_replies": min_replies,
                    "min_retweets": min_retweets,
                    "min_views": min_views,
                    "native_retweets": native_retweets,
                    "near": near,
                    "news": news,
                    "overlap_mode": overlap_mode,
                    "place": place,
                    "place_country": place_country,
                    "point_radius": point_radius,
                    "query_type": query_type,
                    "quotes": quotes,
                    "quotes_of_tweet_id": quotes_of_tweet_id,
                    "relation_targets": relation_targets,
                    "replies": replies,
                    "results_limit": results_limit,
                    "retweets": retweets,
                    "retweets_of_tweet_id": retweets_of_tweet_id,
                    "safe": safe,
                    "scope": scope,
                    "search_queries": search_queries,
                    "search_query": search_query,
                    "since_date": since_date,
                    "since_id": since_id,
                    "since_time": since_time,
                    "sort": sort,
                    "source": source,
                    "start_cursor": start_cursor,
                    "target_community_id": target_community_id,
                    "target_community_ids": target_community_ids,
                    "target_list_id": target_list_id,
                    "target_list_ids": target_list_ids,
                    "targets": targets,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_tweet_ids": target_tweet_ids,
                    "target_username": target_username,
                    "target_usernames": target_usernames,
                    "to_user": to_user,
                    "until_date": until_date,
                    "until_time": until_time,
                    "url": url,
                    "username_contains": username_contains,
                    "verified_only": verified_only,
                    "verified_type": verified_type,
                    "within": within,
                    "within_time": within_time,
                },
                extraction_estimate_cost_params.ExtractionEstimateCostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractionEstimateCostResponse,
        )

    def export_results(
        self,
        id: str,
        *,
        format: Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"],
        has_description: bool | Omit = omit,
        has_location: bool | Omit = omit,
        has_media: bool | Omit = omit,
        lang: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_posts: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_likes: int | Omit = omit,
        min_posts: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        search: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        verified: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Export extraction results

        Args:
          format: Export file format

          has_description: Require a non-empty description.

          has_location: Require a non-empty location.

          has_media: Require media.

          lang: Filter by language code.

          max_followers: Maximum follower count.

          max_following: Maximum following count.

          max_posts: Maximum post count.

          min_followers: Minimum follower count.

          min_following: Minimum following count.

          min_likes: Minimum like count.

          min_posts: Minimum post count.

          min_replies: Minimum reply count.

          min_retweets: Minimum repost count.

          min_views: Minimum view count.

          search: Search exported result text.

          since_date: Include results on or after this date.

          until_date: Include results on or before this date.

          verified: Filter by verified status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template("/extractions/{id}/export", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "has_description": has_description,
                        "has_location": has_location,
                        "has_media": has_media,
                        "lang": lang,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_posts": max_posts,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_likes": min_likes,
                        "min_posts": min_posts,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "search": search,
                        "since_date": since_date,
                        "until_date": until_date,
                        "verified": verified,
                    },
                    extraction_export_results_params.ExtractionExportResultsParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def run(
        self,
        *,
        tool_type: Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
            "favoriters",
            "follower_explorer",
            "following_explorer",
            "list_follower_explorer",
            "list_member_extractor",
            "list_post_extractor",
            "mention_extractor",
            "people_search",
            "post_extractor",
            "quote_extractor",
            "reply_extractor",
            "repost_extractor",
            "space_explorer",
            "thread_extractor",
            "tweet_search_extractor",
            "user_likes",
            "user_media",
            "verified_follower_explorer",
        ],
        dry_run: bool | Omit = omit,
        advanced_query: str | Omit = omit,
        any_words: str | Omit = omit,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        bounding_box: str | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        collection_strategy: Literal["auto", "complete", "direct", "search", "thread"] | Omit = omit,
        conversation_id: str | Omit = omit,
        dedupe_across_targets: bool | Omit = omit,
        dedupe_mode: Literal["none", "first", "merge"] | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_original_author: bool | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_media_only: bool | Omit = omit,
        has_website: bool | Omit = omit,
        include_original_post: bool | Omit = omit,
        include_search_terms: bool | Omit = omit,
        include_target_metadata: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        list_id: str | Omit = omit,
        location_contains: str | Omit = omit,
        max_depth: int | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_id: str | Omit = omit,
        max_items_per_target: int | Omit = omit,
        max_likes: int | Omit = omit,
        max_pages_per_target: int | Omit = omit,
        max_posts: int | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_faves: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_posts: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        overlap_mode: bool | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: Literal["Latest", "Top", "Both"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        relation_targets: Iterable[extraction_run_params.RelationTarget] | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        results_limit: int | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        scope: Literal["all", "direct", "nested"] | Omit = omit,
        search_queries: SequenceNotStr[str] | Omit = omit,
        search_query: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: Union[Union[str, datetime], int] | Omit = omit,
        sort: Literal["relevance", "latest", "oldest", "likes"] | Omit = omit,
        source: str | Omit = omit,
        start_cursor: str | Omit = omit,
        target_community_id: str | Omit = omit,
        target_community_ids: SequenceNotStr[str] | Omit = omit,
        target_list_id: str | Omit = omit,
        target_list_ids: SequenceNotStr[str] | Omit = omit,
        targets: SequenceNotStr[extraction_run_params.Target] | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_tweet_ids: SequenceNotStr[str] | Omit = omit,
        target_username: str | Omit = omit,
        target_usernames: SequenceNotStr[str] | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: Union[Union[str, datetime], int] | Omit = omit,
        url: str | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionRunResponse:
        """
        Run extraction

        Args:
          tool_type: Identifier for the extraction tool used to run a job.

          dry_run: Estimate cost without creating an extraction.

          advanced_query: Raw advanced search query appended as-is (tweet_search_extractor)

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines. (tweet_search_extractor)

          bio_contains: Bio terms separated by commas or lines.

          blue_verified_only: Return only Blue-verified Tweet authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8 (tweet_search_extractor)

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          collection_strategy: Reply collection strategy.

          conversation_id: Conversation ID filter (tweet_search_extractor)

          dedupe_across_targets: Merge duplicate results across collection targets.

          dedupe_mode: Keep target duplicates, first rows, or merged overlap.

          exact_phrase: Exact phrase to match (tweet_search_extractor)

          exclude_original_author: Exclude replies from the source author.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.
              (tweet_search_extractor)

          from_user: Filter by author username (tweet_search_extractor)

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          has_location: Require a profile location.

          has_media_only: Return only replies with media.

          has_website: Require a profile website.

          include_original_post: Include the source post in reply results.

          include_search_terms: Add matching search terms to collection metadata.

          include_target_metadata: Add source target metadata to each result.

          in_reply_to_tweet_id: Only replies to this tweet ID (tweet_search_extractor)

          language: Language code filter (tweet_search_extractor)

          list_id: Search within a list ID (tweet_search_extractor)

          location_contains: Required profile location text.

          max_depth: Maximum nested reply depth.

          max_followers: Maximum follower count for profile results.

          max_following: Maximum following count for profile results.

          max_id: Return Tweets older than this Tweet ID.

          max_items_per_target: Maximum results collected for each target.

          max_likes: Maximum Tweet like count.

          max_pages_per_target: Reply pages collected for each target.

          max_posts: Maximum post count for profile results.

          max_quotes: Maximum Tweet quote count.

          max_replies: Maximum Tweet reply count.

          max_retweets: Maximum Tweet repost count.

          media_type: Media type filter (tweet_search_extractor)

          mentioning: Filter tweets mentioning a username (tweet_search_extractor)

          min_account_age_days: Minimum profile age in days.

          min_bookmarks: Minimum Tweet bookmark count.

          min_faves: Minimum likes threshold (tweet_search_extractor)

          min_followers: Minimum follower count for profile results.

          min_following: Minimum following count for profile results.

          min_posts: Minimum post count for profile results.

          min_quotes: Minimum quote count threshold (tweet_search_extractor)

          min_replies: Minimum replies threshold (tweet_search_extractor)

          min_retweets: Minimum retweets threshold (tweet_search_extractor)

          min_views: Minimum Tweet view count.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          overlap_mode: Shortcut for dedupeMode=merge.

          place: Search within a place ID (tweet_search_extractor)

          place_country: Search within a country code (tweet_search_extractor)

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi (tweet_search_extractor)

          query_type: Search ranking applied to every query.

          quotes: Quote mode (tweet_search_extractor)

          quotes_of_tweet_id: Only quotes of this tweet ID (tweet_search_extractor)

          relation_targets: Profile relations processed within one job.

          replies: Reply mode (tweet_search_extractor)

          results_limit: Maximum number of results to extract. When set, the extraction stops after
              reaching this limit.

          retweets: Retweet mode (tweet_search_extractor)

          retweets_of_tweet_id: Only retweets of this tweet ID (tweet_search_extractor)

          safe: Enable the safe-search filter.

          scope: Reply depth scope.

          search_queries: Search queries processed as one collection job.

          search_query: Required for tweet_search_extractor & community_search.

          since_date: Start date YYYY-MM-DD (tweet_search_extractor)

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Reply start time as ISO 8601 or Unix seconds.

          sort: Reply result order.

          source: Match the source application.

          start_cursor: Resume one reply target from this cursor.

          target_community_id: Required for community_post_extractor & community_search.

          target_community_ids: Community IDs processed as one collection job.

          target_list_id: Required for list_follower_explorer, list_member_extractor &
              list_post_extractor.

          target_list_ids: List IDs processed as one collection job.

          targets: Mixed targets auto-routed within one job.

          target_space_id: Required for space_explorer.

          target_tweet_ids: Tweet IDs processed as one collection job.

          target_usernames: Usernames processed as one collection job.

          to_user: Filter replies sent to a username (tweet_search_extractor)

          until_date: End date YYYY-MM-DD (tweet_search_extractor)

          until_time: Reply end time as ISO 8601 or Unix seconds.

          url: URL substring or domain filter (tweet_search_extractor)

          username_contains: Required username text.

          verified_only: Only verified authors (tweet_search_extractor)

          verified_type: Exact profile verification type.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/extractions",
            body=maybe_transform(
                {
                    "tool_type": tool_type,
                    "advanced_query": advanced_query,
                    "any_words": any_words,
                    "bio_contains": bio_contains,
                    "blue_verified_only": blue_verified_only,
                    "bounding_box": bounding_box,
                    "card_name": card_name,
                    "cashtags": cashtags,
                    "collection_strategy": collection_strategy,
                    "conversation_id": conversation_id,
                    "dedupe_across_targets": dedupe_across_targets,
                    "dedupe_mode": dedupe_mode,
                    "exact_phrase": exact_phrase,
                    "exclude_original_author": exclude_original_author,
                    "exclude_source": exclude_source,
                    "exclude_words": exclude_words,
                    "from_user": from_user,
                    "geocode": geocode,
                    "hashtags": hashtags,
                    "has_location": has_location,
                    "has_media_only": has_media_only,
                    "has_website": has_website,
                    "include_original_post": include_original_post,
                    "include_search_terms": include_search_terms,
                    "include_target_metadata": include_target_metadata,
                    "in_reply_to_tweet_id": in_reply_to_tweet_id,
                    "language": language,
                    "list_id": list_id,
                    "location_contains": location_contains,
                    "max_depth": max_depth,
                    "max_followers": max_followers,
                    "max_following": max_following,
                    "max_id": max_id,
                    "max_items_per_target": max_items_per_target,
                    "max_likes": max_likes,
                    "max_pages_per_target": max_pages_per_target,
                    "max_posts": max_posts,
                    "max_quotes": max_quotes,
                    "max_replies": max_replies,
                    "max_retweets": max_retweets,
                    "media_type": media_type,
                    "mentioning": mentioning,
                    "min_account_age_days": min_account_age_days,
                    "min_bookmarks": min_bookmarks,
                    "min_faves": min_faves,
                    "min_followers": min_followers,
                    "min_following": min_following,
                    "min_posts": min_posts,
                    "min_quotes": min_quotes,
                    "min_replies": min_replies,
                    "min_retweets": min_retweets,
                    "min_views": min_views,
                    "native_retweets": native_retweets,
                    "near": near,
                    "news": news,
                    "overlap_mode": overlap_mode,
                    "place": place,
                    "place_country": place_country,
                    "point_radius": point_radius,
                    "query_type": query_type,
                    "quotes": quotes,
                    "quotes_of_tweet_id": quotes_of_tweet_id,
                    "relation_targets": relation_targets,
                    "replies": replies,
                    "results_limit": results_limit,
                    "retweets": retweets,
                    "retweets_of_tweet_id": retweets_of_tweet_id,
                    "safe": safe,
                    "scope": scope,
                    "search_queries": search_queries,
                    "search_query": search_query,
                    "since_date": since_date,
                    "since_id": since_id,
                    "since_time": since_time,
                    "sort": sort,
                    "source": source,
                    "start_cursor": start_cursor,
                    "target_community_id": target_community_id,
                    "target_community_ids": target_community_ids,
                    "target_list_id": target_list_id,
                    "target_list_ids": target_list_ids,
                    "targets": targets,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_tweet_ids": target_tweet_ids,
                    "target_username": target_username,
                    "target_usernames": target_usernames,
                    "to_user": to_user,
                    "until_date": until_date,
                    "until_time": until_time,
                    "url": url,
                    "username_contains": username_contains,
                    "verified_only": verified_only,
                    "verified_type": verified_type,
                    "within": within,
                    "within_time": within_time,
                },
                extraction_run_params.ExtractionRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"dry_run": dry_run}, extraction_run_params.ExtractionRunParams),
            ),
            cast_to=ExtractionRunResponse,
        )


class AsyncExtractionsResource(AsyncAPIResource):
    """Bulk data extraction (23 tool types)"""

    @cached_property
    def with_raw_response(self) -> AsyncExtractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncExtractionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        field_style: Literal["source", "camelCase", "snake_case"] | Omit = omit,
        include_raw: bool | Omit = omit,
        limit: int | Omit = omit,
        output_mode: Literal["compact", "full", "raw"] | Omit = omit,
        output_preset: Literal["nested", "flat"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionRetrieveResponse:
        """
        Get extraction results

        Args:
          cursor: Previous nextCursor.

          field_style: Preserve source keys or convert result field names.

          include_raw: Use outputMode=raw instead.

          limit: Maximum number of results to return (1-1000, default 100)

          output_mode: Select compact, full, or raw-compatible result fields.

          output_preset: Keep enrichment nested or merge it into each result.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/extractions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "field_style": field_style,
                        "include_raw": include_raw,
                        "limit": limit,
                        "output_mode": output_mode,
                        "output_preset": output_preset,
                    },
                    extraction_retrieve_params.ExtractionRetrieveParams,
                ),
            ),
            cast_to=ExtractionRetrieveResponse,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        tool_type: Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
            "favoriters",
            "follower_explorer",
            "following_explorer",
            "list_follower_explorer",
            "list_member_extractor",
            "list_post_extractor",
            "mention_extractor",
            "people_search",
            "post_extractor",
            "quote_extractor",
            "reply_extractor",
            "repost_extractor",
            "space_explorer",
            "thread_extractor",
            "tweet_search_extractor",
            "user_likes",
            "user_media",
            "verified_follower_explorer",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionListResponse:
        """
        List extraction jobs

        Args:
          cursor: Previous nextCursor.

          limit: Maximum number of items to return (1-100, default 50). For paid per-result
              endpoints, the returned count may be lower when remaining credits cannot cover
              the requested page. If zero paid results are affordable, the endpoint returns
              402 insufficient_credits.

          status: Filter by job status

          tool_type: Filter by extraction tool type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/extractions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "tool_type": tool_type,
                    },
                    extraction_list_params.ExtractionListParams,
                ),
            ),
            cast_to=ExtractionListResponse,
        )

    async def estimate_cost(
        self,
        *,
        tool_type: Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
            "favoriters",
            "follower_explorer",
            "following_explorer",
            "list_follower_explorer",
            "list_member_extractor",
            "list_post_extractor",
            "mention_extractor",
            "people_search",
            "post_extractor",
            "quote_extractor",
            "reply_extractor",
            "repost_extractor",
            "space_explorer",
            "thread_extractor",
            "tweet_search_extractor",
            "user_likes",
            "user_media",
            "verified_follower_explorer",
        ],
        advanced_query: str | Omit = omit,
        any_words: str | Omit = omit,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        bounding_box: str | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        collection_strategy: Literal["auto", "complete", "direct", "search", "thread"] | Omit = omit,
        conversation_id: str | Omit = omit,
        dedupe_across_targets: bool | Omit = omit,
        dedupe_mode: Literal["none", "first", "merge"] | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_original_author: bool | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_media_only: bool | Omit = omit,
        has_website: bool | Omit = omit,
        include_original_post: bool | Omit = omit,
        include_search_terms: bool | Omit = omit,
        include_target_metadata: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        list_id: str | Omit = omit,
        location_contains: str | Omit = omit,
        max_depth: int | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_id: str | Omit = omit,
        max_items_per_target: int | Omit = omit,
        max_likes: int | Omit = omit,
        max_pages_per_target: int | Omit = omit,
        max_posts: int | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_faves: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_posts: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        overlap_mode: bool | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: Literal["Latest", "Top", "Both"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        relation_targets: Iterable[extraction_estimate_cost_params.RelationTarget] | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        results_limit: int | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        scope: Literal["all", "direct", "nested"] | Omit = omit,
        search_queries: SequenceNotStr[str] | Omit = omit,
        search_query: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: Union[Union[str, datetime], int] | Omit = omit,
        sort: Literal["relevance", "latest", "oldest", "likes"] | Omit = omit,
        source: str | Omit = omit,
        start_cursor: str | Omit = omit,
        target_community_id: str | Omit = omit,
        target_community_ids: SequenceNotStr[str] | Omit = omit,
        target_list_id: str | Omit = omit,
        target_list_ids: SequenceNotStr[str] | Omit = omit,
        targets: SequenceNotStr[extraction_estimate_cost_params.Target] | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_tweet_ids: SequenceNotStr[str] | Omit = omit,
        target_username: str | Omit = omit,
        target_usernames: SequenceNotStr[str] | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: Union[Union[str, datetime], int] | Omit = omit,
        url: str | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionEstimateCostResponse:
        """
        Estimate extraction cost

        Args:
          tool_type: Identifier for the extraction tool used to run a job.

          advanced_query: Raw advanced search query appended as-is (tweet_search_extractor)

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines. (tweet_search_extractor)

          bio_contains: Bio terms separated by commas or lines.

          blue_verified_only: Return only Blue-verified Tweet authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8 (tweet_search_extractor)

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          collection_strategy: Reply collection strategy.

          conversation_id: Conversation ID filter (tweet_search_extractor)

          dedupe_across_targets: Merge duplicate results across collection targets.

          dedupe_mode: Keep target duplicates, first rows, or merged overlap.

          exact_phrase: Exact phrase to match (tweet_search_extractor)

          exclude_original_author: Exclude replies from the source author.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.
              (tweet_search_extractor)

          from_user: Filter by author username (tweet_search_extractor)

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          has_location: Require a profile location.

          has_media_only: Return only replies with media.

          has_website: Require a profile website.

          include_original_post: Include the source post in reply results.

          include_search_terms: Add matching search terms to collection metadata.

          include_target_metadata: Add source target metadata to each result.

          in_reply_to_tweet_id: Only replies to this tweet ID (tweet_search_extractor)

          language: Language code filter (tweet_search_extractor)

          list_id: Search within a list ID (tweet_search_extractor)

          location_contains: Required profile location text.

          max_depth: Maximum nested reply depth.

          max_followers: Maximum follower count for profile results.

          max_following: Maximum following count for profile results.

          max_id: Return Tweets older than this Tweet ID.

          max_items_per_target: Maximum results collected for each target.

          max_likes: Maximum Tweet like count.

          max_pages_per_target: Reply pages collected for each target.

          max_posts: Maximum post count for profile results.

          max_quotes: Maximum Tweet quote count.

          max_replies: Maximum Tweet reply count.

          max_retweets: Maximum Tweet repost count.

          media_type: Media type filter (tweet_search_extractor)

          mentioning: Filter tweets mentioning a username (tweet_search_extractor)

          min_account_age_days: Minimum profile age in days.

          min_bookmarks: Minimum Tweet bookmark count.

          min_faves: Minimum likes threshold (tweet_search_extractor)

          min_followers: Minimum follower count for profile results.

          min_following: Minimum following count for profile results.

          min_posts: Minimum post count for profile results.

          min_quotes: Minimum quote count threshold (tweet_search_extractor)

          min_replies: Minimum replies threshold (tweet_search_extractor)

          min_retweets: Minimum retweets threshold (tweet_search_extractor)

          min_views: Minimum Tweet view count.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          overlap_mode: Shortcut for dedupeMode=merge.

          place: Search within a place ID (tweet_search_extractor)

          place_country: Search within a country code (tweet_search_extractor)

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi (tweet_search_extractor)

          query_type: Search ranking applied to every query.

          quotes: Quote mode (tweet_search_extractor)

          quotes_of_tweet_id: Only quotes of this tweet ID (tweet_search_extractor)

          relation_targets: Profile relations processed within one job.

          replies: Reply mode (tweet_search_extractor)

          results_limit: Maximum number of results to extract. When set, the extraction stops after
              reaching this limit.

          retweets: Retweet mode (tweet_search_extractor)

          retweets_of_tweet_id: Only retweets of this tweet ID (tweet_search_extractor)

          safe: Enable the safe-search filter.

          scope: Reply depth scope.

          search_queries: Search queries processed as one collection job.

          search_query: Required for tweet_search_extractor & community_search.

          since_date: Start date YYYY-MM-DD (tweet_search_extractor)

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Reply start time as ISO 8601 or Unix seconds.

          sort: Reply result order.

          source: Match the source application.

          start_cursor: Resume one reply target from this cursor.

          target_community_id: Required for community_post_extractor & community_search.

          target_community_ids: Community IDs processed as one collection job.

          target_list_id: Required for list_follower_explorer, list_member_extractor &
              list_post_extractor.

          target_list_ids: List IDs processed as one collection job.

          targets: Mixed targets auto-routed within one job.

          target_space_id: Required for space_explorer.

          target_tweet_ids: Tweet IDs processed as one collection job.

          target_usernames: Usernames processed as one collection job.

          to_user: Filter replies sent to a username (tweet_search_extractor)

          until_date: End date YYYY-MM-DD (tweet_search_extractor)

          until_time: Reply end time as ISO 8601 or Unix seconds.

          url: URL substring or domain filter (tweet_search_extractor)

          username_contains: Required username text.

          verified_only: Only verified authors (tweet_search_extractor)

          verified_type: Exact profile verification type.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extractions/estimate",
            body=await async_maybe_transform(
                {
                    "tool_type": tool_type,
                    "advanced_query": advanced_query,
                    "any_words": any_words,
                    "bio_contains": bio_contains,
                    "blue_verified_only": blue_verified_only,
                    "bounding_box": bounding_box,
                    "card_name": card_name,
                    "cashtags": cashtags,
                    "collection_strategy": collection_strategy,
                    "conversation_id": conversation_id,
                    "dedupe_across_targets": dedupe_across_targets,
                    "dedupe_mode": dedupe_mode,
                    "exact_phrase": exact_phrase,
                    "exclude_original_author": exclude_original_author,
                    "exclude_source": exclude_source,
                    "exclude_words": exclude_words,
                    "from_user": from_user,
                    "geocode": geocode,
                    "hashtags": hashtags,
                    "has_location": has_location,
                    "has_media_only": has_media_only,
                    "has_website": has_website,
                    "include_original_post": include_original_post,
                    "include_search_terms": include_search_terms,
                    "include_target_metadata": include_target_metadata,
                    "in_reply_to_tweet_id": in_reply_to_tweet_id,
                    "language": language,
                    "list_id": list_id,
                    "location_contains": location_contains,
                    "max_depth": max_depth,
                    "max_followers": max_followers,
                    "max_following": max_following,
                    "max_id": max_id,
                    "max_items_per_target": max_items_per_target,
                    "max_likes": max_likes,
                    "max_pages_per_target": max_pages_per_target,
                    "max_posts": max_posts,
                    "max_quotes": max_quotes,
                    "max_replies": max_replies,
                    "max_retweets": max_retweets,
                    "media_type": media_type,
                    "mentioning": mentioning,
                    "min_account_age_days": min_account_age_days,
                    "min_bookmarks": min_bookmarks,
                    "min_faves": min_faves,
                    "min_followers": min_followers,
                    "min_following": min_following,
                    "min_posts": min_posts,
                    "min_quotes": min_quotes,
                    "min_replies": min_replies,
                    "min_retweets": min_retweets,
                    "min_views": min_views,
                    "native_retweets": native_retweets,
                    "near": near,
                    "news": news,
                    "overlap_mode": overlap_mode,
                    "place": place,
                    "place_country": place_country,
                    "point_radius": point_radius,
                    "query_type": query_type,
                    "quotes": quotes,
                    "quotes_of_tweet_id": quotes_of_tweet_id,
                    "relation_targets": relation_targets,
                    "replies": replies,
                    "results_limit": results_limit,
                    "retweets": retweets,
                    "retweets_of_tweet_id": retweets_of_tweet_id,
                    "safe": safe,
                    "scope": scope,
                    "search_queries": search_queries,
                    "search_query": search_query,
                    "since_date": since_date,
                    "since_id": since_id,
                    "since_time": since_time,
                    "sort": sort,
                    "source": source,
                    "start_cursor": start_cursor,
                    "target_community_id": target_community_id,
                    "target_community_ids": target_community_ids,
                    "target_list_id": target_list_id,
                    "target_list_ids": target_list_ids,
                    "targets": targets,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_tweet_ids": target_tweet_ids,
                    "target_username": target_username,
                    "target_usernames": target_usernames,
                    "to_user": to_user,
                    "until_date": until_date,
                    "until_time": until_time,
                    "url": url,
                    "username_contains": username_contains,
                    "verified_only": verified_only,
                    "verified_type": verified_type,
                    "within": within,
                    "within_time": within_time,
                },
                extraction_estimate_cost_params.ExtractionEstimateCostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractionEstimateCostResponse,
        )

    async def export_results(
        self,
        id: str,
        *,
        format: Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"],
        has_description: bool | Omit = omit,
        has_location: bool | Omit = omit,
        has_media: bool | Omit = omit,
        lang: str | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_posts: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_likes: int | Omit = omit,
        min_posts: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        search: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        verified: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Export extraction results

        Args:
          format: Export file format

          has_description: Require a non-empty description.

          has_location: Require a non-empty location.

          has_media: Require media.

          lang: Filter by language code.

          max_followers: Maximum follower count.

          max_following: Maximum following count.

          max_posts: Maximum post count.

          min_followers: Minimum follower count.

          min_following: Minimum following count.

          min_likes: Minimum like count.

          min_posts: Minimum post count.

          min_replies: Minimum reply count.

          min_retweets: Minimum repost count.

          min_views: Minimum view count.

          search: Search exported result text.

          since_date: Include results on or after this date.

          until_date: Include results on or before this date.

          verified: Filter by verified status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/extractions/{id}/export", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "has_description": has_description,
                        "has_location": has_location,
                        "has_media": has_media,
                        "lang": lang,
                        "max_followers": max_followers,
                        "max_following": max_following,
                        "max_posts": max_posts,
                        "min_followers": min_followers,
                        "min_following": min_following,
                        "min_likes": min_likes,
                        "min_posts": min_posts,
                        "min_replies": min_replies,
                        "min_retweets": min_retweets,
                        "min_views": min_views,
                        "search": search,
                        "since_date": since_date,
                        "until_date": until_date,
                        "verified": verified,
                    },
                    extraction_export_results_params.ExtractionExportResultsParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def run(
        self,
        *,
        tool_type: Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
            "favoriters",
            "follower_explorer",
            "following_explorer",
            "list_follower_explorer",
            "list_member_extractor",
            "list_post_extractor",
            "mention_extractor",
            "people_search",
            "post_extractor",
            "quote_extractor",
            "reply_extractor",
            "repost_extractor",
            "space_explorer",
            "thread_extractor",
            "tweet_search_extractor",
            "user_likes",
            "user_media",
            "verified_follower_explorer",
        ],
        dry_run: bool | Omit = omit,
        advanced_query: str | Omit = omit,
        any_words: str | Omit = omit,
        bio_contains: str | Omit = omit,
        blue_verified_only: bool | Omit = omit,
        bounding_box: str | Omit = omit,
        card_name: str | Omit = omit,
        cashtags: str | Omit = omit,
        collection_strategy: Literal["auto", "complete", "direct", "search", "thread"] | Omit = omit,
        conversation_id: str | Omit = omit,
        dedupe_across_targets: bool | Omit = omit,
        dedupe_mode: Literal["none", "first", "merge"] | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_original_author: bool | Omit = omit,
        exclude_source: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        geocode: str | Omit = omit,
        hashtags: str | Omit = omit,
        has_location: bool | Omit = omit,
        has_media_only: bool | Omit = omit,
        has_website: bool | Omit = omit,
        include_original_post: bool | Omit = omit,
        include_search_terms: bool | Omit = omit,
        include_target_metadata: bool | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        list_id: str | Omit = omit,
        location_contains: str | Omit = omit,
        max_depth: int | Omit = omit,
        max_followers: int | Omit = omit,
        max_following: int | Omit = omit,
        max_id: str | Omit = omit,
        max_items_per_target: int | Omit = omit,
        max_likes: int | Omit = omit,
        max_pages_per_target: int | Omit = omit,
        max_posts: int | Omit = omit,
        max_quotes: int | Omit = omit,
        max_replies: int | Omit = omit,
        max_retweets: int | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_account_age_days: int | Omit = omit,
        min_bookmarks: int | Omit = omit,
        min_faves: int | Omit = omit,
        min_followers: int | Omit = omit,
        min_following: int | Omit = omit,
        min_posts: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        min_views: int | Omit = omit,
        native_retweets: bool | Omit = omit,
        near: str | Omit = omit,
        news: bool | Omit = omit,
        overlap_mode: bool | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        query_type: Literal["Latest", "Top", "Both"] | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        relation_targets: Iterable[extraction_run_params.RelationTarget] | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        results_limit: int | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        safe: bool | Omit = omit,
        scope: Literal["all", "direct", "nested"] | Omit = omit,
        search_queries: SequenceNotStr[str] | Omit = omit,
        search_query: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        since_id: str | Omit = omit,
        since_time: Union[Union[str, datetime], int] | Omit = omit,
        sort: Literal["relevance", "latest", "oldest", "likes"] | Omit = omit,
        source: str | Omit = omit,
        start_cursor: str | Omit = omit,
        target_community_id: str | Omit = omit,
        target_community_ids: SequenceNotStr[str] | Omit = omit,
        target_list_id: str | Omit = omit,
        target_list_ids: SequenceNotStr[str] | Omit = omit,
        targets: SequenceNotStr[extraction_run_params.Target] | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_tweet_ids: SequenceNotStr[str] | Omit = omit,
        target_username: str | Omit = omit,
        target_usernames: SequenceNotStr[str] | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        until_time: Union[Union[str, datetime], int] | Omit = omit,
        url: str | Omit = omit,
        username_contains: str | Omit = omit,
        verified_only: bool | Omit = omit,
        verified_type: str | Omit = omit,
        within: str | Omit = omit,
        within_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractionRunResponse:
        """
        Run extraction

        Args:
          tool_type: Identifier for the extraction tool used to run a job.

          dry_run: Estimate cost without creating an extraction.

          advanced_query: Raw advanced search query appended as-is (tweet_search_extractor)

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines. (tweet_search_extractor)

          bio_contains: Bio terms separated by commas or lines.

          blue_verified_only: Return only Blue-verified Tweet authors.

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8 (tweet_search_extractor)

          card_name: Match the Tweet card name.

          cashtags: Cashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          collection_strategy: Reply collection strategy.

          conversation_id: Conversation ID filter (tweet_search_extractor)

          dedupe_across_targets: Merge duplicate results across collection targets.

          dedupe_mode: Keep target duplicates, first rows, or merged overlap.

          exact_phrase: Exact phrase to match (tweet_search_extractor)

          exclude_original_author: Exclude replies from the source author.

          exclude_source: Exclude a source application.

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.
              (tweet_search_extractor)

          from_user: Filter by author username (tweet_search_extractor)

          geocode: Match latitude, longitude, and radius.

          hashtags: Hashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          has_location: Require a profile location.

          has_media_only: Return only replies with media.

          has_website: Require a profile website.

          include_original_post: Include the source post in reply results.

          include_search_terms: Add matching search terms to collection metadata.

          include_target_metadata: Add source target metadata to each result.

          in_reply_to_tweet_id: Only replies to this tweet ID (tweet_search_extractor)

          language: Language code filter (tweet_search_extractor)

          list_id: Search within a list ID (tweet_search_extractor)

          location_contains: Required profile location text.

          max_depth: Maximum nested reply depth.

          max_followers: Maximum follower count for profile results.

          max_following: Maximum following count for profile results.

          max_id: Return Tweets older than this Tweet ID.

          max_items_per_target: Maximum results collected for each target.

          max_likes: Maximum Tweet like count.

          max_pages_per_target: Reply pages collected for each target.

          max_posts: Maximum post count for profile results.

          max_quotes: Maximum Tweet quote count.

          max_replies: Maximum Tweet reply count.

          max_retweets: Maximum Tweet repost count.

          media_type: Media type filter (tweet_search_extractor)

          mentioning: Filter tweets mentioning a username (tweet_search_extractor)

          min_account_age_days: Minimum profile age in days.

          min_bookmarks: Minimum Tweet bookmark count.

          min_faves: Minimum likes threshold (tweet_search_extractor)

          min_followers: Minimum follower count for profile results.

          min_following: Minimum following count for profile results.

          min_posts: Minimum post count for profile results.

          min_quotes: Minimum quote count threshold (tweet_search_extractor)

          min_replies: Minimum replies threshold (tweet_search_extractor)

          min_retweets: Minimum retweets threshold (tweet_search_extractor)

          min_views: Minimum Tweet view count.

          native_retweets: Only return native reposts.

          near: Match a place name.

          news: Only return news results.

          overlap_mode: Shortcut for dedupeMode=merge.

          place: Search within a place ID (tweet_search_extractor)

          place_country: Search within a country code (tweet_search_extractor)

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi (tweet_search_extractor)

          query_type: Search ranking applied to every query.

          quotes: Quote mode (tweet_search_extractor)

          quotes_of_tweet_id: Only quotes of this tweet ID (tweet_search_extractor)

          relation_targets: Profile relations processed within one job.

          replies: Reply mode (tweet_search_extractor)

          results_limit: Maximum number of results to extract. When set, the extraction stops after
              reaching this limit.

          retweets: Retweet mode (tweet_search_extractor)

          retweets_of_tweet_id: Only retweets of this tweet ID (tweet_search_extractor)

          safe: Enable the safe-search filter.

          scope: Reply depth scope.

          search_queries: Search queries processed as one collection job.

          search_query: Required for tweet_search_extractor & community_search.

          since_date: Start date YYYY-MM-DD (tweet_search_extractor)

          since_id: Return Tweets newer than this Tweet ID.

          since_time: Reply start time as ISO 8601 or Unix seconds.

          sort: Reply result order.

          source: Match the source application.

          start_cursor: Resume one reply target from this cursor.

          target_community_id: Required for community_post_extractor & community_search.

          target_community_ids: Community IDs processed as one collection job.

          target_list_id: Required for list_follower_explorer, list_member_extractor &
              list_post_extractor.

          target_list_ids: List IDs processed as one collection job.

          targets: Mixed targets auto-routed within one job.

          target_space_id: Required for space_explorer.

          target_tweet_ids: Tweet IDs processed as one collection job.

          target_usernames: Usernames processed as one collection job.

          to_user: Filter replies sent to a username (tweet_search_extractor)

          until_date: End date YYYY-MM-DD (tweet_search_extractor)

          until_time: Reply end time as ISO 8601 or Unix seconds.

          url: URL substring or domain filter (tweet_search_extractor)

          username_contains: Required username text.

          verified_only: Only verified authors (tweet_search_extractor)

          verified_type: Exact profile verification type.

          within: Set the radius for the near filter.

          within_time: Match Tweets inside a recent time window.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/extractions",
            body=await async_maybe_transform(
                {
                    "tool_type": tool_type,
                    "advanced_query": advanced_query,
                    "any_words": any_words,
                    "bio_contains": bio_contains,
                    "blue_verified_only": blue_verified_only,
                    "bounding_box": bounding_box,
                    "card_name": card_name,
                    "cashtags": cashtags,
                    "collection_strategy": collection_strategy,
                    "conversation_id": conversation_id,
                    "dedupe_across_targets": dedupe_across_targets,
                    "dedupe_mode": dedupe_mode,
                    "exact_phrase": exact_phrase,
                    "exclude_original_author": exclude_original_author,
                    "exclude_source": exclude_source,
                    "exclude_words": exclude_words,
                    "from_user": from_user,
                    "geocode": geocode,
                    "hashtags": hashtags,
                    "has_location": has_location,
                    "has_media_only": has_media_only,
                    "has_website": has_website,
                    "include_original_post": include_original_post,
                    "include_search_terms": include_search_terms,
                    "include_target_metadata": include_target_metadata,
                    "in_reply_to_tweet_id": in_reply_to_tweet_id,
                    "language": language,
                    "list_id": list_id,
                    "location_contains": location_contains,
                    "max_depth": max_depth,
                    "max_followers": max_followers,
                    "max_following": max_following,
                    "max_id": max_id,
                    "max_items_per_target": max_items_per_target,
                    "max_likes": max_likes,
                    "max_pages_per_target": max_pages_per_target,
                    "max_posts": max_posts,
                    "max_quotes": max_quotes,
                    "max_replies": max_replies,
                    "max_retweets": max_retweets,
                    "media_type": media_type,
                    "mentioning": mentioning,
                    "min_account_age_days": min_account_age_days,
                    "min_bookmarks": min_bookmarks,
                    "min_faves": min_faves,
                    "min_followers": min_followers,
                    "min_following": min_following,
                    "min_posts": min_posts,
                    "min_quotes": min_quotes,
                    "min_replies": min_replies,
                    "min_retweets": min_retweets,
                    "min_views": min_views,
                    "native_retweets": native_retweets,
                    "near": near,
                    "news": news,
                    "overlap_mode": overlap_mode,
                    "place": place,
                    "place_country": place_country,
                    "point_radius": point_radius,
                    "query_type": query_type,
                    "quotes": quotes,
                    "quotes_of_tweet_id": quotes_of_tweet_id,
                    "relation_targets": relation_targets,
                    "replies": replies,
                    "results_limit": results_limit,
                    "retweets": retweets,
                    "retweets_of_tweet_id": retweets_of_tweet_id,
                    "safe": safe,
                    "scope": scope,
                    "search_queries": search_queries,
                    "search_query": search_query,
                    "since_date": since_date,
                    "since_id": since_id,
                    "since_time": since_time,
                    "sort": sort,
                    "source": source,
                    "start_cursor": start_cursor,
                    "target_community_id": target_community_id,
                    "target_community_ids": target_community_ids,
                    "target_list_id": target_list_id,
                    "target_list_ids": target_list_ids,
                    "targets": targets,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_tweet_ids": target_tweet_ids,
                    "target_username": target_username,
                    "target_usernames": target_usernames,
                    "to_user": to_user,
                    "until_date": until_date,
                    "until_time": until_time,
                    "url": url,
                    "username_contains": username_contains,
                    "verified_only": verified_only,
                    "verified_type": verified_type,
                    "within": within,
                    "within_time": within_time,
                },
                extraction_run_params.ExtractionRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"dry_run": dry_run}, extraction_run_params.ExtractionRunParams),
            ),
            cast_to=ExtractionRunResponse,
        )


class ExtractionsResourceWithRawResponse:
    def __init__(self, extractions: ExtractionsResource) -> None:
        self._extractions = extractions

        self.retrieve = to_raw_response_wrapper(
            extractions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            extractions.list,
        )
        self.estimate_cost = to_raw_response_wrapper(
            extractions.estimate_cost,
        )
        self.export_results = to_custom_raw_response_wrapper(
            extractions.export_results,
            BinaryAPIResponse,
        )
        self.run = to_raw_response_wrapper(
            extractions.run,
        )


class AsyncExtractionsResourceWithRawResponse:
    def __init__(self, extractions: AsyncExtractionsResource) -> None:
        self._extractions = extractions

        self.retrieve = async_to_raw_response_wrapper(
            extractions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            extractions.list,
        )
        self.estimate_cost = async_to_raw_response_wrapper(
            extractions.estimate_cost,
        )
        self.export_results = async_to_custom_raw_response_wrapper(
            extractions.export_results,
            AsyncBinaryAPIResponse,
        )
        self.run = async_to_raw_response_wrapper(
            extractions.run,
        )


class ExtractionsResourceWithStreamingResponse:
    def __init__(self, extractions: ExtractionsResource) -> None:
        self._extractions = extractions

        self.retrieve = to_streamed_response_wrapper(
            extractions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            extractions.list,
        )
        self.estimate_cost = to_streamed_response_wrapper(
            extractions.estimate_cost,
        )
        self.export_results = to_custom_streamed_response_wrapper(
            extractions.export_results,
            StreamedBinaryAPIResponse,
        )
        self.run = to_streamed_response_wrapper(
            extractions.run,
        )


class AsyncExtractionsResourceWithStreamingResponse:
    def __init__(self, extractions: AsyncExtractionsResource) -> None:
        self._extractions = extractions

        self.retrieve = async_to_streamed_response_wrapper(
            extractions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            extractions.list,
        )
        self.estimate_cost = async_to_streamed_response_wrapper(
            extractions.estimate_cost,
        )
        self.export_results = async_to_custom_streamed_response_wrapper(
            extractions.export_results,
            AsyncStreamedBinaryAPIResponse,
        )
        self.run = async_to_streamed_response_wrapper(
            extractions.run,
        )
