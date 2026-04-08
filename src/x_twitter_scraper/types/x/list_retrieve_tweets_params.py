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

    since_time: Annotated[str, PropertyInfo(alias="sinceTime")]
    """Unix timestamp - filter after"""

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """Unix timestamp - filter before"""
