from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_pull_request_activity_action import RestPullRequestActivityAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_pull_request_activity_user import RestPullRequestActivityUser


T = TypeVar("T", bound="RestPullRequestActivity")


@_attrs_define
class RestPullRequestActivity:
    action: RestPullRequestActivityAction | Unset = UNSET
    created_date: int | Unset = UNSET
    id: int | Unset = UNSET
    user: RestPullRequestActivityUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        created_date = self.created_date

        id = self.id

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if id is not UNSET:
            field_dict["id"] = id
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_pull_request_activity_user import RestPullRequestActivityUser

        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: RestPullRequestActivityAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = RestPullRequestActivityAction(_action)

        created_date = d.pop("createdDate", UNSET)

        id = d.pop("id", UNSET)

        _user = d.pop("user", UNSET)
        user: RestPullRequestActivityUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RestPullRequestActivityUser.from_dict(_user)

        rest_pull_request_activity = cls(
            action=action,
            created_date=created_date,
            id=id,
            user=user,
        )

        rest_pull_request_activity.additional_properties = d
        return rest_pull_request_activity

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
