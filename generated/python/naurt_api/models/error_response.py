from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ErrorResponse")



@_attrs_define
class ErrorResponse:
    """ All Naurt errors come in this standard format.

    `code` is a unique error code you can quote to support, should you need to

    `reason` explains why this error has been received

    `remediation` gives steps to help resolve this error

        Attributes:
            code (str):
            reason (str):
            remediation (str):
     """

    code: str
    reason: str
    remediation: str





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        reason = self.reason

        remediation = self.remediation


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code": code,
            "reason": reason,
            "remediation": remediation,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        reason = d.pop("reason")

        remediation = d.pop("remediation")

        error_response = cls(
            code=code,
            reason=reason,
            remediation=remediation,
        )

        return error_response

