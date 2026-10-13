# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .monitor import Monitor
from .._models import BaseModel

__all__ = ["MonitorListResponse"]


class MonitorListResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    monitors: List[Monitor]

    total: int
    """Account monitors on this page."""

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
