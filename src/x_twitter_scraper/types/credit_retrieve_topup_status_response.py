# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["CreditRetrieveTopupStatusResponse"]


class CreditRetrieveTopupStatusResponse(BaseModel):
    status: Literal["paid", "processing", "failed", "expired"]

    amount_dollars: Optional[int] = None
    """Dollar amount requested for the top-up."""

    charged_currency: Optional[Currency] = FieldInfo(alias="chargedCurrency", default=None)
    """Currency the checkout charged."""

    charged_minor_units: Optional[int] = FieldInfo(alias="chargedMinorUnits", default=None)
    """Amount the checkout charged before tax, in the currency's smallest unit.

    JPY and KRW have no decimals, so 1580 JPY is ¥1,580.
    """

    credits: Optional[str] = None
    """Bigint string credit amount granted or pending."""
