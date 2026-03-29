# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["XGetNotificationsResponse", "Notification"]


class Notification(BaseModel):
    id: str

    message: Optional[str] = None

    timestamp: Optional[str] = None

    type: Optional[str] = None


class XGetNotificationsResponse(BaseModel):
    has_next_page: bool

    next_cursor: str

    notifications: List[Notification]
