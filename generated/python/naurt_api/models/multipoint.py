from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.multipoint_type import MultipointType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Multipoint")



@_attrs_define
class Multipoint:
    """ 
        Attributes:
            coordinates (list[list[float]] | Unset):
            type_ (MultipointType | Unset):
     """

    coordinates: list[list[float]] | Unset = UNSET
    type_: MultipointType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        coordinates: list[list[float]] | Unset = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = []
            for coordinates_item_data in self.coordinates:
                coordinates_item = coordinates_item_data


                coordinates.append(coordinates_item)



        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _coordinates = d.pop("coordinates", UNSET)
        coordinates: list[list[float]] | Unset = UNSET
        if _coordinates is not UNSET:
            coordinates = []
            for coordinates_item_data in _coordinates:
                coordinates_item = cast(list[float], coordinates_item_data)

                coordinates.append(coordinates_item)


        _type_ = d.pop("type", UNSET)
        type_: MultipointType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = MultipointType(_type_)




        multipoint = cls(
            coordinates=coordinates,
            type_=type_,
        )


        multipoint.additional_properties = d
        return multipoint

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
