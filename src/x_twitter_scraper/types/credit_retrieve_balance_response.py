# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CreditRetrieveBalanceResponse"]


class CreditRetrieveBalanceResponse(BaseModel):
    auto_topup_enabled: bool

    balance: int

    lifetime_purchased: int

    lifetime_used: int
