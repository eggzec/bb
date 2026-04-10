from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_repository_policy_permission import RestRepositoryPolicyPermission
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRepositoryPolicy")


@_attrs_define
class RestRepositoryPolicy:
    permission: RestRepositoryPolicyPermission | Unset = UNSET
    """ The permission required to delete repositories. Must be one of: "SYS_ADMIN", "ADMIN", "PROJECT_ADMIN",
    "REPO_ADMIN". """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permission: str | Unset = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _permission = d.pop("permission", UNSET)
        permission: RestRepositoryPolicyPermission | Unset
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = RestRepositoryPolicyPermission(_permission)

        rest_repository_policy = cls(
            permission=permission,
        )

        rest_repository_policy.additional_properties = d
        return rest_repository_policy

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
