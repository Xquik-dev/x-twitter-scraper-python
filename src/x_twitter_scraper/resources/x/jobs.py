# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.x import job_search_params, job_retrieve_params, job_list_locations_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.x.job_search_response import JobSearchResponse
from ...types.x.job_retrieve_response import JobRetrieveResponse
from ...types.x.job_list_locations_response import JobListLocationsResponse

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    """Public X job listings, search and details"""

    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobRetrieveResponse:
        """
        Returns a public job listing with its description as text & Markdown, work type,
        seniority, salary, company & apply link. A job that closed returns job_not_found
        & is free.

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
            path_template("/x/jobs/{id}", id=id),
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
                    job_retrieve_params.JobRetrieveParams,
                ),
            ),
            cast_to=JobRetrieveResponse,
        )

    def list_locations(
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
    ) -> JobListLocationsResponse:
        """
        Returns the places whose names match a query, each with the location ID that GET
        /x/jobs/search takes. No match returns an empty list, free.

        Args:
          q: Place name or its start, such as new york. Alias: query.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Most places to return. Without it, every match returns. Aliases: pageSize,
              count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/jobs/locations",
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
                    job_list_locations_params.JobListLocationsParams,
                ),
            ),
            cast_to=JobListLocationsResponse,
        )

    def search(
        self,
        *,
        q: str,
        company: str | Omit = omit,
        cursor: str | Omit = omit,
        employment_type: str | Omit = omit,
        fields: str | Omit = omit,
        location: str | Omit = omit,
        location_id: str | Omit = omit,
        location_type: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        seniority: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobSearchResponse:
        """Returns job listings with title, location, salary, company & apply link.

        Add
        filters to narrow them. A job that closed is left out & free. Follow next_cursor
        for more.

        Args:
          q: Keyword, such as a job title or skill. Alias: query.

          company: Company name to match.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          employment_type: Comma list of full_time, full_time_contract, part_time & contract_to_hire. Any
              case works, with spaces or hyphens between words.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          location: City, region or country as text, such as Berlin.

          location_id: Location ID from GET /x/jobs/locations. Replaces location when both are sent.

          location_type: Where the work happens. Comma list of onsite, remote & hybrid. Any case works,
              with spaces or hyphens between words.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          seniority: Comma list of intern, entry_level, junior, mid_level, senior, lead, manager &
              executive. Any case works, with spaces or hyphens between words.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/x/jobs/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "company": company,
                        "cursor": cursor,
                        "employment_type": employment_type,
                        "fields": fields,
                        "location": location,
                        "location_id": location_id,
                        "location_type": location_type,
                        "omit": omit,
                        "page_size": page_size,
                        "seniority": seniority,
                    },
                    job_search_params.JobSearchParams,
                ),
            ),
            cast_to=JobSearchResponse,
        )


class AsyncJobsResource(AsyncAPIResource):
    """Public X job listings, search and details"""

    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        Prefix for any HTTP method call that returns the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#accessing-raw-response-data
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Xquik-dev/x-twitter-scraper-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        omit: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobRetrieveResponse:
        """
        Returns a public job listing with its description as text & Markdown, work type,
        seniority, salary, company & apply link. A job that closed returns job_not_found
        & is free.

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
            path_template("/x/jobs/{id}", id=id),
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
                    job_retrieve_params.JobRetrieveParams,
                ),
            ),
            cast_to=JobRetrieveResponse,
        )

    async def list_locations(
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
    ) -> JobListLocationsResponse:
        """
        Returns the places whose names match a query, each with the location ID that GET
        /x/jobs/search takes. No match returns an empty list, free.

        Args:
          q: Place name or its start, such as new york. Alias: query.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          limit: Most places to return. Without it, every match returns. Aliases: pageSize,
              count, max_results, maxItems, max_items & per_page.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/jobs/locations",
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
                    job_list_locations_params.JobListLocationsParams,
                ),
            ),
            cast_to=JobListLocationsResponse,
        )

    async def search(
        self,
        *,
        q: str,
        company: str | Omit = omit,
        cursor: str | Omit = omit,
        employment_type: str | Omit = omit,
        fields: str | Omit = omit,
        location: str | Omit = omit,
        location_id: str | Omit = omit,
        location_type: str | Omit = omit,
        omit: str | Omit = omit,
        page_size: int | Omit = omit,
        seniority: str | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobSearchResponse:
        """Returns job listings with title, location, salary, company & apply link.

        Add
        filters to narrow them. A job that closed is left out & free. Follow next_cursor
        for more.

        Args:
          q: Keyword, such as a job title or skill. Alias: query.

          company: Company name to match.

          cursor: Pagination cursor for collection results. Also read as next_cursor, next_token,
              pagination_token or continuation_token.

          employment_type: Comma list of full_time, full_time_contract, part_time & contract_to_hire. Any
              case works, with spaces or hyphens between words.

          fields: Fields to keep in each row, comma-separated. Use dots for nested fields, such as
              author.username. A list keeps the field in each item. Case & underscores do not
              matter. A row that lacks a field leaves it out. Cursors, counts & diagnostics
              always stay. An unknown name answers 400 unknown_field with the valid names,
              before any read. The price stays the same. SDK row types then hold only the
              named fields.

          location: City, region or country as text, such as Berlin.

          location_id: Location ID from GET /x/jobs/locations. Replaces location when both are sent.

          location_type: Where the work happens. Comma list of onsite, remote & hybrid. Any case works,
              with spaces or hyphens between words.

          omit: Fields to drop from each row, comma-separated. It takes the same names as
              fields. With fields, it drops from the kept fields.

          page_size: Items per page (1-100, default 20). Source, filters or credits can return fewer.
              Follow next_cursor for more pages. Aliases: limit, count, max_results, maxItems,
              max_items & per_page.

          seniority: Comma list of intern, entry_level, junior, mid_level, senior, lead, manager &
              executive. Any case works, with spaces or hyphens between words.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/x/jobs/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "company": company,
                        "cursor": cursor,
                        "employment_type": employment_type,
                        "fields": fields,
                        "location": location,
                        "location_id": location_id,
                        "location_type": location_type,
                        "omit": omit,
                        "page_size": page_size,
                        "seniority": seniority,
                    },
                    job_search_params.JobSearchParams,
                ),
            ),
            cast_to=JobSearchResponse,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.retrieve = to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list_locations = to_raw_response_wrapper(
            jobs.list_locations,
        )
        self.search = to_raw_response_wrapper(
            jobs.search,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_raw_response_wrapper(
            jobs.retrieve,
        )
        self.list_locations = async_to_raw_response_wrapper(
            jobs.list_locations,
        )
        self.search = async_to_raw_response_wrapper(
            jobs.search,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.retrieve = to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list_locations = to_streamed_response_wrapper(
            jobs.list_locations,
        )
        self.search = to_streamed_response_wrapper(
            jobs.search,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.retrieve = async_to_streamed_response_wrapper(
            jobs.retrieve,
        )
        self.list_locations = async_to_streamed_response_wrapper(
            jobs.list_locations,
        )
        self.search = async_to_streamed_response_wrapper(
            jobs.search,
        )
