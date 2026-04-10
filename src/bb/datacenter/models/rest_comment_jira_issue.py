from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestCommentJiraIssue")


@_attrs_define
class RestCommentJiraIssue:
    comment_id: int | Unset = UNSET
    issue_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        issue_key = self.issue_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment_id is not UNSET:
            field_dict["commentId"] = comment_id
        if issue_key is not UNSET:
            field_dict["issueKey"] = issue_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_id = d.pop("commentId", UNSET)

        issue_key = d.pop("issueKey", UNSET)

        rest_comment_jira_issue = cls(
            comment_id=comment_id,
            issue_key=issue_key,
        )

        rest_comment_jira_issue.additional_properties = d
        return rest_comment_jira_issue

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
