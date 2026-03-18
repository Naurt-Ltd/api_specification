from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.feedback_location import FeedbackLocation





T = TypeVar("T", bound="FeedbackQuery")



@_attrs_define
class FeedbackQuery:
    """ 
        Attributes:
            id (UUID | Unset): Existing Naurt ID for the address being updated
            address_string (str | Unset): Address text for a new feedback item. Address strings are not matched
                with current data, so existing addresses should use `id` instead.
            parking_location (FeedbackLocation | Unset):
            door_location (FeedbackLocation | Unset):
     """

    id: UUID | Unset = UNSET
    address_string: str | Unset = UNSET
    parking_location: FeedbackLocation | Unset = UNSET
    door_location: FeedbackLocation | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.feedback_location import FeedbackLocation
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        address_string = self.address_string

        parking_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parking_location, Unset):
            parking_location = self.parking_location.to_dict()

        door_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.door_location, Unset):
            door_location = self.door_location.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if address_string is not UNSET:
            field_dict["address_string"] = address_string
        if parking_location is not UNSET:
            field_dict["parking_location"] = parking_location
        if door_location is not UNSET:
            field_dict["door_location"] = door_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feedback_location import FeedbackLocation
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        address_string = d.pop("address_string", UNSET)

        _parking_location = d.pop("parking_location", UNSET)
        parking_location: FeedbackLocation | Unset
        if isinstance(_parking_location,  Unset):
            parking_location = UNSET
        else:
            parking_location = FeedbackLocation.from_dict(_parking_location)




        _door_location = d.pop("door_location", UNSET)
        door_location: FeedbackLocation | Unset
        if isinstance(_door_location,  Unset):
            door_location = UNSET
        else:
            door_location = FeedbackLocation.from_dict(_door_location)




        feedback_query = cls(
            id=id,
            address_string=address_string,
            parking_location=parking_location,
            door_location=door_location,
        )

        return feedback_query

