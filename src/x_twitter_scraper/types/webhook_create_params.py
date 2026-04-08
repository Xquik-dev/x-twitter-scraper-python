# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.event_type import EventType

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    event_types: Required[Annotated[List[EventType], PropertyInfo(alias="eventTypes")]]
    """Array of event types to subscribe to."""

    url: Required[str]
    """HTTPS URL"""
