# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

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

    filtered_count: Optional[int] = None
