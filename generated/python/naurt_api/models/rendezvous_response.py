from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rendezvous_hit import RendezvousHit
  from ..models.rendezvous_query import RendezvousQuery





T = TypeVar("T", bound="RendezvousResponse")



@_attrs_define
class RendezvousResponse:
    """ 
        Attributes:
            responses (list[RendezvousHit]):
            unmatched (list[RendezvousQuery]): Queries that could not be matched
            version (None | str | Unset): API version used to service the request
            request_id (None | str | Unset): Request identifier useful when reporting issues to Naurt.
                Mentioned in the prose docs, though not shown in the response shape block.
     """

    responses: list[RendezvousHit]
    unmatched: list[RendezvousQuery]
    version: None | str | Unset = UNSET
    request_id: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.rendezvous_hit import RendezvousHit
        from ..models.rendezvous_query import RendezvousQuery
        responses = []
        for responses_item_data in self.responses:
            responses_item = responses_item_data.to_dict()
            responses.append(responses_item)



        unmatched = []
        for unmatched_item_data in self.unmatched:
            unmatched_item = unmatched_item_data.to_dict()
            unmatched.append(unmatched_item)



        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        request_id: None | str | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "responses": responses,
            "unmatched": unmatched,
        })
        if version is not UNSET:
            field_dict["version"] = version
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rendezvous_hit import RendezvousHit
        from ..models.rendezvous_query import RendezvousQuery
        d = dict(src_dict)
        responses = []
        _responses = d.pop("responses")
        for responses_item_data in (_responses):
            responses_item = RendezvousHit.from_dict(responses_item_data)



            responses.append(responses_item)


        unmatched = []
        _unmatched = d.pop("unmatched")
        for unmatched_item_data in (_unmatched):
            unmatched_item = RendezvousQuery.from_dict(unmatched_item_data)



            unmatched.append(unmatched_item)


        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))


        def _parse_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_id = _parse_request_id(d.pop("request_id", UNSET))


        rendezvous_response = cls(
            responses=responses,
            unmatched=unmatched,
            version=version,
            request_id=request_id,
        )

        return rendezvous_response

