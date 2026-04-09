from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repository_group_permission_permission import RepositoryGroupPermissionPermission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group import Group
    from ..models.repository import Repository
    from ..models.repository_group_permission_links import RepositoryGroupPermissionLinks


T = TypeVar("T", bound="RepositoryGroupPermission")


@_attrs_define
class RepositoryGroupPermission:
    """A group's permission for a given repository."""

    type_: str
    links: RepositoryGroupPermissionLinks | Unset = UNSET
    permission: RepositoryGroupPermissionPermission | Unset = UNSET
    group: Group | Unset = UNSET
    repository: Repository | Unset = UNSET
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

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

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
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group import Group
        from ..models.repository import Repository
        from ..models.repository_group_permission_links import RepositoryGroupPermissionLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: RepositoryGroupPermissionLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RepositoryGroupPermissionLinks.from_dict(_links)

        _permission = d.pop("permission", UNSET)
        permission: RepositoryGroupPermissionPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = RepositoryGroupPermissionPermission(_permission)

        _group = d.pop("group", UNSET)
        group: Group | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = Group.from_dict(_group)

        _repository = d.pop("repository", UNSET)
        repository: Repository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        repository_group_permission = cls(
            type_=type_,
            links=links,
            permission=permission,
            group=group,
            repository=repository,
        )

        repository_group_permission.additional_properties = d
        return repository_group_permission

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
