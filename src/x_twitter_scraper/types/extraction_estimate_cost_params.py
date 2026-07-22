# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExtractionEstimateCostParams"]


class ExtractionEstimateCostParams(TypedDict, total=False):
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
    """Raw advanced query string appended to the estimate (tweet_search_extractor)"""

    any_words: Annotated[str, PropertyInfo(alias="anyWords")]
    """Alternative words or quoted phrases for estimated results.

    Separate with spaces, commas, or lines.
    """

    bounding_box: Annotated[str, PropertyInfo(alias="boundingBox")]
    """Geo bounding box used for estimation, e.g.

    -74.1 40.6 -73.9 40.8 (tweet_search_extractor)
    """

    cashtags: str
    """Cashtags applied to the estimate, separated by spaces, commas, or lines."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """Conversation ID filter used for estimation (tweet_search_extractor)"""

    exact_phrase: Annotated[str, PropertyInfo(alias="exactPhrase")]
    """Exact phrase filter for search estimation"""

    exclude_words: Annotated[str, PropertyInfo(alias="excludeWords")]
    """Words or quoted phrases excluded from estimated results.

    Separate with spaces, commas, or lines.
    """

    from_user: Annotated[str, PropertyInfo(alias="fromUser")]
    """Estimate only tweets from this author username (tweet_search_extractor)"""

    hashtags: str
    """Hashtags applied to the estimate, separated by spaces, commas, or lines."""

    in_reply_to_tweet_id: Annotated[str, PropertyInfo(alias="inReplyToTweetId")]
    """Estimate only replies to this tweet ID (tweet_search_extractor)"""

    language: str
    """Language code used for estimate filtering (tweet_search_extractor)"""

    list_id: Annotated[str, PropertyInfo(alias="listId")]
    """Estimate search results within this list ID (tweet_search_extractor)"""

    media_type: Annotated[
        Literal["images", "videos", "gifs", "media", "links", "none"], PropertyInfo(alias="mediaType")
    ]
    """Media type used for estimate filtering (tweet_search_extractor)"""

    mentioning: str
    """Estimate tweets mentioning this username (tweet_search_extractor)"""

    min_faves: Annotated[int, PropertyInfo(alias="minFaves")]
    """Minimum likes threshold for estimated results (tweet_search_extractor)"""

    min_quotes: Annotated[int, PropertyInfo(alias="minQuotes")]
    """Minimum quote count threshold for estimated results (tweet_search_extractor)"""

    min_replies: Annotated[int, PropertyInfo(alias="minReplies")]
    """Minimum replies threshold for estimated results (tweet_search_extractor)"""

    min_retweets: Annotated[int, PropertyInfo(alias="minRetweets")]
    """Minimum retweets threshold for estimated results (tweet_search_extractor)"""

    place: str
    """Estimate search results within this place ID (tweet_search_extractor)"""

    place_country: Annotated[str, PropertyInfo(alias="placeCountry")]
    """Estimate search results within this country code (tweet_search_extractor)"""

    point_radius: Annotated[str, PropertyInfo(alias="pointRadius")]
    """Geo point radius used for estimation, e.g.

    -73.99 40.73 25mi (tweet_search_extractor)
    """

    quotes: Literal["include", "exclude", "only"]
    """Quote mode used for estimation (tweet_search_extractor)"""

    quotes_of_tweet_id: Annotated[str, PropertyInfo(alias="quotesOfTweetId")]
    """Estimate only quotes of this tweet ID (tweet_search_extractor)"""

    replies: Literal["include", "exclude", "only"]
    """Reply mode used for estimation (tweet_search_extractor)"""

    results_limit: Annotated[int, PropertyInfo(alias="resultsLimit")]
    """Maximum number of results to estimate.

    When set, the estimate caps projected results to this value.
    """

    retweets: Literal["include", "exclude", "only"]
    """Retweet mode used for estimation (tweet_search_extractor)"""

    retweets_of_tweet_id: Annotated[str, PropertyInfo(alias="retweetsOfTweetId")]
    """Estimate only retweets of this tweet ID (tweet_search_extractor)"""

    search_query: Annotated[str, PropertyInfo(alias="searchQuery")]
    """Query used to price tweet_search_extractor or community_search."""

    since_date: Annotated[Union[str, date], PropertyInfo(alias="sinceDate", format="iso8601")]
    """Estimate start date in YYYY-MM-DD format (tweet_search_extractor)"""

    target_community_id: Annotated[str, PropertyInfo(alias="targetCommunityId")]
    """Community ID used to price community_post_extractor or community_search."""

    target_list_id: Annotated[str, PropertyInfo(alias="targetListId")]
    """
    List ID used to price list_follower_explorer, list_member_extractor, or
    list_post_extractor.
    """

    target_space_id: Annotated[str, PropertyInfo(alias="targetSpaceId")]
    """Space ID used to price space_explorer."""

    target_tweet_id: Annotated[str, PropertyInfo(alias="targetTweetId")]

    target_username: Annotated[str, PropertyInfo(alias="targetUsername")]

    to_user: Annotated[str, PropertyInfo(alias="toUser")]
    """Estimate replies sent to this username (tweet_search_extractor)"""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """Estimate end date in YYYY-MM-DD format (tweet_search_extractor)"""

    url: str
    """URL substring or domain filter used for estimation (tweet_search_extractor)"""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Estimate only verified authors (tweet_search_extractor)"""
