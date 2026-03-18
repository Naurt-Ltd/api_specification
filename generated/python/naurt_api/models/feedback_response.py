from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FeedbackResponse")



@_attrs_define
class FeedbackResponse:
    """ 
        Attributes:
            success (bool): Confirms that Naurt received the suggestion
     """

    success: bool





    def to_dict(self) -> dict[str, Any]:
        success = self.success


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "success": success,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        feedback_response = cls(
            success=success,
        )

        return feedback_response

