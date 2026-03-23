from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="OptionsResponse")



@_attrs_define
class OptionsResponse:
    """ 
        Attributes:
            current_version (str):
            deprecated_versions (list[str]):
     """

    current_version: str
    deprecated_versions: list[str]





    def to_dict(self) -> dict[str, Any]:
        current_version = self.current_version

        deprecated_versions = self.deprecated_versions




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "current_version": current_version,
            "deprecated_versions": deprecated_versions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_version = d.pop("current_version")

        deprecated_versions = cast(list[str], d.pop("deprecated_versions"))


        options_response = cls(
            current_version=current_version,
            deprecated_versions=deprecated_versions,
        )

        return options_response

