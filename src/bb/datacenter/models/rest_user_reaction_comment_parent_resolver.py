from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_user_reaction_comment_parent_resolver_type import RestUserReactionCommentParentResolverType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_user_reaction_comment_parent_resolver_links import RestUserReactionCommentParentResolverLinks


T = TypeVar("T", bound="RestUserReactionCommentParentResolver")


@_attrs_define
class RestUserReactionCommentParentResolver:
    display_name: str
    name: str
    slug: str
    type_: RestUserReactionCommentParentResolverType
    active: bool | Unset = UNSET
    avatar_url: str | Unset = UNSET
    email_address: str | Unset = UNSET
    id: int | Unset = UNSET
    links: RestUserReactionCommentParentResolverLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        name = self.name

        slug = self.slug

        type_ = self.type_.value

        active = self.active

        avatar_url = self.avatar_url

        email_address = self.email_address

        id = self.id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "name": name,
                "slug": slug,
                "type": type_,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if avatar_url is not UNSET:
            field_dict["avatarUrl"] = avatar_url
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_user_reaction_comment_parent_resolver_links import RestUserReactionCommentParentResolverLinks

        d = dict(src_dict)
        display_name = d.pop("displayName")

        name = d.pop("name")

        slug = d.pop("slug")

        type_ = RestUserReactionCommentParentResolverType(d.pop("type"))

        active = d.pop("active", UNSET)

        avatar_url = d.pop("avatarUrl", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: RestUserReactionCommentParentResolverLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestUserReactionCommentParentResolverLinks.from_dict(_links)

        rest_user_reaction_comment_parent_resolver = cls(
            display_name=display_name,
            name=name,
            slug=slug,
            type_=type_,
            active=active,
            avatar_url=avatar_url,
            email_address=email_address,
            id=id,
            links=links,
        )

        rest_user_reaction_comment_parent_resolver.additional_properties = d
        return rest_user_reaction_comment_parent_resolver

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
