# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CreditTopupBalanceResponse"]


class CreditTopupBalanceResponse(BaseModel):
    redirect_url: str
    """Stable first-party Xquik redirect URL for the active Stripe Checkout session."""

    url: str
    """Same stable first-party Xquik redirect URL as redirect_url.

    The response never exposes a raw Stripe Checkout URL.
    """
