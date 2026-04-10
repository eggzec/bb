from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.login_option_entity_type import LoginOptionEntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginOptionEntity")


@_attrs_define
class LoginOptionEntity:
    button_text: str | Unset = UNSET
    id: int | Unset = UNSET
    login_link: str | Unset = UNSET
    type_: LoginOptionEntityType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        button_text = self.button_text

        id = self.id

        login_link = self.login_link

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if button_text is not UNSET:
            field_dict["buttonText"] = button_text
        if id is not UNSET:
            field_dict["id"] = id
        if login_link is not UNSET:
            field_dict["loginLink"] = login_link
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        button_text = d.pop("buttonText", UNSET)

        id = d.pop("id", UNSET)

        login_link = d.pop("loginLink", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: LoginOptionEntityType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = LoginOptionEntityType(_type_)

        login_option_entity = cls(
            button_text=button_text,
            id=id,
            login_link=login_link,
            type_=type_,
        )

        login_option_entity.additional_properties = d
        return login_option_entity

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
