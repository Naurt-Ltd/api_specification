from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FinalDestinationSourceIdRequest")



@_attrs_define
class FinalDestinationSourceIdRequest:
    """ 
        Attributes:
            one_of (Any | Unset):
     """

    one_of: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        one_of = self.one_of


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if one_of is not UNSET:
            field_dict["oneOf"] = one_of

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        one_of = d.pop("oneOf", UNSET)

        final_destination_source_id_request = cls(
            one_of=one_of,
        )

        return final_destination_source_id_request

