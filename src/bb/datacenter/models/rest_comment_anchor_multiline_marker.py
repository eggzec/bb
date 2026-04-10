from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_comment_anchor_multiline_marker_start_line_type import RestCommentAnchorMultilineMarkerStartLineType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestCommentAnchorMultilineMarker")


@_attrs_define
class RestCommentAnchorMultilineMarker:
    start_line_type: RestCommentAnchorMultilineMarkerStartLineType
    """ The segment type of the start line of the multiline comment """
    start_line: int | Unset = UNSET
    """ The line number where the multiline comment will begin """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_line_type = self.start_line_type.value

        start_line = self.start_line

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startLineType": start_line_type,
            }
        )
        if start_line is not UNSET:
            field_dict["startLine"] = start_line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_line_type = RestCommentAnchorMultilineMarkerStartLineType(d.pop("startLineType"))

        start_line = d.pop("startLine", UNSET)

        rest_comment_anchor_multiline_marker = cls(
            start_line_type=start_line_type,
            start_line=start_line,
        )

        rest_comment_anchor_multiline_marker.additional_properties = d
        return rest_comment_anchor_multiline_marker

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
