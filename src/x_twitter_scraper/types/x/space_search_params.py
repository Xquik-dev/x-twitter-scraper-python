# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SpaceSearchParams"]


class SpaceSearchParams(TypedDict, total=False):
    q: Required[str]
    """Words, hashtags or X search operators, such as from:solana.

    The search adds filter:spaces. Alias query.
    """

    cursor: str
    """Pagination cursor for collection results.

    Also read as next_cursor, next_token, pagination_token or continuation_token.
    """

    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Posts a page reads, 20 at a time (1-100, default 20).

    Posts often share the same Space, so a page returns fewer Spaces. Send 100 to
    read a search fastest. Aliases: limit, count, max_results, maxItems, max_items &
    per_page.
    """

    query_type: Annotated[Literal["Latest", "Top"], PropertyInfo(alias="queryType")]
    """Latest sorts by post time.

    Top ranks by engagement. Any case works. Aliases result_type, sort_order, type,
    search_type, product, category & section.
    """
