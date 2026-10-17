# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from ..._models import BaseModel
from ..shared.broadcast import Broadcast, PeriscopeUser as BroadcastPeriscopeUser

__all__ = ["BroadcastRetrieveResponse", "Broadcast", "BroadcastPeriscopeUser"]


class BroadcastRetrieveResponse(BaseModel):
    broadcast: Broadcast
    """X broadcast, a live video"""
