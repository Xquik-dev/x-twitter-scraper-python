# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import draw_run_params, draw_list_params, draw_export_params
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
from ..types.draw_run_response import DrawRunResponse
from ..types.draw_list_response import DrawListResponse
from ..types.draw_retrieve_response import DrawRetrieveResponse

__all__ = ["DrawsResource", "AsyncDrawsResource"]


class DrawsResource(SyncAPIResource):
    """Giveaway draws from tweet replies"""

    @cached_property
    def with_raw_response(self) -> DrawsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return DrawsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DrawsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return DrawsResourceWithStreamingResponse(self)

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
    ) -> DrawRetrieveResponse:
        """
        Get draw details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/draws/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DrawRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DrawListResponse:
        """
        List draws

        Args:
          after: Cursor for keyset pagination

          limit: Maximum number of items to return (1-100, default 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/draws",
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
                    draw_list_params.DrawListParams,
                ),
            ),
            cast_to=DrawListResponse,
        )

    def export(
        self,
        id: str,
        *,
        format: Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"] | Omit = omit,
        type: Literal["winners", "entries"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Export draw data

        Args:
          format: Export output format

          type: Export winners or all entries

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template("/draws/{id}/export", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "type": type,
                    },
                    draw_export_params.DrawExportParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def run(
        self,
        *,
        tweet_url: str,
        backup_count: int | Omit = omit,
        filter_account_age_days: int | Omit = omit,
        filter_language: str | Omit = omit,
        filter_min_followers: int | Omit = omit,
        must_follow_username: str | Omit = omit,
        must_retweet: bool | Omit = omit,
        required_hashtags: SequenceNotStr[str] | Omit = omit,
        required_keywords: SequenceNotStr[str] | Omit = omit,
        required_mentions: SequenceNotStr[str] | Omit = omit,
        unique_authors_only: bool | Omit = omit,
        winner_count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DrawRunResponse:
        """
        Run giveaway draw

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/draws",
            body=maybe_transform(
                {
                    "tweet_url": tweet_url,
                    "backup_count": backup_count,
                    "filter_account_age_days": filter_account_age_days,
                    "filter_language": filter_language,
                    "filter_min_followers": filter_min_followers,
                    "must_follow_username": must_follow_username,
                    "must_retweet": must_retweet,
                    "required_hashtags": required_hashtags,
                    "required_keywords": required_keywords,
                    "required_mentions": required_mentions,
                    "unique_authors_only": unique_authors_only,
                    "winner_count": winner_count,
                },
                draw_run_params.DrawRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DrawRunResponse,
        )


class AsyncDrawsResource(AsyncAPIResource):
    """Giveaway draws from tweet replies"""

    @cached_property
    def with_raw_response(self) -> AsyncDrawsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDrawsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDrawsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncDrawsResourceWithStreamingResponse(self)

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
    ) -> DrawRetrieveResponse:
        """
        Get draw details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/draws/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DrawRetrieveResponse,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DrawListResponse:
        """
        List draws

        Args:
          after: Cursor for keyset pagination

          limit: Maximum number of items to return (1-100, default 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/draws",
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
                    draw_list_params.DrawListParams,
                ),
            ),
            cast_to=DrawListResponse,
        )

    async def export(
        self,
        id: str,
        *,
        format: Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"] | Omit = omit,
        type: Literal["winners", "entries"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Export draw data

        Args:
          format: Export output format

          type: Export winners or all entries

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/draws/{id}/export", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "type": type,
                    },
                    draw_export_params.DrawExportParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def run(
        self,
        *,
        tweet_url: str,
        backup_count: int | Omit = omit,
        filter_account_age_days: int | Omit = omit,
        filter_language: str | Omit = omit,
        filter_min_followers: int | Omit = omit,
        must_follow_username: str | Omit = omit,
        must_retweet: bool | Omit = omit,
        required_hashtags: SequenceNotStr[str] | Omit = omit,
        required_keywords: SequenceNotStr[str] | Omit = omit,
        required_mentions: SequenceNotStr[str] | Omit = omit,
        unique_authors_only: bool | Omit = omit,
        winner_count: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DrawRunResponse:
        """
        Run giveaway draw

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/draws",
            body=await async_maybe_transform(
                {
                    "tweet_url": tweet_url,
                    "backup_count": backup_count,
                    "filter_account_age_days": filter_account_age_days,
                    "filter_language": filter_language,
                    "filter_min_followers": filter_min_followers,
                    "must_follow_username": must_follow_username,
                    "must_retweet": must_retweet,
                    "required_hashtags": required_hashtags,
                    "required_keywords": required_keywords,
                    "required_mentions": required_mentions,
                    "unique_authors_only": unique_authors_only,
                    "winner_count": winner_count,
                },
                draw_run_params.DrawRunParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DrawRunResponse,
        )


class DrawsResourceWithRawResponse:
    def __init__(self, draws: DrawsResource) -> None:
        self._draws = draws

        self.retrieve = to_raw_response_wrapper(
            draws.retrieve,
        )
        self.list = to_raw_response_wrapper(
            draws.list,
        )
        self.export = to_custom_raw_response_wrapper(
            draws.export,
            BinaryAPIResponse,
        )
        self.run = to_raw_response_wrapper(
            draws.run,
        )


class AsyncDrawsResourceWithRawResponse:
    def __init__(self, draws: AsyncDrawsResource) -> None:
        self._draws = draws

        self.retrieve = async_to_raw_response_wrapper(
            draws.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            draws.list,
        )
        self.export = async_to_custom_raw_response_wrapper(
            draws.export,
            AsyncBinaryAPIResponse,
        )
        self.run = async_to_raw_response_wrapper(
            draws.run,
        )


class DrawsResourceWithStreamingResponse:
    def __init__(self, draws: DrawsResource) -> None:
        self._draws = draws

        self.retrieve = to_streamed_response_wrapper(
            draws.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            draws.list,
        )
        self.export = to_custom_streamed_response_wrapper(
            draws.export,
            StreamedBinaryAPIResponse,
        )
        self.run = to_streamed_response_wrapper(
            draws.run,
        )


class AsyncDrawsResourceWithStreamingResponse:
    def __init__(self, draws: AsyncDrawsResource) -> None:
        self._draws = draws

        self.retrieve = async_to_streamed_response_wrapper(
            draws.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            draws.list,
        )
        self.export = async_to_custom_streamed_response_wrapper(
            draws.export,
            AsyncStreamedBinaryAPIResponse,
        )
        self.run = async_to_streamed_response_wrapper(
            draws.run,
        )
