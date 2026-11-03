# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing_extensions import Literal, TypeAlias

__all__ = ["Currency"]

Currency: TypeAlias = Literal[
    "USD",
    "EUR",
    "GBP",
    "TRY",
    "JPY",
    "CNY",
    "KRW",
    "CAD",
    "AUD",
    "MXN",
    "AED",
    "BRL",
    "CHF",
    "CZK",
    "DKK",
    "HKD",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "MYR",
    "NOK",
    "NZD",
    "PHP",
    "PLN",
    "QAR",
    "RON",
    "SAR",
    "SEK",
    "SGD",
    "THB",
    "ZAR",
]
"""ISO 4217 code of a currency Xquik charges in."""
