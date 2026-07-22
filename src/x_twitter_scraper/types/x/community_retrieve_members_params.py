# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunityRetrieveMembersParams"]


class CommunityRetrieveMembersParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Items per page (20-200, default 20).

    This is an upper bound for paid authenticated calls: remaining credits can
    reduce the returned page size, and zero affordable results returns 402
    insufficient_credits.
    """
