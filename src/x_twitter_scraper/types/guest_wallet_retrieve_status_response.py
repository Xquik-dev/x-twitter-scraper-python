# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GuestWalletRetrieveStatusResponse", "LatestPurchase", "LatestPurchaseAmount", "TopUp"]


class LatestPurchaseAmount(BaseModel):
    """Confirmed USD amount for a guest wallet purchase."""

    amount_minor: int
    """USD amount in cents. Accepted range is $10-$250."""

    currency: Literal["usd"]


class LatestPurchase(BaseModel):
    """Latest guest wallet purchase fulfillment state."""

    amount: LatestPurchaseAmount
    """Confirmed USD amount for a guest wallet purchase."""

    checkout_url: Optional[str] = None
    """Present only while the purchase is pending."""

    credits: str

    expires_at: datetime

    purchase_id: str

    status: Literal["creating", "pending", "paid", "expired", "failed", "refunded", "disputed"]


class TopUp(BaseModel):
    """Top-up action when usable and no checkout is pending."""

    method: Literal["POST"]

    path: Literal["/api/v1/guest-wallets/topups"]


class GuestWalletRetrieveStatusResponse(BaseModel):
    """Current balance, usability, and latest guest purchase state."""

    balance: str

    latest_purchase: Optional[LatestPurchase] = None
    """Latest guest wallet purchase fulfillment state."""

    poll_after_seconds: Optional[Literal[2]] = None
    """Polling delay while payment is pending. Null means stop."""

    scope: Literal["paid_reads"]

    status: Literal["active", "pending", "expired", "failed", "frozen", "closed"]
    """Combined wallet and pending-checkout state.

    A pending top-up can coexist with usable true. Terminal expired or failed states
    require a new guest wallet.
    """

    top_up: Optional[TopUp] = None
    """Top-up action when usable and no checkout is pending."""

    usable: bool
    """Authoritative paid-read readiness. Use instead of status."""

    wallet_id: str
