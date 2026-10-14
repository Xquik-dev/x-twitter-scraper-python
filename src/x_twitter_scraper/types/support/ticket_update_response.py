# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TicketUpdateResponse"]


class TicketUpdateResponse(BaseModel):
    public_id: str = FieldInfo(alias="publicId")

    status: Literal["open", "resolved", "closed"]
