from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_permitted_user_permission import RestPermittedUserPermission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_permitted_user_user import RestPermittedUserUser


T = TypeVar("T", bound="RestPermittedUser")


@_attrs_define
class RestPermittedUser:
    permission: RestPermittedUserPermission | Unset = UNSET
    user: RestPermittedUserUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_permitted_user_user import RestPermittedUserUser

        d = dict(src_dict)
        _permission = d.pop("permission", UNSET)
        permission: RestPermittedUserPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = RestPermittedUserPermission(_permission)

        _user = d.pop("user", UNSET)
        user: RestPermittedUserUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RestPermittedUserUser.from_dict(_user)

        rest_permitted_user = cls(
            permission=permission,
            user=user,
        )

        rest_permitted_user.additional_properties = d
        return rest_permitted_user

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
