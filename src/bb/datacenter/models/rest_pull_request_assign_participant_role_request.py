from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_pull_request_assign_participant_role_request_role import (
    RestPullRequestAssignParticipantRoleRequestRole,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_pull_request_assign_participant_role_request_user import (
        RestPullRequestAssignParticipantRoleRequestUser,
    )


T = TypeVar("T", bound="RestPullRequestAssignParticipantRoleRequest")


@_attrs_define
class RestPullRequestAssignParticipantRoleRequest:
    role: RestPullRequestAssignParticipantRoleRequestRole | Unset = UNSET
    user: RestPullRequestAssignParticipantRoleRequestUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_pull_request_assign_participant_role_request_user import (
            RestPullRequestAssignParticipantRoleRequestUser,
        )

        d = dict(src_dict)
        _role = d.pop("role", UNSET)
        role: RestPullRequestAssignParticipantRoleRequestRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RestPullRequestAssignParticipantRoleRequestRole(_role)

        _user = d.pop("user", UNSET)
        user: RestPullRequestAssignParticipantRoleRequestUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RestPullRequestAssignParticipantRoleRequestUser.from_dict(_user)

        rest_pull_request_assign_participant_role_request = cls(
            role=role,
            user=user,
        )

        rest_pull_request_assign_participant_role_request.additional_properties = d
        return rest_pull_request_assign_participant_role_request

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
