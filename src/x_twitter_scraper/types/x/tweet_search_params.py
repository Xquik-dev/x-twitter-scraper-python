# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TweetSearchParams"]


class TweetSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query (keywords,"""

    cursor: str
    """Pagination cursor from previous response"""

    limit: int
    """Max tweets to return (server paginates internally). Omit for single page (~20)."""

    query_type: Annotated[Literal["Latest", "Top"], PropertyInfo(alias="queryType")]
    """Sort order — Latest (chronological) or Top (engagement-ranked)"""

    since_time: Annotated[str, PropertyInfo(alias="sinceTime")]
    """ISO 8601 timestamp — only return tweets after this time"""

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """ISO 8601 timestamp — only return tweets before this time"""
