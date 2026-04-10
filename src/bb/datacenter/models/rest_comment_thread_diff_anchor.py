from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_comment_thread_diff_anchor_diff_type import RestCommentThreadDiffAnchorDiffType
from ..models.rest_comment_thread_diff_anchor_file_type import RestCommentThreadDiffAnchorFileType
from ..models.rest_comment_thread_diff_anchor_line_type import RestCommentThreadDiffAnchorLineType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_comment_thread_diff_anchor_multiline_marker import RestCommentThreadDiffAnchorMultilineMarker
    from ..models.rest_comment_thread_diff_anchor_multiline_span import RestCommentThreadDiffAnchorMultilineSpan
    from ..models.rest_comment_thread_diff_anchor_path import RestCommentThreadDiffAnchorPath
    from ..models.rest_comment_thread_diff_anchor_pull_request import RestCommentThreadDiffAnchorPullRequest
    from ..models.rest_comment_thread_diff_anchor_src_path import RestCommentThreadDiffAnchorSrcPath


T = TypeVar("T", bound="RestCommentThreadDiffAnchor")


@_attrs_define
class RestCommentThreadDiffAnchor:
    diff_type: RestCommentThreadDiffAnchorDiffType | Unset = UNSET
    file_type: RestCommentThreadDiffAnchorFileType | Unset = UNSET
    from_hash: str | Unset = UNSET
    line: int | Unset = UNSET
    line_type: RestCommentThreadDiffAnchorLineType | Unset = UNSET
    multiline_marker: RestCommentThreadDiffAnchorMultilineMarker | Unset = UNSET
    multiline_span: RestCommentThreadDiffAnchorMultilineSpan | Unset = UNSET
    path: RestCommentThreadDiffAnchorPath | Unset = UNSET
    pull_request: RestCommentThreadDiffAnchorPullRequest | Unset = UNSET
    src_path: RestCommentThreadDiffAnchorSrcPath | Unset = UNSET
    to_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        diff_type: str | Unset = UNSET
        if not isinstance(self.diff_type, Unset):
            diff_type = self.diff_type.value

        file_type: str | Unset = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        from_hash = self.from_hash

        line = self.line

        line_type: str | Unset = UNSET
        if not isinstance(self.line_type, Unset):
            line_type = self.line_type.value

        multiline_marker: dict[str, Any] | Unset = UNSET
        if not isinstance(self.multiline_marker, Unset):
            multiline_marker = self.multiline_marker.to_dict()

        multiline_span: dict[str, Any] | Unset = UNSET
        if not isinstance(self.multiline_span, Unset):
            multiline_span = self.multiline_span.to_dict()

        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        pull_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pull_request, Unset):
            pull_request = self.pull_request.to_dict()

        src_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.src_path, Unset):
            src_path = self.src_path.to_dict()

        to_hash = self.to_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if diff_type is not UNSET:
            field_dict["diffType"] = diff_type
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if from_hash is not UNSET:
            field_dict["fromHash"] = from_hash
        if line is not UNSET:
            field_dict["line"] = line
        if line_type is not UNSET:
            field_dict["lineType"] = line_type
        if multiline_marker is not UNSET:
            field_dict["multilineMarker"] = multiline_marker
        if multiline_span is not UNSET:
            field_dict["multilineSpan"] = multiline_span
        if path is not UNSET:
            field_dict["path"] = path
        if pull_request is not UNSET:
            field_dict["pullRequest"] = pull_request
        if src_path is not UNSET:
            field_dict["srcPath"] = src_path
        if to_hash is not UNSET:
            field_dict["toHash"] = to_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_comment_thread_diff_anchor_multiline_marker import RestCommentThreadDiffAnchorMultilineMarker
        from ..models.rest_comment_thread_diff_anchor_multiline_span import RestCommentThreadDiffAnchorMultilineSpan
        from ..models.rest_comment_thread_diff_anchor_path import RestCommentThreadDiffAnchorPath
        from ..models.rest_comment_thread_diff_anchor_pull_request import RestCommentThreadDiffAnchorPullRequest
        from ..models.rest_comment_thread_diff_anchor_src_path import RestCommentThreadDiffAnchorSrcPath

        d = dict(src_dict)
        _diff_type = d.pop("diffType", UNSET)
        diff_type: RestCommentThreadDiffAnchorDiffType | Unset
        if isinstance(_diff_type, Unset):
            diff_type = UNSET
        else:
            diff_type = RestCommentThreadDiffAnchorDiffType(_diff_type)

        _file_type = d.pop("fileType", UNSET)
        file_type: RestCommentThreadDiffAnchorFileType | Unset
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = RestCommentThreadDiffAnchorFileType(_file_type)

        from_hash = d.pop("fromHash", UNSET)

        line = d.pop("line", UNSET)

        _line_type = d.pop("lineType", UNSET)
        line_type: RestCommentThreadDiffAnchorLineType | Unset
        if isinstance(_line_type, Unset):
            line_type = UNSET
        else:
            line_type = RestCommentThreadDiffAnchorLineType(_line_type)

        _multiline_marker = d.pop("multilineMarker", UNSET)
        multiline_marker: RestCommentThreadDiffAnchorMultilineMarker | Unset
        if isinstance(_multiline_marker, Unset):
            multiline_marker = UNSET
        else:
            multiline_marker = RestCommentThreadDiffAnchorMultilineMarker.from_dict(_multiline_marker)

        _multiline_span = d.pop("multilineSpan", UNSET)
        multiline_span: RestCommentThreadDiffAnchorMultilineSpan | Unset
        if isinstance(_multiline_span, Unset):
            multiline_span = UNSET
        else:
            multiline_span = RestCommentThreadDiffAnchorMultilineSpan.from_dict(_multiline_span)

        _path = d.pop("path", UNSET)
        path: RestCommentThreadDiffAnchorPath | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = RestCommentThreadDiffAnchorPath.from_dict(_path)

        _pull_request = d.pop("pullRequest", UNSET)
        pull_request: RestCommentThreadDiffAnchorPullRequest | Unset
        if isinstance(_pull_request, Unset):
            pull_request = UNSET
        else:
            pull_request = RestCommentThreadDiffAnchorPullRequest.from_dict(_pull_request)

        _src_path = d.pop("srcPath", UNSET)
        src_path: RestCommentThreadDiffAnchorSrcPath | Unset
        if isinstance(_src_path, Unset):
            src_path = UNSET
        else:
            src_path = RestCommentThreadDiffAnchorSrcPath.from_dict(_src_path)

        to_hash = d.pop("toHash", UNSET)

        rest_comment_thread_diff_anchor = cls(
            diff_type=diff_type,
            file_type=file_type,
            from_hash=from_hash,
            line=line,
            line_type=line_type,
            multiline_marker=multiline_marker,
            multiline_span=multiline_span,
            path=path,
            pull_request=pull_request,
            src_path=src_path,
            to_hash=to_hash,
        )

        rest_comment_thread_diff_anchor.additional_properties = d
        return rest_comment_thread_diff_anchor

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
