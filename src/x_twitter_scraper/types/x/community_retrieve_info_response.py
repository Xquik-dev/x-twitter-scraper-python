# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CommunityRetrieveInfoResponse", "Community", "CommunityPrimaryTopic", "CommunityRule"]


class CommunityPrimaryTopic(BaseModel):
    """Primary topic"""

    id: Optional[str] = None

    name: Optional[str] = None


class CommunityRule(BaseModel):
    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None


class Community(BaseModel):
    """Community info object"""

    id: str
    """Community ID"""

    banner_url: Optional[str] = None
    """Community banner image URL"""

    created_at: Optional[str] = None
    """Community creation timestamp"""

    description: Optional[str] = None
    """Community description"""

    join_policy: Optional[str] = None
    """Join policy (open or restricted)"""

    member_count: Optional[int] = None
    """Total member count"""

    moderator_count: Optional[int] = None
    """Total moderator count"""

    name: Optional[str] = None
    """Community name"""

    primary_topic: Optional[CommunityPrimaryTopic] = None
    """Primary topic"""

    rules: Optional[List[CommunityRule]] = None
    """Community rules"""


class CommunityRetrieveInfoResponse(BaseModel):
    community: Community
    """Community info object"""
