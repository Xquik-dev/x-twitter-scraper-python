# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .search_tweet import SearchTweet
from .user_profile import UserProfile

__all__ = ["Broadcast", "PeriscopeUser"]


class PeriscopeUser(BaseModel):
    """Broadcaster, as X's live video service names the account"""

    id: Optional[str] = None
    """Live video account ID"""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Live video display name"""

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)
    """Live video avatar URL"""

    profile_picture_original: Optional[str] = FieldInfo(alias="profilePictureOriginal", default=None)
    """The broadcaster's avatar at full size"""

    username: Optional[str] = None
    """Live video username"""


class Broadcast(BaseModel):
    """X broadcast, a live video"""

    id: str
    """Broadcast ID"""

    camera_rotation: Optional[int] = FieldInfo(alias="cameraRotation", default=None)
    """Camera rotation in degrees"""

    chat_option: Optional[int] = FieldInfo(alias="chatOption", default=None)
    """X's code for who may chat"""

    creator: Optional[UserProfile] = None
    """Public X profile."""

    ended_at: Optional[datetime] = FieldInfo(alias="endedAt", default=None)
    """When the broadcast ended"""

    height: Optional[int] = None
    """Video height in pixels"""

    is_available_for_replay: Optional[bool] = FieldInfo(alias="isAvailableForReplay", default=None)
    """Whether X offers a recording of the broadcast"""

    is_high_latency: Optional[bool] = FieldInfo(alias="isHighLatency", default=None)
    """Whether the video stream runs in high-latency mode"""

    is_private_chat: Optional[bool] = FieldInfo(alias="isPrivateChat", default=None)
    """Whether X marks the chat private"""

    is_title_edited: Optional[bool] = FieldInfo(alias="isTitleEdited", default=None)
    """Whether the broadcaster edited the title of the replay"""

    last_ping_at: Optional[datetime] = FieldInfo(alias="lastPingAt", default=None)
    """When the video stream last reached X"""

    media_key: Optional[str] = FieldInfo(alias="mediaKey", default=None)
    """X's media key for the video"""

    periscope_user: Optional[PeriscopeUser] = FieldInfo(alias="periscopeUser", default=None)
    """Broadcaster, as X's live video service names the account"""

    pre_live_slate_url: Optional[str] = FieldInfo(alias="preLiveSlateUrl", default=None)
    """Image X shows before the broadcast starts"""

    scheduled_start: Optional[datetime] = FieldInfo(alias="scheduledStart", default=None)
    """When the broadcast was set to start"""

    source: Optional[str] = None
    """What produced the video stream, as X names it"""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """When the broadcast went live"""

    state: Optional[str] = None
    """Such as NotStarted, Running or Ended, as X names it"""

    title: Optional[str] = None
    """Broadcast title"""

    total_watched: Optional[int] = FieldInfo(alias="totalWatched", default=None)
    """Accounts that watched, live or after"""

    total_watching: Optional[int] = FieldInfo(alias="totalWatching", default=None)
    """Accounts watching, as X counts them"""

    tweet: Optional[SearchTweet] = None
    """Search tweet with author. Zero metrics may mean X omitted counts."""

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)
    """ID of the post that announces the broadcast"""

    version: Optional[int] = None
    """X's revision number of the broadcast"""

    width: Optional[int] = None
    """Video width in pixels"""
