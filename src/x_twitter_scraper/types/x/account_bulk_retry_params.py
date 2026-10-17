# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AccountBulkRetryParams"]


class AccountBulkRetryParams(TypedDict, total=False):
    account_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="accountIds")]
    """IDs of the X accounts to retry.

    Accounts that failed for another reason, or belong to someone else, stay as they
    are.
    """
