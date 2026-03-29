# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccountListResponse", "Account"]


class Account(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    status: str

    x_user_id: str = FieldInfo(alias="xUserId")

    x_username: str = FieldInfo(alias="xUsername")


class AccountListResponse(BaseModel):
    accounts: List[Account]
