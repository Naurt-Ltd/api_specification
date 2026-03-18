from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="StructuredAddress")



@_attrs_define
class StructuredAddress:
    """ Naurt's own format for structured address data. Please see:
    https://docs.naurt.com/reference/address-structure/ for significant more
    details on this data format.

        Attributes:
            unit (str | Unset):
            house_name (str | Unset):
            street_number (str | Unset):
            street_name (str | Unset):
            locality (str | Unset):
            city (str | Unset):
            county (str | Unset):
            state (str | Unset):
            country (str | Unset):
            postalcode (str | Unset):
     """

    unit: str | Unset = UNSET
    house_name: str | Unset = UNSET
    street_number: str | Unset = UNSET
    street_name: str | Unset = UNSET
    locality: str | Unset = UNSET
    city: str | Unset = UNSET
    county: str | Unset = UNSET
    state: str | Unset = UNSET
    country: str | Unset = UNSET
    postalcode: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        house_name = self.house_name

        street_number = self.street_number

        street_name = self.street_name

        locality = self.locality

        city = self.city

        county = self.county

        state = self.state

        country = self.country

        postalcode = self.postalcode


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if unit is not UNSET:
            field_dict["unit"] = unit
        if house_name is not UNSET:
            field_dict["house_name"] = house_name
        if street_number is not UNSET:
            field_dict["street_number"] = street_number
        if street_name is not UNSET:
            field_dict["street_name"] = street_name
        if locality is not UNSET:
            field_dict["locality"] = locality
        if city is not UNSET:
            field_dict["city"] = city
        if county is not UNSET:
            field_dict["county"] = county
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if postalcode is not UNSET:
            field_dict["postalcode"] = postalcode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit = d.pop("unit", UNSET)

        house_name = d.pop("house_name", UNSET)

        street_number = d.pop("street_number", UNSET)

        street_name = d.pop("street_name", UNSET)

        locality = d.pop("locality", UNSET)

        city = d.pop("city", UNSET)

        county = d.pop("county", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        postalcode = d.pop("postalcode", UNSET)

        structured_address = cls(
            unit=unit,
            house_name=house_name,
            street_number=street_number,
            street_name=street_name,
            locality=locality,
            city=city,
            county=county,
            state=state,
            country=country,
            postalcode=postalcode,
        )

        return structured_address

