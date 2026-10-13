# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserRetrieveBatchTweetsParams"]


class UserRetrieveBatchTweetsParams(TypedDict, total=False):
    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    ids: str
    """Comma-separated numeric user IDs (1-20 values).

    Duplicate IDs are ignored while preserving first-seen order.
    """

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Posts per user (1-20, default 20).

    Credits can return fewer. Aliases: limit, count, max_results, maxItems,
    max_items & per_page.
    """

    usernames: str
    """
    Comma-separated X usernames, with or without @, or profile links such as
    x.com/nasa (1-20 values), in place of ids. A name in another case is the same
    account.
    """
