# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .user_profile import UserProfile

__all__ = [
    "Community",
    "Banner",
    "BannerColor",
    "BannerFocus",
    "Creator",
    "CreatorUnionMember1",
    "MembersFacepile",
    "MembersFacepileCommunityMemberPreview",
    "PrimaryTopic",
    "Rule",
]


class BannerColor(BaseModel):
    blue: int
    """Blue value of the color"""

    green: int
    """Green value of the color"""

    percentage: float
    """Share of the banner in this color"""

    red: int
    """Red value of the color"""


class BannerFocus(BaseModel):
    """Area X keeps in view when it crops the banner, in pixels from the top left"""

    height: Optional[int] = None
    """Height of the area"""

    left: Optional[int] = None
    """Distance from the left edge"""

    top: Optional[int] = None
    """Distance from the top edge"""

    width: Optional[int] = None
    """Width of the area"""


class Banner(BaseModel):
    """The banner X shows for a community, with its size & colors."""

    url: str
    """Banner image URL at its original size"""

    colors: Optional[List[BannerColor]] = None
    """Main colors of the banner, largest share first"""

    focus: Optional[BannerFocus] = None
    """Area X keeps in view when it crops the banner, in pixels from the top left"""

    height: Optional[int] = None
    """Banner height in pixels"""

    width: Optional[int] = None
    """Banner width in pixels"""


class CreatorUnionMember1(BaseModel):
    id: str
    """Numeric X user ID of the creator"""

    username: str
    """X username of the creator"""

    verified: bool
    """Whether X shows the creator a badge"""


Creator: TypeAlias = Union[UserProfile, CreatorUnionMember1]


class MembersFacepileCommunityMemberPreview(BaseModel):
    """A member X previews by ID & profile picture only."""

    id: str
    """Numeric X user ID of the member"""

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)
    """Profile picture URL of the member"""


MembersFacepile: TypeAlias = Union[UserProfile, MembersFacepileCommunityMemberPreview]


class PrimaryTopic(BaseModel):
    """Primary topic.

    Its id is absent when X lists the community in a keyword or topic result.
    """

    name: str
    """Topic name X shows on the community"""

    id: Optional[str] = None
    """Topic ID that /x/communities/popular takes"""


class Rule(BaseModel):
    id: Optional[str] = None
    """Rule ID"""

    description: Optional[str] = None
    """What the rule asks of members"""

    name: Optional[str] = None
    """Rule title"""


class Community(BaseModel):
    """Public X Community, as every Community read returns it."""

    id: str
    """Unique community identifier"""

    is_nsfw: bool
    """Whether the community is marked sensitive"""

    member_count: int
    """Total member count"""

    name: str
    """Display name of the community"""

    admin: Optional[UserProfile] = None
    """Public X profile."""

    banner: Optional[Banner] = None
    """The banner X shows for a community, with its size & colors."""

    banner_url: Optional[str] = None
    """Community banner image URL"""

    created_at: Optional[str] = None
    """Community creation timestamp"""

    creator: Optional[Creator] = None
    """
    The creator's public profile, or the ID, username and badge alone when X sends
    no profile
    """

    description: Optional[str] = None
    """About text for the community"""

    invites_policy: Optional[str] = None
    """Invitation policy"""

    join_policy: Optional[str] = None
    """Join policy (open or restricted)"""

    members_facepile: Optional[List[MembersFacepile]] = FieldInfo(alias="membersFacepile", default=None)
    """The members X previews beside the member count.

    A keyword or topic result gives each member's ID & picture only.
    """

    moderator_count: Optional[int] = None
    """Total moderator count"""

    primary_topic: Optional[PrimaryTopic] = None
    """Primary topic.

    Its id is absent when X lists the community in a keyword or topic result.
    """

    question: Optional[str] = None
    """What the community asks a user who joins"""

    rules: Optional[List[Rule]] = None
    """Community rules"""

    search_tags: Optional[List[str]] = FieldInfo(alias="searchTags", default=None)
    """Tags X finds the community by"""
