from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_ssh_access_key_permission import RestSshAccessKeyPermission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_ssh_access_key_key import RestSshAccessKeyKey
    from ..models.rest_ssh_access_key_project import RestSshAccessKeyProject
    from ..models.rest_ssh_access_key_repository import RestSshAccessKeyRepository


T = TypeVar("T", bound="RestSshAccessKey")


@_attrs_define
class RestSshAccessKey:
    key: RestSshAccessKeyKey | Unset = UNSET
    permission: RestSshAccessKeyPermission | Unset = UNSET
    project: RestSshAccessKeyProject | Unset = UNSET
    repository: RestSshAccessKeyRepository | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if permission is not UNSET:
            field_dict["permission"] = permission
        if project is not UNSET:
            field_dict["project"] = project
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_ssh_access_key_key import RestSshAccessKeyKey
        from ..models.rest_ssh_access_key_project import RestSshAccessKeyProject
        from ..models.rest_ssh_access_key_repository import RestSshAccessKeyRepository

        d = dict(src_dict)
        _key = d.pop("key", UNSET)
        key: RestSshAccessKeyKey | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = RestSshAccessKeyKey.from_dict(_key)

        _permission = d.pop("permission", UNSET)
        permission: RestSshAccessKeyPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = RestSshAccessKeyPermission(_permission)

        _project = d.pop("project", UNSET)
        project: RestSshAccessKeyProject | Unset
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = RestSshAccessKeyProject.from_dict(_project)

        _repository = d.pop("repository", UNSET)
        repository: RestSshAccessKeyRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RestSshAccessKeyRepository.from_dict(_repository)

        rest_ssh_access_key = cls(
            key=key,
            permission=permission,
            project=project,
            repository=repository,
        )

        rest_ssh_access_key.additional_properties = d
        return rest_ssh_access_key

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
