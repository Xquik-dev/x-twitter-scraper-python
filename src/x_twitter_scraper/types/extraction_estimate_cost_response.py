# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtractionEstimateCostResponse"]


class ExtractionEstimateCostResponse(BaseModel):
    """Free conservative cost estimate.

    Post estimates use the supported cap without a live profile lookup. It never creates a job or charges.
    """

    allowed: bool
    """Whether the balance covers the full estimate."""

    credits_available: str = FieldInfo(alias="creditsAvailable")

    credits_required: str = FieldInfo(alias="creditsRequired")

    estimated_results: int = FieldInfo(alias="estimatedResults")
    """Credit calculation row count, not source availability."""

    source: Literal[
        "followers",
        "following",
        "collection",
        "paginationCap",
        "quoteCount",
        "replyCount",
        "resultsLimit",
        "retweetCount",
        "unknown",
    ]

    resolved_x_user_id: Optional[str] = FieldInfo(alias="resolvedXUserId", default=None)
    """Resolved X user ID from count-based profile estimates."""
