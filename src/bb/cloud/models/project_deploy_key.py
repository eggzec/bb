from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.project import Project
    from ..models.project_deploy_key_links import ProjectDeployKeyLinks


T = TypeVar("T", bound="ProjectDeployKey")


@_attrs_define
class ProjectDeployKey:
    type_: str
    key: str | Unset = UNSET
    """ The deploy key value. """
    project: Project | Unset = UNSET
    comment: str | Unset = UNSET
    """ The comment parsed from the deploy key (if present) """
    label: str | Unset = UNSET
    """ The user-defined label for the deploy key """
    added_on: datetime.datetime | Unset = UNSET
    last_used: datetime.datetime | Unset = UNSET
    links: ProjectDeployKeyLinks | Unset = UNSET
    created_by: Account | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        key = self.key

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        comment = self.comment

        label = self.label

        added_on: str | Unset = UNSET
        if not isinstance(self.added_on, Unset):
            added_on = self.added_on.isoformat()

        last_used: str | Unset = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if project is not UNSET:
            field_dict["project"] = project
        if comment is not UNSET:
            field_dict["comment"] = comment
        if label is not UNSET:
            field_dict["label"] = label
        if added_on is not UNSET:
            field_dict["added_on"] = added_on
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if links is not UNSET:
            field_dict["links"] = links
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.project import Project
        from ..models.project_deploy_key_links import ProjectDeployKeyLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        key = d.pop("key", UNSET)

        _project = d.pop("project", UNSET)
        project: Project | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        comment = d.pop("comment", UNSET)

        label = d.pop("label", UNSET)

        _added_on = d.pop("added_on", UNSET)
        added_on: datetime.datetime | Unset
        if isinstance(_added_on, Unset):
            added_on = UNSET
        else:
            added_on = isoparse(_added_on)

        _last_used = d.pop("last_used", UNSET)
        last_used: datetime.datetime | Unset
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        _links = d.pop("links", UNSET)
        links: ProjectDeployKeyLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ProjectDeployKeyLinks.from_dict(_links)

        _created_by = d.pop("created_by", UNSET)
        created_by: Account | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = Account.from_dict(_created_by)

        project_deploy_key = cls(
            type_=type_,
            key=key,
            project=project,
            comment=comment,
            label=label,
            added_on=added_on,
            last_used=last_used,
            links=links,
            created_by=created_by,
        )

        project_deploy_key.additional_properties = d
        return project_deploy_key

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
