# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GuestWalletTopupResponse", "Amount", "Authorization"]


class Amount(BaseModel):
    """Confirmed USD amount for a guest wallet purchase."""

    amount_minor: int
    """USD amount in cents. Accepted range is $10-$250."""

    currency: Literal["usd"]


class Authorization(BaseModel):
    header: Literal["Authorization"]

    scheme: Literal["Bearer"]


class GuestWalletTopupResponse(BaseModel):
    """Pending Stripe checkout and guest wallet purchase details."""

    account_required: Literal[False]

    amount: Amount
    """Confirmed USD amount for a guest wallet purchase."""

    checkout_url: str
    """Raw Stripe-hosted checkout URL for user interaction."""

    credits: str
    """Credits granted after verified payment."""

    expires_at: datetime
    """Time when the pending checkout expires."""

    instructions: Literal[
        "Give checkout_url to the user. They must complete payment on Stripe. Never submit payment for them. After payment, poll status_url every poll_after_seconds until latest_purchase.status is no longer pending."
    ]

    poll_after_seconds: Literal[2]
    """Wait at least this long before polling status_url."""

    purchase_id: str

    requires_user_interaction: Literal[True]

    status: Literal["creating", "pending", "paid", "expired", "failed", "refunded", "disputed"]

    status_url: Literal["https://xquik.com/api/v1/guest-wallets/status"]

    wallet_id: str

    api_key: Optional[str] = None
    """Paid-read bearer credential returned only by initial creation.

    Store it as a secret. Never place it in a URL or log.
    """

    authorization: Optional[Authorization] = None

    credential_notice: Optional[
        Literal[
            "Store api_key and the Idempotency-Key securely before sharing checkout_url. No email recovery is available."
        ]
    ] = None
