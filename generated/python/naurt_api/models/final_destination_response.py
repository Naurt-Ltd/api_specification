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
  from ..models.final_destination_hits import FinalDestinationHits
  from ..models.final_destination_logging import FinalDestinationLogging





T = TypeVar("T", bound="FinalDestinationResponse")



@_attrs_define
class FinalDestinationResponse:
    """ A response from the API. The `responses` are in the same order as the original
    `queries` from the request.

        Attributes:
            responses (list[FinalDestinationHits]):
            version (str):
            request_id (UUID):
            logging (FinalDestinationLogging | Unset):
     """

    responses: list[FinalDestinationHits]
    version: str
    request_id: UUID
    logging: FinalDestinationLogging | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.final_destination_hits import FinalDestinationHits
        from ..models.final_destination_logging import FinalDestinationLogging
        responses = []
        for responses_item_data in self.responses:
            responses_item = responses_item_data.to_dict()
            responses.append(responses_item)



        version = self.version

        request_id = str(self.request_id)

        logging: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logging, Unset):
            logging = self.logging.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "responses": responses,
            "version": version,
            "request_id": request_id,
        })
        if logging is not UNSET:
            field_dict["logging"] = logging

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.final_destination_hits import FinalDestinationHits
        from ..models.final_destination_logging import FinalDestinationLogging
        d = dict(src_dict)
        responses = []
        _responses = d.pop("responses")
        for responses_item_data in (_responses):
            responses_item = FinalDestinationHits.from_dict(responses_item_data)



            responses.append(responses_item)


        version = d.pop("version")

        request_id = UUID(d.pop("request_id"))




        _logging = d.pop("logging", UNSET)
        logging: FinalDestinationLogging | Unset
        if isinstance(_logging,  Unset):
            logging = UNSET
        else:
            logging = FinalDestinationLogging.from_dict(_logging)




        final_destination_response = cls(
            responses=responses,
            version=version,
            request_id=request_id,
            logging=logging,
        )

        return final_destination_response

