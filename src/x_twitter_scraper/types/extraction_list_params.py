# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExtractionListParams"]


class ExtractionListParams(TypedDict, total=False):
    cursor: str
    """Previous nextCursor. Offset pagination is not supported."""

    limit: int
    """Maximum items per page: 1 to 100, default 50.

    Credits can reduce paid results. The endpoint returns 402 insufficient_credits
    when none are affordable.
    """

    status: Literal["pending", "running", "canceled", "completed", "failed"]
    """Filter by job status"""

    tool_type: Annotated[
        Literal[
            "article_extractor",
            "community_extractor",
            "community_moderator_explorer",
            "community_post_extractor",
            "community_search",
            "favoriters",
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
            "user_likes",
            "user_media",
            "verified_follower_explorer",
        ],
        PropertyInfo(alias="toolType"),
    ]
    """Filter by extraction tool type"""
