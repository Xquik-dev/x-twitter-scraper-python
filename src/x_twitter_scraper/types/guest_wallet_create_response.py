# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .guest_wallet_amount import GuestWalletAmount

__all__ = ["GuestWalletCreateResponse", "Authorization"]


class Authorization(BaseModel):
    header: Literal["Authorization"]

    scheme: Literal["Bearer"]


class GuestWalletCreateResponse(BaseModel):
    """Initial guest wallet response containing the one-time key."""

    account_required: Literal[False]

    amount: GuestWalletAmount
    """Confirmed USD amount for a guest wallet purchase."""

    api_key: str
    """Paid-read bearer credential returned only by initial creation.

    Store it as a secret. Never place it in a URL or log.
    """

    authorization: Authorization

    checkout_url: str
    """Hosted checkout URL for user interaction."""

    credential_notice: Literal[
        "Store api_key and the Idempotency-Key securely before sharing checkout_url. No email recovery is available."
    ]

    credits: str
    """Credits granted after verified payment."""

    expires_at: datetime
    """Time when the pending checkout expires."""

    instructions: str
    """Hosted checkout and status polling instructions."""

    poll_after_seconds: Literal[2]
    """Wait at least this long before polling status_url."""

    purchase_id: str

    requires_user_interaction: Literal[True]

    status: Literal["creating", "pending", "paid", "expired", "failed", "refunded", "disputed"]

    status_url: Literal["https://xquik.com/api/v1/guest-wallets/status"]

    wallet_id: str
