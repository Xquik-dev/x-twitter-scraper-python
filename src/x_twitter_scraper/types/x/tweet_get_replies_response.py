# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.paginated_tweets import PaginatedTweets

__all__ = [
    "TweetGetRepliesResponse",
    "TweetGetRepliesResponseDiagnostic",
    "TweetGetRepliesResponseDiagnosticRichness",
    "TweetGetRepliesResponseDiagnosticStrategiesAttempted",
]


class TweetGetRepliesResponseDiagnosticRichness(BaseModel):
    """Field-presence counts across the collected direct replies."""

    article: int
    """Replies with article content."""

    author: int
    """Replies with author details."""

    card: int
    """Replies with card metadata."""

    community_note: int = FieldInfo(alias="communityNote")
    """Replies with community-note data."""

    created_at: int = FieldInfo(alias="createdAt")
    """Replies with a creation timestamp."""

    engagement_counts: int = FieldInfo(alias="engagementCounts")
    """Replies with engagement counts."""

    entities: int
    """Replies with entity metadata."""

    language: int
    """Replies with a language value."""

    media: int
    """Replies with media metadata."""

    quoted_or_reposted_tweet: int = FieldInfo(alias="quotedOrRepostedTweet")
    """Replies with quoted or reposted tweet data."""

    text: int
    """Replies with text."""

    total_replies: int = FieldInfo(alias="totalReplies")
    """Total unique direct replies evaluated for richness."""

    url: int
    """Replies with a canonical URL."""


class TweetGetRepliesResponseDiagnosticStrategiesAttempted(BaseModel):
    name: str

    new_direct_replies: int = FieldInfo(alias="newDirectReplies")

    new_nested_replies: int = FieldInfo(alias="newNestedReplies")

    pages_attempted: int = FieldInfo(alias="pagesAttempted")

    stop_reason: Literal[
        "deadline", "empty_pages", "error", "missing_cursor", "no_next_page", "page_cap", "repeated_cursor"
    ] = FieldInfo(alias="stopReason")


class TweetGetRepliesResponseDiagnostic(BaseModel):
    """Evidence for direct-reply coverage and collector behavior."""

    complete: bool
    """Whether coverage met the target without truncation."""

    coverage_percentage: float = FieldInfo(alias="coveragePercentage")
    """Unique direct replies as a percentage of the reported count."""

    cursor_failures: int = FieldInfo(alias="cursorFailures")
    """Cursor requests that failed."""

    duplicate_count: int = FieldInfo(alias="duplicateCount")
    """Duplicate tweet IDs removed across pages and strategies."""

    empty_false_progress_pages: int = FieldInfo(alias="emptyFalseProgressPages")
    """Empty pages rejected because they did not make progress."""

    malformed_count: int = FieldInfo(alias="malformedCount")
    """Malformed response items rejected."""

    missing_response_modules_or_fields: List[str] = FieldInfo(alias="missingResponseModulesOrFields")
    """Expected response modules or fields missing from X."""

    nested_reply_count: int = FieldInfo(alias="nestedReplyCount")
    """Unique nested replies kept outside direct coverage."""

    pages_attempted: int = FieldInfo(alias="pagesAttempted")
    """Total pages attempted across all strategies."""

    recommended_fallback: str = FieldInfo(alias="recommendedFallback")
    """Recommended next action when coverage is incomplete."""

    repeated_cursor_count: int = FieldInfo(alias="repeatedCursorCount")
    """Repeated cursors rejected to prevent loops."""

    reported_reply_count: int = FieldInfo(alias="reportedReplyCount")
    """Reply count reported on the source post."""

    response_truncated: bool = FieldInfo(alias="responseTruncated")
    """Whether the requested row limit truncated safe results."""

    richness: TweetGetRepliesResponseDiagnosticRichness
    """Field-presence counts across the collected direct replies."""

    strategies_attempted: List[TweetGetRepliesResponseDiagnosticStrategiesAttempted] = FieldInfo(
        alias="strategiesAttempted"
    )
    """Per-strategy pagination and contribution evidence."""

    target_direct_replies: int = FieldInfo(alias="targetDirectReplies")
    """Minimum direct replies required for the coverage target."""

    unique_direct_replies: int = FieldInfo(alias="uniqueDirectReplies")
    """Unique replies whose parent ID equals the source post ID."""

    unrelated_count: int = FieldInfo(alias="unrelatedCount")
    """Tweets rejected because they belonged elsewhere."""


class TweetGetRepliesResponse(PaginatedTweets):
    """Direct reply rows.

    No-mode requests use resumable automatic coverage. Complete mode also returns nested replies and coverage diagnostics. Keep nested replies separate from direct coverage.
    """

    diagnostic: Optional[TweetGetRepliesResponseDiagnostic] = None
    """Evidence for direct-reply coverage and collector behavior."""

    nested_replies: Optional[List["SearchTweet"]] = None
    """Nested replies. Excluded from direct coverage."""


from ..shared.search_tweet import SearchTweet
