# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserRetrieveTweetsParams"]


class UserRetrieveTweetsParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous response"""

    include_parent_tweet: Annotated[bool, PropertyInfo(alias="includeParentTweet")]
    """Include parent tweet for replies"""

    include_replies: Annotated[bool, PropertyInfo(alias="includeReplies")]
    """Include reply tweets"""
