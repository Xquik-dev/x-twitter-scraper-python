# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtractionListResponse", "Extraction"]


class Extraction(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    status: Literal["running", "completed", "failed"]

    tool_type: Literal[
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
    ] = FieldInfo(alias="toolType")

    total_results: int = FieldInfo(alias="totalResults")

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)


class ExtractionListResponse(BaseModel):
    extractions: List[Extraction]

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
