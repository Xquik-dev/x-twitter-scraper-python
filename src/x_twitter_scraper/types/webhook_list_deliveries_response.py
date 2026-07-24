# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .delivery import Delivery

__all__ = ["WebhookListDeliveriesResponse"]


class WebhookListDeliveriesResponse(BaseModel):
    deliveries: List[Delivery]
