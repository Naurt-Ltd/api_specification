from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rendezvous_options import RendezvousOptions
  from ..models.rendezvous_query import RendezvousQuery





T = TypeVar("T", bound="RendezvousRequest")



@_attrs_define
class RendezvousRequest:
    """ 
        Attributes:
            queries (list[RendezvousQuery]): List of Query objects. The Query object is shared across Naurt APIs.
                Different query types may be mixed in the same request.
            options (RendezvousOptions | Unset): Optional Rendezvous request options
     """

    queries: list[RendezvousQuery]
    options: RendezvousOptions | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.rendezvous_options import RendezvousOptions
        from ..models.rendezvous_query import RendezvousQuery
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
        from ..models.rendezvous_options import RendezvousOptions
        from ..models.rendezvous_query import RendezvousQuery
        d = dict(src_dict)
        queries = []
        _queries = d.pop("queries")
        for queries_item_data in (_queries):
            queries_item = RendezvousQuery.from_dict(queries_item_data)



            queries.append(queries_item)


        _options = d.pop("options", UNSET)
        options: RendezvousOptions | Unset
        if isinstance(_options,  Unset):
            options = UNSET
        else:
            options = RendezvousOptions.from_dict(_options)




        rendezvous_request = cls(
            queries=queries,
            options=options,
        )

        return rendezvous_request

