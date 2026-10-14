# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TweetSearchParams"]


class TweetSearchParams(TypedDict, total=False):
    q: Required[str]
    """Query, Tweet ID, or URL.

    Alias query. Hyphens negate terms. Use exactPhrase for literals. Valid bounds
    apply per page. `since:` & `until:` dates are UTC days, written YYYY-MM-DD.
    25/12/2026 & 12/25/2026 also work, since each has 1 reading. 04/01/2026 has 2 &
    answers 424 with the form to write. `since_time:` & `until_time:` take Unix
    seconds or an ISO 8601 time. `list:` takes a public List's ID. A private List
    answers 404 list_not_found. X searches up to 512 characters. A longer query
    answers 424 before any read, unless a term of its first OR group fits alone.
    """

    advanced_query: Annotated[str, PropertyInfo(alias="advancedQuery")]
    """Raw advanced search query appended as-is."""

    any_words: Annotated[str, PropertyInfo(alias="anyWords")]
    """Words or quoted phrases where any one can match.

    Separate with spaces, commas, or lines.
    """

    blue_verified_only: Annotated[bool, PropertyInfo(alias="blueVerifiedOnly")]
    """Only return tweets from Blue-verified authors."""

    bounding_box: Annotated[str, PropertyInfo(alias="boundingBox")]
    """Geo bounding box, e.g. -74.1 40.6 -73.9 40.8."""

    card_name: Annotated[str, PropertyInfo(alias="cardName")]
    """Keep only Tweets with this card type, such as poll2choice_text_only.

    Tweet search checks each Tweet's card.
    """

    cashtags: str
    """Cashtags separated by spaces, commas, or lines."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """Conversation ID filter."""

    cursor: str
    """Cursor from the previous response.

    Existing unprefixed cursors keep legacy standard behavior. Pages can be empty
    before more rows; follow next_cursor. Also read as next_cursor, next_token,
    pagination_token or continuation_token.
    """

    exact_phrase: Annotated[str, PropertyInfo(alias="exactPhrase")]
    """Match this literal phrase, including any hyphens."""

    exclude_source: Annotated[str, PropertyInfo(alias="excludeSource")]
    """X search no longer supports excludeSource.

    A Tweet search with it answers 424 & charges nothing.
    """

    exclude_words: Annotated[str, PropertyInfo(alias="excludeWords")]
    """Words or quoted phrases to exclude. Separate with spaces, commas, or lines."""

    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    from_user: Annotated[str, PropertyInfo(alias="fromUser")]
    """Filter by author username."""

    geocode: str
    """X search no longer supports geocode.

    A Tweet search with it answers 424 & charges nothing.
    """

    hashtags: str
    """Hashtags separated by spaces, commas, or lines."""

    in_reply_to_tweet_id: Annotated[str, PropertyInfo(alias="inReplyToTweetId")]
    """Only replies to this tweet ID."""

    keywords: str
    """Words the Tweets must match, in X search syntax."""

    language: str
    """Filter by language. Alias `lang` is accepted."""

    limit: int
    """Most unique matches to return after filtering.

    Default 20; explicit coverage defaults to 2000. At the deadline it returns kept
    rows & diagnostics. Only returned rows are billed; credits can cut results, & 0
    affordable rows returns 402. Aliases: pageSize, count, max_results, maxItems,
    max_items & per_page.
    """

    list_id: Annotated[str, PropertyInfo(alias="listId")]
    """Search within a list ID."""

    max_faves: Annotated[int, PropertyInfo(alias="maxFaves")]
    """Maximum likes threshold. maxLikes & max_likes also work."""

    max_id: Annotated[str, PropertyInfo(alias="maxId")]
    """Return Tweets at or below this ID."""

    max_quotes: Annotated[int, PropertyInfo(alias="maxQuotes")]
    """Maximum quotes threshold."""

    max_replies: Annotated[int, PropertyInfo(alias="maxReplies")]
    """Maximum replies threshold."""

    max_retweets: Annotated[int, PropertyInfo(alias="maxRetweets")]
    """Maximum retweets threshold."""

    media_type: Annotated[
        Literal["images", "videos", "gifs", "media", "links", "none"], PropertyInfo(alias="mediaType")
    ]
    """Filter media. Aliases: has_video, has_media."""

    mentioning: str
    """Filter tweets mentioning a username."""

    min_bookmarks: Annotated[int, PropertyInfo(alias="minBookmarks")]
    """Minimum bookmark count threshold."""

    min_likes: Annotated[int, PropertyInfo(alias="minLikes")]
    """Minimum likes. Aliases: minFaves, min_likes, min_faves."""

    min_quotes: Annotated[int, PropertyInfo(alias="minQuotes")]
    """Minimum quote count threshold."""

    min_replies: Annotated[int, PropertyInfo(alias="minReplies")]
    """Minimum replies threshold."""

    min_retweets: Annotated[int, PropertyInfo(alias="minRetweets")]
    """Minimum retweets threshold."""

    min_views: Annotated[int, PropertyInfo(alias="minViews")]
    """Minimum view count threshold."""

    mode: Literal["standard", "coverage"]
    """Omit mode for resumable maximum coverage.

    Standard keeps legacy pagination. Coverage returns diagnostics once and rejects
    cursors.
    """

    native_retweets: Annotated[bool, PropertyInfo(alias="nativeRetweets")]
    """Only return native reposts."""

    near: str
    """Match a place name."""

    news: bool
    """X no longer searches filter:news."""

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    place: str
    """Search within a place ID."""

    place_country: Annotated[str, PropertyInfo(alias="placeCountry")]
    """Search within a country code."""

    point_radius: Annotated[str, PropertyInfo(alias="pointRadius")]
    """Geo point radius, e.g. -73.99 40.73 25mi."""

    query_type: Annotated[str, PropertyInfo(alias="queryType")]
    """Latest lists posts newest first.

    Top keeps X's engagement ranking within each read. Xquik reads several of X's
    views, so a later page can hold a post X ranks higher. Top skips posts X shows
    above a ranked reply that cannot match the query. They cost nothing. Any case
    works. Photos, Videos & Media read Latest with mediaType images, videos or
    media, unless mediaType is set. People & Lists answer 400 & point to
    /x/users/search & /x/lists/search. Aliases result_type, sort_order, type,
    search_type, product, category & section.
    """

    quotes: Literal["include", "exclude", "only"]
    """Only when the caller requests a quote mode."""

    quotes_of_tweet_id: Annotated[str, PropertyInfo(alias="quotesOfTweetId")]
    """Only quotes of this tweet ID."""

    replies: Literal["include", "exclude", "only"]
    """Reply mode. Exclude keeps own-thread replies."""

    retweets: Literal["include", "exclude", "only"]
    """Only when the caller requests a repost mode."""

    retweets_of_tweet_id: Annotated[str, PropertyInfo(alias="retweetsOfTweetId")]
    """Only retweets of this tweet ID."""

    safe: bool
    """Enable the safe-search filter."""

    since_date: Annotated[Union[str, date], PropertyInfo(alias="sinceDate", format="iso8601")]
    """Start date as a UTC day, written YYYY-MM-DD.

    25/12/2026 & 12/25/2026 also work, since each has 1 reading. A date that fits
    both orders reads month first, so 04/01/2026 is 1 April.
    """

    since_id: Annotated[str, PropertyInfo(alias="sinceId")]
    """Return Tweets whose IDs exceed this ID."""

    since_time: Annotated[str, PropertyInfo(alias="sinceTime")]
    """Inclusive ISO bound for Tweet creation time, such as 2026-09-25T19:20:41Z.

    Unix seconds also work. A time without an offset is UTC.
    """

    source: str
    """X search no longer supports source.

    A Tweet search with it answers 424 & charges nothing.
    """

    to_user: Annotated[str, PropertyInfo(alias="toUser")]
    """Filter replies sent to a username."""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """End date as a UTC day, inclusive, so its own posts count.

    It takes the same date forms as sinceDate.
    """

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """Exclusive ISO bound for Tweet creation time.

    Unix seconds also work. A time without an offset is UTC.
    """

    url: str
    """URL substring or domain filter."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only return tweets from verified authors."""

    within: str
    """X search no longer supports within.

    A Tweet search with it answers 424 & charges nothing. Use near alone.
    """

    within_time: Annotated[str, PropertyInfo(alias="withinTime")]
    """Keeps Tweets from a recent window, such as 90m or 7d.

    Use a whole number & s, m, h or d.
    """
