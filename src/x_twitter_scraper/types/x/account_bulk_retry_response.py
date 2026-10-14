# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from ..._models import BaseModel

__all__ = ["AccountBulkRetryResponse"]


class AccountBulkRetryResponse(BaseModel):
    cleared: int
    """Number of accounts cleared"""
