# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FollowerRetrieveCheckResponse"]


class FollowerRetrieveCheckResponse(BaseModel):
    is_followed_by: bool = FieldInfo(alias="isFollowedBy")

    is_following: bool = FieldInfo(alias="isFollowing")

    source_username: str = FieldInfo(alias="sourceUsername")

    target_username: str = FieldInfo(alias="targetUsername")
