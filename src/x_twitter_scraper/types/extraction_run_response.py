# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtractionRunResponse", "ExtractionEstimate", "Accepted"]


class ExtractionEstimate(BaseModel):
    """Free conservative cost estimate.

    Post estimates use the supported cap without a live profile lookup. It never creates a job or charges.
    """

    allowed: bool
    """Whether the balance covers the full estimate."""

    credits_available: str = FieldInfo(alias="creditsAvailable")

    credits_required: str = FieldInfo(alias="creditsRequired")

    estimated_results: int = FieldInfo(alias="estimatedResults")
    """Credit calculation row count, not source availability."""

    source: Literal[
        "followers",
        "following",
        "collection",
        "paginationCap",
        "quoteCount",
        "replyCount",
        "resultsLimit",
        "retweetCount",
        "unknown",
    ]

    resolved_x_user_id: Optional[str] = FieldInfo(alias="resolvedXUserId", default=None)
    """Resolved X user ID from count-based profile estimates."""


class Accepted(BaseModel):
    id: str

    poll_after_ms: int = FieldInfo(alias="pollAfterMs")

    status: Literal["pending", "running", "canceled", "completed", "failed"]

    status_url: str = FieldInfo(alias="statusUrl")

    tool_type: Literal[
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
    ] = FieldInfo(alias="toolType")
    """Identifier for the extraction tool used to run a job."""

    wait_url: str = FieldInfo(alias="waitUrl")


ExtractionRunResponse: TypeAlias = Union[ExtractionEstimate, Accepted]
