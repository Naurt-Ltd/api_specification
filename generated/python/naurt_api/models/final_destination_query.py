from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.country import Country
from ..models.language import Language
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.structured_address import StructuredAddress
  from ..models.final_destination_location import FinalDestinationLocation
  from ..models.final_destination_source_id_request import FinalDestinationSourceIdRequest





T = TypeVar("T", bound="FinalDestinationQuery")



@_attrs_define
class FinalDestinationQuery:
    """ A single search query. It can be used to lookup a door and parking spot by:
    - Forward geocode
    - Reverse geocode
    - Structured geocode
    - Naurt ID lookup
    - Source ID lookup

        Attributes:
            address_string (str | Unset):
            address_structured (StructuredAddress | Unset): Naurt's own format for structured address data. Please see:
                https://docs.naurt.com/reference/address-structure/ for significant more
                details on this data format.
            location (FinalDestinationLocation | Unset): A location, using WGS84 latitude and longitude.

                Used for a reverse geocode, or to add some location bias to a forward geocode.

                Use `distance_filter` to optionally limit the distance from this point that
                results can appear within
            id (UUID | Unset):
            country (Country | Unset): An enum representing all possible countries that Naurt currently supports
            source_id (FinalDestinationSourceIdRequest | Unset):
            additional_matches (bool | Unset):  Default: False.
            language (Language | Unset): Used for reverse geocodes only, to decide which language the response is in.
                In a forward geocode, the response language will match the input language.

                See: https://docs.naurt.com/reference/language/ for detailed information on
                language availability for all countries (not all countries have alternative
                languages)
     """

    address_string: str | Unset = UNSET
    address_structured: StructuredAddress | Unset = UNSET
    location: FinalDestinationLocation | Unset = UNSET
    id: UUID | Unset = UNSET
    country: Country | Unset = UNSET
    source_id: FinalDestinationSourceIdRequest | Unset = UNSET
    additional_matches: bool | Unset = False
    language: Language | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.structured_address import StructuredAddress
        from ..models.final_destination_location import FinalDestinationLocation
        from ..models.final_destination_source_id_request import FinalDestinationSourceIdRequest
        address_string = self.address_string

        address_structured: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address_structured, Unset):
            address_structured = self.address_structured.to_dict()

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        country: str | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.value


        source_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_id, Unset):
            source_id = self.source_id.to_dict()

        additional_matches = self.additional_matches

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if address_string is not UNSET:
            field_dict["address_string"] = address_string
        if address_structured is not UNSET:
            field_dict["address_structured"] = address_structured
        if location is not UNSET:
            field_dict["location"] = location
        if id is not UNSET:
            field_dict["id"] = id
        if country is not UNSET:
            field_dict["country"] = country
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if additional_matches is not UNSET:
            field_dict["additional_matches"] = additional_matches
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.structured_address import StructuredAddress
        from ..models.final_destination_location import FinalDestinationLocation
        from ..models.final_destination_source_id_request import FinalDestinationSourceIdRequest
        d = dict(src_dict)
        address_string = d.pop("address_string", UNSET)

        _address_structured = d.pop("address_structured", UNSET)
        address_structured: StructuredAddress | Unset
        if isinstance(_address_structured,  Unset):
            address_structured = UNSET
        else:
            address_structured = StructuredAddress.from_dict(_address_structured)




        _location = d.pop("location", UNSET)
        location: FinalDestinationLocation | Unset
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = FinalDestinationLocation.from_dict(_location)




        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _country = d.pop("country", UNSET)
        country: Country | Unset
        if isinstance(_country,  Unset):
            country = UNSET
        else:
            country = Country(_country)




        _source_id = d.pop("source_id", UNSET)
        source_id: FinalDestinationSourceIdRequest | Unset
        if isinstance(_source_id,  Unset):
            source_id = UNSET
        else:
            source_id = FinalDestinationSourceIdRequest.from_dict(_source_id)




        additional_matches = d.pop("additional_matches", UNSET)

        _language = d.pop("language", UNSET)
        language: Language | Unset
        if isinstance(_language,  Unset):
            language = UNSET
        else:
            language = Language(_language)




        final_destination_query = cls(
            address_string=address_string,
            address_structured=address_structured,
            location=location,
            id=id,
            country=country,
            source_id=source_id,
            additional_matches=additional_matches,
            language=language,
        )

        return final_destination_query

