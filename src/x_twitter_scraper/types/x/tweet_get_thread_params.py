# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TweetGetThreadParams"]


class TweetGetThreadParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for thread tweets"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Maximum items requested from this page (1-100, default 20).

    The response can contain fewer items because the source returned fewer, filters
    removed items, or remaining credits cover fewer results. Keep requesting
    next_cursor while has_next_page is true, even when a page is empty. The
    deprecated limit and count aliases remain accepted.
    """
