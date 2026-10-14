# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from .._models import BaseModel

__all__ = ["CreditRetrieveBalanceResponse"]


class CreditRetrieveBalanceResponse(BaseModel):
    auto_topup_amount_dollars: float
    """Configured dollar amount for each automatic top-up."""

    auto_topup_enabled: bool

    auto_topup_stopped: bool
    """Whether declined charges stopped automatic top-up while it is enabled.

    It stops after 3 declines in a row on one card. A paid top-up, a paid plan
    renewal, or the next automatic top-up on a new card clears it.
    """

    auto_topup_threshold: str
    """
    Credit balance threshold that triggers automatic top-up when enabled,
    represented as a bigint string.
    """

    balance: str
    """
    Current credit balance as a bigint string to preserve precision above
    Number.MAX_SAFE_INTEGER.
    """

    lifetime_purchased: str
    """Lifetime purchased credits as a bigint string."""

    lifetime_used: str
    """Lifetime consumed credits as a bigint string."""
