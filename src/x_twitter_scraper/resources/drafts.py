# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import draft_list_params, draft_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.draft_detail import DraftDetail
from ..types.draft_list_response import DraftListResponse

__all__ = ["DraftsResource", "AsyncDraftsResource"]


class DraftsResource(SyncAPIResource):
    """AI tweet composition, drafts, writing styles, and radar"""

    @cached_property
    def with_raw_response(self) -> DraftsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return DraftsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DraftsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return DraftsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        text: str,
        goal: Literal["engagement", "followers", "authority", "conversation"] | Omit = omit,
        topic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DraftDetail:
        """
        Save a tweet draft

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/drafts",
            body=maybe_transform(
                {
                    "text": text,
                    "goal": goal,
                    "topic": topic,
                },
                draft_create_params.DraftCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DraftDetail,
        )

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
    ) -> DraftDetail:
        """
        Get draft by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/drafts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DraftDetail,
        )

    def list(
        self,
        *,
        after_cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DraftListResponse:
        """
        List saved drafts

        Args:
          after_cursor: Cursor for pagination

          limit: Maximum number of items to return (1-100, default 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/drafts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "limit": limit,
                    },
                    draft_list_params.DraftListParams,
                ),
            ),
            cast_to=DraftListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a draft

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/drafts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDraftsResource(AsyncAPIResource):
    """AI tweet composition, drafts, writing styles, and radar"""

    @cached_property
    def with_raw_response(self) -> AsyncDraftsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDraftsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDraftsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncDraftsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        text: str,
        goal: Literal["engagement", "followers", "authority", "conversation"] | Omit = omit,
        topic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DraftDetail:
        """
        Save a tweet draft

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/drafts",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "goal": goal,
                    "topic": topic,
                },
                draft_create_params.DraftCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DraftDetail,
        )

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
    ) -> DraftDetail:
        """
        Get draft by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/drafts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DraftDetail,
        )

    async def list(
        self,
        *,
        after_cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DraftListResponse:
        """
        List saved drafts

        Args:
          after_cursor: Cursor for pagination

          limit: Maximum number of items to return (1-100, default 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/drafts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "limit": limit,
                    },
                    draft_list_params.DraftListParams,
                ),
            ),
            cast_to=DraftListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a draft

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/drafts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DraftsResourceWithRawResponse:
    def __init__(self, drafts: DraftsResource) -> None:
        self._drafts = drafts

        self.create = to_raw_response_wrapper(
            drafts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            drafts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            drafts.list,
        )
        self.delete = to_raw_response_wrapper(
            drafts.delete,
        )


class AsyncDraftsResourceWithRawResponse:
    def __init__(self, drafts: AsyncDraftsResource) -> None:
        self._drafts = drafts

        self.create = async_to_raw_response_wrapper(
            drafts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            drafts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            drafts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            drafts.delete,
        )


class DraftsResourceWithStreamingResponse:
    def __init__(self, drafts: DraftsResource) -> None:
        self._drafts = drafts

        self.create = to_streamed_response_wrapper(
            drafts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            drafts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            drafts.list,
        )
        self.delete = to_streamed_response_wrapper(
            drafts.delete,
        )


class AsyncDraftsResourceWithStreamingResponse:
    def __init__(self, drafts: AsyncDraftsResource) -> None:
        self._drafts = drafts

        self.create = async_to_streamed_response_wrapper(
            drafts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            drafts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            drafts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            drafts.delete,
        )
