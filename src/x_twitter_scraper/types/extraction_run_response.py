# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtractionRunResponse"]


class ExtractionRunResponse(BaseModel):
    id: str

    status: Literal["running"]

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
