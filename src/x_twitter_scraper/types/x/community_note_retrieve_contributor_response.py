# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from ..._models import BaseModel
from .community_notes_contributor import (
    NotesCount as ContributorNotesCount,
    RatingsCount as ContributorRatingsCount,
    CommunityNotesContributor,
    CommunityNotesContributor as Contributor,
)
from .community_notes_rating_outcome import (
    CommunityNotesRatingOutcome as ContributorRatingsCountSuccessful,
    CommunityNotesRatingOutcome as ContributorRatingsCountUnsuccessful,
)

__all__ = [
    "CommunityNoteRetrieveContributorResponse",
    "Contributor",
    "ContributorNotesCount",
    "ContributorRatingsCount",
    "ContributorRatingsCountSuccessful",
    "ContributorRatingsCountUnsuccessful",
]


class CommunityNoteRetrieveContributorResponse(BaseModel):
    contributor: CommunityNotesContributor
    """A Community Notes contributor.

    X names contributors by an alias, never by their X account. A field X leaves out
    is left out. Beside a note, X sends its writer with only some of the counts.
    """
