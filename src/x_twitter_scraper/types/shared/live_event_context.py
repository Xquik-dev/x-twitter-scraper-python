# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LiveEventContext"]


class LiveEventContext(BaseModel):
    """The live event the post belongs to, such as an election."""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """The event's image."""

    title: Optional[str] = None
    """Event name."""

    url: Optional[str] = None
    """The event's page on X."""
