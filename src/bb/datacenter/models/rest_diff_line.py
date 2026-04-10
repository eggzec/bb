from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_diff_line_conflict_marker import RestDiffLineConflictMarker
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestDiffLine")


@_attrs_define
class RestDiffLine:
    comment_ids: list[int] | Unset = UNSET
    conflict_marker: RestDiffLineConflictMarker | Unset = UNSET
    destination: int | Unset = UNSET
    line: str | Unset = UNSET
    source: int | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_ids: list[int] | Unset = UNSET
        if not isinstance(self.comment_ids, Unset):
            comment_ids = self.comment_ids

        conflict_marker: str | Unset = UNSET
        if not isinstance(self.conflict_marker, Unset):
            conflict_marker = self.conflict_marker.value

        destination = self.destination

        line = self.line

        source = self.source

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment_ids is not UNSET:
            field_dict["commentIds"] = comment_ids
        if conflict_marker is not UNSET:
            field_dict["conflictMarker"] = conflict_marker
        if destination is not UNSET:
            field_dict["destination"] = destination
        if line is not UNSET:
            field_dict["line"] = line
        if source is not UNSET:
            field_dict["source"] = source
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_ids = cast(list[int], d.pop("commentIds", UNSET))

        _conflict_marker = d.pop("conflictMarker", UNSET)
        conflict_marker: RestDiffLineConflictMarker | Unset
        if isinstance(_conflict_marker, Unset):
            conflict_marker = UNSET
        else:
            conflict_marker = RestDiffLineConflictMarker(_conflict_marker)

        destination = d.pop("destination", UNSET)

        line = d.pop("line", UNSET)

        source = d.pop("source", UNSET)

        truncated = d.pop("truncated", UNSET)

        rest_diff_line = cls(
            comment_ids=comment_ids,
            conflict_marker=conflict_marker,
            destination=destination,
            line=line,
            source=source,
            truncated=truncated,
        )

        rest_diff_line.additional_properties = d
        return rest_diff_line

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
