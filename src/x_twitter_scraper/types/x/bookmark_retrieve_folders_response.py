# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BookmarkRetrieveFoldersResponse", "Folder", "FolderMedia", "FolderMediaPalette", "FolderMediaPaletteRgb"]


class FolderMediaPaletteRgb(BaseModel):
    blue: Optional[float] = None

    green: Optional[float] = None

    red: Optional[float] = None


class FolderMediaPalette(BaseModel):
    percentage: Optional[float] = None

    rgb: Optional[FolderMediaPaletteRgb] = None


class FolderMedia(BaseModel):
    """Public folder cover image metadata."""

    id: Optional[str] = None
    """Media object ID."""

    media_id: Optional[str] = FieldInfo(alias="mediaId", default=None)
    """Media ID."""

    media_key: Optional[str] = FieldInfo(alias="mediaKey", default=None)
    """Stable media key."""

    original_image_height: Optional[int] = FieldInfo(alias="originalImageHeight", default=None)
    """Original image height."""

    original_image_url: Optional[str] = FieldInfo(alias="originalImageUrl", default=None)
    """Original image URL."""

    original_image_width: Optional[int] = FieldInfo(alias="originalImageWidth", default=None)
    """Original image width."""

    palette: Optional[List[FolderMediaPalette]] = None
    """Dominant image colors and their proportions."""

    type: Optional[str] = None
    """Media object type."""


class Folder(BaseModel):
    """Bookmark folder and its optional public cover image."""

    id: str
    """Folder ID."""

    media: Optional[FolderMedia] = None
    """Public folder cover image metadata."""

    name: Optional[str] = None
    """Folder name."""


class BookmarkRetrieveFoldersResponse(BaseModel):
    folders: List[Folder]

    has_next_page: bool
    """Whether another folder page is available"""

    next_cursor: str
    """Cursor for the next folder page"""
