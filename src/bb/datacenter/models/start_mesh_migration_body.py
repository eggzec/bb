from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartMeshMigrationBody")


@_attrs_define
class StartMeshMigrationBody:
    project_ids: list[int]
    repository_ids: list[int]
    all_: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_ids = self.project_ids

        repository_ids = self.repository_ids

        all_ = self.all_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectIds": project_ids,
                "repositoryIds": repository_ids,
            }
        )
        if all_ is not UNSET:
            field_dict["all"] = all_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_ids = cast(list[int], d.pop("projectIds"))

        repository_ids = cast(list[int], d.pop("repositoryIds"))

        all_ = d.pop("all", UNSET)

        start_mesh_migration_body = cls(
            project_ids=project_ids,
            repository_ids=repository_ids,
            all_=all_,
        )

        start_mesh_migration_body.additional_properties = d
        return start_mesh_migration_body

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
