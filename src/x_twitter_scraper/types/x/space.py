# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .space_participant import SpaceParticipant
from ..shared.search_tweet import SearchTweet
from ..shared.user_profile import UserProfile

__all__ = ["Space", "Sharing"]


class Sharing(BaseModel):
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

    admins: List[SpaceParticipant]
    """Hosts and co-hosts"""

    listeners: List[SpaceParticipant]
    """Accounts X lists as listeners"""

    speakers: List[SpaceParticipant]
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

    sharings: Optional[List[Sharing]] = None
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
