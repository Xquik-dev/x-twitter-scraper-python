# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "XSearchPlacesResponse",
    "Place",
    "PlaceBoundingBox",
    "PlaceContainedWithin",
    "PlaceContainedWithinBoundingBox",
]


class PlaceBoundingBox(BaseModel):
    """Outline of the place as GeoJSON. Each point holds longitude, then latitude."""

    coordinates: List[List[List[float]]]
    """Rings of points that draw the outline."""

    type: str
    """GeoJSON shape of the outline."""


class PlaceContainedWithinBoundingBox(BaseModel):
    """Outline of the place as GeoJSON. Each point holds longitude, then latitude."""

    coordinates: List[List[List[float]]]
    """Rings of points that draw the outline."""

    type: str
    """GeoJSON shape of the outline."""


class PlaceContainedWithin(BaseModel):
    """A place on X, such as a city or a neighborhood."""

    id: str
    """Place ID. Pass it as place to /x/tweets/search."""

    attributes: Dict[str, object]
    """Extra details X attaches to some places. Often empty."""

    bounding_box: Optional[PlaceContainedWithinBoundingBox] = FieldInfo(alias="boundingBox", default=None)
    """Outline of the place as GeoJSON. Each point holds longitude, then latitude."""

    centroid: Optional[List[float]] = None
    """Center of the place. Longitude, then latitude."""

    country: Optional[str] = None
    """Country the place lies in."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """2-letter code of the country the place lies in."""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """Name with the region or country around the place."""

    name: str
    """Short name of the place."""

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)
    """X's kind of place, such as city, admin, neighborhood, poi or country."""

    url: Optional[str] = None
    """X's own reference URL for the place."""


class Place(BaseModel):
    """A place X found, with the larger places it lies in."""

    id: str
    """Place ID. Pass it as place to /x/tweets/search."""

    attributes: Dict[str, object]
    """Extra details X attaches to some places. Often empty."""

    bounding_box: Optional[PlaceBoundingBox] = FieldInfo(alias="boundingBox", default=None)
    """Outline of the place as GeoJSON. Each point holds longitude, then latitude."""

    centroid: Optional[List[float]] = None
    """Center of the place. Longitude, then latitude."""

    contained_within: List[PlaceContainedWithin] = FieldInfo(alias="containedWithin")
    """Larger places this place lies in. Often 1."""

    country: Optional[str] = None
    """Country the place lies in."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """2-letter code of the country the place lies in."""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """Name with the region or country around the place."""

    name: str
    """Short name of the place."""

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)
    """X's kind of place, such as city, admin, neighborhood, poi or country."""

    url: Optional[str] = None
    """X's own reference URL for the place."""


class XSearchPlacesResponse(BaseModel):
    count: int
    """Places returned & charged."""

    places: List[Place]

    total: int
    """Places X found, before limit."""

    message: Optional[str] = None
    """What to send instead. Present only when X finds no place."""
