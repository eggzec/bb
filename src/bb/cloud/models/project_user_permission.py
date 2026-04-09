from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_user_permission_permission import ProjectUserPermissionPermission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project import Project
    from ..models.project_user_permission_links import ProjectUserPermissionLinks
    from ..models.user import User


T = TypeVar("T", bound="ProjectUserPermission")


@_attrs_define
class ProjectUserPermission:
    """A user's direct permission for a given project."""

    type_: str
    links: ProjectUserPermissionLinks | Unset = UNSET
    permission: ProjectUserPermissionPermission | Unset = UNSET
    user: User | Unset = UNSET
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

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

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
        if user is not UNSET:
            field_dict["user"] = user
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project import Project
        from ..models.project_user_permission_links import ProjectUserPermissionLinks
        from ..models.user import User

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: ProjectUserPermissionLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ProjectUserPermissionLinks.from_dict(_links)

        _permission = d.pop("permission", UNSET)
        permission: ProjectUserPermissionPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = ProjectUserPermissionPermission(_permission)

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        _project = d.pop("project", UNSET)
        project: Project | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = Project.from_dict(_project)

        project_user_permission = cls(
            type_=type_,
            links=links,
            permission=permission,
            user=user,
            project=project,
        )

        project_user_permission.additional_properties = d
        return project_user_permission

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
