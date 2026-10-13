# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TweetListTopParams"]


class TweetListTopParams(TypedDict, total=False):
    country: str
    """
    Only tweets from one country, as a 2- or 3-letter ISO 3166 code, such as US or
    USA. Send country or language, not both.
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

    language: str
    """Only tweets in one language, as a 2-letter code, such as en.

    Send country or language, not both.
    """

    metric: Literal["likes", "replies", "quotes", "bookmarks", "shares", "views"]
    """What to rank tweets by.

    Defaults to likes. Singular names work too, such as like.
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

    window: Literal["day", "week", "month"]
    """How far back to look.

    Defaults to day. Also takes 24h, 7d, 30d, daily, weekly and monthly.
    """
