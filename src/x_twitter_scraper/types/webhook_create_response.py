# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.event_type import EventType
from .monitors.post_monitor import PostEventType

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    event_types: List[Union[EventType, PostEventType]] = FieldInfo(alias="eventTypes")
    """Array of event types to subscribe to."""

    secret: str
    """Plaintext HMAC signing secret returned only at creation."""

    url: str

    ignored_fields: Optional[List[str]] = FieldInfo(alias="ignoredFields", default=None)
    """Fields the request sent that this route does not read, in the order sent.

    They changed nothing. The answer leaves this out when the route read every
    field.
    """
