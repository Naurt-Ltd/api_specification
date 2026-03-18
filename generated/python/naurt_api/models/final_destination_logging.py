from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FinalDestinationLogging")



@_attrs_define
class FinalDestinationLogging:
    """ 
        Attributes:
            info (list[str] | Unset):
            warnings (list[str] | Unset):
            errors (list[str] | Unset):
     """

    info: list[str] | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    errors: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        info: list[str] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = self.info



        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings



        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if info is not UNSET:
            field_dict["info"] = info
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        info = cast(list[str], d.pop("info", UNSET))


        warnings = cast(list[str], d.pop("warnings", UNSET))


        errors = cast(list[str], d.pop("errors", UNSET))


        final_destination_logging = cls(
            info=info,
            warnings=warnings,
            errors=errors,
        )

        return final_destination_logging

