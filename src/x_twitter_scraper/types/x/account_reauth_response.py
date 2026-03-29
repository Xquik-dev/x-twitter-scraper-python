# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccountReauthResponse"]


class AccountReauthResponse(BaseModel):
    id: str

    status: str

    x_username: str = FieldInfo(alias="xUsername")
