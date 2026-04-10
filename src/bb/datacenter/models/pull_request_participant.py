from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pull_request_participant_role import PullRequestParticipantRole
from ..models.pull_request_participant_status import PullRequestParticipantStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_user import ApplicationUser
    from ..models.pull_request import PullRequest


T = TypeVar("T", bound="PullRequestParticipant")


@_attrs_define
class PullRequestParticipant:
    pull_request: PullRequest
    role: PullRequestParticipantRole
    status: PullRequestParticipantStatus
    user: ApplicationUser
    approved: bool | Unset = UNSET
    last_reviewed_commit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pull_request = self.pull_request.to_dict()

        role = self.role.value

        status = self.status.value

        user = self.user.to_dict()

        approved = self.approved

        last_reviewed_commit = self.last_reviewed_commit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pullRequest": pull_request,
                "role": role,
                "status": status,
                "user": user,
            }
        )
        if approved is not UNSET:
            field_dict["approved"] = approved
        if last_reviewed_commit is not UNSET:
            field_dict["lastReviewedCommit"] = last_reviewed_commit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_user import ApplicationUser
        from ..models.pull_request import PullRequest

        d = dict(src_dict)
        pull_request = PullRequest.from_dict(d.pop("pullRequest"))

        role = PullRequestParticipantRole(d.pop("role"))

        status = PullRequestParticipantStatus(d.pop("status"))

        user = ApplicationUser.from_dict(d.pop("user"))

        approved = d.pop("approved", UNSET)

        last_reviewed_commit = d.pop("lastReviewedCommit", UNSET)

        pull_request_participant = cls(
            pull_request=pull_request,
            role=role,
            status=status,
            user=user,
            approved=approved,
            last_reviewed_commit=last_reviewed_commit,
        )

        pull_request_participant.additional_properties = d
        return pull_request_participant

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
