# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from ..._models import BaseModel

__all__ = ["UserRetrieveFollowerIdsResponse"]


class UserRetrieveFollowerIdsResponse(BaseModel):
    """A page of user IDs without profiles.

    Follow next_cursor while the response reports more pages.
    """

    has_next_page: bool

    ids: List[str]
    """X user IDs, newest relationship first."""

    next_cursor: str
