from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FinalDestinationLocation")



@_attrs_define
class FinalDestinationLocation:
    """ A location, using WGS84 latitude and longitude.

    Used for a reverse geocode, or to add some location bias to a forward geocode.

    Use `distance_filter` to optionally limit the distance from this point that
    results can appear within

        Attributes:
            latitude (float):
            longitude (float):
            distance_filter (float | Unset):  Default: 5000.0.
     """

    latitude: float
    longitude: float
    distance_filter: float | Unset = 5000.0





    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        distance_filter = self.distance_filter


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "latitude": latitude,
            "longitude": longitude,
        })
        if distance_filter is not UNSET:
            field_dict["distance_filter"] = distance_filter

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        distance_filter = d.pop("distance_filter", UNSET)

        final_destination_location = cls(
            latitude=latitude,
            longitude=longitude,
            distance_filter=distance_filter,
        )

        return final_destination_location

