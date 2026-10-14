from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.search_tweet import SearchTweet
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
    """Result counts and stop reason for one Tweet search strategy."""

    duplicate_count: int = FieldInfo(alias="duplicateCount")
    """Whole number from 0."""

    pages_fetched: int = FieldInfo(alias="pagesFetched")
    """Whole number from 0."""

    query_type: Literal["Latest", "Top"] = FieldInfo(alias="queryType")

    stop_reason: Literal[
        "cursor_failure", "deadline", "exhausted", "failed", "page_limit", "result_limit", "stalled"
    ] = FieldInfo(alias="stopReason")
    """Reason a coverage strategy stopped."""

    strategy: int

    unique_added: int = FieldInfo(alias="uniqueAdded")
    """Whole number from 0."""

    window: Optional[TweetSearchCoverageResponseDiagnosticStrategyWindow] = None
    """Non-overlapping time partition used by one strategy."""


class TweetSearchCoverageResponseDiagnostic(BaseModel):
    """Coverage evidence across parallel search strategies."""

    complete: bool
    """True after all active strategies exhaust their sources.

    An empty read of the whole search window also ends its time slices.
    """

    cursor_failure_count: int = FieldInfo(alias="cursorFailureCount")
    """Whole number from 0."""

    deadline_reached: bool = FieldInfo(alias="deadlineReached")

    duplicate_count: int = FieldInfo(alias="duplicateCount")
    """Whole number from 0."""

    failed_strategy_count: int = FieldInfo(alias="failedStrategyCount")
    """Whole number from 0."""

    malformed_count: int = FieldInfo(alias="malformedCount")
    """Whole number from 0."""

    pages_fetched: int = FieldInfo(alias="pagesFetched")
    """Whole number from 0."""

    partitioned: bool
    """Whether bounded time windows ran in parallel."""

    response_truncated: bool = FieldInfo(alias="responseTruncated")
    """True when credits or the requested limit reduce output."""

    result_limit_reached: bool = FieldInfo(alias="resultLimitReached")

    returned_tweets: int = FieldInfo(alias="returnedTweets")

    stalled_strategy_count: int = FieldInfo(alias="stalledStrategyCount")
    """Whole number from 0."""

    strategies: List[TweetSearchCoverageResponseDiagnosticStrategy]

    strategy_count: int = FieldInfo(alias="strategyCount")

    unique_tweets: int = FieldInfo(alias="uniqueTweets")


class TweetSearchCoverageResponse(PaginatedTweets):
    """Terminal Tweet search coverage response with diagnostics."""

    tweets: List[SearchTweet]

    diagnostic: TweetSearchCoverageResponseDiagnostic
    """Coverage evidence across parallel search strategies."""

    has_next_page: Optional[Literal[False]] = None  # type: ignore

    next_cursor: Optional[Literal[""]] = None  # type: ignore


TweetSearchResponse: TypeAlias = Union[PaginatedTweets, TweetSearchCoverageResponse]
