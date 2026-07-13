# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CreditQuickTopupBalanceResponse", "UnionMember0", "UnionMember1", "Outcome"]


class UnionMember0(BaseModel):
    balance: str
    """Updated credit balance as a bigint string."""

    credits: str
    """Credits added by this top-up as a bigint string."""

    outcome: Literal["charged"]


class UnionMember1(BaseModel):
    client_secret: str = FieldInfo(alias="clientSecret")
    """Payment client secret for completing authentication."""

    outcome: Literal["requires_action"]


class Outcome(BaseModel):
    outcome: Literal["no_payment_method"]


CreditQuickTopupBalanceResponse: TypeAlias = Union[UnionMember0, UnionMember1, Outcome]
