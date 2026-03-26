from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.final_destination_status import FinalDestinationStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.final_destination_hit import FinalDestinationHit
  from ..models.final_destination_query import FinalDestinationQuery





T = TypeVar("T", bound="FinalDestinationHits")



@_attrs_define
class FinalDestinationHits:
    """ 
        Attributes:
            best_match (FinalDestinationHit | None):
            additional_matches (list[FinalDestinationHit]):
            status (FinalDestinationStatus): The `queries` and `responses` arrays are always 1:1. If no match can be found,
                a 404 will NOT be returned. Instead, check this enum for `no_matches`. That
                indicates no error has happened, but nothing was found. `ok` when something is
                found.
            original_request (FinalDestinationQuery | Unset): A single search query. It can be used to lookup a door and
                parking spot by:
                - Forward geocode
                - Reverse geocode
                - Structured geocode
                - Naurt ID lookup
                - Source ID lookup
     """

    best_match: FinalDestinationHit | None
    additional_matches: list[FinalDestinationHit]
    status: FinalDestinationStatus
    original_request: FinalDestinationQuery | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.final_destination_hit import FinalDestinationHit
        from ..models.final_destination_query import FinalDestinationQuery
        best_match: dict[str, Any] | None
        if isinstance(self.best_match, FinalDestinationHit):
            best_match = self.best_match.to_dict()
        else:
            best_match = self.best_match

        additional_matches = []
        for additional_matches_item_data in self.additional_matches:
            additional_matches_item = additional_matches_item_data.to_dict()
            additional_matches.append(additional_matches_item)



        status = self.status.value

        original_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_request, Unset):
            original_request = self.original_request.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "best_match": best_match,
            "additional_matches": additional_matches,
            "status": status,
        })
        if original_request is not UNSET:
            field_dict["original_request"] = original_request

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.final_destination_hit import FinalDestinationHit
        from ..models.final_destination_query import FinalDestinationQuery
        d = dict(src_dict)
        def _parse_best_match(data: object) -> FinalDestinationHit | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                best_match_type_0 = FinalDestinationHit.from_dict(data)



                return best_match_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FinalDestinationHit | None, data)

        best_match = _parse_best_match(d.pop("best_match"))


        additional_matches = []
        _additional_matches = d.pop("additional_matches")
        for additional_matches_item_data in (_additional_matches):
            additional_matches_item = FinalDestinationHit.from_dict(additional_matches_item_data)



            additional_matches.append(additional_matches_item)


        status = FinalDestinationStatus(d.pop("status"))




        _original_request = d.pop("original_request", UNSET)
        original_request: FinalDestinationQuery | Unset
        if isinstance(_original_request,  Unset):
            original_request = UNSET
        else:
            original_request = FinalDestinationQuery.from_dict(_original_request)




        final_destination_hits = cls(
            best_match=best_match,
            additional_matches=additional_matches,
            status=status,
            original_request=original_request,
        )

        return final_destination_hits

