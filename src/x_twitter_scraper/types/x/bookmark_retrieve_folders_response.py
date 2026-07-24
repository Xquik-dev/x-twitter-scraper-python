# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["BookmarkRetrieveFoldersResponse", "Folder"]


class Folder(BaseModel):
    id: str

    name: str


class BookmarkRetrieveFoldersResponse(BaseModel):
    folders: List[Folder]

    has_next_page: bool
    """Always false for the current bookmark folder route"""

    next_cursor: str
    """Always empty for the current bookmark folder route"""
