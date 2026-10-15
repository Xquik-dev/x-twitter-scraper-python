from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.paginated_users import PaginatedUsers

__all__ = [
    "ListRetrieveMembersResponse",
    "UserListPage",
    "UserListPageScanLimit",
    "UserListCoverageResponse",
    "UserListCoverageResponseDiagnostic",
    "UserListCoverageResponseDiagnosticStrategy",
]


class UserListPageScanLimit(BaseModel):
    """Present on the last page of a filtered automatic read that sent no maxScan, once the list scanned 100,000 profiles across its pages.

    That page is the list's last.
    """

    limit: Literal[100000]
    """The profiles a filtered read scans of a list without maxScan."""

    message: str
    """What stopped the list & how to read further."""

    rows_read: int = FieldInfo(alias="rowsRead")
    """Profiles the list read across its pages, kept or dropped by the filters.

    The last page may read past the limit.
    """


class UserListPage(PaginatedUsers):
    """A relationship page.

    A filtered read's last page may name the scan limit that ended it.
    """

    scan_limit: Optional[UserListPageScanLimit] = FieldInfo(alias="scanLimit", default=None)
    """
    Present on the last page of a filtered automatic read that sent no maxScan, once
    the list scanned 100,000 profiles across its pages. That page is the list's
    last.
    """


class UserListCoverageResponseDiagnosticStrategy(BaseModel):
    """Result counts and stop reason for one relationship strategy."""

    duplicate_count: int = FieldInfo(alias="duplicateCount")
    """Whole number from 0."""

    pages_fetched: int = FieldInfo(alias="pagesFetched")
    """Whole number from 0."""

    stop_reason: Literal[
        "cursor_failure", "deadline", "exhausted", "failed", "page_limit", "result_limit", "stalled"
    ] = FieldInfo(alias="stopReason")
    """Reason a coverage strategy stopped."""

    strategy: int

    unique_added: int = FieldInfo(alias="uniqueAdded")
    """Whole number from 0."""


class UserListCoverageResponseDiagnostic(BaseModel):
    """Coverage evidence across parallel relationship strategies."""

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

    response_truncated: bool = FieldInfo(alias="responseTruncated")
    """True when credits or the requested limit reduce output."""

    result_limit_reached: bool = FieldInfo(alias="resultLimitReached")

    returned_users: int = FieldInfo(alias="returnedUsers")

    stalled_strategy_count: int = FieldInfo(alias="stalledStrategyCount")
    """Whole number from 0."""

    strategies: List[UserListCoverageResponseDiagnosticStrategy]

    strategy_count: int = FieldInfo(alias="strategyCount")

    unique_users: int = FieldInfo(alias="uniqueUsers")


class UserListCoverageResponse(PaginatedUsers):
    """Terminal relationship coverage response with diagnostics."""

    diagnostic: UserListCoverageResponseDiagnostic
    """Coverage evidence across parallel relationship strategies."""

    has_next_page: Optional[Literal[False]] = None  # type: ignore

    next_cursor: Optional[Literal[""]] = None  # type: ignore


ListRetrieveMembersResponse: TypeAlias = Union[UserListPage, UserListCoverageResponse]
