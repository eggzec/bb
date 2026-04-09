from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="TeamLinks")


@_attrs_define
class TeamLinks:
    avatar: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    self_: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    html: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    members: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    projects: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    repositories: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        self_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        html: dict[str, Any] | Unset = UNSET
        if not isinstance(self.html, Unset):
            html = self.html.to_dict()

        members: dict[str, Any] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members.to_dict()

        projects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        repositories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = self.repositories.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if self_ is not UNSET:
            field_dict["self"] = self_
        if html is not UNSET:
            field_dict["html"] = html
        if members is not UNSET:
            field_dict["members"] = members
        if projects is not UNSET:
            field_dict["projects"] = projects
        if repositories is not UNSET:
            field_dict["repositories"] = repositories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link

        d = dict(src_dict)
        _avatar = d.pop("avatar", UNSET)
        avatar: Link | Unset
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Link.from_dict(_avatar)

        _self_ = d.pop("self", UNSET)
        self_: Link | Unset
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = Link.from_dict(_self_)

        _html = d.pop("html", UNSET)
        html: Link | Unset
        if isinstance(_html, Unset):
            html = UNSET
        else:
            html = Link.from_dict(_html)

        _members = d.pop("members", UNSET)
        members: Link | Unset
        if isinstance(_members, Unset):
            members = UNSET
        else:
            members = Link.from_dict(_members)

        _projects = d.pop("projects", UNSET)
        projects: Link | Unset
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = Link.from_dict(_projects)

        _repositories = d.pop("repositories", UNSET)
        repositories: Link | Unset
        if isinstance(_repositories, Unset):
            repositories = UNSET
        else:
            repositories = Link.from_dict(_repositories)

        team_links = cls(
            avatar=avatar,
            self_=self_,
            html=html,
            members=members,
            projects=projects,
            repositories=repositories,
        )

        team_links.additional_properties = d
        return team_links

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
