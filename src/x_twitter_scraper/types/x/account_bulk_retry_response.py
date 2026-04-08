# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AccountBulkRetryResponse"]


class AccountBulkRetryResponse(BaseModel):
    cleared: int
    """Number of accounts cleared"""
