# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreditTopupBalanceParams"]


class CreditTopupBalanceParams(TypedDict, total=False):
    dollars: Required[int]
    """Amount to top up in US dollars. Minimum 10."""

    locale: str
    """Optional checkout locale. Defaults to en."""
