# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GuestWalletAmount"]


class GuestWalletAmount(BaseModel):
    """Confirmed USD amount for a guest wallet purchase."""

    amount_minor: int
    """USD amount in cents. Accepted range is $10-$250."""

    currency: Literal["usd"]
