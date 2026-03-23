from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.feature_properties_naurt_type import FeaturePropertiesNaurtType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.accuracy import Accuracy





T = TypeVar("T", bound="FeatureProperties")



@_attrs_define
class FeatureProperties:
    """ 
        Attributes:
            naurt_type (FeaturePropertiesNaurtType):
            accuracy (Accuracy | Unset):
            minimum_parking_to_door_distance (float | Unset):
     """

    naurt_type: FeaturePropertiesNaurtType
    accuracy: Accuracy | Unset = UNSET
    minimum_parking_to_door_distance: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.accuracy import Accuracy
        naurt_type = self.naurt_type.value

        accuracy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accuracy, Unset):
            accuracy = self.accuracy.to_dict()

        minimum_parking_to_door_distance = self.minimum_parking_to_door_distance


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "naurt_type": naurt_type,
        })
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy
        if minimum_parking_to_door_distance is not UNSET:
            field_dict["minimum_parking_to_door_distance"] = minimum_parking_to_door_distance

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accuracy import Accuracy
        d = dict(src_dict)
        naurt_type = FeaturePropertiesNaurtType(d.pop("naurt_type"))




        _accuracy = d.pop("accuracy", UNSET)
        accuracy: Accuracy | Unset
        if isinstance(_accuracy,  Unset):
            accuracy = UNSET
        else:
            accuracy = Accuracy.from_dict(_accuracy)




        minimum_parking_to_door_distance = d.pop("minimum_parking_to_door_distance", UNSET)

        feature_properties = cls(
            naurt_type=naurt_type,
            accuracy=accuracy,
            minimum_parking_to_door_distance=minimum_parking_to_door_distance,
        )


        feature_properties.additional_properties = d
        return feature_properties

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
