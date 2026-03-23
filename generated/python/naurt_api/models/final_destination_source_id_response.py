from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FinalDestinationSourceIdResponse")



@_attrs_define
class FinalDestinationSourceIdResponse:
    """ An object containing information on source IDs. Source IDs refer to underlying
    IDs from address data sets. Currently supporting UPRN and UDPRN in the UK
    referring to the OrdnanceSurvey datasets

        Example:
            {'UPRN': {'value': {'os_uprn': '100062664604'}}, 'UDPRN': {'value': {'os_udprn': '25962203'}}}

        Attributes:
            os_uprn (str | Unset):
            os_udprn (str | Unset):
     """

    os_uprn: str | Unset = UNSET
    os_udprn: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        os_uprn = self.os_uprn

        os_udprn = self.os_udprn


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if os_uprn is not UNSET:
            field_dict["os_uprn"] = os_uprn
        if os_udprn is not UNSET:
            field_dict["os_udprn"] = os_udprn

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        os_uprn = d.pop("os_uprn", UNSET)

        os_udprn = d.pop("os_udprn", UNSET)

        final_destination_source_id_response = cls(
            os_uprn=os_uprn,
            os_udprn=os_udprn,
        )

        return final_destination_source_id_response

