# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import space_search_params, space_retrieve_params, space_retrieve_replay_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.space_search_response import SpaceSearchResponse
from ...types.x.space_retrieve_response import SpaceRetrieveResponse
from ...types.x.space_retrieve_replay_response import SpaceRetrieveReplayResponse

__all__ = ["SpacesResource", "AsyncSpacesResource"]


class SpacesResource(SyncAPIResource):
    """X Space details, host, and speakers"""

    @cached_property
    def with_raw_response(self) -> SpacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return SpacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return SpacesResourceWithStreamingResponse(self)

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
    ) -> SpaceRetrieveResponse:
        """Returns one X Space as X shows it, live, scheduled or ended.

        Accepts the Space
        ID or the URL-encoded Space URL. A Space X limits to subscribers or a community
        answers 404.

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
            path_template("/x/spaces/{id}", id=id),
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
                    space_retrieve_params.SpaceRetrieveParams,
                ),
            ),
            cast_to=SpaceRetrieveResponse,
        )

    def retrieve_replay(
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
    ) -> SpaceRetrieveReplayResponse:
        """
        Returns the recording X plays back once a Space is over, in state Ended or
        TimedOut. Accepts the Space ID or the URL-encoded Space URL. Check state and
        isAvailableForReplay with the Space lookup first. A live or scheduled Space
        answers 409, and a cancelled one 404.

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
            path_template("/x/spaces/{id}/replay", id=id),
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
                    space_retrieve_replay_params.SpaceRetrieveReplayParams,
                ),
            ),
            cast_to=SpaceRetrieveReplayResponse,
        )

    def search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpaceSearchResponse:
        """
        Returns the public Spaces that posts matching the query share, live, scheduled
        or ended. Each page reads up to pageSize posts, 20 by default, and returns each
        Space once. Costs 1 credit per Space.

        Args:
          q: Words, hashtags or X search operators, such as from:solana. The search adds
              filter:spaces. Alias query.

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

          page_size: Posts a page reads, 20 at a time (1-100, default 20). Posts often share the same
              Space, so a page returns fewer Spaces. Send 100 to read a search fastest.
              Aliases: limit, count, max_results, maxItems, max_items & per_page.

          query_type: Latest sorts by post time. Top ranks by engagement. Any case works. Aliases
              result_type, sort_order, type, search_type, product, category & section.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/spaces/search",
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
                        "query_type": query_type,
                    },
                    space_search_params.SpaceSearchParams,
                ),
            ),
            cast_to=SpaceSearchResponse,
        )


class AsyncSpacesResource(AsyncAPIResource):
    """X Space details, host, and speakers"""

    @cached_property
    def with_raw_response(self) -> AsyncSpacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncSpacesResourceWithStreamingResponse(self)

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
    ) -> SpaceRetrieveResponse:
        """Returns one X Space as X shows it, live, scheduled or ended.

        Accepts the Space
        ID or the URL-encoded Space URL. A Space X limits to subscribers or a community
        answers 404.

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
            path_template("/x/spaces/{id}", id=id),
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
                    space_retrieve_params.SpaceRetrieveParams,
                ),
            ),
            cast_to=SpaceRetrieveResponse,
        )

    async def retrieve_replay(
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
    ) -> SpaceRetrieveReplayResponse:
        """
        Returns the recording X plays back once a Space is over, in state Ended or
        TimedOut. Accepts the Space ID or the URL-encoded Space URL. Check state and
        isAvailableForReplay with the Space lookup first. A live or scheduled Space
        answers 409, and a cancelled one 404.

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
            path_template("/x/spaces/{id}/replay", id=id),
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
                    space_retrieve_replay_params.SpaceRetrieveReplayParams,
                ),
            ),
            cast_to=SpaceRetrieveReplayResponse,
        )

    async def search(
        self,
        *,
        q: str,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        query_type: Literal["Latest", "Top"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpaceSearchResponse:
        """
        Returns the public Spaces that posts matching the query share, live, scheduled
        or ended. Each page reads up to pageSize posts, 20 by default, and returns each
        Space once. Costs 1 credit per Space.

        Args:
          q: Words, hashtags or X search operators, such as from:solana. The search adds
              filter:spaces. Alias query.

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

          page_size: Posts a page reads, 20 at a time (1-100, default 20). Posts often share the same
              Space, so a page returns fewer Spaces. Send 100 to read a search fastest.
              Aliases: limit, count, max_results, maxItems, max_items & per_page.

          query_type: Latest sorts by post time. Top ranks by engagement. Any case works. Aliases
              result_type, sort_order, type, search_type, product, category & section.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/spaces/search",
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
                        "query_type": query_type,
                    },
                    space_search_params.SpaceSearchParams,
                ),
            ),
            cast_to=SpaceSearchResponse,
        )


class SpacesResourceWithRawResponse:
    def __init__(self, spaces: SpacesResource) -> None:
        self._spaces = spaces

        self.retrieve = to_raw_response_wrapper(
            spaces.retrieve,
        )
        self.retrieve_replay = to_raw_response_wrapper(
            spaces.retrieve_replay,
        )
        self.search = to_raw_response_wrapper(
            spaces.search,
        )


class AsyncSpacesResourceWithRawResponse:
    def __init__(self, spaces: AsyncSpacesResource) -> None:
        self._spaces = spaces

        self.retrieve = async_to_raw_response_wrapper(
            spaces.retrieve,
        )
        self.retrieve_replay = async_to_raw_response_wrapper(
            spaces.retrieve_replay,
        )
        self.search = async_to_raw_response_wrapper(
            spaces.search,
        )


class SpacesResourceWithStreamingResponse:
    def __init__(self, spaces: SpacesResource) -> None:
        self._spaces = spaces

        self.retrieve = to_streamed_response_wrapper(
            spaces.retrieve,
        )
        self.retrieve_replay = to_streamed_response_wrapper(
            spaces.retrieve_replay,
        )
        self.search = to_streamed_response_wrapper(
            spaces.search,
        )


class AsyncSpacesResourceWithStreamingResponse:
    def __init__(self, spaces: AsyncSpacesResource) -> None:
        self._spaces = spaces

        self.retrieve = async_to_streamed_response_wrapper(
            spaces.retrieve,
        )
        self.retrieve_replay = async_to_streamed_response_wrapper(
            spaces.retrieve_replay,
        )
        self.search = async_to_streamed_response_wrapper(
            spaces.search,
        )
