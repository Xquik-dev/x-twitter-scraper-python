# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List

from ..._models import BaseModel

__all__ = ["JobListLocationsResponse", "Location"]


class Location(BaseModel):
    """A place a job search can name by its ID."""

    id: str
    """Location ID, which the job search locationId takes."""

    name: str
    """Place name with its region or country code."""


class JobListLocationsResponse(BaseModel):
    """The places whose names match a query."""

    count: int
    """Places returned, each charged 1 credit."""

    locations: List[Location]
    """Matching places, best match first."""
