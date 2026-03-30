# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.event_type import EventType

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    event_types: Annotated[List[EventType], PropertyInfo(alias="eventTypes")]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    url: str
