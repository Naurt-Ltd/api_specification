from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.final_destination_options import FinalDestinationOptions
  from ..models.final_destination_query import FinalDestinationQuery





T = TypeVar("T", bound="FinalDestinationRequest")



@_attrs_define
class FinalDestinationRequest:
    """ A single request to the API, which can contain up to 200 queries. Each query
    is independent and can be of a different type.

        Attributes:
            queries (list[FinalDestinationQuery]):
            options (FinalDestinationOptions | Unset): `options` impact all `queries` within a request
     """

    queries: list[FinalDestinationQuery]
    options: FinalDestinationOptions | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.final_destination_options import FinalDestinationOptions
        from ..models.final_destination_query import FinalDestinationQuery
        queries = []
        for queries_item_data in self.queries:
            queries_item = queries_item_data.to_dict()
            queries.append(queries_item)



        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "queries": queries,
        })
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.final_destination_options import FinalDestinationOptions
        from ..models.final_destination_query import FinalDestinationQuery
        d = dict(src_dict)
        queries = []
        _queries = d.pop("queries")
        for queries_item_data in (_queries):
            queries_item = FinalDestinationQuery.from_dict(queries_item_data)



            queries.append(queries_item)


        _options = d.pop("options", UNSET)
        options: FinalDestinationOptions | Unset
        if isinstance(_options,  Unset):
            options = UNSET
        else:
            options = FinalDestinationOptions.from_dict(_options)




        final_destination_request = cls(
            queries=queries,
            options=options,
        )

        return final_destination_request

