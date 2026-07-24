# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TicketReplyResponse", "Attachment"]


class Attachment(BaseModel):
    """Attachment identifier and initial processing state."""

    public_id: str = FieldInfo(alias="publicId")

    status: Literal["pending", "ready", "failed"]


class TicketReplyResponse(BaseModel):
    attachments: List[Attachment]

    public_id: str = FieldInfo(alias="publicId")
