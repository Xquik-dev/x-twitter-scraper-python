# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.event_type import EventType

__all__ = ["KeywordCreateParams"]


class KeywordCreateParams(TypedDict, total=False):
    event_types: Required[Annotated[List[EventType], PropertyInfo(alias="eventTypes")]]
    """Array of event types to subscribe to."""

    query: Required[str]
    """X search query to monitor. Whitespace is normalized."""

    name: str
    """Your own label for the keyword monitor. Its events carry it as monitorName."""
