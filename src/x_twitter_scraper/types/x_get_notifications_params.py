# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["XGetNotificationsParams"]


class XGetNotificationsParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for collection results.

    Also read as next_cursor, next_token, pagination_token or continuation_token.
    """

    type: Literal["All", "Verified", "Mentions"]
    """Notification type filter. Unrecognized values fall back to All."""
