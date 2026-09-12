# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .draft import Draft

__all__ = ["DraftDetail"]


class DraftDetail(Draft):
    """Full tweet draft including update timestamp."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
