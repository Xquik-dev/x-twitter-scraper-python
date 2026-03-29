# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountSetXUsernameResponse"]


class AccountSetXUsernameResponse(BaseModel):
    success: Literal[True]

    x_username: str = FieldInfo(alias="xUsername")
