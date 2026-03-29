# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse", "CurrentPeriod"]


class CurrentPeriod(BaseModel):
    end: datetime

    start: datetime

    usage_percent: float = FieldInfo(alias="usagePercent")


class AccountRetrieveResponse(BaseModel):
    monitors_allowed: int = FieldInfo(alias="monitorsAllowed")

    monitors_used: int = FieldInfo(alias="monitorsUsed")

    plan: Literal["active", "inactive"]

    current_period: Optional[CurrentPeriod] = FieldInfo(alias="currentPeriod", default=None)
