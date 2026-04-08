# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookListDeliveriesResponse", "Delivery"]


class Delivery(BaseModel):
    """Webhook delivery attempt record with status and retry count."""

    id: str

    attempts: int

    created_at: datetime = FieldInfo(alias="createdAt")

    status: str

    stream_event_id: str = FieldInfo(alias="streamEventId")

    delivered_at: Optional[datetime] = FieldInfo(alias="deliveredAt", default=None)

    last_error: Optional[str] = FieldInfo(alias="lastError", default=None)

    last_status_code: Optional[int] = FieldInfo(alias="lastStatusCode", default=None)


class WebhookListDeliveriesResponse(BaseModel):
    deliveries: List[Delivery]
