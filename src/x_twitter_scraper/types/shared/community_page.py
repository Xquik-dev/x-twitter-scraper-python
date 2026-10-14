# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from ..._models import BaseModel
from .community import Community

__all__ = ["CommunityPage"]


class CommunityPage(BaseModel):
    """1 page of X Communities, in X's order."""

    communities: List[Community]
    """Communities in X's order"""

    has_next_page: bool
    """Whether another page of communities follows"""

    next_cursor: str
    """Cursor for the next page of communities. Empty at the end."""
