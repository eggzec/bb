from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_file import CommitFile
    from ..models.search_content_match import SearchContentMatch
    from ..models.search_segment import SearchSegment


T = TypeVar("T", bound="SearchCodeSearchResult")


@_attrs_define
class SearchCodeSearchResult:
    type_: str | Unset = UNSET
    content_match_count: int | Unset = UNSET
    content_matches: list[SearchContentMatch] | Unset = UNSET
    path_matches: list[SearchSegment] | Unset = UNSET
    file: CommitFile | Unset = UNSET
    """ A file object, representing a file at a commit in a repository """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        content_match_count = self.content_match_count

        content_matches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content_matches, Unset):
            content_matches = []
            for content_matches_item_data in self.content_matches:
                content_matches_item = content_matches_item_data.to_dict()
                content_matches.append(content_matches_item)

        path_matches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.path_matches, Unset):
            path_matches = []
            for path_matches_item_data in self.path_matches:
                path_matches_item = path_matches_item_data.to_dict()
                path_matches.append(path_matches_item)

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content_match_count is not UNSET:
            field_dict["content_match_count"] = content_match_count
        if content_matches is not UNSET:
            field_dict["content_matches"] = content_matches
        if path_matches is not UNSET:
            field_dict["path_matches"] = path_matches
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit_file import CommitFile
        from ..models.search_content_match import SearchContentMatch
        from ..models.search_segment import SearchSegment

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        content_match_count = d.pop("content_match_count", UNSET)

        _content_matches = d.pop("content_matches", UNSET)
        content_matches: list[SearchContentMatch] | Unset = UNSET
        if _content_matches is not UNSET:
            content_matches = []
            for content_matches_item_data in _content_matches:
                content_matches_item = SearchContentMatch.from_dict(content_matches_item_data)

                content_matches.append(content_matches_item)

        _path_matches = d.pop("path_matches", UNSET)
        path_matches: list[SearchSegment] | Unset = UNSET
        if _path_matches is not UNSET:
            path_matches = []
            for path_matches_item_data in _path_matches:
                path_matches_item = SearchSegment.from_dict(path_matches_item_data)

                path_matches.append(path_matches_item)

        _file = d.pop("file", UNSET)
        file: CommitFile | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = CommitFile.from_dict(_file)

        search_code_search_result = cls(
            type_=type_,
            content_match_count=content_match_count,
            content_matches=content_matches,
            path_matches=path_matches,
            file=file,
        )

        search_code_search_result.additional_properties = d
        return search_code_search_result

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
