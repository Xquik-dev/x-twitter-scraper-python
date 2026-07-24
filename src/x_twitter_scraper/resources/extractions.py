# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import (
    extraction_run_params,
    extraction_list_params,
    extraction_retrieve_params,
    extraction_estimate_cost_params,
    extraction_export_results_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
        limit: int | Omit = omit,
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
          cursor: Cursor for keyset pagination from prior response next_cursor

          limit: Maximum number of results to return (1-1000, default 100)

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
                        "limit": limit,
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
          cursor: Cursor for keyset pagination from prior response next_cursor

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
        bounding_box: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        list_id: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        results_limit: int | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        search_query: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        target_community_id: str | Omit = omit,
        target_list_id: str | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_username: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
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

          advanced_query: Raw advanced query string appended to the estimate (tweet_search_extractor)

          any_words: Alternative words or quoted phrases for estimated results. Separate with spaces,
              commas, or lines.

          bounding_box: Geo bounding box used for estimation, e.g. -74.1 40.6 -73.9 40.8
              (tweet_search_extractor)

          cashtags: Cashtags applied to the estimate, separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter used for estimation (tweet_search_extractor)

          exact_phrase: Exact phrase filter for search estimation

          exclude_words: Words or quoted phrases excluded from estimated results. Separate with spaces,
              commas, or lines.

          from_user: Estimate only tweets from this author username (tweet_search_extractor)

          hashtags: Hashtags applied to the estimate, separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Estimate only replies to this tweet ID (tweet_search_extractor)

          language: Language code used for estimate filtering (tweet_search_extractor)

          list_id: Estimate search results within this list ID (tweet_search_extractor)

          media_type: Media type used for estimate filtering (tweet_search_extractor)

          mentioning: Estimate tweets mentioning this username (tweet_search_extractor)

          min_faves: Minimum likes threshold for estimated results (tweet_search_extractor)

          min_quotes: Minimum quote count threshold for estimated results (tweet_search_extractor)

          min_replies: Minimum replies threshold for estimated results (tweet_search_extractor)

          min_retweets: Minimum retweets threshold for estimated results (tweet_search_extractor)

          place: Estimate search results within this place ID (tweet_search_extractor)

          place_country: Estimate search results within this country code (tweet_search_extractor)

          point_radius: Geo point radius used for estimation, e.g. -73.99 40.73 25mi
              (tweet_search_extractor)

          quotes: Quote mode used for estimation (tweet_search_extractor)

          quotes_of_tweet_id: Estimate only quotes of this tweet ID (tweet_search_extractor)

          replies: Reply mode used for estimation (tweet_search_extractor)

          results_limit: Maximum number of results to estimate. When set, the estimate caps projected
              results to this value.

          retweets: Retweet mode used for estimation (tweet_search_extractor)

          retweets_of_tweet_id: Estimate only retweets of this tweet ID (tweet_search_extractor)

          search_query: Query used to price tweet_search_extractor or community_search.

          since_date: Estimate start date in YYYY-MM-DD format (tweet_search_extractor)

          target_community_id: Community ID used to price community_post_extractor or community_search.

          target_list_id: List ID used to price list_follower_explorer, list_member_extractor, or
              list_post_extractor.

          target_space_id: Space ID used to price space_explorer.

          to_user: Estimate replies sent to this username (tweet_search_extractor)

          until_date: Estimate end date in YYYY-MM-DD format (tweet_search_extractor)

          url: URL substring or domain filter used for estimation (tweet_search_extractor)

          verified_only: Estimate only verified authors (tweet_search_extractor)

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
                    "bounding_box": bounding_box,
                    "cashtags": cashtags,
                    "conversation_id": conversation_id,
                    "exact_phrase": exact_phrase,
                    "exclude_words": exclude_words,
                    "from_user": from_user,
                    "hashtags": hashtags,
                    "in_reply_to_tweet_id": in_reply_to_tweet_id,
                    "language": language,
                    "list_id": list_id,
                    "media_type": media_type,
                    "mentioning": mentioning,
                    "min_faves": min_faves,
                    "min_quotes": min_quotes,
                    "min_replies": min_replies,
                    "min_retweets": min_retweets,
                    "place": place,
                    "place_country": place_country,
                    "point_radius": point_radius,
                    "quotes": quotes,
                    "quotes_of_tweet_id": quotes_of_tweet_id,
                    "replies": replies,
                    "results_limit": results_limit,
                    "retweets": retweets,
                    "retweets_of_tweet_id": retweets_of_tweet_id,
                    "search_query": search_query,
                    "since_date": since_date,
                    "target_community_id": target_community_id,
                    "target_list_id": target_list_id,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_username": target_username,
                    "to_user": to_user,
                    "until_date": until_date,
                    "url": url,
                    "verified_only": verified_only,
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
                    {"format": format}, extraction_export_results_params.ExtractionExportResultsParams
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
        advanced_query: str | Omit = omit,
        any_words: str | Omit = omit,
        bounding_box: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        list_id: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        results_limit: int | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        search_query: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        target_community_id: str | Omit = omit,
        target_list_id: str | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_username: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
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

          advanced_query: Raw advanced search query appended as-is (tweet_search_extractor)

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines. (tweet_search_extractor)

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8 (tweet_search_extractor)

          cashtags: Cashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          conversation_id: Conversation ID filter (tweet_search_extractor)

          exact_phrase: Exact phrase to match (tweet_search_extractor)

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.
              (tweet_search_extractor)

          from_user: Filter by author username (tweet_search_extractor)

          hashtags: Hashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          in_reply_to_tweet_id: Only replies to this tweet ID (tweet_search_extractor)

          language: Language code filter (tweet_search_extractor)

          list_id: Search within a list ID (tweet_search_extractor)

          media_type: Media type filter (tweet_search_extractor)

          mentioning: Filter tweets mentioning a username (tweet_search_extractor)

          min_faves: Minimum likes threshold (tweet_search_extractor)

          min_quotes: Minimum quote count threshold (tweet_search_extractor)

          min_replies: Minimum replies threshold (tweet_search_extractor)

          min_retweets: Minimum retweets threshold (tweet_search_extractor)

          place: Search within a place ID (tweet_search_extractor)

          place_country: Search within a country code (tweet_search_extractor)

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi (tweet_search_extractor)

          quotes: Quote mode (tweet_search_extractor)

          quotes_of_tweet_id: Only quotes of this tweet ID (tweet_search_extractor)

          replies: Reply mode (tweet_search_extractor)

          results_limit: Maximum number of results to extract. When set, the extraction stops after
              reaching this limit.

          retweets: Retweet mode (tweet_search_extractor)

          retweets_of_tweet_id: Only retweets of this tweet ID (tweet_search_extractor)

          search_query: Required for tweet_search_extractor & community_search.

          since_date: Start date YYYY-MM-DD (tweet_search_extractor)

          target_community_id: Required for community_post_extractor & community_search.

          target_list_id: Required for list_follower_explorer, list_member_extractor &
              list_post_extractor.

          target_space_id: Required for space_explorer.

          to_user: Filter replies sent to a username (tweet_search_extractor)

          until_date: End date YYYY-MM-DD (tweet_search_extractor)

          url: URL substring or domain filter (tweet_search_extractor)

          verified_only: Only verified authors (tweet_search_extractor)

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
                    "bounding_box": bounding_box,
                    "cashtags": cashtags,
                    "conversation_id": conversation_id,
                    "exact_phrase": exact_phrase,
                    "exclude_words": exclude_words,
                    "from_user": from_user,
                    "hashtags": hashtags,
                    "in_reply_to_tweet_id": in_reply_to_tweet_id,
                    "language": language,
                    "list_id": list_id,
                    "media_type": media_type,
                    "mentioning": mentioning,
                    "min_faves": min_faves,
                    "min_quotes": min_quotes,
                    "min_replies": min_replies,
                    "min_retweets": min_retweets,
                    "place": place,
                    "place_country": place_country,
                    "point_radius": point_radius,
                    "quotes": quotes,
                    "quotes_of_tweet_id": quotes_of_tweet_id,
                    "replies": replies,
                    "results_limit": results_limit,
                    "retweets": retweets,
                    "retweets_of_tweet_id": retweets_of_tweet_id,
                    "search_query": search_query,
                    "since_date": since_date,
                    "target_community_id": target_community_id,
                    "target_list_id": target_list_id,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_username": target_username,
                    "to_user": to_user,
                    "until_date": until_date,
                    "url": url,
                    "verified_only": verified_only,
                },
                extraction_run_params.ExtractionRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        limit: int | Omit = omit,
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
          cursor: Cursor for keyset pagination from prior response next_cursor

          limit: Maximum number of results to return (1-1000, default 100)

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
                        "limit": limit,
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
          cursor: Cursor for keyset pagination from prior response next_cursor

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
        bounding_box: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        list_id: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        results_limit: int | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        search_query: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        target_community_id: str | Omit = omit,
        target_list_id: str | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_username: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
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

          advanced_query: Raw advanced query string appended to the estimate (tweet_search_extractor)

          any_words: Alternative words or quoted phrases for estimated results. Separate with spaces,
              commas, or lines.

          bounding_box: Geo bounding box used for estimation, e.g. -74.1 40.6 -73.9 40.8
              (tweet_search_extractor)

          cashtags: Cashtags applied to the estimate, separated by spaces, commas, or lines.

          conversation_id: Conversation ID filter used for estimation (tweet_search_extractor)

          exact_phrase: Exact phrase filter for search estimation

          exclude_words: Words or quoted phrases excluded from estimated results. Separate with spaces,
              commas, or lines.

          from_user: Estimate only tweets from this author username (tweet_search_extractor)

          hashtags: Hashtags applied to the estimate, separated by spaces, commas, or lines.

          in_reply_to_tweet_id: Estimate only replies to this tweet ID (tweet_search_extractor)

          language: Language code used for estimate filtering (tweet_search_extractor)

          list_id: Estimate search results within this list ID (tweet_search_extractor)

          media_type: Media type used for estimate filtering (tweet_search_extractor)

          mentioning: Estimate tweets mentioning this username (tweet_search_extractor)

          min_faves: Minimum likes threshold for estimated results (tweet_search_extractor)

          min_quotes: Minimum quote count threshold for estimated results (tweet_search_extractor)

          min_replies: Minimum replies threshold for estimated results (tweet_search_extractor)

          min_retweets: Minimum retweets threshold for estimated results (tweet_search_extractor)

          place: Estimate search results within this place ID (tweet_search_extractor)

          place_country: Estimate search results within this country code (tweet_search_extractor)

          point_radius: Geo point radius used for estimation, e.g. -73.99 40.73 25mi
              (tweet_search_extractor)

          quotes: Quote mode used for estimation (tweet_search_extractor)

          quotes_of_tweet_id: Estimate only quotes of this tweet ID (tweet_search_extractor)

          replies: Reply mode used for estimation (tweet_search_extractor)

          results_limit: Maximum number of results to estimate. When set, the estimate caps projected
              results to this value.

          retweets: Retweet mode used for estimation (tweet_search_extractor)

          retweets_of_tweet_id: Estimate only retweets of this tweet ID (tweet_search_extractor)

          search_query: Query used to price tweet_search_extractor or community_search.

          since_date: Estimate start date in YYYY-MM-DD format (tweet_search_extractor)

          target_community_id: Community ID used to price community_post_extractor or community_search.

          target_list_id: List ID used to price list_follower_explorer, list_member_extractor, or
              list_post_extractor.

          target_space_id: Space ID used to price space_explorer.

          to_user: Estimate replies sent to this username (tweet_search_extractor)

          until_date: Estimate end date in YYYY-MM-DD format (tweet_search_extractor)

          url: URL substring or domain filter used for estimation (tweet_search_extractor)

          verified_only: Estimate only verified authors (tweet_search_extractor)

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
                    "bounding_box": bounding_box,
                    "cashtags": cashtags,
                    "conversation_id": conversation_id,
                    "exact_phrase": exact_phrase,
                    "exclude_words": exclude_words,
                    "from_user": from_user,
                    "hashtags": hashtags,
                    "in_reply_to_tweet_id": in_reply_to_tweet_id,
                    "language": language,
                    "list_id": list_id,
                    "media_type": media_type,
                    "mentioning": mentioning,
                    "min_faves": min_faves,
                    "min_quotes": min_quotes,
                    "min_replies": min_replies,
                    "min_retweets": min_retweets,
                    "place": place,
                    "place_country": place_country,
                    "point_radius": point_radius,
                    "quotes": quotes,
                    "quotes_of_tweet_id": quotes_of_tweet_id,
                    "replies": replies,
                    "results_limit": results_limit,
                    "retweets": retweets,
                    "retweets_of_tweet_id": retweets_of_tweet_id,
                    "search_query": search_query,
                    "since_date": since_date,
                    "target_community_id": target_community_id,
                    "target_list_id": target_list_id,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_username": target_username,
                    "to_user": to_user,
                    "until_date": until_date,
                    "url": url,
                    "verified_only": verified_only,
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
                    {"format": format}, extraction_export_results_params.ExtractionExportResultsParams
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
        advanced_query: str | Omit = omit,
        any_words: str | Omit = omit,
        bounding_box: str | Omit = omit,
        cashtags: str | Omit = omit,
        conversation_id: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        from_user: str | Omit = omit,
        hashtags: str | Omit = omit,
        in_reply_to_tweet_id: str | Omit = omit,
        language: str | Omit = omit,
        list_id: str | Omit = omit,
        media_type: Literal["images", "videos", "gifs", "media", "links", "none"] | Omit = omit,
        mentioning: str | Omit = omit,
        min_faves: int | Omit = omit,
        min_quotes: int | Omit = omit,
        min_replies: int | Omit = omit,
        min_retweets: int | Omit = omit,
        place: str | Omit = omit,
        place_country: str | Omit = omit,
        point_radius: str | Omit = omit,
        quotes: Literal["include", "exclude", "only"] | Omit = omit,
        quotes_of_tweet_id: str | Omit = omit,
        replies: Literal["include", "exclude", "only"] | Omit = omit,
        results_limit: int | Omit = omit,
        retweets: Literal["include", "exclude", "only"] | Omit = omit,
        retweets_of_tweet_id: str | Omit = omit,
        search_query: str | Omit = omit,
        since_date: Union[str, date] | Omit = omit,
        target_community_id: str | Omit = omit,
        target_list_id: str | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_username: str | Omit = omit,
        to_user: str | Omit = omit,
        until_date: Union[str, date] | Omit = omit,
        url: str | Omit = omit,
        verified_only: bool | Omit = omit,
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

          advanced_query: Raw advanced search query appended as-is (tweet_search_extractor)

          any_words: Words or quoted phrases where any one can match. Separate with spaces, commas,
              or lines. (tweet_search_extractor)

          bounding_box: Geo bounding box, e.g. -74.1 40.6 -73.9 40.8 (tweet_search_extractor)

          cashtags: Cashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          conversation_id: Conversation ID filter (tweet_search_extractor)

          exact_phrase: Exact phrase to match (tweet_search_extractor)

          exclude_words: Words or quoted phrases to exclude. Separate with spaces, commas, or lines.
              (tweet_search_extractor)

          from_user: Filter by author username (tweet_search_extractor)

          hashtags: Hashtags separated by spaces, commas, or lines. (tweet_search_extractor)

          in_reply_to_tweet_id: Only replies to this tweet ID (tweet_search_extractor)

          language: Language code filter (tweet_search_extractor)

          list_id: Search within a list ID (tweet_search_extractor)

          media_type: Media type filter (tweet_search_extractor)

          mentioning: Filter tweets mentioning a username (tweet_search_extractor)

          min_faves: Minimum likes threshold (tweet_search_extractor)

          min_quotes: Minimum quote count threshold (tweet_search_extractor)

          min_replies: Minimum replies threshold (tweet_search_extractor)

          min_retweets: Minimum retweets threshold (tweet_search_extractor)

          place: Search within a place ID (tweet_search_extractor)

          place_country: Search within a country code (tweet_search_extractor)

          point_radius: Geo point radius, e.g. -73.99 40.73 25mi (tweet_search_extractor)

          quotes: Quote mode (tweet_search_extractor)

          quotes_of_tweet_id: Only quotes of this tweet ID (tweet_search_extractor)

          replies: Reply mode (tweet_search_extractor)

          results_limit: Maximum number of results to extract. When set, the extraction stops after
              reaching this limit.

          retweets: Retweet mode (tweet_search_extractor)

          retweets_of_tweet_id: Only retweets of this tweet ID (tweet_search_extractor)

          search_query: Required for tweet_search_extractor & community_search.

          since_date: Start date YYYY-MM-DD (tweet_search_extractor)

          target_community_id: Required for community_post_extractor & community_search.

          target_list_id: Required for list_follower_explorer, list_member_extractor &
              list_post_extractor.

          target_space_id: Required for space_explorer.

          to_user: Filter replies sent to a username (tweet_search_extractor)

          until_date: End date YYYY-MM-DD (tweet_search_extractor)

          url: URL substring or domain filter (tweet_search_extractor)

          verified_only: Only verified authors (tweet_search_extractor)

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
                    "bounding_box": bounding_box,
                    "cashtags": cashtags,
                    "conversation_id": conversation_id,
                    "exact_phrase": exact_phrase,
                    "exclude_words": exclude_words,
                    "from_user": from_user,
                    "hashtags": hashtags,
                    "in_reply_to_tweet_id": in_reply_to_tweet_id,
                    "language": language,
                    "list_id": list_id,
                    "media_type": media_type,
                    "mentioning": mentioning,
                    "min_faves": min_faves,
                    "min_quotes": min_quotes,
                    "min_replies": min_replies,
                    "min_retweets": min_retweets,
                    "place": place,
                    "place_country": place_country,
                    "point_radius": point_radius,
                    "quotes": quotes,
                    "quotes_of_tweet_id": quotes_of_tweet_id,
                    "replies": replies,
                    "results_limit": results_limit,
                    "retweets": retweets,
                    "retweets_of_tweet_id": retweets_of_tweet_id,
                    "search_query": search_query,
                    "since_date": since_date,
                    "target_community_id": target_community_id,
                    "target_list_id": target_list_id,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_username": target_username,
                    "to_user": to_user,
                    "until_date": until_date,
                    "url": url,
                    "verified_only": verified_only,
                },
                extraction_run_params.ExtractionRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
