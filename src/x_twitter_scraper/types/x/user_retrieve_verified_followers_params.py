# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserRetrieveVerifiedFollowersParams"]


class UserRetrieveVerifiedFollowersParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for verified followers"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Maximum user profiles requested from this page (20-200, default 200).

    The response can contain fewer profiles because the source returned fewer or
    remaining credits cover fewer results. Keep requesting next_cursor while
    has_next_page is true. The deprecated limit and count aliases remain accepted.
    """
