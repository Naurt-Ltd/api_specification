from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.rendezvous_hit_data import RendezvousHitData





T = TypeVar("T", bound="RendezvousHit")



@_attrs_define
class RendezvousHit:
    """ 
        Attributes:
            centre (RendezvousHitData):
            covers (list[RendezvousHitData]):
     """

    centre: RendezvousHitData
    covers: list[RendezvousHitData]





    def to_dict(self) -> dict[str, Any]:
        from ..models.rendezvous_hit_data import RendezvousHitData
        centre = self.centre.to_dict()

        covers = []
        for covers_item_data in self.covers:
            covers_item = covers_item_data.to_dict()
            covers.append(covers_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "centre": centre,
            "covers": covers,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rendezvous_hit_data import RendezvousHitData
        d = dict(src_dict)
        centre = RendezvousHitData.from_dict(d.pop("centre"))




        covers = []
        _covers = d.pop("covers")
        for covers_item_data in (_covers):
            covers_item = RendezvousHitData.from_dict(covers_item_data)



            covers.append(covers_item)


        rendezvous_hit = cls(
            centre=centre,
            covers=covers,
        )

        return rendezvous_hit

