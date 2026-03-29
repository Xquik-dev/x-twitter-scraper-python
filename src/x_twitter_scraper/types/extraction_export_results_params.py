# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ExtractionExportResultsParams"]


class ExtractionExportResultsParams(TypedDict, total=False):
    format: Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"]
