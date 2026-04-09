from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_group_permission_permission import ProjectGroupPermissionPermission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.project import Project
    from ..models.project_group_permission_links import ProjectGroupPermissionLinks


T = TypeVar("T", bound="ProjectGroupPermission")


@_attrs_define
class ProjectGroupPermission:
    """A group's permission for a given project."""

    type_: str
    links: ProjectGroupPermissionLinks | Unset = UNSET
    permission: ProjectGroupPermissionPermission | Unset = UNSET
    group: Group | Unset = UNSET
    project: Project | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if permission is not UNSET:
            field_dict["permission"] = permission
        if group is not UNSET:
            field_dict["group"] = group
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group import Group
        from ..models.project import Project
        from ..models.project_group_permission_links import ProjectGroupPermissionLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: ProjectGroupPermissionLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ProjectGroupPermissionLinks.from_dict(_links)

        _permission = d.pop("permission", UNSET)
        permission: ProjectGroupPermissionPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = ProjectGroupPermissionPermission(_permission)

        _group = d.pop("group", UNSET)
        group: Group | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = Group.from_dict(_group)

        _project = d.pop("project", UNSET)
        project: Project | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        project_group_permission = cls(
            type_=type_,
            links=links,
            permission=permission,
            group=group,
            project=project,
        )

        project_group_permission.additional_properties = d
        return project_group_permission

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
