# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ActivityListParams"]


class ActivityListParams(TypedDict, total=False):
    category: str
    """Activity group, like the Activity page's tabs.

    `all` by default, or `actions`, `extractions`, `monitors`, `webhooks` or
    `billing`.
    """

    format: Literal["json"]
    """Leave it out or pass json to get the rows. Use export for a file."""

    limit: int
    """Most rows to return, from 1 to 100,000. 100 by default."""

    q: str
    """Search text."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Oldest time, ISO 8601."""

    status: str
    """Comma-separated statuses."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Newest time, ISO 8601."""
