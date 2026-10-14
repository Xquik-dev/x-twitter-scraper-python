# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Draft"]


class Draft(BaseModel):
    """Private Xquik draft with optional topic and goal."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    text: str

    goal: Optional[str] = None

    topic: Optional[str] = None
