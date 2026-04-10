from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RestDelayedSyncRepository")


@_attrs_define
class RestDelayedSyncRepository:
    project_key: str
    repository_id: str
    repository_slug: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_key = self.project_key

        repository_id = self.repository_id

        repository_slug = self.repository_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectKey": project_key,
                "repositoryId": repository_id,
                "repositorySlug": repository_slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_key = d.pop("projectKey")

        repository_id = d.pop("repositoryId")

        repository_slug = d.pop("repositorySlug")

        rest_delayed_sync_repository = cls(
            project_key=project_key,
            repository_id=repository_id,
            repository_slug=repository_slug,
        )

        rest_delayed_sync_repository.additional_properties = d
        return rest_delayed_sync_repository

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
