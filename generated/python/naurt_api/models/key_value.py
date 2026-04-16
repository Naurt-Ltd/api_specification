from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.multipoint import Multipoint
  from ..models.polygon import Polygon
  from ..models.point import Point





T = TypeVar("T", bound="KeyValue")



@_attrs_define
class KeyValue:
    """ 
        Attributes:
            default_geocode (Point):
            building (Polygon | Unset):
            entrance (Multipoint | Unset):
            parking (Polygon | Unset):
     """

    default_geocode: Point
    building: Polygon | Unset = UNSET
    entrance: Multipoint | Unset = UNSET
    parking: Polygon | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.multipoint import Multipoint
        from ..models.polygon import Polygon
        from ..models.point import Point
        default_geocode = self.default_geocode.to_dict()

        building: dict[str, Any] | Unset = UNSET
        if not isinstance(self.building, Unset):
            building = self.building.to_dict()

        entrance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entrance, Unset):
            entrance = self.entrance.to_dict()

        parking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parking, Unset):
            parking = self.parking.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "default_geocode": default_geocode,
        })
        if building is not UNSET:
            field_dict["building"] = building
        if entrance is not UNSET:
            field_dict["entrance"] = entrance
        if parking is not UNSET:
            field_dict["parking"] = parking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multipoint import Multipoint
        from ..models.polygon import Polygon
        from ..models.point import Point
        d = dict(src_dict)
        default_geocode = Point.from_dict(d.pop("default_geocode"))




        _building = d.pop("building", UNSET)
        building: Polygon | Unset
        if isinstance(_building,  Unset):
            building = UNSET
        else:
            building = Polygon.from_dict(_building)




        _entrance = d.pop("entrance", UNSET)
        entrance: Multipoint | Unset
        if isinstance(_entrance,  Unset):
            entrance = UNSET
        else:
            entrance = Multipoint.from_dict(_entrance)




        _parking = d.pop("parking", UNSET)
        parking: Polygon | Unset
        if isinstance(_parking,  Unset):
            parking = UNSET
        else:
            parking = Polygon.from_dict(_parking)




        key_value = cls(
            default_geocode=default_geocode,
            building=building,
            entrance=entrance,
            parking=parking,
        )


        key_value.additional_properties = d
        return key_value

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
