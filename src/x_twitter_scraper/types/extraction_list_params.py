# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExtractionListParams"]


class ExtractionListParams(TypedDict, total=False):
    after: str
    """Cursor for keyset pagination"""

    limit: int
    """Maximum number of items to return (1-100, default 50)"""

    status: Literal["running", "completed", "failed"]
    """Filter by job status"""

    tool_type: Annotated[
        Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
            "follower_explorer",
            "following_explorer",
            "list_follower_explorer",
            "list_member_extractor",
            "list_post_extractor",
            "mention_extractor",
            "people_search",
            "post_extractor",
            "quote_extractor",
            "reply_extractor",
            "repost_extractor",
            "space_explorer",
            "thread_extractor",
            "tweet_search_extractor",
            "verified_follower_explorer",
        ],
        PropertyInfo(alias="toolType"),
    ]
    """Filter by extraction tool type"""
