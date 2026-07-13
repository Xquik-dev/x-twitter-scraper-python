# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Error"]


class Error(BaseModel):
    """Error response.

    Default v1 returns a legacy string error code. Send `xquik-api-contract: 2026-04-29` to receive the structured best-practice error object.
    """

    error: Error
