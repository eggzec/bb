from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.bitbucket_apps_permissions_serializers_project_permission_update_schema_permission import (
    BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchemaPermission,
)

T = TypeVar("T", bound="BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema")


@_attrs_define
class BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema:
    permission: BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchemaPermission

    def to_dict(self) -> dict[str, Any]:
        permission = self.permission.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "permission": permission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permission = BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchemaPermission(d.pop("permission"))

        bitbucket_apps_permissions_serializers_project_permission_update_schema = cls(
            permission=permission,
        )

        return bitbucket_apps_permissions_serializers_project_permission_update_schema
