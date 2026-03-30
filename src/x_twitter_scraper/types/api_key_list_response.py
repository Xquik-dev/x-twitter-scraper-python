# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .api_key import APIKey
from .._models import BaseModel

__all__ = ["APIKeyListResponse"]


class APIKeyListResponse(BaseModel):
    keys: List[APIKey]
