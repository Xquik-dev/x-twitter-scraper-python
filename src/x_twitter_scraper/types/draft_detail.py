# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime

from pydantic import Field as FieldInfo

from .draft import Draft

__all__ = ["DraftDetail"]


class DraftDetail(Draft):
    """Full private Xquik draft including update timestamp."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
