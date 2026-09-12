# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MonitorDeactivateResponse"]


class MonitorDeactivateResponse(BaseModel):
    deletion_status: Literal["deleting"] = FieldInfo(alias="deletionStatus")

    status_url: str = FieldInfo(alias="statusUrl")
    """Poll this monitor URL until it returns 404."""

    success: Literal[True]
