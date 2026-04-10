from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_multiline_comment_marker_start_line_type import RestMultilineCommentMarkerStartLineType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestMultilineCommentMarker")


@_attrs_define
class RestMultilineCommentMarker:
    start_line: int | Unset = UNSET
    """ The line number where the multiline comment will begin """
    start_line_type: RestMultilineCommentMarkerStartLineType | Unset = UNSET
    """ The segment type of the start line of the multiline comment """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_line = self.start_line

        start_line_type: str | Unset = UNSET
        if not isinstance(self.start_line_type, Unset):
            start_line_type = self.start_line_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_line is not UNSET:
            field_dict["startLine"] = start_line
        if start_line_type is not UNSET:
            field_dict["startLineType"] = start_line_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_line = d.pop("startLine", UNSET)

        _start_line_type = d.pop("startLineType", UNSET)
        start_line_type: RestMultilineCommentMarkerStartLineType | Unset
        if isinstance(_start_line_type, Unset):
            start_line_type = UNSET
        else:
            start_line_type = RestMultilineCommentMarkerStartLineType(_start_line_type)

        rest_multiline_comment_marker = cls(
            start_line=start_line,
            start_line_type=start_line_type,
        )

        rest_multiline_comment_marker.additional_properties = d
        return rest_multiline_comment_marker

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
