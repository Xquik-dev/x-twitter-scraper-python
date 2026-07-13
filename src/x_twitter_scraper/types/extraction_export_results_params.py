# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExtractionExportResultsParams"]


class ExtractionExportResultsParams(TypedDict, total=False):
    format: Required[Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"]]
    """Export file format"""
