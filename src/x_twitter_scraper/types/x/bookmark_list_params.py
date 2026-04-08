# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BookmarkListParams"]


class BookmarkListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for bookmarks"""

    folder_id: Annotated[str, PropertyInfo(alias="folderId")]
    """Optional bookmark folder ID"""
