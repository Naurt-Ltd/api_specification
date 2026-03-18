from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RendezvousQuery")



@_attrs_define
class RendezvousQuery:
    """ Shared Naurt Query object.

    The Rendezvous spec refers to the shared Search Query specification.
    At minimum, address-based queries such as `address_string` are supported.
    Other shared query forms may also be accepted.

        Example:
            {'address_string': '18a, Montague Place, Brighton, BN2 1JE, United Kingdom'}

        Attributes:
            address_string (str | Unset): Free-form address query string
            latitude (float | Unset):
            longitude (float | Unset):
     """

    address_string: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        address_string = self.address_string

        latitude = self.latitude

        longitude = self.longitude


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address_string is not UNSET:
            field_dict["address_string"] = address_string
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address_string = d.pop("address_string", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        rendezvous_query = cls(
            address_string=address_string,
            latitude=latitude,
            longitude=longitude,
        )


        rendezvous_query.additional_properties = d
        return rendezvous_query

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
