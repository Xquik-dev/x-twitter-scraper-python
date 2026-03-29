# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CommunityCreateResponse"]


class CommunityCreateResponse(BaseModel):
    community_id: str = FieldInfo(alias="communityId")

    success: Literal[True]

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)
