# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.search_tweet import SearchTweet

__all__ = [
    "CommunityNoteListContributorDeletedNotesResponse",
    "Note",
    "NoteContributor",
    "NoteContributorNotesCount",
    "NoteContributorRatingsCount",
    "NoteContributorRatingsCountSuccessful",
    "NoteContributorRatingsCountUnsuccessful",
    "NoteEntity",
    "NoteEntityRef",
    "NotePostUnavailable",
]


class NoteContributorNotesCount(BaseModel):
    """How many notes a contributor wrote, by X's current rating."""

    awaiting_more_ratings: Optional[int] = FieldInfo(alias="awaitingMoreRatings", default=None)
    """Notes that need more ratings."""

    currently_rated_helpful: Optional[int] = FieldInfo(alias="currentlyRatedHelpful", default=None)
    """Notes X rates helpful now."""

    currently_rated_not_helpful: Optional[int] = FieldInfo(alias="currentlyRatedNotHelpful", default=None)
    """Notes X rates not helpful now."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When X last counted the notes."""


class NoteContributorRatingsCountSuccessful(BaseModel):
    """Ratings that matched the rating X gave the note."""

    helpful_count: Optional[int] = FieldInfo(alias="helpfulCount", default=None)
    """Ratings that called a note helpful."""

    not_helpful_count: Optional[int] = FieldInfo(alias="notHelpfulCount", default=None)
    """Ratings that called a note not helpful."""

    total: Optional[int] = None
    """All ratings in the group, when X sends the sum."""


class NoteContributorRatingsCountUnsuccessful(BaseModel):
    """Ratings that went against the rating X gave the note."""

    helpful_count: Optional[int] = FieldInfo(alias="helpfulCount", default=None)
    """Ratings that called a note helpful."""

    not_helpful_count: Optional[int] = FieldInfo(alias="notHelpfulCount", default=None)
    """Ratings that called a note not helpful."""

    total: Optional[int] = None
    """All ratings in the group, when X sends the sum."""


class NoteContributorRatingsCount(BaseModel):
    """How a contributor's ratings of other notes went."""

    awaiting_more_ratings: Optional[int] = FieldInfo(alias="awaitingMoreRatings", default=None)
    """Ratings on notes that need more ratings."""

    rated_after_decision: Optional[int] = FieldInfo(alias="ratedAfterDecision", default=None)
    """Ratings made after X rated the note."""

    successful: Optional[NoteContributorRatingsCountSuccessful] = None
    """Ratings that matched the rating X gave the note."""

    unsuccessful: Optional[NoteContributorRatingsCountUnsuccessful] = None
    """Ratings that went against the rating X gave the note."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When X last counted the ratings."""


class NoteContributor(BaseModel):
    """The note's writer, with the counts X sends beside a note.

    GET /x/community-notes/contributors/{alias} serves every count.
    """

    alias: str
    """The alias X gives the contributor."""

    deleted_notes_count: Optional[int] = FieldInfo(alias="deletedNotesCount", default=None)
    """Notes the contributor deleted."""

    is_api_contributor: Optional[bool] = FieldInfo(alias="isApiContributor", default=None)
    """Whether the contributor writes notes through X's API."""

    is_top_writer: Optional[bool] = FieldInfo(alias="isTopWriter", default=None)
    """Whether X marks the contributor as a top writer."""

    notes_count: Optional[NoteContributorNotesCount] = FieldInfo(alias="notesCount", default=None)
    """How many notes a contributor wrote, by X's current rating."""

    ratings_count: Optional[NoteContributorRatingsCount] = FieldInfo(alias="ratingsCount", default=None)
    """How a contributor's ratings of other notes went."""


class NoteEntityRef(BaseModel):
    """What it points at."""

    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)
    """A mentioned account's username."""

    text: Optional[str] = None
    """A hashtag's or cashtag's text."""

    type: Optional[str] = None
    """X's kind, such as TimelineUrl."""

    url: Optional[str] = None
    """The link."""

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)
    """How X opens the link, such as ExternalUrl."""


class NoteEntity(BaseModel):
    """A link, tag or account inside a note's text."""

    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)
    """Where it starts in the text."""

    ref: Optional[NoteEntityRef] = None
    """What it points at."""

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)
    """Where it ends in the text."""


class NotePostUnavailable(BaseModel):
    """Why X shows no post, when X says."""

    reason: str
    """Why X shows no post, as X names it."""


class Note(BaseModel):
    """A Community Note as its writer's page lists it, with the post it is on.

    A deleted note has no text, classification or post. A field X leaves out is left out.
    """

    id: str
    """Note ID."""

    above_pcrh_threshold: Optional[bool] = FieldInfo(alias="abovePcrhThreshold", default=None)
    """Whether the note scores above X's bar for a possible helpful rating."""

    appeal_status: Optional[str] = FieldInfo(alias="appealStatus", default=None)
    """Whether the rating is under appeal."""

    classification: Optional[str] = None
    """
    What the writer says of the post, such as MisinformedOrPotentiallyMisleading or
    NotMisleading.
    """

    contributor: Optional[NoteContributor] = None
    """The note's writer, with the counts X sends beside a note.

    GET /x/community-notes/contributors/{alias} serves every count.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the contributor wrote the note."""

    decided_by: Optional[str] = FieldInfo(alias="decidedBy", default=None)
    """The X scoring model that set the rating."""

    deleted: Optional[bool] = None
    """Whether the writer deleted the note."""

    display_url: Optional[str] = FieldInfo(alias="displayUrl", default=None)
    """The link a link note is on, as X shows it."""

    entities: Optional[List[NoteEntity]] = None
    """Links, tags & accounts inside the text, by character range."""

    fully_visible_model: Optional[bool] = FieldInfo(alias="fullyVisibleModel", default=None)
    """Whether X marks that scoring model as fully visible."""

    helpful_tags: Optional[List[str]] = FieldInfo(alias="helpfulTags", default=None)
    """Why raters called the note helpful."""

    impression_count: Optional[int] = FieldInfo(alias="impressionCount", default=None)
    """Views of the note, when X shares them."""

    is_api_author: Optional[bool] = FieldInfo(alias="isApiAuthor", default=None)
    """Whether the note came through X's API."""

    is_media_note: Optional[bool] = FieldInfo(alias="isMediaNote", default=None)
    """Whether the note is about the post's media.

    X can show such a note on other posts.
    """

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)
    """Whether X offers a translation of the note."""

    is_url_note: Optional[bool] = FieldInfo(alias="isUrlNote", default=None)
    """Whether the note is on a link."""

    language: Optional[str] = None
    """Language code of the note."""

    media_note_match_count: Optional[int] = FieldInfo(alias="mediaNoteMatchCount", default=None)
    """Other posts X matched a media note to."""

    not_helpful_tags: Optional[List[str]] = FieldInfo(alias="notHelpfulTags", default=None)
    """Why raters called the note not helpful."""

    post: Optional[SearchTweet] = None
    """The post the note is on. Null when X no longer shows it."""

    post_id: Optional[str] = FieldInfo(alias="postId", default=None)
    """ID of the post the note is on."""

    post_unavailable: Optional[NotePostUnavailable] = FieldInfo(alias="postUnavailable", default=None)
    """Why X shows no post, when X says."""

    rating_status: Optional[str] = FieldInfo(alias="ratingStatus", default=None)
    """
    X's current rating, such as NeedsMoreRatings, CurrentlyRatedHelpful or
    CurrentlyRatedNotHelpful. x.com shows only helpful notes under posts.
    """

    text: Optional[str] = None
    """What the note says."""

    time_to_helpful_from_note_ms: Optional[int] = FieldInfo(alias="timeToHelpfulFromNoteMs", default=None)
    """Milliseconds from the note's creation to its helpful rating."""

    time_to_helpful_from_post_ms: Optional[int] = FieldInfo(alias="timeToHelpfulFromPostMs", default=None)
    """Milliseconds from the post's creation to the note's helpful rating."""

    tombstone: Optional[str] = None
    """X's notice in place of a deleted note."""


class CommunityNoteListContributorDeletedNotesResponse(BaseModel):
    """1 page of Community Notes.

    Follow next_cursor while the response reports more pages.
    """

    has_next_page: bool

    next_cursor: str

    notes: List[Note]
