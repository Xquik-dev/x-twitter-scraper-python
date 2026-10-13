# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookCreateTelegramLinkResponse"]


class WebhookCreateTelegramLinkResponse(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")
    """When the link stops working, 15 minutes on."""

    url: str
    """Opens @XquikBot with the link's code."""
