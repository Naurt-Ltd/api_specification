from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.feature_collection import FeatureCollection





T = TypeVar("T", bound="RendezvousHitData")



@_attrs_define
class RendezvousHitData:
    """ 
        Attributes:
            id (str):
            address (str): Normalised address; may differ from the searched address
            geojson (FeatureCollection):
            distance (float | Unset): Distance in metres from the searched latitude/longitude.
                Present only when searching with latitude and longitude.
     """

    id: str
    address: str
    geojson: FeatureCollection
    distance: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.feature_collection import FeatureCollection
        id = self.id

        address = self.address

        geojson = self.geojson.to_dict()

        distance = self.distance


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "address": address,
            "geojson": geojson,
        })
        if distance is not UNSET:
            field_dict["distance"] = distance

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature_collection import FeatureCollection
        d = dict(src_dict)
        id = d.pop("id")

        address = d.pop("address")

        geojson = FeatureCollection.from_dict(d.pop("geojson"))




        distance = d.pop("distance", UNSET)

        rendezvous_hit_data = cls(
            id=id,
            address=address,
            geojson=geojson,
            distance=distance,
        )

        return rendezvous_hit_data

