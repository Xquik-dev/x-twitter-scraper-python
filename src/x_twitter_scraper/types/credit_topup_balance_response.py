# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["CreditTopupBalanceResponse"]


class CreditTopupBalanceResponse(BaseModel):
    charged_currency: Currency = FieldInfo(alias="chargedCurrency")
    """Currency the checkout charges."""

    charged_minor_units: int = FieldInfo(alias="chargedMinorUnits")
    """Amount the checkout charges before tax, in the currency's smallest unit.

    JPY and KRW have no decimals, so 1580 JPY is ¥1,580.
    """

    redirect_url: str
    """Stable Xquik redirect URL for the active checkout."""

    url: str
    """Same stable Xquik redirect URL as redirect_url.

    The response never exposes the hosted checkout URL.
    """
