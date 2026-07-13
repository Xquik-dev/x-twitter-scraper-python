# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListRetrieveTweetsParams"]


class ListRetrieveTweetsParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for list tweets"""

    include_replies: Annotated[bool, PropertyInfo(alias="includeReplies")]
    """Include replies (default false)"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Maximum items requested from this page (1-100, default 20).

    The response can contain fewer items because the source returned fewer, filters
    removed items, or remaining credits cover fewer results. Keep requesting
    next_cursor while has_next_page is true, even when a page is empty. The
    deprecated limit and count aliases remain accepted.
    """

    since_time: Annotated[str, PropertyInfo(alias="sinceTime")]
    """Unix timestamp - filter after"""

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """Unix timestamp - filter before"""
