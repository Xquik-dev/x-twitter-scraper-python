# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CommunityActionResult"]


class CommunityActionResult(BaseModel):
    community_id: str = FieldInfo(alias="communityId")

    community_name: str = FieldInfo(alias="communityName")

    success: Literal[True]
