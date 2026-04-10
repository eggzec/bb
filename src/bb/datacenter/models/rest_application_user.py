from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_application_user_type import RestApplicationUserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_application_user_links import RestApplicationUserLinks


T = TypeVar("T", bound="RestApplicationUser")


@_attrs_define
class RestApplicationUser:
    active: bool | Unset = UNSET
    avatar_url: str | Unset = UNSET
    display_name: str | Unset = UNSET
    email_address: str | Unset = UNSET
    id: int | Unset = UNSET
    links: RestApplicationUserLinks | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    type_: RestApplicationUserType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        avatar_url = self.avatar_url

        display_name = self.display_name

        email_address = self.email_address

        id = self.id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

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
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_application_user_links import RestApplicationUserLinks

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        display_name = d.pop("displayName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: RestApplicationUserLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestApplicationUserLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RestApplicationUserType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestApplicationUserType(_type_)

        rest_application_user = cls(
            active=active,
            avatar_url=avatar_url,
            display_name=display_name,
            email_address=email_address,
            id=id,
            links=links,
            name=name,
            slug=slug,
            type_=type_,
        )

        rest_application_user.additional_properties = d
        return rest_application_user

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
