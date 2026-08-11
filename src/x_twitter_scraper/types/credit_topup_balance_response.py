# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CreditTopupBalanceResponse"]


class CreditTopupBalanceResponse(BaseModel):
    redirect_url: str
    """Stable Xquik redirect URL for the active checkout."""

    url: str
    """Same stable Xquik redirect URL as redirect_url.

    The response never exposes the hosted checkout URL.
    """
