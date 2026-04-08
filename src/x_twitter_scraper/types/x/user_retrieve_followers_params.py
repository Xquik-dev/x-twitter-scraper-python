# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserRetrieveFollowersParams"]


class UserRetrieveFollowersParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for followers list"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Items per page (20-200, default 200)"""
