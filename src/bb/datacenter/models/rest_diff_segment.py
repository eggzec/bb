from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_diff_segment_type import RestDiffSegmentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_diff_line import RestDiffLine


T = TypeVar("T", bound="RestDiffSegment")


@_attrs_define
class RestDiffSegment:
    lines: list[RestDiffLine] | Unset = UNSET
    truncated: bool | Unset = UNSET
    type_: RestDiffSegmentType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        truncated = self.truncated

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lines is not UNSET:
            field_dict["lines"] = lines
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_diff_line import RestDiffLine

        d = dict(src_dict)
        _lines = d.pop("lines", UNSET)
        lines: list[RestDiffLine] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = RestDiffLine.from_dict(lines_item_data)

                lines.append(lines_item)

        truncated = d.pop("truncated", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RestDiffSegmentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestDiffSegmentType(_type_)

        rest_diff_segment = cls(
            lines=lines,
            truncated=truncated,
            type_=type_,
        )

        rest_diff_segment.additional_properties = d
        return rest_diff_segment

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
