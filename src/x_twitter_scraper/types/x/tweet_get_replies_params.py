# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TweetGetRepliesParams"]


class TweetGetRepliesParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for tweet replies"""

    since_time: Annotated[str, PropertyInfo(alias="sinceTime")]
    """Unix timestamp - return replies posted after this time"""

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """Unix timestamp - return replies posted before this time"""
