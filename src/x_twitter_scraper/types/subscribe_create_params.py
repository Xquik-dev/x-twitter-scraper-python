# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .shared.currency import Currency

__all__ = ["SubscribeCreateParams"]


class SubscribeCreateParams(TypedDict, total=False):
    currency: Currency
    """Currency to pay in, USD by default.

    Xquik converts the USD plan price at the latest daily ECB rate, and each renewal
    charges the same amount before tax. An account that already pays in USD gets a
    USD checkout. With rates over 3 ECB working days old, the checkout charges USD.
    charged_currency shows the currency charged.
    """

    tier: Literal["starter", "pro", "business"]
    """Subscription tier to pre-select."""
