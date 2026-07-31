# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunityRetrieveSearchParams"]


class CommunityRetrieveSearchParams(TypedDict, total=False):
    community_id: Required[Annotated[str, PropertyInfo(alias="communityId")]]
    """Numeric ID of the community whose posts to search"""

    q: Required[str]
    """Search query"""

    cursor: str
    """Pagination cursor for community search"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Maximum page items (1-100, default 20).

    Source, filters, or credits can reduce results. Continue while has_next_page is
    true. Deprecated limit and count aliases remain accepted.
    """

    query_type: Annotated[Literal["Latest", "Top"], PropertyInfo(alias="queryType")]
    """Sort order (Latest or Top)"""
