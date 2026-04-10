from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.application_user_type import ApplicationUserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationUser")


@_attrs_define
class ApplicationUser:
    active: bool | Unset = UNSET
    display_name: str | Unset = UNSET
    email_address: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    type_: ApplicationUserType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        display_name = self.display_name

        email_address = self.email_address

        id = self.id

        name = self.name

        slug = self.slug

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active", UNSET)

        display_name = d.pop("displayName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ApplicationUserType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ApplicationUserType(_type_)

        application_user = cls(
            active=active,
            display_name=display_name,
            email_address=email_address,
            id=id,
            name=name,
            slug=slug,
            type_=type_,
        )

        application_user.additional_properties = d
        return application_user

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
