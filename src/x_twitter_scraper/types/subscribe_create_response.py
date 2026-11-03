# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["SubscribeCreateResponse"]


class SubscribeCreateResponse(BaseModel):
    message: str

    status: Literal["checkout_created", "already_subscribed", "payment_issue"]

    url: str

    charged_currency: Optional[Currency] = FieldInfo(alias="chargedCurrency", default=None)
    """Currency the checkout charges. Only a checkout_created answer has it."""
