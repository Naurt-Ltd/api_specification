from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.geojson_type import GeojsonType
from ..models.input_filter import InputFilter
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.source_id_request import SourceIdRequest





T = TypeVar("T", bound="FinalDestinationOptions")



@_attrs_define
class FinalDestinationOptions:
    """ `options` impact all `queries` within a request

        Attributes:
            pretty_print (bool | Unset): This will format the response in a more human readable way. Only
                recommended for debug, as it increases payload size
                 Default: False.
            verbose (bool | Unset): Returns additional debug information about request processing. Only
                recommended for debug, as it increases payload size
                 Default: False.
            structured_response (bool | Unset): Adds the Naurt structured format of the address to the response
                 Default: False.
            geojson_type (GeojsonType | Unset): Use this to switch between a key-value style GeoJSON or a classic GeoJSON
            return_original (bool | Unset): Returns your original query back in the response
                 Default: False.
            input_filter (InputFilter | Unset): Input filtering helps when you have addresses from sources you can't
                control.
                Sometimes, providers might miss out on important parts of addresses, like a
                street number or postcode. If Naurt detects that an address is missing too
                many fields to be likely to give a good match, it can be rejected by this
                feature

                `none` turns this feature off and does not do any input filtering. This may
                result in some poor responses

                `loose` is the default - it does filter out some poor inputs but allows some
                missing fields

                `strict` is our strictest, and only allows searches which are likely to
                produce good matches
            source_id (SourceIdRequest | Unset): Use this to request that Naurt returns a source ID for the addresses. Note
                that
                if a requested source ID is not available for that address, this option will
                be ignored.
     """

    pretty_print: bool | Unset = False
    verbose: bool | Unset = False
    structured_response: bool | Unset = False
    geojson_type: GeojsonType | Unset = UNSET
    return_original: bool | Unset = False
    input_filter: InputFilter | Unset = UNSET
    source_id: SourceIdRequest | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.source_id_request import SourceIdRequest
        pretty_print = self.pretty_print

        verbose = self.verbose

        structured_response = self.structured_response

        geojson_type: str | Unset = UNSET
        if not isinstance(self.geojson_type, Unset):
            geojson_type = self.geojson_type.value


        return_original = self.return_original

        input_filter: str | Unset = UNSET
        if not isinstance(self.input_filter, Unset):
            input_filter = self.input_filter.value


        source_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_id, Unset):
            source_id = self.source_id.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if pretty_print is not UNSET:
            field_dict["pretty_print"] = pretty_print
        if verbose is not UNSET:
            field_dict["verbose"] = verbose
        if structured_response is not UNSET:
            field_dict["structured_response"] = structured_response
        if geojson_type is not UNSET:
            field_dict["geojson_type"] = geojson_type
        if return_original is not UNSET:
            field_dict["return_original"] = return_original
        if input_filter is not UNSET:
            field_dict["input_filter"] = input_filter
        if source_id is not UNSET:
            field_dict["source_id"] = source_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_id_request import SourceIdRequest
        d = dict(src_dict)
        pretty_print = d.pop("pretty_print", UNSET)

        verbose = d.pop("verbose", UNSET)

        structured_response = d.pop("structured_response", UNSET)

        _geojson_type = d.pop("geojson_type", UNSET)
        geojson_type: GeojsonType | Unset
        if isinstance(_geojson_type,  Unset):
            geojson_type = UNSET
        else:
            geojson_type = GeojsonType(_geojson_type)




        return_original = d.pop("return_original", UNSET)

        _input_filter = d.pop("input_filter", UNSET)
        input_filter: InputFilter | Unset
        if isinstance(_input_filter,  Unset):
            input_filter = UNSET
        else:
            input_filter = InputFilter(_input_filter)




        _source_id = d.pop("source_id", UNSET)
        source_id: SourceIdRequest | Unset
        if isinstance(_source_id,  Unset):
            source_id = UNSET
        else:
            source_id = SourceIdRequest.from_dict(_source_id)




        final_destination_options = cls(
            pretty_print=pretty_print,
            verbose=verbose,
            structured_response=structured_response,
            geojson_type=geojson_type,
            return_original=return_original,
            input_filter=input_filter,
            source_id=source_id,
        )

        return final_destination_options

