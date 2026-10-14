# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookTestResponse"]


class WebhookTestResponse(BaseModel):
    status_code: int = FieldInfo(alias="statusCode")

    success: bool

    error: Optional[str] = None
