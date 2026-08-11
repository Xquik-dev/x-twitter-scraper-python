# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.paginated_users import PaginatedUsers

__all__ = [
    "UserRetrieveVerifiedFollowersResponse",
    "UserListCoverageResponse",
    "UserListCoverageResponseDiagnostic",
    "UserListCoverageResponseDiagnosticStrategy",
]


class UserListCoverageResponseDiagnosticStrategy(BaseModel):
    duplicate_count: int = FieldInfo(alias="duplicateCount")

    pages_fetched: int = FieldInfo(alias="pagesFetched")

    stop_reason: Literal[
        "cursor_failure", "deadline", "exhausted", "failed", "page_limit", "result_limit", "stalled"
    ] = FieldInfo(alias="stopReason")

    strategy: int

    unique_added: int = FieldInfo(alias="uniqueAdded")


class UserListCoverageResponseDiagnostic(BaseModel):
    """Coverage evidence across parallel relationship strategies."""

    complete: bool
    """True when every strategy exhausted its source."""

    cursor_failure_count: int = FieldInfo(alias="cursorFailureCount")

    deadline_reached: bool = FieldInfo(alias="deadlineReached")

    duplicate_count: int = FieldInfo(alias="duplicateCount")

    failed_strategy_count: int = FieldInfo(alias="failedStrategyCount")

    malformed_count: int = FieldInfo(alias="malformedCount")

    pages_fetched: int = FieldInfo(alias="pagesFetched")

    response_truncated: bool = FieldInfo(alias="responseTruncated")
    """Whether credits or the requested limit reduced output."""

    result_limit_reached: bool = FieldInfo(alias="resultLimitReached")

    returned_users: int = FieldInfo(alias="returnedUsers")

    stalled_strategy_count: int = FieldInfo(alias="stalledStrategyCount")

    strategies: List[UserListCoverageResponseDiagnosticStrategy]

    strategy_count: int = FieldInfo(alias="strategyCount")

    unique_users: int = FieldInfo(alias="uniqueUsers")


class UserListCoverageResponse(PaginatedUsers):
    """Paginated user profiles.

    No-mode follower, following, and verified follower requests merge independent views automatically. Response fields, page size, aliases, filters, and per-returned-profile billing stay unchanged. Existing unprefixed cursors retain legacy behavior. Follow next_cursor while has_next_page is true.
    """

    diagnostic: UserListCoverageResponseDiagnostic
    """Coverage evidence across parallel relationship strategies."""

    has_next_page: Optional[Literal[False]] = None  # type: ignore

    next_cursor: Optional[Literal[""]] = None  # type: ignore


UserRetrieveVerifiedFollowersResponse: TypeAlias = Union[PaginatedUsers, UserListCoverageResponse]
