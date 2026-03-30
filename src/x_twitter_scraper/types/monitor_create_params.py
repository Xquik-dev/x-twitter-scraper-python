# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.event_type import EventType

__all__ = ["MonitorCreateParams"]


class MonitorCreateParams(TypedDict, total=False):
    event_types: Required[Annotated[List[EventType], PropertyInfo(alias="eventTypes")]]

    username: Required[str]
    """X username (without @)"""
