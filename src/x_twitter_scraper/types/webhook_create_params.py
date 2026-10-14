# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

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
    """HTTPS URL.

    A Discord channel webhook URL gets each event as a Discord message, & a Slack
    incoming webhook URL as a Slack message. To deliver to Telegram, use POST
    /webhooks/telegram instead.
    """
