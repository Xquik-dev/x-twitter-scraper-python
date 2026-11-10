# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Union
from typing_extensions import TypeAlias

from .account_create_response import (
    SanitizedXAccount,
    XAccountConnectionChallenge,
    XAccountConnectionAttemptPending,
)

__all__ = ["AccountReauthResponse"]

AccountReauthResponse: TypeAlias = Union[
    SanitizedXAccount, XAccountConnectionAttemptPending, XAccountConnectionChallenge
]
