# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.search_tweet import SearchTweet
from ..shared.user_profile import UserProfile

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


class SpaceAdminAffiliatesHighlightedLabel(BaseModel):
    """Organization affiliation label shown on an X profile."""

    badge_url: Optional[str] = FieldInfo(alias="badgeUrl", default=None)

    description: Optional[str] = None

    long_description: Optional[Dict[str, object]] = FieldInfo(alias="longDescription", default=None)
    """Public text, ranges, references, and mention data."""

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)

    user_label_display_type: Optional[str] = FieldInfo(alias="userLabelDisplayType", default=None)

    user_label_type: Optional[str] = FieldInfo(alias="userLabelType", default=None)


class SpaceAdmin(BaseModel):
    """An account on a Space's stage or in its audience, as X lists it there."""

    id: str

    name: str
    """Name the account shows in the Space"""

    username: str

    affiliates_highlighted_label: Optional[SpaceAdminAffiliatesHighlightedLabel] = FieldInfo(
        alias="affiliatesHighlightedLabel", default=None
    )
    """Organization affiliation label shown on an X profile."""

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)
    """Whether the account has X Premium verification"""

    is_muted_by_admin: Optional[bool] = FieldInfo(alias="isMutedByAdmin", default=None)
    """Whether a host muted the account"""

    is_muted_by_guest: Optional[bool] = FieldInfo(alias="isMutedByGuest", default=None)
    """Whether the account muted itself"""

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether X shows a verified badge in the Space"""

    joined_at: Optional[datetime] = FieldInfo(alias="joinedAt", default=None)
    """When the account joined the Space"""

    periscope_user_id: Optional[str] = FieldInfo(alias="periscopeUserId", default=None)
    """The account's ID in X's broadcast service"""

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)
    """Profile picture URL"""

    profile_picture_original: Optional[str] = FieldInfo(alias="profilePictureOriginal", default=None)
    """The participant's profile picture at full size"""

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)
    """Business or Government badge type"""


class SpaceListenerAffiliatesHighlightedLabel(BaseModel):
    """Organization affiliation label shown on an X profile."""

    badge_url: Optional[str] = FieldInfo(alias="badgeUrl", default=None)

    description: Optional[str] = None

    long_description: Optional[Dict[str, object]] = FieldInfo(alias="longDescription", default=None)
    """Public text, ranges, references, and mention data."""

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)

    user_label_display_type: Optional[str] = FieldInfo(alias="userLabelDisplayType", default=None)

    user_label_type: Optional[str] = FieldInfo(alias="userLabelType", default=None)


class SpaceListener(BaseModel):
    """An account on a Space's stage or in its audience, as X lists it there."""

    id: str

    name: str
    """Name the account shows in the Space"""

    username: str

    affiliates_highlighted_label: Optional[SpaceListenerAffiliatesHighlightedLabel] = FieldInfo(
        alias="affiliatesHighlightedLabel", default=None
    )
    """Organization affiliation label shown on an X profile."""

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)
    """Whether the account has X Premium verification"""

    is_muted_by_admin: Optional[bool] = FieldInfo(alias="isMutedByAdmin", default=None)
    """Whether a host muted the account"""

    is_muted_by_guest: Optional[bool] = FieldInfo(alias="isMutedByGuest", default=None)
    """Whether the account muted itself"""

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether X shows a verified badge in the Space"""

    joined_at: Optional[datetime] = FieldInfo(alias="joinedAt", default=None)
    """When the account joined the Space"""

    periscope_user_id: Optional[str] = FieldInfo(alias="periscopeUserId", default=None)
    """The account's ID in X's broadcast service"""

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)
    """Profile picture URL"""

    profile_picture_original: Optional[str] = FieldInfo(alias="profilePictureOriginal", default=None)
    """The participant's profile picture at full size"""

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)
    """Business or Government badge type"""


class SpaceSpeakerAffiliatesHighlightedLabel(BaseModel):
    """Organization affiliation label shown on an X profile."""

    badge_url: Optional[str] = FieldInfo(alias="badgeUrl", default=None)

    description: Optional[str] = None

    long_description: Optional[Dict[str, object]] = FieldInfo(alias="longDescription", default=None)
    """Public text, ranges, references, and mention data."""

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)

    user_label_display_type: Optional[str] = FieldInfo(alias="userLabelDisplayType", default=None)

    user_label_type: Optional[str] = FieldInfo(alias="userLabelType", default=None)


class SpaceSpeaker(BaseModel):
    """An account on a Space's stage or in its audience, as X lists it there."""

    id: str

    name: str
    """Name the account shows in the Space"""

    username: str

    affiliates_highlighted_label: Optional[SpaceSpeakerAffiliatesHighlightedLabel] = FieldInfo(
        alias="affiliatesHighlightedLabel", default=None
    )
    """Organization affiliation label shown on an X profile."""

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)
    """Whether the account has X Premium verification"""

    is_muted_by_admin: Optional[bool] = FieldInfo(alias="isMutedByAdmin", default=None)
    """Whether a host muted the account"""

    is_muted_by_guest: Optional[bool] = FieldInfo(alias="isMutedByGuest", default=None)
    """Whether the account muted itself"""

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether X shows a verified badge in the Space"""

    joined_at: Optional[datetime] = FieldInfo(alias="joinedAt", default=None)
    """When the account joined the Space"""

    periscope_user_id: Optional[str] = FieldInfo(alias="periscopeUserId", default=None)
    """The account's ID in X's broadcast service"""

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)
    """Profile picture URL"""

    profile_picture_original: Optional[str] = FieldInfo(alias="profilePictureOriginal", default=None)
    """The participant's profile picture at full size"""

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)
    """Business or Government badge type"""


class SpaceSharing(BaseModel):
    """A post shared in a Space, & the account that shared it."""

    id: Optional[str] = None
    """X's ID of the sharing, not of the post"""

    shared_at: Optional[datetime] = FieldInfo(alias="sharedAt", default=None)
    """When the post was shared"""

    shared_by: Optional[UserProfile] = FieldInfo(alias="sharedBy", default=None)
    """Public X profile."""

    tweet: Optional[SearchTweet] = None
    """Search tweet with author. Zero metrics may mean X omitted counts."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When X last changed the sharing"""


class Space(BaseModel):
    """X Space"""

    id: str
    """Space ID"""

    admins: List[SpaceAdmin]
    """Hosts and co-hosts"""

    listeners: List[SpaceListener]
    """Accounts X lists as listeners"""

    speakers: List[SpaceSpeaker]
    """Accounts X lists as speakers"""

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)
    """Audio or video kind, as X names it"""

    conversation_controls: Optional[int] = FieldInfo(alias="conversationControls", default=None)
    """X's code for who may speak"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the Space was made"""

    creator: Optional[UserProfile] = None
    """Public X profile."""

    disallow_join: Optional[bool] = FieldInfo(alias="disallowJoin", default=None)
    """Whether X lets no more accounts join"""

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)
    """When the Space ended"""

    is_available_for_clipping: Optional[bool] = FieldInfo(alias="isAvailableForClipping", default=None)
    """Whether listeners may clip the Space"""

    is_available_for_replay: Optional[bool] = FieldInfo(alias="isAvailableForReplay", default=None)
    """Whether X offers a recording"""

    is_employee_only: Optional[bool] = FieldInfo(alias="isEmployeeOnly", default=None)
    """Whether only X employees may join"""

    is_locked: Optional[bool] = FieldInfo(alias="isLocked", default=None)
    """Whether the host locked the Space"""

    max_admin_capacity: Optional[int] = FieldInfo(alias="maxAdminCapacity", default=None)
    """Most hosts and co-hosts the Space allows"""

    media_key: Optional[str] = FieldInfo(alias="mediaKey", default=None)
    """X's media key for the Space's audio"""

    mentioned_user_ids: Optional[List[str]] = FieldInfo(alias="mentionedUserIds", default=None)
    """IDs of the accounts the host tagged"""

    no_incognito: Optional[bool] = FieldInfo(alias="noIncognito", default=None)
    """Whether anonymous listening is off"""

    participant_count: Optional[int] = FieldInfo(alias="participantCount", default=None)
    """Accounts in the Space now, while it is live"""

    scheduled_start: Optional[datetime] = FieldInfo(alias="scheduledStart", default=None)
    """When the Space was set to start"""

    sharings: Optional[List[SpaceSharing]] = None
    """Posts the hosts and speakers shared in the Space, in X's order.

    Present only when X lists them.
    """

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """When the Space went live"""

    state: Optional[str] = None
    """
    NotStarted (scheduled), Running (live), Ended, Canceled (scheduled, never
    started) or TimedOut (closed by X, not by its host)
    """

    title: Optional[str] = None
    """Space title"""

    total_live_listeners: Optional[int] = FieldInfo(alias="totalLiveListeners", default=None)
    """Accounts that listened live"""

    total_replay_watched: Optional[int] = FieldInfo(alias="totalReplayWatched", default=None)
    """Accounts that played the recording"""

    tweet: Optional[SearchTweet] = None
    """Search tweet with author. Zero metrics may mean X omitted counts."""

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)
    """ID of the post that announces the Space"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When X last changed the Space"""


class SpaceSearchResponse(BaseModel):
    has_next_page: bool

    next_cursor: str

    spaces: List[Space]
    """Public Spaces, in the order the posts share them"""
