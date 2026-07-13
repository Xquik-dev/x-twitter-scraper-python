# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
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
    ]
    """Identifier for the extraction tool used to run a job."""

    advanced_query: Annotated[str, PropertyInfo(alias="advancedQuery")]
    """Raw advanced search query appended as-is (tweet_search_extractor)"""

    any_words: Annotated[str, PropertyInfo(alias="anyWords")]
    """Words or quoted phrases where any one can match.

    Separate with spaces, commas, or lines. (tweet_search_extractor)
    """

    bounding_box: Annotated[str, PropertyInfo(alias="boundingBox")]
    """Geo bounding box, e.g. -74.1 40.6 -73.9 40.8 (tweet_search_extractor)"""

    cashtags: str
    """Cashtags separated by spaces, commas, or lines. (tweet_search_extractor)"""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """Conversation ID filter (tweet_search_extractor)"""

    exact_phrase: Annotated[str, PropertyInfo(alias="exactPhrase")]
    """Exact phrase to match (tweet_search_extractor)"""

    exclude_words: Annotated[str, PropertyInfo(alias="excludeWords")]
    """Words or quoted phrases to exclude.

    Separate with spaces, commas, or lines. (tweet_search_extractor)
    """

    from_user: Annotated[str, PropertyInfo(alias="fromUser")]
    """Filter by author username (tweet_search_extractor)"""

    hashtags: str
    """Hashtags separated by spaces, commas, or lines. (tweet_search_extractor)"""

    in_reply_to_tweet_id: Annotated[str, PropertyInfo(alias="inReplyToTweetId")]
    """Only replies to this tweet ID (tweet_search_extractor)"""

    language: str
    """Language code filter (tweet_search_extractor)"""

    list_id: Annotated[str, PropertyInfo(alias="listId")]
    """Search within a list ID (tweet_search_extractor)"""

    media_type: Annotated[
        Literal["images", "videos", "gifs", "media", "links", "none"], PropertyInfo(alias="mediaType")
    ]
    """Media type filter (tweet_search_extractor)"""

    mentioning: str
    """Filter tweets mentioning a username (tweet_search_extractor)"""

    min_faves: Annotated[int, PropertyInfo(alias="minFaves")]
    """Minimum likes threshold (tweet_search_extractor)"""

    min_quotes: Annotated[int, PropertyInfo(alias="minQuotes")]
    """Minimum quote count threshold (tweet_search_extractor)"""

    min_replies: Annotated[int, PropertyInfo(alias="minReplies")]
    """Minimum replies threshold (tweet_search_extractor)"""

    min_retweets: Annotated[int, PropertyInfo(alias="minRetweets")]
    """Minimum retweets threshold (tweet_search_extractor)"""

    place: str
    """Search within a place ID (tweet_search_extractor)"""

    place_country: Annotated[str, PropertyInfo(alias="placeCountry")]
    """Search within a country code (tweet_search_extractor)"""

    point_radius: Annotated[str, PropertyInfo(alias="pointRadius")]
    """Geo point radius, e.g. -73.99 40.73 25mi (tweet_search_extractor)"""

    quotes: Literal["include", "exclude", "only"]
    """Quote mode (tweet_search_extractor)"""

    quotes_of_tweet_id: Annotated[str, PropertyInfo(alias="quotesOfTweetId")]
    """Only quotes of this tweet ID (tweet_search_extractor)"""

    replies: Literal["include", "exclude", "only"]
    """Reply mode (tweet_search_extractor)"""

    results_limit: Annotated[int, PropertyInfo(alias="resultsLimit")]
    """Maximum number of results to extract.

    When set, the extraction stops after reaching this limit.
    """

    retweets: Literal["include", "exclude", "only"]
    """Retweet mode (tweet_search_extractor)"""

    retweets_of_tweet_id: Annotated[str, PropertyInfo(alias="retweetsOfTweetId")]
    """Only retweets of this tweet ID (tweet_search_extractor)"""

    search_query: Annotated[str, PropertyInfo(alias="searchQuery")]
    """Required for tweet_search_extractor & community_search."""

    since_date: Annotated[Union[str, date], PropertyInfo(alias="sinceDate", format="iso8601")]
    """Start date YYYY-MM-DD (tweet_search_extractor)"""

    target_community_id: Annotated[str, PropertyInfo(alias="targetCommunityId")]
    """Required for community_post_extractor & community_search."""

    target_list_id: Annotated[str, PropertyInfo(alias="targetListId")]
    """
    Required for list_follower_explorer, list_member_extractor &
    list_post_extractor.
    """

    target_space_id: Annotated[str, PropertyInfo(alias="targetSpaceId")]
    """Required for space_explorer."""

    target_tweet_id: Annotated[str, PropertyInfo(alias="targetTweetId")]

    target_username: Annotated[str, PropertyInfo(alias="targetUsername")]

    to_user: Annotated[str, PropertyInfo(alias="toUser")]
    """Filter replies sent to a username (tweet_search_extractor)"""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """End date YYYY-MM-DD (tweet_search_extractor)"""

    url: str
    """URL substring or domain filter (tweet_search_extractor)"""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only verified authors (tweet_search_extractor)"""
