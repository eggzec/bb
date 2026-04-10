from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_diff_segment import RestDiffSegment


T = TypeVar("T", bound="RestDiffHunk")


@_attrs_define
class RestDiffHunk:
    context: str | Unset = UNSET
    destination_line: int | Unset = UNSET
    destination_span: int | Unset = UNSET
    segments: list[RestDiffSegment] | Unset = UNSET
    source_line: int | Unset = UNSET
    source_span: int | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context = self.context

        destination_line = self.destination_line

        destination_span = self.destination_span

        segments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.segments, Unset):
            segments = []
            for segments_item_data in self.segments:
                segments_item = segments_item_data.to_dict()
                segments.append(segments_item)

        source_line = self.source_line

        source_span = self.source_span

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if destination_line is not UNSET:
            field_dict["destinationLine"] = destination_line
        if destination_span is not UNSET:
            field_dict["destinationSpan"] = destination_span
        if segments is not UNSET:
            field_dict["segments"] = segments
        if source_line is not UNSET:
            field_dict["sourceLine"] = source_line
        if source_span is not UNSET:
            field_dict["sourceSpan"] = source_span
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_diff_segment import RestDiffSegment

        d = dict(src_dict)
        context = d.pop("context", UNSET)

        destination_line = d.pop("destinationLine", UNSET)

        destination_span = d.pop("destinationSpan", UNSET)

        _segments = d.pop("segments", UNSET)
        segments: list[RestDiffSegment] | Unset = UNSET
        if _segments is not UNSET:
            segments = []
            for segments_item_data in _segments:
                segments_item = RestDiffSegment.from_dict(segments_item_data)

                segments.append(segments_item)

        source_line = d.pop("sourceLine", UNSET)

        source_span = d.pop("sourceSpan", UNSET)

        truncated = d.pop("truncated", UNSET)

        rest_diff_hunk = cls(
            context=context,
            destination_line=destination_line,
            destination_span=destination_span,
            segments=segments,
            source_line=source_line,
            source_span=source_span,
            truncated=truncated,
        )

        rest_diff_hunk.additional_properties = d
        return rest_diff_hunk

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
