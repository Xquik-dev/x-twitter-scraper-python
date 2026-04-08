# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DraftListParams"]


class DraftListParams(TypedDict, total=False):
    after_cursor: Annotated[str, PropertyInfo(alias="afterCursor")]
    """Cursor for pagination"""

    limit: int
    """Maximum number of items to return (1-100, default 50)"""
