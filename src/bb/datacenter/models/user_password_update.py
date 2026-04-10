from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPasswordUpdate")


@_attrs_define
class UserPasswordUpdate:
    old_password: str | Unset = UNSET
    password: str | Unset = UNSET
    password_confirm: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        old_password = self.old_password

        password = self.password

        password_confirm = self.password_confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if old_password is not UNSET:
            field_dict["oldPassword"] = old_password
        if password is not UNSET:
            field_dict["password"] = password
        if password_confirm is not UNSET:
            field_dict["passwordConfirm"] = password_confirm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        old_password = d.pop("oldPassword", UNSET)

        password = d.pop("password", UNSET)

        password_confirm = d.pop("passwordConfirm", UNSET)

        user_password_update = cls(
            old_password=old_password,
            password=password,
            password_confirm=password_confirm,
        )

        user_password_update.additional_properties = d
        return user_password_update

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
