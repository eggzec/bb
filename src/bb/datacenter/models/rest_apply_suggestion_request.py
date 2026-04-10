from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestApplySuggestionRequest")


@_attrs_define
class RestApplySuggestionRequest:
    comment_version: int
    pull_request_version: int
    suggestion_index: int
    commit_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_version = self.comment_version

        pull_request_version = self.pull_request_version

        suggestion_index = self.suggestion_index

        commit_message = self.commit_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commentVersion": comment_version,
                "pullRequestVersion": pull_request_version,
                "suggestionIndex": suggestion_index,
            }
        )
        if commit_message is not UNSET:
            field_dict["commitMessage"] = commit_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_version = d.pop("commentVersion")

        pull_request_version = d.pop("pullRequestVersion")

        suggestion_index = d.pop("suggestionIndex")

        commit_message = d.pop("commitMessage", UNSET)

        rest_apply_suggestion_request = cls(
            comment_version=comment_version,
            pull_request_version=pull_request_version,
            suggestion_index=suggestion_index,
            commit_message=commit_message,
        )

        rest_apply_suggestion_request.additional_properties = d
        return rest_apply_suggestion_request

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
