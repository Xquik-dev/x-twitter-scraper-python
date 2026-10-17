# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import (
    community_note_retrieve_contributor_params,
    community_note_list_contributor_notes_params,
    community_note_list_contributor_deleted_notes_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.paginated_community_notes import PaginatedCommunityNotes
from ...types.x.community_note_retrieve_contributor_response import CommunityNoteRetrieveContributorResponse

__all__ = ["CommunityNotesResource", "AsyncCommunityNotesResource"]


class CommunityNotesResource(SyncAPIResource):
    """Community Notes contributors, their notes, ratings & deleted notes"""

    @cached_property
    def with_raw_response(self) -> CommunityNotesResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return CommunityNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommunityNotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return CommunityNotesResourceWithStreamingResponse(self)

    def list_contributor_deleted_notes(
        self,
        alias: str,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedCommunityNotes:
        """Returns the notes a contributor deleted, newest first.

        X keeps each note's ID,
        times, rating & tags. A notice replaces its text & post. Each note costs 1
        credit. A contributor who deleted none returns an empty list, free.

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

          page_size: Notes per page (1-10, default 10). A low credit balance can return fewer. Follow
              next_cursor for more pages. Also read as limit, count, max_results, maxItems,
              max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alias:
            raise ValueError(f"Expected a non-empty value for `alias` but received {alias!r}")
        return self._get(
            path_template("/x/community-notes/contributors/{alias}/deleted-notes", alias=alias),
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
                    },
                    community_note_list_contributor_deleted_notes_params.CommunityNoteListContributorDeletedNotesParams,
                ),
            ),
            cast_to=PaginatedCommunityNotes,
        )

    def list_contributor_notes(
        self,
        alias: str,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedCommunityNotes:
        """Returns a contributor's notes, newest first, each with the post it is on.

        Includes notes X has not rated helpful, which x.com shows under no post. Each
        note costs 1 credit. Follow next_cursor for more.

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

          page_size: Notes per page (1-10, default 10). A low credit balance can return fewer. Follow
              next_cursor for more pages. Also read as limit, count, max_results, maxItems,
              max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alias:
            raise ValueError(f"Expected a non-empty value for `alias` but received {alias!r}")
        return self._get(
            path_template("/x/community-notes/contributors/{alias}/notes", alias=alias),
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
                    },
                    community_note_list_contributor_notes_params.CommunityNoteListContributorNotesParams,
                ),
            ),
            cast_to=PaginatedCommunityNotes,
        )

    def retrieve_contributor(
        self,
        alias: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityNoteRetrieveContributorResponse:
        """Returns 1 Community Notes contributor by the alias X gives them.

        Includes note
        counts by rating, rating counts & the deleted notes count. Each lookup costs 1
        credit.

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
        if not alias:
            raise ValueError(f"Expected a non-empty value for `alias` but received {alias!r}")
        return self._get(
            path_template("/x/community-notes/contributors/{alias}", alias=alias),
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
                    community_note_retrieve_contributor_params.CommunityNoteRetrieveContributorParams,
                ),
            ),
            cast_to=CommunityNoteRetrieveContributorResponse,
        )


class AsyncCommunityNotesResource(AsyncAPIResource):
    """Community Notes contributors, their notes, ratings & deleted notes"""

    @cached_property
    def with_raw_response(self) -> AsyncCommunityNotesResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncCommunityNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommunityNotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncCommunityNotesResourceWithStreamingResponse(self)

    async def list_contributor_deleted_notes(
        self,
        alias: str,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedCommunityNotes:
        """Returns the notes a contributor deleted, newest first.

        X keeps each note's ID,
        times, rating & tags. A notice replaces its text & post. Each note costs 1
        credit. A contributor who deleted none returns an empty list, free.

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

          page_size: Notes per page (1-10, default 10). A low credit balance can return fewer. Follow
              next_cursor for more pages. Also read as limit, count, max_results, maxItems,
              max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alias:
            raise ValueError(f"Expected a non-empty value for `alias` but received {alias!r}")
        return await self._get(
            path_template("/x/community-notes/contributors/{alias}/deleted-notes", alias=alias),
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
                    },
                    community_note_list_contributor_deleted_notes_params.CommunityNoteListContributorDeletedNotesParams,
                ),
            ),
            cast_to=PaginatedCommunityNotes,
        )

    async def list_contributor_notes(
        self,
        alias: str,
        *,
        cursor: str | Omit = omit,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedCommunityNotes:
        """Returns a contributor's notes, newest first, each with the post it is on.

        Includes notes X has not rated helpful, which x.com shows under no post. Each
        note costs 1 credit. Follow next_cursor for more.

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

          page_size: Notes per page (1-10, default 10). A low credit balance can return fewer. Follow
              next_cursor for more pages. Also read as limit, count, max_results, maxItems,
              max_items & per_page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alias:
            raise ValueError(f"Expected a non-empty value for `alias` but received {alias!r}")
        return await self._get(
            path_template("/x/community-notes/contributors/{alias}/notes", alias=alias),
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
                    },
                    community_note_list_contributor_notes_params.CommunityNoteListContributorNotesParams,
                ),
            ),
            cast_to=PaginatedCommunityNotes,
        )

    async def retrieve_contributor(
        self,
        alias: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityNoteRetrieveContributorResponse:
        """Returns 1 Community Notes contributor by the alias X gives them.

        Includes note
        counts by rating, rating counts & the deleted notes count. Each lookup costs 1
        credit.

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
        if not alias:
            raise ValueError(f"Expected a non-empty value for `alias` but received {alias!r}")
        return await self._get(
            path_template("/x/community-notes/contributors/{alias}", alias=alias),
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
                    community_note_retrieve_contributor_params.CommunityNoteRetrieveContributorParams,
                ),
            ),
            cast_to=CommunityNoteRetrieveContributorResponse,
        )


class CommunityNotesResourceWithRawResponse:
    def __init__(self, community_notes: CommunityNotesResource) -> None:
        self._community_notes = community_notes

        self.list_contributor_deleted_notes = to_raw_response_wrapper(
            community_notes.list_contributor_deleted_notes,
        )
        self.list_contributor_notes = to_raw_response_wrapper(
            community_notes.list_contributor_notes,
        )
        self.retrieve_contributor = to_raw_response_wrapper(
            community_notes.retrieve_contributor,
        )


class AsyncCommunityNotesResourceWithRawResponse:
    def __init__(self, community_notes: AsyncCommunityNotesResource) -> None:
        self._community_notes = community_notes

        self.list_contributor_deleted_notes = async_to_raw_response_wrapper(
            community_notes.list_contributor_deleted_notes,
        )
        self.list_contributor_notes = async_to_raw_response_wrapper(
            community_notes.list_contributor_notes,
        )
        self.retrieve_contributor = async_to_raw_response_wrapper(
            community_notes.retrieve_contributor,
        )


class CommunityNotesResourceWithStreamingResponse:
    def __init__(self, community_notes: CommunityNotesResource) -> None:
        self._community_notes = community_notes

        self.list_contributor_deleted_notes = to_streamed_response_wrapper(
            community_notes.list_contributor_deleted_notes,
        )
        self.list_contributor_notes = to_streamed_response_wrapper(
            community_notes.list_contributor_notes,
        )
        self.retrieve_contributor = to_streamed_response_wrapper(
            community_notes.retrieve_contributor,
        )


class AsyncCommunityNotesResourceWithStreamingResponse:
    def __init__(self, community_notes: AsyncCommunityNotesResource) -> None:
        self._community_notes = community_notes

        self.list_contributor_deleted_notes = async_to_streamed_response_wrapper(
            community_notes.list_contributor_deleted_notes,
        )
        self.list_contributor_notes = async_to_streamed_response_wrapper(
            community_notes.list_contributor_notes,
        )
        self.retrieve_contributor = async_to_streamed_response_wrapper(
            community_notes.retrieve_contributor,
        )
