# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.event_type import EventType

__all__ = ["Event"]


class Event(BaseModel):
    id: str

    data: Dict[str, object]

    monitor_id: str = FieldInfo(alias="monitorId")

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    type: EventType

    username: str
