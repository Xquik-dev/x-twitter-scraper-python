# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ActivityExportParams"]


class ActivityExportParams(TypedDict, total=False):
    format: Required[Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"]]
    """File format. PDF stops at 10,000 rows."""

    category: str
    """Activity group, like the Activity page's tabs.

    `all` by default, or `actions`, `extractions`, `monitors`, `webhooks` or
    `billing`.
    """

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
