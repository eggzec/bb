from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_comment import RestComment
    from ..models.rest_diff_destination import RestDiffDestination
    from ..models.rest_diff_hunk import RestDiffHunk
    from ..models.rest_diff_properties import RestDiffProperties
    from ..models.rest_diff_source import RestDiffSource


T = TypeVar("T", bound="RestDiff")


@_attrs_define
class RestDiff:
    binary: bool | Unset = UNSET
    destination: RestDiffDestination | Unset = UNSET
    hunks: list[RestDiffHunk] | Unset = UNSET
    line_comments: list[RestComment] | Unset = UNSET
    properties: RestDiffProperties | Unset = UNSET
    source: RestDiffSource | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        binary = self.binary

        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        hunks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hunks, Unset):
            hunks = []
            for hunks_item_data in self.hunks:
                hunks_item = hunks_item_data.to_dict()
                hunks.append(hunks_item)

        line_comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_comments, Unset):
            line_comments = []
            for line_comments_item_data in self.line_comments:
                line_comments_item = line_comments_item_data.to_dict()
                line_comments.append(line_comments_item)

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if binary is not UNSET:
            field_dict["binary"] = binary
        if destination is not UNSET:
            field_dict["destination"] = destination
        if hunks is not UNSET:
            field_dict["hunks"] = hunks
        if line_comments is not UNSET:
            field_dict["lineComments"] = line_comments
        if properties is not UNSET:
            field_dict["properties"] = properties
        if source is not UNSET:
            field_dict["source"] = source
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_comment import RestComment
        from ..models.rest_diff_destination import RestDiffDestination
        from ..models.rest_diff_hunk import RestDiffHunk
        from ..models.rest_diff_properties import RestDiffProperties
        from ..models.rest_diff_source import RestDiffSource

        d = dict(src_dict)
        binary = d.pop("binary", UNSET)

        _destination = d.pop("destination", UNSET)
        destination: RestDiffDestination | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = RestDiffDestination.from_dict(_destination)

        _hunks = d.pop("hunks", UNSET)
        hunks: list[RestDiffHunk] | Unset = UNSET
        if _hunks is not UNSET:
            hunks = []
            for hunks_item_data in _hunks:
                hunks_item = RestDiffHunk.from_dict(hunks_item_data)

                hunks.append(hunks_item)

        _line_comments = d.pop("lineComments", UNSET)
        line_comments: list[RestComment] | Unset = UNSET
        if _line_comments is not UNSET:
            line_comments = []
            for line_comments_item_data in _line_comments:
                line_comments_item = RestComment.from_dict(line_comments_item_data)

                line_comments.append(line_comments_item)

        _properties = d.pop("properties", UNSET)
        properties: RestDiffProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = RestDiffProperties.from_dict(_properties)

        _source = d.pop("source", UNSET)
        source: RestDiffSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = RestDiffSource.from_dict(_source)

        truncated = d.pop("truncated", UNSET)

        rest_diff = cls(
            binary=binary,
            destination=destination,
            hunks=hunks,
            line_comments=line_comments,
            properties=properties,
            source=source,
            truncated=truncated,
        )

        rest_diff.additional_properties = d
        return rest_diff

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
