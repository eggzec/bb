from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="WorkspaceLinks")


@_attrs_define
class WorkspaceLinks:
    avatar: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    html: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    members: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    owners: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    projects: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    repositories: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    snippets: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    self_: Link | Unset = UNSET
    """ A link to a resource related to this object. """

    def to_dict(self) -> dict[str, Any]:
        avatar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        html: dict[str, Any] | Unset = UNSET
        if not isinstance(self.html, Unset):
            html = self.html.to_dict()

        members: dict[str, Any] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members.to_dict()

        owners: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owners, Unset):
            owners = self.owners.to_dict()

        projects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        repositories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = self.repositories.to_dict()

        snippets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snippets, Unset):
            snippets = self.snippets.to_dict()

        self_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if html is not UNSET:
            field_dict["html"] = html
        if members is not UNSET:
            field_dict["members"] = members
        if owners is not UNSET:
            field_dict["owners"] = owners
        if projects is not UNSET:
            field_dict["projects"] = projects
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if snippets is not UNSET:
            field_dict["snippets"] = snippets
        if self_ is not UNSET:
            field_dict["self"] = self_

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

        _owners = d.pop("owners", UNSET)
        owners: Link | Unset
        if isinstance(_owners, Unset):
            owners = UNSET
        else:
            owners = Link.from_dict(_owners)

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

        _snippets = d.pop("snippets", UNSET)
        snippets: Link | Unset
        if isinstance(_snippets, Unset):
            snippets = UNSET
        else:
            snippets = Link.from_dict(_snippets)

        _self_ = d.pop("self", UNSET)
        self_: Link | Unset
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = Link.from_dict(_self_)

        workspace_links = cls(
            avatar=avatar,
            html=html,
            members=members,
            owners=owners,
            projects=projects,
            repositories=repositories,
            snippets=snippets,
            self_=self_,
        )

        return workspace_links
