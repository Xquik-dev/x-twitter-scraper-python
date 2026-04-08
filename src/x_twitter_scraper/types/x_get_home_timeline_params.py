# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["XGetHomeTimelineParams"]


class XGetHomeTimelineParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for timeline"""

    seen_tweet_ids: Annotated[str, PropertyInfo(alias="seenTweetIds")]
    """Comma-separated tweet IDs to exclude from results"""
