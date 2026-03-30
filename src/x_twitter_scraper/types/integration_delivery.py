# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IntegrationDelivery"]


class IntegrationDelivery(BaseModel):
    id: str

    attempts: int

    created_at: datetime = FieldInfo(alias="createdAt")

    event_type: str = FieldInfo(alias="eventType")

    status: str

    delivered_at: Optional[datetime] = FieldInfo(alias="deliveredAt", default=None)

    last_error: Optional[str] = FieldInfo(alias="lastError", default=None)

    last_status_code: Optional[int] = FieldInfo(alias="lastStatusCode", default=None)

    source_id: Optional[str] = FieldInfo(alias="sourceId", default=None)

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)
