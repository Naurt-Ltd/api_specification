from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.final_destination_source_id_response import FinalDestinationSourceIdResponse
  from ..models.feature_collection import FeatureCollection
  from ..models.structured_address import StructuredAddress
  from ..models.key_value import KeyValue





T = TypeVar("T", bound="FinalDestinationHit")



@_attrs_define
class FinalDestinationHit:
    """ 
        Attributes:
            id (UUID):
            address (str):
            geojson (FeatureCollection | KeyValue):
            distance (float | Unset):
            search_confidence (float | Unset): Confidence score in the range 0.0 to 1.0 indicating how well the result
                matches the query. Higher is better.

                See: https://docs.naurt.com/reference/search-confidence

                Not to be confused with Accuracy, which is how good the data itself is. This
                is about the likelihood of a good match.
                 Example: 0.93.
            structured_response (StructuredAddress | Unset): Naurt's own format for structured address data. Please see:
                https://docs.naurt.com/reference/address-structure/ for significant more
                details on this data format.

                When searching, do not use `country_code` - as it is not used. `country_code`
                is for responses only.
            source_id (FinalDestinationSourceIdResponse | Unset): An object containing information on source IDs. Source IDs
                refer to underlying
                IDs from address data sets. Currently supporting UPRN and UDPRN in the UK
                referring to the OrdnanceSurvey datasets
                 Example: {'UPRN': {'value': {'os_uprn': '100062664604'}}, 'UDPRN': {'value': {'os_udprn': '25962203'}}}.
     """

    id: UUID
    address: str
    geojson: FeatureCollection | KeyValue
    distance: float | Unset = UNSET
    search_confidence: float | Unset = UNSET
    structured_response: StructuredAddress | Unset = UNSET
    source_id: FinalDestinationSourceIdResponse | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.final_destination_source_id_response import FinalDestinationSourceIdResponse
        from ..models.feature_collection import FeatureCollection
        from ..models.structured_address import StructuredAddress
        from ..models.key_value import KeyValue
        id = str(self.id)

        address = self.address

        geojson: dict[str, Any]
        if isinstance(self.geojson, FeatureCollection):
            geojson = self.geojson.to_dict()
        else:
            geojson = self.geojson.to_dict()


        distance = self.distance

        search_confidence = self.search_confidence

        structured_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.structured_response, Unset):
            structured_response = self.structured_response.to_dict()

        source_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_id, Unset):
            source_id = self.source_id.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "address": address,
            "geojson": geojson,
        })
        if distance is not UNSET:
            field_dict["distance"] = distance
        if search_confidence is not UNSET:
            field_dict["search_confidence"] = search_confidence
        if structured_response is not UNSET:
            field_dict["structured_response"] = structured_response
        if source_id is not UNSET:
            field_dict["source_id"] = source_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.final_destination_source_id_response import FinalDestinationSourceIdResponse
        from ..models.feature_collection import FeatureCollection
        from ..models.structured_address import StructuredAddress
        from ..models.key_value import KeyValue
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        address = d.pop("address")

        def _parse_geojson(data: object) -> FeatureCollection | KeyValue:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geojson_type_0 = FeatureCollection.from_dict(data)



                return geojson_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            geojson_type_1 = KeyValue.from_dict(data)



            return geojson_type_1

        geojson = _parse_geojson(d.pop("geojson"))


        distance = d.pop("distance", UNSET)

        search_confidence = d.pop("search_confidence", UNSET)

        _structured_response = d.pop("structured_response", UNSET)
        structured_response: StructuredAddress | Unset
        if isinstance(_structured_response,  Unset):
            structured_response = UNSET
        else:
            structured_response = StructuredAddress.from_dict(_structured_response)




        _source_id = d.pop("source_id", UNSET)
        source_id: FinalDestinationSourceIdResponse | Unset
        if isinstance(_source_id,  Unset):
            source_id = UNSET
        else:
            source_id = FinalDestinationSourceIdResponse.from_dict(_source_id)




        final_destination_hit = cls(
            id=id,
            address=address,
            geojson=geojson,
            distance=distance,
            search_confidence=search_confidence,
            structured_response=structured_response,
            source_id=source_id,
        )

        return final_destination_hit

