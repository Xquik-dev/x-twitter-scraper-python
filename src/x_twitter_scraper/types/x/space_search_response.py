# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from .space import Space, Sharing as SpaceSharing
from ..._models import BaseModel
from .space_participant import (
    SpaceParticipant as SpaceAdmin,
    SpaceParticipant as SpaceListener,
    SpaceParticipant as SpaceSpeaker,
    AffiliatesHighlightedLabel as SpaceAdminAffiliatesHighlightedLabel,
    AffiliatesHighlightedLabel as SpaceListenerAffiliatesHighlightedLabel,
    AffiliatesHighlightedLabel as SpaceSpeakerAffiliatesHighlightedLabel,
)

__all__ = [
    "SpaceSearchResponse",
    "Space",
    "SpaceAdmin",
    "SpaceAdminAffiliatesHighlightedLabel",
    "SpaceListener",
    "SpaceListenerAffiliatesHighlightedLabel",
    "SpaceSpeaker",
    "SpaceSpeakerAffiliatesHighlightedLabel",
    "SpaceSharing",
]


class SpaceSearchResponse(BaseModel):
    has_next_page: bool

    next_cursor: str

    spaces: List[Space]
    """Public Spaces, in the order the posts share them"""
