# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountUpdateLocaleResponse"]


class AccountUpdateLocaleResponse(BaseModel):
    success: Literal[True]

    ignored_fields: Optional[List[str]] = FieldInfo(alias="ignoredFields", default=None)
    """Fields the request sent that this route does not read, in the order sent.

    They changed nothing. The answer leaves this out when the route read every
    field.
    """
