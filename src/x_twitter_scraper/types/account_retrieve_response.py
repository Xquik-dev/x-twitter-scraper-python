# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse", "CreditInfo"]


class CreditInfo(BaseModel):
    auto_topup_enabled: bool = FieldInfo(alias="autoTopupEnabled")

    balance: int

    lifetime_purchased: int = FieldInfo(alias="lifetimePurchased")

    lifetime_used: int = FieldInfo(alias="lifetimeUsed")


class AccountRetrieveResponse(BaseModel):
    monitors_allowed: int = FieldInfo(alias="monitorsAllowed")

    monitors_used: int = FieldInfo(alias="monitorsUsed")

    plan: Literal["active", "inactive"]

    credit_info: Optional[CreditInfo] = FieldInfo(alias="creditInfo", default=None)
