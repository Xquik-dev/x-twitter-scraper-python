# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JobSearchParams"]


class JobSearchParams(TypedDict, total=False):
    q: Required[str]
    """Keyword, such as a job title or skill. Alias: query."""

    company: str
    """Company name to match."""

    cursor: str
    """Pagination cursor for collection results.

    Also read as next_cursor, next_token, pagination_token or continuation_token.
    """

    employment_type: Annotated[str, PropertyInfo(alias="employmentType")]
    """Comma list of full_time, full_time_contract, part_time & contract_to_hire.

    Any case works, with spaces or hyphens between words.
    """

    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    location: str
    """City, region or country as text, such as Berlin."""

    location_id: Annotated[str, PropertyInfo(alias="locationId")]
    """Location ID from GET /x/jobs/locations. Replaces location when both are sent."""

    location_type: Annotated[str, PropertyInfo(alias="locationType")]
    """Where the work happens.

    Comma list of onsite, remote & hybrid. Any case works, with spaces or hyphens
    between words.
    """

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Items per page (1-100, default 20).

    Source, filters or credits can return fewer. Follow next_cursor for more pages.
    Aliases: limit, count, max_results, maxItems, max_items & per_page.
    """

    seniority: str
    """
    Comma list of intern, entry_level, junior, mid_level, senior, lead, manager &
    executive. Any case works, with spaces or hyphens between words.
    """
