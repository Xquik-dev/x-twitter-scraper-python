# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SubscribeCreateResponse"]


class SubscribeCreateResponse(BaseModel):
    message: str

    status: Literal["checkout_created", "already_subscribed", "payment_issue"]

    url: str
