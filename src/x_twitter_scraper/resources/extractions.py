# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
    """Bulk data extraction (20 tool types)"""

    @cached_property
    def with_raw_response(self) -> ExtractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return ExtractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return ExtractionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
          after: Cursor for keyset pagination

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
                        "after": after,
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
        after: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        tool_type: Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
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
          after: Cursor for keyset pagination

          limit: Maximum number of items to return (1-100, default 50)

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
                        "after": after,
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
            "verified_follower_explorer",
        ],
        advanced_query: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        search_query: str | Omit = omit,
        target_community_id: str | Omit = omit,
        target_list_id: str | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_username: str | Omit = omit,
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

          exact_phrase: Exact phrase filter for search estimation

          exclude_words: Words excluded from estimated search results

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
                    "exact_phrase": exact_phrase,
                    "exclude_words": exclude_words,
                    "search_query": search_query,
                    "target_community_id": target_community_id,
                    "target_list_id": target_list_id,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_username": target_username,
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
        format: Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"] | Omit = omit,
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
            "verified_follower_explorer",
        ],
        advanced_query: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        search_query: str | Omit = omit,
        target_community_id: str | Omit = omit,
        target_list_id: str | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_username: str | Omit = omit,
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

          exact_phrase: Exact phrase to match (tweet_search_extractor)

          exclude_words: Words to exclude from results (tweet_search_extractor)

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
                    "exact_phrase": exact_phrase,
                    "exclude_words": exclude_words,
                    "search_query": search_query,
                    "target_community_id": target_community_id,
                    "target_list_id": target_list_id,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_username": target_username,
                },
                extraction_run_params.ExtractionRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractionRunResponse,
        )


class AsyncExtractionsResource(AsyncAPIResource):
    """Bulk data extraction (20 tool types)"""

    @cached_property
    def with_raw_response(self) -> AsyncExtractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncExtractionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        after: str | Omit = omit,
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
          after: Cursor for keyset pagination

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
                        "after": after,
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
        after: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["running", "completed", "failed"] | Omit = omit,
        tool_type: Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
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
          after: Cursor for keyset pagination

          limit: Maximum number of items to return (1-100, default 50)

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
                        "after": after,
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
            "verified_follower_explorer",
        ],
        advanced_query: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        search_query: str | Omit = omit,
        target_community_id: str | Omit = omit,
        target_list_id: str | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_username: str | Omit = omit,
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

          exact_phrase: Exact phrase filter for search estimation

          exclude_words: Words excluded from estimated search results

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
                    "exact_phrase": exact_phrase,
                    "exclude_words": exclude_words,
                    "search_query": search_query,
                    "target_community_id": target_community_id,
                    "target_list_id": target_list_id,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_username": target_username,
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
        format: Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"] | Omit = omit,
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
            "verified_follower_explorer",
        ],
        advanced_query: str | Omit = omit,
        exact_phrase: str | Omit = omit,
        exclude_words: str | Omit = omit,
        search_query: str | Omit = omit,
        target_community_id: str | Omit = omit,
        target_list_id: str | Omit = omit,
        target_space_id: str | Omit = omit,
        target_tweet_id: str | Omit = omit,
        target_username: str | Omit = omit,
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

          exact_phrase: Exact phrase to match (tweet_search_extractor)

          exclude_words: Words to exclude from results (tweet_search_extractor)

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
                    "exact_phrase": exact_phrase,
                    "exclude_words": exclude_words,
                    "search_query": search_query,
                    "target_community_id": target_community_id,
                    "target_list_id": target_list_id,
                    "target_space_id": target_space_id,
                    "target_tweet_id": target_tweet_id,
                    "target_username": target_username,
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
