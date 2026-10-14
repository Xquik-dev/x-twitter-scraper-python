# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountConnectionChallengeSubmitParams"]


class AccountConnectionChallengeSubmitParams(TypedDict, total=False):
    email_code: Required[str]
    """Code sent to the account email."""
