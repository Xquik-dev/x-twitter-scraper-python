# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .post_monitor import PostEventType

__all__ = ["PostUpdateParams"]


class PostUpdateParams(TypedDict, total=False):
    event_types: Annotated[List[PostEventType], PropertyInfo(alias="eventTypes")]
    """Post event types to send. Without it, a monitor sends new replies, new quotes,
    like & retweet changes, edits & deletion.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    name: Optional[str]
    """New label for the post monitor. Send null to remove it."""
