# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountSetXUsernameResponse"]


class AccountSetXUsernameResponse(BaseModel):
    success: Literal[True]

    x_username: str = FieldInfo(alias="xUsername")
