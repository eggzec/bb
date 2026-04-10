from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestPullRequestFinishReviewRequest")


@_attrs_define
class RestPullRequestFinishReviewRequest:
    comment_text: str | Unset = UNSET
    last_reviewed_commit: str | Unset = UNSET
    participant_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_text = self.comment_text

        last_reviewed_commit = self.last_reviewed_commit

        participant_status = self.participant_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment_text is not UNSET:
            field_dict["commentText"] = comment_text
        if last_reviewed_commit is not UNSET:
            field_dict["lastReviewedCommit"] = last_reviewed_commit
        if participant_status is not UNSET:
            field_dict["participantStatus"] = participant_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_text = d.pop("commentText", UNSET)

        last_reviewed_commit = d.pop("lastReviewedCommit", UNSET)

        participant_status = d.pop("participantStatus", UNSET)

        rest_pull_request_finish_review_request = cls(
            comment_text=comment_text,
            last_reviewed_commit=last_reviewed_commit,
            participant_status=participant_status,
        )

        rest_pull_request_finish_review_request.additional_properties = d
        return rest_pull_request_finish_review_request

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
