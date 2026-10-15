# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CommunityNoteRetrieveContributorResponse",
    "Contributor",
    "ContributorNotesCount",
    "ContributorRatingsCount",
    "ContributorRatingsCountSuccessful",
    "ContributorRatingsCountUnsuccessful",
]


class ContributorNotesCount(BaseModel):
    """How many notes a contributor wrote, by X's current rating."""

    awaiting_more_ratings: Optional[int] = FieldInfo(alias="awaitingMoreRatings", default=None)
    """Notes that need more ratings."""

    currently_rated_helpful: Optional[int] = FieldInfo(alias="currentlyRatedHelpful", default=None)
    """Notes X rates helpful now."""

    currently_rated_not_helpful: Optional[int] = FieldInfo(alias="currentlyRatedNotHelpful", default=None)
    """Notes X rates not helpful now."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When X last counted the notes."""


class ContributorRatingsCountSuccessful(BaseModel):
    """Ratings that matched the rating X gave the note."""

    helpful_count: Optional[int] = FieldInfo(alias="helpfulCount", default=None)
    """Ratings that called a note helpful."""

    not_helpful_count: Optional[int] = FieldInfo(alias="notHelpfulCount", default=None)
    """Ratings that called a note not helpful."""

    total: Optional[int] = None
    """All ratings in the group, when X sends the sum."""


class ContributorRatingsCountUnsuccessful(BaseModel):
    """Ratings that went against the rating X gave the note."""

    helpful_count: Optional[int] = FieldInfo(alias="helpfulCount", default=None)
    """Ratings that called a note helpful."""

    not_helpful_count: Optional[int] = FieldInfo(alias="notHelpfulCount", default=None)
    """Ratings that called a note not helpful."""

    total: Optional[int] = None
    """All ratings in the group, when X sends the sum."""


class ContributorRatingsCount(BaseModel):
    """How a contributor's ratings of other notes went."""

    awaiting_more_ratings: Optional[int] = FieldInfo(alias="awaitingMoreRatings", default=None)
    """Ratings on notes that need more ratings."""

    rated_after_decision: Optional[int] = FieldInfo(alias="ratedAfterDecision", default=None)
    """Ratings made after X rated the note."""

    successful: Optional[ContributorRatingsCountSuccessful] = None
    """Ratings that matched the rating X gave the note."""

    unsuccessful: Optional[ContributorRatingsCountUnsuccessful] = None
    """Ratings that went against the rating X gave the note."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When X last counted the ratings."""


class Contributor(BaseModel):
    """A Community Notes contributor.

    X names contributors by an alias, never by their X account. A field X leaves out is left out. Beside a note, X sends its writer with only some of the counts.
    """

    alias: str
    """The alias X gives the contributor."""

    deleted_notes_count: Optional[int] = FieldInfo(alias="deletedNotesCount", default=None)
    """Notes the contributor deleted."""

    is_api_contributor: Optional[bool] = FieldInfo(alias="isApiContributor", default=None)
    """Whether the contributor writes notes through X's API."""

    is_top_writer: Optional[bool] = FieldInfo(alias="isTopWriter", default=None)
    """Whether X marks the contributor as a top writer."""

    notes_count: Optional[ContributorNotesCount] = FieldInfo(alias="notesCount", default=None)
    """How many notes a contributor wrote, by X's current rating."""

    ratings_count: Optional[ContributorRatingsCount] = FieldInfo(alias="ratingsCount", default=None)
    """How a contributor's ratings of other notes went."""


class CommunityNoteRetrieveContributorResponse(BaseModel):
    contributor: Contributor
    """A Community Notes contributor.

    X names contributors by an alias, never by their X account. A field X leaves out
    is left out. Beside a note, X sends its writer with only some of the counts.
    """
