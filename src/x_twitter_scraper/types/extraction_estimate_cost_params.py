# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ExtractionEstimateCostParams", "RelationTarget", "Target", "TargetUnionMember1"]


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
    """Raw advanced search query appended as-is (tweet_search_extractor)"""

    any_words: Annotated[str, PropertyInfo(alias="anyWords")]
    """Any matching term or phrase (tweet_search_extractor)."""

    bio_contains: Annotated[str, PropertyInfo(alias="bioContains")]
    """Bio terms separated by commas or lines."""

    blue_verified_only: Annotated[bool, PropertyInfo(alias="blueVerifiedOnly")]
    """Return only Blue-verified Tweet authors."""

    bounding_box: Annotated[str, PropertyInfo(alias="boundingBox")]
    """Geo bounding box, e.g. -74.1 40.6 -73.9 40.8 (tweet_search_extractor)"""

    card_name: Annotated[str, PropertyInfo(alias="cardName")]
    """Require Tweet cards whose name matches this value."""

    cashtags: str
    """Matching cashtags (tweet_search_extractor)."""

    collection_strategy: Annotated[
        Literal["auto", "complete", "direct", "search", "thread"], PropertyInfo(alias="collectionStrategy")
    ]
    """Reply collection strategy."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """Conversation ID filter (tweet_search_extractor)"""

    dedupe_across_targets: Annotated[bool, PropertyInfo(alias="dedupeAcrossTargets")]
    """Merge duplicate results across collection targets."""

    dedupe_mode: Annotated[Literal["none", "first", "merge"], PropertyInfo(alias="dedupeMode")]
    """Keep target duplicates, first rows, or merged overlap."""

    exact_phrase: Annotated[str, PropertyInfo(alias="exactPhrase")]
    """Exact phrase to match (tweet_search_extractor)"""

    exclude_original_author: Annotated[bool, PropertyInfo(alias="excludeOriginalAuthor")]
    """Exclude replies from the source author."""

    exclude_source: Annotated[str, PropertyInfo(alias="excludeSource")]
    """Drop Tweets from this source application."""

    exclude_words: Annotated[str, PropertyInfo(alias="excludeWords")]
    """Excluded terms or phrases (tweet_search_extractor)."""

    from_user: Annotated[str, PropertyInfo(alias="fromUser")]
    """Filter by author username (tweet_search_extractor)"""

    geocode: str
    """Restrict Tweets by latitude, longitude, and radius."""

    hashtags: str
    """Matching hashtags (tweet_search_extractor)."""

    has_location: Annotated[bool, PropertyInfo(alias="hasLocation")]
    """Require a profile location."""

    has_media_only: Annotated[bool, PropertyInfo(alias="hasMediaOnly")]
    """Return only replies with media."""

    has_website: Annotated[bool, PropertyInfo(alias="hasWebsite")]
    """Require a profile website."""

    include_original_post: Annotated[bool, PropertyInfo(alias="includeOriginalPost")]
    """Include the source post in reply results."""

    include_search_terms: Annotated[bool, PropertyInfo(alias="includeSearchTerms")]
    """Add matching search terms to collection metadata."""

    include_target_metadata: Annotated[bool, PropertyInfo(alias="includeTargetMetadata")]
    """Add source target metadata to each result."""

    in_reply_to_tweet_id: Annotated[str, PropertyInfo(alias="inReplyToTweetId")]
    """Only replies to this tweet ID (tweet_search_extractor)"""

    language: str
    """Tweet or Community search language."""

    list_id: Annotated[str, PropertyInfo(alias="listId")]
    """Search within a list ID (tweet_search_extractor)"""

    location_contains: Annotated[str, PropertyInfo(alias="locationContains")]
    """Required profile location text."""

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum nested reply depth."""

    max_followers: Annotated[int, PropertyInfo(alias="maxFollowers")]
    """Maximum follower count for profile results."""

    max_following: Annotated[int, PropertyInfo(alias="maxFollowing")]
    """Maximum following count for profile results."""

    max_id: Annotated[str, PropertyInfo(alias="maxId")]
    """Require Tweets older than this ID."""

    max_items_per_target: Annotated[int, PropertyInfo(alias="maxItemsPerTarget")]
    """Maximum results collected for each target."""

    max_likes: Annotated[int, PropertyInfo(alias="maxLikes")]
    """Maximum Tweet like count."""

    max_pages_per_target: Annotated[int, PropertyInfo(alias="maxPagesPerTarget")]
    """Reply pages collected for each target."""

    max_posts: Annotated[int, PropertyInfo(alias="maxPosts")]
    """Maximum post count for profile results."""

    max_quotes: Annotated[int, PropertyInfo(alias="maxQuotes")]
    """Maximum Tweet quote count."""

    max_replies: Annotated[int, PropertyInfo(alias="maxReplies")]
    """Maximum Tweet reply count."""

    max_retweets: Annotated[int, PropertyInfo(alias="maxRetweets")]
    """Maximum Tweet repost count."""

    media_type: Annotated[
        Literal["images", "videos", "gifs", "media", "links", "none"], PropertyInfo(alias="mediaType")
    ]
    """Tweet or Community search media."""

    mentioning: str
    """Mentions this username (tweet_search_extractor)."""

    min_account_age_days: Annotated[int, PropertyInfo(alias="minAccountAgeDays")]
    """Minimum profile age in days."""

    min_bookmarks: Annotated[int, PropertyInfo(alias="minBookmarks")]
    """Minimum Tweet bookmark count."""

    min_faves: Annotated[int, PropertyInfo(alias="minFaves")]
    """Tweet or Community search minimum likes."""

    min_followers: Annotated[int, PropertyInfo(alias="minFollowers")]
    """Minimum follower count for profile results."""

    min_following: Annotated[int, PropertyInfo(alias="minFollowing")]
    """Minimum following count for profile results."""

    min_posts: Annotated[int, PropertyInfo(alias="minPosts")]
    """Minimum post count for profile results."""

    min_quotes: Annotated[int, PropertyInfo(alias="minQuotes")]
    """Minimum quote count threshold (tweet_search_extractor)"""

    min_replies: Annotated[int, PropertyInfo(alias="minReplies")]
    """Tweet or Community search minimum replies."""

    min_retweets: Annotated[int, PropertyInfo(alias="minRetweets")]
    """Tweet or Community search minimum reposts."""

    min_views: Annotated[int, PropertyInfo(alias="minViews")]
    """Tweet or Community search minimum views."""

    native_retweets: Annotated[bool, PropertyInfo(alias="nativeRetweets")]
    """Tweet or Community search native reposts."""

    near: str
    """Restrict Tweet search to this place name."""

    news: bool
    """Require news-classified Tweet results."""

    overlap_mode: Annotated[bool, PropertyInfo(alias="overlapMode")]
    """Shortcut for dedupeMode=merge."""

    place: str
    """Search within a place ID (tweet_search_extractor)"""

    place_country: Annotated[str, PropertyInfo(alias="placeCountry")]
    """Search within a country code (tweet_search_extractor)"""

    point_radius: Annotated[str, PropertyInfo(alias="pointRadius")]
    """Geo point radius, e.g. -73.99 40.73 25mi (tweet_search_extractor)"""

    query_type: Annotated[Literal["Latest", "Top", "Both", "relevance"], PropertyInfo(alias="queryType")]
    """Use Top for engagement. The relevance alias maps to Top."""

    quotes: Literal["include", "exclude", "only"]
    """Choose whether tweet search includes, excludes, or isolates quotes."""

    quotes_of_tweet_id: Annotated[str, PropertyInfo(alias="quotesOfTweetId")]
    """Only quotes of this tweet ID (tweet_search_extractor)"""

    relation_targets: Annotated[Iterable[RelationTarget], PropertyInfo(alias="relationTargets")]
    """Profile relations processed within one job."""

    replies: Literal["include", "exclude", "only"]
    """Choose whether tweet search includes, excludes, or isolates replies."""

    results_limit: Annotated[int, PropertyInfo(alias="resultsLimit")]
    """Maximum unique results to emit.

    Billing follows emitted results, not this upper bound.
    """

    retweets: Literal["include", "exclude", "only"]
    """Choose whether tweet search includes, excludes, or isolates reposts."""

    retweets_of_tweet_id: Annotated[str, PropertyInfo(alias="retweetsOfTweetId")]
    """Only retweets of this tweet ID (tweet_search_extractor)"""

    safe: bool
    """Apply safe-search filtering to Tweet results."""

    scope: Literal["all", "direct", "nested"]
    """Reply depth scope."""

    search_queries: Annotated[SequenceNotStr[str], PropertyInfo(alias="searchQueries")]
    """Search queries processed as one collection job."""

    search_query: Annotated[str, PropertyInfo(alias="searchQuery")]
    """Required for tweet_search_extractor & community_search. Passed unchanged."""

    since_date: Annotated[Union[str, date], PropertyInfo(alias="sinceDate", format="iso8601")]
    """Tweet or Community search start date."""

    since_id: Annotated[str, PropertyInfo(alias="sinceId")]
    """Require Tweets newer than this ID."""

    since_time: Annotated[Union[Union[str, datetime], int], PropertyInfo(alias="sinceTime", format="iso8601")]
    """Reply start time as ISO 8601 or Unix seconds."""

    sort: Literal["relevance", "latest", "oldest", "likes"]
    """Reply result order."""

    source: str
    """Require Tweets from this source application."""

    start_cursor: Annotated[str, PropertyInfo(alias="startCursor")]
    """Resume one reply target from this cursor."""

    target_community_id: Annotated[str, PropertyInfo(alias="targetCommunityId")]
    """Required for community_post_extractor & community_search."""

    target_community_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="targetCommunityIds")]
    """Community IDs processed as one collection job."""

    target_list_id: Annotated[str, PropertyInfo(alias="targetListId")]
    """
    Required for list_follower_explorer, list_member_extractor &
    list_post_extractor.
    """

    target_list_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="targetListIds")]
    """List IDs processed as one collection job."""

    targets: SequenceNotStr[Target]
    """Mixed targets auto-routed within one job.

    Use tweet, replies, quotes, thread, or profile_media kinds to collect attached
    media.
    """

    target_space_id: Annotated[str, PropertyInfo(alias="targetSpaceId")]
    """Required for space_explorer."""

    target_tweet_id: Annotated[str, PropertyInfo(alias="targetTweetId")]

    target_tweet_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="targetTweetIds")]
    """Tweet IDs processed as one collection job."""

    target_username: Annotated[str, PropertyInfo(alias="targetUsername")]

    target_usernames: Annotated[SequenceNotStr[str], PropertyInfo(alias="targetUsernames")]
    """Usernames processed concurrently in one job.

    With tweet_search_extractor, each username collects posts.
    """

    to_user: Annotated[str, PropertyInfo(alias="toUser")]
    """Replies to this username (tweet_search_extractor)."""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """Tweet or Community search end date."""

    until_time: Annotated[Union[Union[str, datetime], int], PropertyInfo(alias="untilTime", format="iso8601")]
    """Reply end time as ISO 8601 or Unix seconds."""

    url: str
    """URL substring or domain filter (tweet_search_extractor)"""

    username_contains: Annotated[str, PropertyInfo(alias="usernameContains")]
    """Required username text."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Tweet or Community search verified authors."""

    verified_type: Annotated[str, PropertyInfo(alias="verifiedType")]
    """Exact profile verification type."""

    within: str
    """Set the radius around the requested place."""

    within_time: Annotated[str, PropertyInfo(alias="withinTime")]
    """Restrict Tweets to this recent time window."""


class RelationTarget(TypedDict, total=False):
    """One target and relation in a mixed profile collection."""

    relation: Required[
        Literal["community_members", "followers", "following", "list_followers", "list_members", "verified_followers"]
    ]

    value: Required[str]


class TargetUnionMember1(TypedDict, total=False):
    kind: Required[
        Literal[
            "favoriters",
            "list",
            "profile",
            "profile_likes",
            "profile_media",
            "profile_replies",
            "quotes",
            "replies",
            "retweeters",
            "search",
            "thread",
            "tweet",
        ]
    ]

    value: Required[str]


Target: TypeAlias = Union[str, TargetUnionMember1]
