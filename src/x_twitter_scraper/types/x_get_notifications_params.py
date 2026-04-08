# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["XGetNotificationsParams"]


class XGetNotificationsParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for notifications"""

    type: Literal["All", "Verified", "Mentions"]
    """Notification type filter"""
