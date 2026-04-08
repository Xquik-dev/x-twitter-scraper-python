# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExtractionRunParams"]


class ExtractionRunParams(TypedDict, total=False):
    tool_type: Required[
        Annotated[
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
    ]
    """Identifier for the extraction tool used to run a job."""

    advanced_query: Annotated[str, PropertyInfo(alias="advancedQuery")]
    """Raw advanced search query appended as-is (tweet_search_extractor)"""

    exact_phrase: Annotated[str, PropertyInfo(alias="exactPhrase")]
    """Exact phrase to match (tweet_search_extractor)"""

    exclude_words: Annotated[str, PropertyInfo(alias="excludeWords")]
    """Words to exclude from results (tweet_search_extractor)"""

    search_query: Annotated[str, PropertyInfo(alias="searchQuery")]

    target_community_id: Annotated[str, PropertyInfo(alias="targetCommunityId")]

    target_list_id: Annotated[str, PropertyInfo(alias="targetListId")]

    target_space_id: Annotated[str, PropertyInfo(alias="targetSpaceId")]

    target_tweet_id: Annotated[str, PropertyInfo(alias="targetTweetId")]

    target_username: Annotated[str, PropertyInfo(alias="targetUsername")]
