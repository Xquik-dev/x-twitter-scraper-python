# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .football import FootballLeague

__all__ = ["SportListPostsParams"]


class SportListPostsParams(TypedDict, total=False):
    league: Required[FootballLeague]
    """nfl for the NFL or ncaafb for college football, in any case. Another value
    gets a free 400 `invalid_league` before X is read.
    """

    cursor: str
    """Pagination cursor for collection results. Also read as next_cursor,
    next_token, pagination_token or continuation_token.
    """

    fields: str
    """Fields to keep in each row, comma-separated. Use dots for nested fields, such
    as author.username. A list keeps the field in each item. Case & underscores do
    not matter. A row that lacks a field leaves it out. Cursors, counts &
    diagnostics always stay. An unknown name answers 400 unknown_field with the
    valid names, before any read. The price stays the same. SDK row types then
    hold only the named fields.
    """

    omit: str
    """Fields to drop from each row, comma-separated. It takes the same names as
    fields. With fields, it drops from the kept fields.
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Items per page (1-100, default 20). Source, filters or credits can return
    fewer. Follow next_cursor for more pages. Its aliases are limit, count,
    max_results, maxItems, max_items & per_page.
    """

    query_type: Annotated[Literal["Top", "Latest"], PropertyInfo(alias="queryType")]
    """Top for the posts X ranks highest, or Latest for the newest. Any case works,
    & so do Relevance & Recency. Alias order or sort. Send the same value with each
    cursor.
    """
