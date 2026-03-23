from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.feature_type import FeatureType
from typing import cast

if TYPE_CHECKING:
  from ..models.feature_properties import FeatureProperties
  from ..models.polygon import Polygon
  from ..models.point import Point
  from ..models.multipoint import Multipoint





T = TypeVar("T", bound="Feature")



@_attrs_define
class Feature:
    """ 
        Attributes:
            geometry (Multipoint | Point | Polygon):
            properties (FeatureProperties):
            type_ (FeatureType):
     """

    geometry: Multipoint | Point | Polygon
    properties: FeatureProperties
    type_: FeatureType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.feature_properties import FeatureProperties
        from ..models.polygon import Polygon
        from ..models.point import Point
        from ..models.multipoint import Multipoint
        geometry: dict[str, Any]
        if isinstance(self.geometry, Point):
            geometry = self.geometry.to_dict()
        elif isinstance(self.geometry, Multipoint):
            geometry = self.geometry.to_dict()
        else:
            geometry = self.geometry.to_dict()


        properties = self.properties.to_dict()

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "geometry": geometry,
            "properties": properties,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature_properties import FeatureProperties
        from ..models.polygon import Polygon
        from ..models.point import Point
        from ..models.multipoint import Multipoint
        d = dict(src_dict)
        def _parse_geometry(data: object) -> Multipoint | Point | Polygon:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geometry_type_0 = Point.from_dict(data)



                return geometry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geometry_type_1 = Multipoint.from_dict(data)



                return geometry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            geometry_type_2 = Polygon.from_dict(data)



            return geometry_type_2

        geometry = _parse_geometry(d.pop("geometry"))


        properties = FeatureProperties.from_dict(d.pop("properties"))




        type_ = FeatureType(d.pop("type"))




        feature = cls(
            geometry=geometry,
            properties=properties,
            type_=type_,
        )


        feature.additional_properties = d
        return feature

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
