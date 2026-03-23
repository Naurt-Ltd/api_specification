from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FeedbackLocation")



@_attrs_define
class FeedbackLocation:
    """ 
        Attributes:
            latitude (float):
            longitude (float):
     """

    latitude: float
    longitude: float





    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "latitude": latitude,
            "longitude": longitude,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        feedback_location = cls(
            latitude=latitude,
            longitude=longitude,
        )

        return feedback_location

