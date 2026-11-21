# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from ..._models import BaseModel

__all__ = ["CommunityUnavailable"]


class CommunityUnavailable(BaseModel):
    """Why X shows no Community for the post."""

    reason: str
    """X's reason, as X writes it."""
