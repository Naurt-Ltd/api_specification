from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SourceIdRequest")



@_attrs_define
class SourceIdRequest:
    """ Use this to request that Naurt returns a source ID for the addresses. Note that
    if a requested source ID is not available for that address, this option will
    be ignored.

        Attributes:
            os_uprn (bool | Unset):
            os_udprn (bool | Unset):
     """

    os_uprn: bool | Unset = UNSET
    os_udprn: bool | Unset = UNSET





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

        source_id_request = cls(
            os_uprn=os_uprn,
            os_udprn=os_udprn,
        )

        return source_id_request

