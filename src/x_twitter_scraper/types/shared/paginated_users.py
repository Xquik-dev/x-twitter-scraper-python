# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .user_profile import UserProfile

__all__ = ["PaginatedUsers"]


class PaginatedUsers(BaseModel):
    """Profile coverage preserves shape, billing, aliases, and filters.

    Follow next_cursor while the response reports more pages. Unprefixed cursors remain legacy.
    """

    has_next_page: bool

    next_cursor: str

    users: List[UserProfile]

    end_reason: Optional[Literal["stalled"]] = FieldInfo(alias="endReason", default=None)
    """Present on a last page that X cut short.

    `stalled` means X returned no new results 2 times in a row, so the list may hold more.
    """

    filtered_count: Optional[int] = None
    """Whole number from 0."""
