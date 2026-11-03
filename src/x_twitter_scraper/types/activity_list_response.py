# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List
from typing_extensions import TypeAlias

from .activity_log_row import ActivityLogRow

__all__ = ["ActivityListResponse"]

ActivityListResponse: TypeAlias = List[ActivityLogRow]
