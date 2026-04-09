from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.repository_user_permission_permission import RepositoryUserPermissionPermission
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repository import Repository
    from ..models.repository_user_permission_links import RepositoryUserPermissionLinks
    from ..models.user import User


T = TypeVar("T", bound="RepositoryUserPermission")


@_attrs_define
class RepositoryUserPermission:
    """A user's direct permission for a given repository."""

    type_: str
    permission: RepositoryUserPermissionPermission | Unset = UNSET
    user: User | Unset = UNSET
    repository: Repository | Unset = UNSET
    links: RepositoryUserPermissionLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if permission is not UNSET:
            field_dict["permission"] = permission
        if user is not UNSET:
            field_dict["user"] = user
        if repository is not UNSET:
            field_dict["repository"] = repository
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repository import Repository
        from ..models.repository_user_permission_links import RepositoryUserPermissionLinks
        from ..models.user import User

        d = dict(src_dict)
        type_ = d.pop("type")

        _permission = d.pop("permission", UNSET)
        permission: RepositoryUserPermissionPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = RepositoryUserPermissionPermission(_permission)

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        _repository = d.pop("repository", UNSET)
        repository: Repository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        _links = d.pop("links", UNSET)
        links: RepositoryUserPermissionLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RepositoryUserPermissionLinks.from_dict(_links)

        repository_user_permission = cls(
            type_=type_,
            permission=permission,
            user=user,
            repository=repository,
            links=links,
        )

        repository_user_permission.additional_properties = d
        return repository_user_permission

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
