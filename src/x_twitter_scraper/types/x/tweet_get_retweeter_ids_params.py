# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TweetGetRetweeterIdsParams"]


class TweetGetRetweeterIdsParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for collection results.

    Also read as next_cursor, next_token, pagination_token or continuation_token.
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Profiles to request from this page (1-200, default 200).

    Source, filters or credits can return fewer. Follow next_cursor for more pages.
    Aliases: limit, count, max_results, maxItems, max_items & per_page.
    """
