from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    cursor: str
    """Previous nextCursor.

    The after alias also works. Offset pagination is not supported.
    """

    limit: int
    """Maximum items per page: 1 to 100, default 50.

    Credits can reduce paid results. With none affordable, it returns 402
    insufficient_credits.
    """
