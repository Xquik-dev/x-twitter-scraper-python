from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.search_tweet import SearchTweet
from ..shared.paginated_tweets import PaginatedTweets

__all__ = [
    "TweetGetRepliesResponse",
    "TweetGetRepliesResponseDiagnostic",
    "TweetGetRepliesResponseDiagnosticRichness",
    "TweetGetRepliesResponseDiagnosticStrategiesAttempted",
    "TweetGetRepliesResponseNestedReply",
    "TweetGetRepliesResponseTweet",
]


class TweetGetRepliesResponseDiagnosticRichness(BaseModel):
    """Field counts across collected direct replies."""

    article: int
    """Replies with articles."""

    author: int
    """Replies with author details."""

    card: int
    """Replies with cards."""

    community_note: int = FieldInfo(alias="communityNote")
    """Replies with community notes."""

    created_at: int = FieldInfo(alias="createdAt")
    """Replies with creation timestamps."""

    engagement_counts: int = FieldInfo(alias="engagementCounts")
    """Replies with engagement counts."""

    entities: int
    """Replies with entities."""

    language: int
    """Replies with language."""

    media: int
    """Replies with media."""

    quoted_or_reposted_tweet: int = FieldInfo(alias="quotedOrRepostedTweet")
    """Replies with quotes or reposts."""

    text: int
    """Replies with text."""

    total_replies: int = FieldInfo(alias="totalReplies")
    """Unique direct replies evaluated."""

    url: int
    """Replies with canonical URLs."""


class TweetGetRepliesResponseDiagnosticStrategiesAttempted(BaseModel):
    """Reply counts & stop reason per strategy."""

    name: str

    new_direct_replies: int = FieldInfo(alias="newDirectReplies")
    """Whole number from 0."""

    new_nested_replies: int = FieldInfo(alias="newNestedReplies")
    """Whole number from 0."""

    pages_attempted: int = FieldInfo(alias="pagesAttempted")
    """Whole number from 0."""

    stop_reason: Literal[
        "deadline",
        "empty_pages",
        "error",
        "missing_cursor",
        "no_next_page",
        "page_cap",
        "partial_view",
        "repeated_cursor",
        "window_covered",
        "window_passed",
    ] = FieldInfo(alias="stopReason")

    new_direct_reply_pages: Optional[List[int]] = FieldInfo(alias="newDirectReplyPages", default=None)
    """
    For a search of the post's conversation, the page that listed each new direct
    reply, from 1.
    """


class TweetGetRepliesResponseDiagnostic(BaseModel):
    """Direct-reply coverage & collection evidence."""

    complete: bool
    """Coverage met its target, or read the whole time window, without truncation.

    Protected accounts' replies count but aren't returned.
    """

    coverage_percentage: float = FieldInfo(alias="coveragePercentage")
    """Unique direct replies / reported count, as a percentage."""

    cursor_failures: int = FieldInfo(alias="cursorFailures")
    """Cursor requests that failed."""

    duplicate_count: int = FieldInfo(alias="duplicateCount")
    """Duplicate IDs removed across pages & strategies."""

    empty_false_progress_pages: int = FieldInfo(alias="emptyFalseProgressPages")
    """Empty pages rejected for no progress."""

    malformed_count: int = FieldInfo(alias="malformedCount")
    """Malformed response items rejected."""

    missing_response_modules_or_fields: List[str] = FieldInfo(alias="missingResponseModulesOrFields")
    """Expected X modules or fields missing."""

    nested_reply_count: int = FieldInfo(alias="nestedReplyCount")
    """Unique nested replies, excluded from direct coverage."""

    pages_attempted: int = FieldInfo(alias="pagesAttempted")
    """Pages attempted across strategies."""

    recommended_fallback: str = FieldInfo(alias="recommendedFallback")
    """Recommended next action when coverage is incomplete."""

    repeated_cursor_count: int = FieldInfo(alias="repeatedCursorCount")
    """Looping cursors rejected."""

    reported_reply_count: int = FieldInfo(alias="reportedReplyCount")
    """Source post reply count."""

    response_truncated: bool = FieldInfo(alias="responseTruncated")
    """Requested row limit truncated safe results."""

    richness: TweetGetRepliesResponseDiagnosticRichness
    """Field counts across collected direct replies."""

    sources_ended: bool = FieldInfo(alias="sourcesEnded")
    """Every source ended. A retry returns the same rows."""

    strategies_attempted: List[TweetGetRepliesResponseDiagnosticStrategiesAttempted] = FieldInfo(
        alias="strategiesAttempted"
    )
    """Pagination & contribution evidence per strategy."""

    target_direct_replies: int = FieldInfo(alias="targetDirectReplies")
    """Direct replies required to meet the target."""

    unique_direct_replies: int = FieldInfo(alias="uniqueDirectReplies")
    """Unique direct replies to the source post."""

    unrelated_count: int = FieldInfo(alias="unrelatedCount")
    """Tweets rejected from other conversations."""

    reply_scope_complete: Optional[bool] = FieldInfo(alias="replyScopeComplete", default=None)
    """Replies are accounted for through the requested scope & depth.

    Source errors remain separate.
    """

    reply_tree_complete: Optional[bool] = FieldInfo(alias="replyTreeComplete", default=None)
    """All child counts are known & match collected replies."""


class TweetGetRepliesResponseNestedReply(SearchTweet):
    """Reply row. A reply the post's author hid carries hiddenByAuthor."""

    hidden_by_author: Optional[Literal[True]] = FieldInfo(alias="hiddenByAuthor", default=None)
    """Present on a reply the post's author hid.

    Complete-mode replies carry it when includeHidden asks for them.
    """


class TweetGetRepliesResponseTweet(SearchTweet):
    """Reply row. A reply the post's author hid carries hiddenByAuthor."""

    hidden_by_author: Optional[Literal[True]] = FieldInfo(alias="hiddenByAuthor", default=None)
    """Present on a reply the post's author hid.

    Complete-mode replies carry it when includeHidden asks for them.
    """


class TweetGetRepliesResponse(PaginatedTweets):
    """Direct reply rows.

    No-mode requests use resumable automatic coverage. Complete mode also returns nested replies and coverage diagnostics.
    """

    diagnostic: Optional[TweetGetRepliesResponseDiagnostic] = None
    """Direct-reply coverage & collection evidence."""

    hidden_replies: Optional[int] = FieldInfo(alias="hiddenReplies", default=None)
    """Present on the last automatic page.

    X counts this many more replies but shows them to nobody. They may be hidden,
    protected or deleted. A retry returns the same replies.
    """

    limit_reached: Optional[Literal[True]] = None
    """Present when your limit cut a complete-mode answer.

    The post has more replies; raise limit to get them all.
    """

    message: Optional[str] = None
    """Explains an answer cut by your limit."""

    nested_replies: Optional[List[TweetGetRepliesResponseNestedReply]] = None
    """Nested replies. Excluded from direct coverage."""

    order_partial: Optional[Literal[True]] = FieldInfo(alias="orderPartial", default=None)
    """Present with latest or oldest sort.

    The read stopped before it held every reply X shows. Rows stay sorted by date,
    but replies may be missing between them. Retry later for a gap-free order.
    Complete mode and automatic pages set it alike.
    """

    partial_before: Optional[datetime] = FieldInfo(alias="partialBefore", default=None)
    """
    Present on an answer that lacks replies of a large thread posted before this
    time. X shows only part of the replies older than 7 days. A retry returns about
    the same replies.
    """

    tweets: Optional[List[TweetGetRepliesResponseTweet]] = None  # type: ignore
