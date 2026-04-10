from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_detailed_user_type import RestDetailedUserType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_detailed_user_links import RestDetailedUserLinks


T = TypeVar("T", bound="RestDetailedUser")


@_attrs_define
class RestDetailedUser:
    active: bool | Unset = UNSET
    avatar_url: str | Unset = UNSET
    created_timestamp: float | Unset = UNSET
    deletable: bool | Unset = UNSET
    directory_name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    email_address: str | Unset = UNSET
    id: int | Unset = UNSET
    last_authentication_timestamp: float | Unset = UNSET
    links: RestDetailedUserLinks | Unset = UNSET
    mutable_details: bool | Unset = UNSET
    mutable_groups: bool | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    type_: RestDetailedUserType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        avatar_url = self.avatar_url

        created_timestamp = self.created_timestamp

        deletable = self.deletable

        directory_name = self.directory_name

        display_name = self.display_name

        email_address = self.email_address

        id = self.id

        last_authentication_timestamp = self.last_authentication_timestamp

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        mutable_details = self.mutable_details

        mutable_groups = self.mutable_groups

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
        if created_timestamp is not UNSET:
            field_dict["createdTimestamp"] = created_timestamp
        if deletable is not UNSET:
            field_dict["deletable"] = deletable
        if directory_name is not UNSET:
            field_dict["directoryName"] = directory_name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if id is not UNSET:
            field_dict["id"] = id
        if last_authentication_timestamp is not UNSET:
            field_dict["lastAuthenticationTimestamp"] = last_authentication_timestamp
        if links is not UNSET:
            field_dict["links"] = links
        if mutable_details is not UNSET:
            field_dict["mutableDetails"] = mutable_details
        if mutable_groups is not UNSET:
            field_dict["mutableGroups"] = mutable_groups
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_detailed_user_links import RestDetailedUserLinks

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        created_timestamp = d.pop("createdTimestamp", UNSET)

        deletable = d.pop("deletable", UNSET)

        directory_name = d.pop("directoryName", UNSET)

        display_name = d.pop("displayName", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        id = d.pop("id", UNSET)

        last_authentication_timestamp = d.pop("lastAuthenticationTimestamp", UNSET)

        _links = d.pop("links", UNSET)
        links: RestDetailedUserLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestDetailedUserLinks.from_dict(_links)

        mutable_details = d.pop("mutableDetails", UNSET)

        mutable_groups = d.pop("mutableGroups", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RestDetailedUserType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestDetailedUserType(_type_)

        rest_detailed_user = cls(
            active=active,
            avatar_url=avatar_url,
            created_timestamp=created_timestamp,
            deletable=deletable,
            directory_name=directory_name,
            display_name=display_name,
            email_address=email_address,
            id=id,
            last_authentication_timestamp=last_authentication_timestamp,
            links=links,
            mutable_details=mutable_details,
            mutable_groups=mutable_groups,
            name=name,
            slug=slug,
            type_=type_,
        )

        rest_detailed_user.additional_properties = d
        return rest_detailed_user

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
