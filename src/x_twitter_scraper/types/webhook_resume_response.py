# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookResumeResponse"]


class WebhookResumeResponse(BaseModel):
    status_code: int = FieldInfo(alias="statusCode")

    success: bool

    webhook: Webhook
    """Webhook endpoint registered to receive event deliveries."""
