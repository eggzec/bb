from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_project_type import RestProjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_project_links import RestProjectLinks


T = TypeVar("T", bound="RestProject")


@_attrs_define
class RestProject:
    avatar: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    key: str | Unset = UNSET
    links: RestProjectLinks | Unset = UNSET
    name: str | Unset = UNSET
    public: bool | Unset = UNSET
    scope: str | Unset = UNSET
    type_: RestProjectType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar = self.avatar

        avatar_url = self.avatar_url

        description = self.description

        id = self.id

        key = self.key

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        public = self.public

        scope = self.scope

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if public is not UNSET:
            field_dict["public"] = public
        if scope is not UNSET:
            field_dict["scope"] = scope
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_project_links import RestProjectLinks

        d = dict(src_dict)
        avatar = d.pop("avatar", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        _links = d.pop("links", UNSET)
        links: RestProjectLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestProjectLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        public = d.pop("public", UNSET)

        scope = d.pop("scope", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RestProjectType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestProjectType(_type_)

        rest_project = cls(
            avatar=avatar,
            avatar_url=avatar_url,
            description=description,
            id=id,
            key=key,
            links=links,
            name=name,
            public=public,
            scope=scope,
            type_=type_,
        )

        rest_project.additional_properties = d
        return rest_project

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
