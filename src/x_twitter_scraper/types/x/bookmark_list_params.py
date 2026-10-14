# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BookmarkListParams"]


class BookmarkListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for bookmarks.

    Also read as next_cursor, next_token, pagination_token or continuation_token.
    """

    folder_id: Annotated[str, PropertyInfo(alias="folderId")]
    """Optional bookmark folder ID. Folders need X Premium."""
