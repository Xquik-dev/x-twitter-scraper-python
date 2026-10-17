# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

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
    "SpaceRetrieveResponse",
    "Space",
    "SpaceAdmin",
    "SpaceAdminAffiliatesHighlightedLabel",
    "SpaceListener",
    "SpaceListenerAffiliatesHighlightedLabel",
    "SpaceSpeaker",
    "SpaceSpeakerAffiliatesHighlightedLabel",
    "SpaceSharing",
]


class SpaceRetrieveResponse(BaseModel):
    space: Space
    """X Space"""
