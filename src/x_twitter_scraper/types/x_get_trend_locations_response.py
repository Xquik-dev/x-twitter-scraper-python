# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XGetTrendLocationsResponse", "Location"]


class Location(BaseModel):
    """A place X offers trends for."""

    country: Optional[str] = None
    """Country name. Null for Worldwide."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """2-letter country code. Null for Worldwide."""

    name: str

    parent_woeid: Optional[int] = FieldInfo(alias="parentWoeid", default=None)
    """WOEID of the country or region above it. Null for Worldwide."""

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)
    """X's kind of place. Town, Country, Supername for Worldwide, or Unknown."""

    place_type_code: Optional[int] = FieldInfo(alias="placeTypeCode", default=None)
    """X's numeric code for the kind of place."""

    url: Optional[str] = None
    """X's legacy Yahoo GeoPlanet reference. It may not resolve."""

    woeid: int
    """Location ID. Pass it as woeid to /x/trends."""


class XGetTrendLocationsResponse(BaseModel):
    count: int
    """Locations returned & charged."""

    locations: List[Location]

    total: int
    """Locations that match the filters, before limit."""

    message: Optional[str] = None
    """What to send instead. Present only when no location matches."""
