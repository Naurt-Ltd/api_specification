from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.feature_collection_type import FeatureCollectionType
from typing import cast

if TYPE_CHECKING:
  from ..models.feature import Feature





T = TypeVar("T", bound="FeatureCollection")



@_attrs_define
class FeatureCollection:
    """ 
        Attributes:
            features (list[Feature]):
            type_ (FeatureCollectionType):  Default: FeatureCollectionType.FEATURECOLLECTION.
     """

    features: list[Feature]
    type_: FeatureCollectionType = FeatureCollectionType.FEATURECOLLECTION
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.feature import Feature
        features = []
        for features_item_data in self.features:
            features_item = features_item_data.to_dict()
            features.append(features_item)



        type_ = self.type_.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "features": features,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature import Feature
        d = dict(src_dict)
        features = []
        _features = d.pop("features")
        for features_item_data in (_features):
            features_item = Feature.from_dict(features_item_data)



            features.append(features_item)


        type_ = FeatureCollectionType(d.pop("type"))




        feature_collection = cls(
            features=features,
            type_=type_,
        )


        feature_collection.additional_properties = d
        return feature_collection

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
