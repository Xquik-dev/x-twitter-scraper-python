# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.paginated_tweets import PaginatedTweets

__all__ = [
    "TweetSearchResponse",
    "TweetSearchCoverageResponse",
    "TweetSearchCoverageResponseDiagnostic",
    "TweetSearchCoverageResponseDiagnosticStrategy",
    "TweetSearchCoverageResponseDiagnosticStrategyWindow",
]


class TweetSearchCoverageResponseDiagnosticStrategyWindow(BaseModel):
    """Non-overlapping time partition used by one strategy."""

    since_time: datetime = FieldInfo(alias="sinceTime")

    until_time: datetime = FieldInfo(alias="untilTime")


class TweetSearchCoverageResponseDiagnosticStrategy(BaseModel):
    duplicate_count: int = FieldInfo(alias="duplicateCount")

    pages_fetched: int = FieldInfo(alias="pagesFetched")

    query_type: Literal["Latest", "Top"] = FieldInfo(alias="queryType")

    stop_reason: Literal[
        "cursor_failure", "deadline", "exhausted", "failed", "page_limit", "result_limit", "stalled"
    ] = FieldInfo(alias="stopReason")

    strategy: int

    unique_added: int = FieldInfo(alias="uniqueAdded")

    window: Optional[TweetSearchCoverageResponseDiagnosticStrategyWindow] = None
    """Non-overlapping time partition used by one strategy."""


class TweetSearchCoverageResponseDiagnostic(BaseModel):
    """Coverage evidence across parallel search strategies."""

    complete: bool
    """True when every strategy exhausted its source."""

    cursor_failure_count: int = FieldInfo(alias="cursorFailureCount")

    deadline_reached: bool = FieldInfo(alias="deadlineReached")

    duplicate_count: int = FieldInfo(alias="duplicateCount")

    failed_strategy_count: int = FieldInfo(alias="failedStrategyCount")

    malformed_count: int = FieldInfo(alias="malformedCount")

    pages_fetched: int = FieldInfo(alias="pagesFetched")

    partitioned: bool
    """Whether bounded time windows ran in parallel."""

    response_truncated: bool = FieldInfo(alias="responseTruncated")
    """Whether credits or the requested limit reduced output."""

    result_limit_reached: bool = FieldInfo(alias="resultLimitReached")

    returned_tweets: int = FieldInfo(alias="returnedTweets")

    stalled_strategy_count: int = FieldInfo(alias="stalledStrategyCount")

    strategies: List[TweetSearchCoverageResponseDiagnosticStrategy]

    strategy_count: int = FieldInfo(alias="strategyCount")

    unique_tweets: int = FieldInfo(alias="uniqueTweets")


class TweetSearchCoverageResponse(PaginatedTweets):
    """
    No-mode search, user Tweet, user reply, and direct reply reads use automatic coverage. Shape, filters, aliases, and billing stay compatible. Unprefixed cursors remain legacy. Follow next_cursor while has_next_page is true. An empty filtered page can still have has_next_page true.
    """

    diagnostic: TweetSearchCoverageResponseDiagnostic
    """Coverage evidence across parallel search strategies."""

    has_next_page: Optional[Literal[False]] = None  # type: ignore

    next_cursor: Optional[Literal[""]] = None  # type: ignore


TweetSearchResponse: TypeAlias = Union["PaginatedTweets", TweetSearchCoverageResponse]

from ..shared.paginated_tweets import PaginatedTweets
