# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.currency import Currency

__all__ = ["CreditTopupBalanceParams"]


class CreditTopupBalanceParams(TypedDict, total=False):
    dollars: Required[int]
    """Amount to top up in US dollars. Minimum 10."""

    currency: Currency
    """Currency to pay in, USD by default.

    Xquik converts the dollar amount at the latest daily ECB rate. If the newest
    rates are more than 3 ECB working days old, it charges USD instead, and Checkout
    shows that before payment. charged_currency shows the currency charged. Credits
    always match the dollar amount.
    """

    locale: str
    """Optional site language for Stripe's return page.

    An unsupported 1 uses en, the default.
    """

    return_path: Annotated[str, PropertyInfo(alias="returnPath")]
    """Optional Xquik tool page to return to after Checkout, such as /en/x-article-reader."""
