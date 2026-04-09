from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_links import ProjectLinks
    from ..models.team import Team


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    type_: str
    links: ProjectLinks | Unset = UNSET
    uuid: str | Unset = UNSET
    """ The project's immutable id. """
    key: str | Unset = UNSET
    """ The project's key. """
    owner: Team | Unset = UNSET
    name: str | Unset = UNSET
    """ The name of the project. """
    description: str | Unset = UNSET
    is_private: bool | Unset = UNSET
    """
    Indicates whether the project is publicly accessible, or whether it is
    private to the team and consequently only visible to team members.
    Note that private projects cannot contain public repositories. """
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    has_publicly_visible_repos: bool | Unset = UNSET
    """
    Indicates whether the project contains publicly visible repositories.
    Note that private projects cannot contain public repositories. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        uuid = self.uuid

        key = self.key

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        name = self.name

        description = self.description

        is_private = self.is_private

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        has_publicly_visible_repos = self.has_publicly_visible_repos

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if key is not UNSET:
            field_dict["key"] = key
        if owner is not UNSET:
            field_dict["owner"] = owner
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if has_publicly_visible_repos is not UNSET:
            field_dict["has_publicly_visible_repos"] = has_publicly_visible_repos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_links import ProjectLinks
        from ..models.team import Team

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: ProjectLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ProjectLinks.from_dict(_links)

        uuid = d.pop("uuid", UNSET)

        key = d.pop("key", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Team | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = Team.from_dict(_owner)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        is_private = d.pop("is_private", UNSET)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _updated_on = d.pop("updated_on", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        has_publicly_visible_repos = d.pop("has_publicly_visible_repos", UNSET)

        project = cls(
            type_=type_,
            links=links,
            uuid=uuid,
            key=key,
            owner=owner,
            name=name,
            description=description,
            is_private=is_private,
            created_on=created_on,
            updated_on=updated_on,
            has_publicly_visible_repos=has_publicly_visible_repos,
        )

        project.additional_properties = d
        return project

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
