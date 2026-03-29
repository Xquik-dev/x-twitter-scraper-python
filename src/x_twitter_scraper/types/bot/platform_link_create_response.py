# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PlatformLinkCreateResponse"]


class PlatformLinkCreateResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    platform: str

    platform_user_id: str = FieldInfo(alias="platformUserId")
