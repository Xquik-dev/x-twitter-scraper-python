# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountUpdateLocaleResponse"]


class AccountUpdateLocaleResponse(BaseModel):
    success: Literal[True]
