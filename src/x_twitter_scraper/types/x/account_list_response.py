# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .x_account import XAccount

__all__ = ["AccountListResponse"]


class AccountListResponse(BaseModel):
    accounts: List[XAccount]
