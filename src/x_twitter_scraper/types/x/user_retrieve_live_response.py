# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.broadcast import Broadcast, PeriscopeUser as BroadcastPeriscopeUser

__all__ = ["UserRetrieveLiveResponse", "Broadcast", "BroadcastPeriscopeUser"]


class UserRetrieveLiveResponse(BaseModel):
    """Says whether a user broadcasts live video on X now.

    `broadcast` is their latest broadcast, live or ended, and null when X shows none.
    """

    broadcast: Optional[Broadcast] = None
    """X broadcast, a live video"""

    live: bool
    """True while the user's latest broadcast is running."""

    user_id: str = FieldInfo(alias="userId")
    """ID of the user."""

    user_name: str = FieldInfo(alias="userName")
    """Username of the user."""
