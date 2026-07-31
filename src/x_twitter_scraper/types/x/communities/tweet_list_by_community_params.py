# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TweetListByCommunityParams"]


class TweetListByCommunityParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for community tweets"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Maximum page items (1-100, default 20).

    Source, filters, or credits can reduce results. Continue while has_next_page is
    true. Deprecated limit and count aliases remain accepted.
    """
