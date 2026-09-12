# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExtractionRetrieveParams"]


class ExtractionRetrieveParams(TypedDict, total=False):
    cursor: str
    """Previous nextCursor. Offset pagination is not supported."""

    field_style: Annotated[Literal["source", "camelCase", "snake_case"], PropertyInfo(alias="fieldStyle")]
    """Preserve source keys or convert result field names."""

    include_raw: Annotated[bool, PropertyInfo(alias="includeRaw")]
    """Use outputMode=raw instead."""

    limit: int
    """Maximum results per page (1-1000, default 100)."""

    output_mode: Annotated[Literal["compact", "full", "raw"], PropertyInfo(alias="outputMode")]
    """
    Use compact for core fields and tweet counts, full for nested enrichment, or raw
    for a source copy.
    """

    output_preset: Annotated[Literal["nested", "flat"], PropertyInfo(alias="outputPreset")]
    """Keep enrichment nested or merge it into each result."""

    wait: int
    """Wait up to this many seconds when the job is active."""
