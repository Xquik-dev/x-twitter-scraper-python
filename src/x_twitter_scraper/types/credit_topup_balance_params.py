# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreditTopupBalanceParams"]


class CreditTopupBalanceParams(TypedDict, total=False):
    amount: Required[int]
    """Amount to top up in credits"""
