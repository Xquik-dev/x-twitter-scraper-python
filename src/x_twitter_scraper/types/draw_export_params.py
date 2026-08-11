# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DrawExportParams"]


class DrawExportParams(TypedDict, total=False):
    format: Required[Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"]]
    """Export output format.

    PDF entry exports include up to 10,000 rows. Other entry formats include up to
    100,000 rows.
    """

    type: Literal["winners", "entries"]
    """Export winners or all entries"""
