# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .post_monitor import PostEventType

__all__ = ["PostCreateParams"]


class PostCreateParams(TypedDict, total=False):
    post: Required[str]
    """Post link or ID. x.com, twitter.com, mobile & /i/web/status/ links work with
    any query string.
    """

    event_types: Annotated[List[PostEventType], PropertyInfo(alias="eventTypes")]
    """Post event types to send. Without it, a monitor sends new replies, new quotes,
    like & retweet changes, edits & deletion.
    """

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
    """Send false to create the monitor paused.

    A paused monitor reads nothing & costs nothing until a PATCH sets isActive to
    true.
    """

    name: Optional[str]
    """Your own label for the post monitor. Its events carry it as monitorName."""
