# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccountRetrieveResponse"]


class AccountRetrieveResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    status: str

    x_user_id: str = FieldInfo(alias="xUserId")

    x_username: str = FieldInfo(alias="xUsername")

    cookies_obtained_at: Optional[datetime] = FieldInfo(alias="cookiesObtainedAt", default=None)

    proxy_country: Optional[str] = FieldInfo(alias="proxyCountry", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
