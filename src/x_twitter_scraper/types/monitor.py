# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.event_type import EventType

__all__ = ["Monitor"]


class Monitor(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    event_types: List[EventType] = FieldInfo(alias="eventTypes")

    is_active: bool = FieldInfo(alias="isActive")

    username: str

    x_user_id: str = FieldInfo(alias="xUserId")
