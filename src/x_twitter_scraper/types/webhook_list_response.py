# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookListResponse"]


class WebhookListResponse(BaseModel):
    webhooks: List[Webhook]
