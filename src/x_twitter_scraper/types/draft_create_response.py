# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional

from pydantic import Field as FieldInfo

from .draft_detail import DraftDetail

__all__ = ["DraftCreateResponse"]


class DraftCreateResponse(DraftDetail):
    """Full private Xquik draft including update timestamp."""

    ignored_fields: Optional[List[str]] = FieldInfo(alias="ignoredFields", default=None)
    """Fields the request sent that this route does not read, in the order sent.

    They changed nothing. The answer leaves this out when the route read every
    field.
    """
