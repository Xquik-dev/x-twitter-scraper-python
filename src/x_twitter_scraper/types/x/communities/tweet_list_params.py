# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TweetListParams"]


class TweetListParams(TypedDict, total=False):
    q: Required[str]
    """Search query"""

    cursor: str
    """Pagination cursor"""

    query_type: Annotated[str, PropertyInfo(alias="queryType")]
    """Sort order (Latest or Top)"""
