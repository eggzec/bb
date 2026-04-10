from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comment_thread_diff_anchor_diff_type import CommentThreadDiffAnchorDiffType
from ..models.comment_thread_diff_anchor_file_type import CommentThreadDiffAnchorFileType
from ..models.comment_thread_diff_anchor_line_type import CommentThreadDiffAnchorLineType
from ..models.comment_thread_diff_anchor_multiline_start_line_type import CommentThreadDiffAnchorMultilineStartLineType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_number_range import LineNumberRange


T = TypeVar("T", bound="CommentThreadDiffAnchor")


@_attrs_define
class CommentThreadDiffAnchor:
    diff_type: CommentThreadDiffAnchorDiffType
    file_type: CommentThreadDiffAnchorFileType
    from_hash: str
    line_type: CommentThreadDiffAnchorLineType
    multiline_destination_range: LineNumberRange
    multiline_source_range: LineNumberRange
    multiline_start_line: int
    multiline_start_line_type: CommentThreadDiffAnchorMultilineStartLineType
    path: str
    src_path: str
    to_hash: str
    file_anchor: bool | Unset = UNSET
    line: int | Unset = UNSET
    line_anchor: bool | Unset = UNSET
    multiline_anchor: bool | Unset = UNSET
    orphaned: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        diff_type = self.diff_type.value

        file_type = self.file_type.value

        from_hash = self.from_hash

        line_type = self.line_type.value

        multiline_destination_range = self.multiline_destination_range.to_dict()

        multiline_source_range = self.multiline_source_range.to_dict()

        multiline_start_line = self.multiline_start_line

        multiline_start_line_type = self.multiline_start_line_type.value

        path = self.path

        src_path = self.src_path

        to_hash = self.to_hash

        file_anchor = self.file_anchor

        line = self.line

        line_anchor = self.line_anchor

        multiline_anchor = self.multiline_anchor

        orphaned = self.orphaned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "diffType": diff_type,
                "fileType": file_type,
                "fromHash": from_hash,
                "lineType": line_type,
                "multilineDestinationRange": multiline_destination_range,
                "multilineSourceRange": multiline_source_range,
                "multilineStartLine": multiline_start_line,
                "multilineStartLineType": multiline_start_line_type,
                "path": path,
                "srcPath": src_path,
                "toHash": to_hash,
            }
        )
        if file_anchor is not UNSET:
            field_dict["fileAnchor"] = file_anchor
        if line is not UNSET:
            field_dict["line"] = line
        if line_anchor is not UNSET:
            field_dict["lineAnchor"] = line_anchor
        if multiline_anchor is not UNSET:
            field_dict["multilineAnchor"] = multiline_anchor
        if orphaned is not UNSET:
            field_dict["orphaned"] = orphaned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.line_number_range import LineNumberRange

        d = dict(src_dict)
        diff_type = CommentThreadDiffAnchorDiffType(d.pop("diffType"))

        file_type = CommentThreadDiffAnchorFileType(d.pop("fileType"))

        from_hash = d.pop("fromHash")

        line_type = CommentThreadDiffAnchorLineType(d.pop("lineType"))

        multiline_destination_range = LineNumberRange.from_dict(d.pop("multilineDestinationRange"))

        multiline_source_range = LineNumberRange.from_dict(d.pop("multilineSourceRange"))

        multiline_start_line = d.pop("multilineStartLine")

        multiline_start_line_type = CommentThreadDiffAnchorMultilineStartLineType(d.pop("multilineStartLineType"))

        path = d.pop("path")

        src_path = d.pop("srcPath")

        to_hash = d.pop("toHash")

        file_anchor = d.pop("fileAnchor", UNSET)

        line = d.pop("line", UNSET)

        line_anchor = d.pop("lineAnchor", UNSET)

        multiline_anchor = d.pop("multilineAnchor", UNSET)

        orphaned = d.pop("orphaned", UNSET)

        comment_thread_diff_anchor = cls(
            diff_type=diff_type,
            file_type=file_type,
            from_hash=from_hash,
            line_type=line_type,
            multiline_destination_range=multiline_destination_range,
            multiline_source_range=multiline_source_range,
            multiline_start_line=multiline_start_line,
            multiline_start_line_type=multiline_start_line_type,
            path=path,
            src_path=src_path,
            to_hash=to_hash,
            file_anchor=file_anchor,
            line=line,
            line_anchor=line_anchor,
            multiline_anchor=multiline_anchor,
            orphaned=orphaned,
        )

        comment_thread_diff_anchor.additional_properties = d
        return comment_thread_diff_anchor

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
