# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["XAccount"]


class XAccount(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    status: str

    x_user_id: str = FieldInfo(alias="xUserId")

    x_username: str = FieldInfo(alias="xUsername")
