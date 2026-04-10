from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_user import ApplicationUser
    from ..models.rest_reviewer_group_scope import RestReviewerGroupScope


T = TypeVar("T", bound="RestReviewerGroup")


@_attrs_define
class RestReviewerGroup:
    avatar_url: str | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    scope: RestReviewerGroupScope | Unset = UNSET
    users: list[ApplicationUser] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar_url = self.avatar_url

        description = self.description

        id = self.id

        name = self.name

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_user import ApplicationUser
        from ..models.rest_reviewer_group_scope import RestReviewerGroupScope

        d = dict(src_dict)
        avatar_url = d.pop("avatarUrl", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: RestReviewerGroupScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RestReviewerGroupScope.from_dict(_scope)

        _users = d.pop("users", UNSET)
        users: list[ApplicationUser] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = ApplicationUser.from_dict(users_item_data)

                users.append(users_item)

        rest_reviewer_group = cls(
            avatar_url=avatar_url,
            description=description,
            id=id,
            name=name,
            scope=scope,
            users=users,
        )

        rest_reviewer_group.additional_properties = d
        return rest_reviewer_group

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
