from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_migration_repository_migration_state import RestMigrationRepositoryMigrationState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_migration_repository_repository import RestMigrationRepositoryRepository


T = TypeVar("T", bound="RestMigrationRepository")


@_attrs_define
class RestMigrationRepository:
    migration_state: RestMigrationRepositoryMigrationState | Unset = UNSET
    repository: RestMigrationRepositoryRepository | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        migration_state: str | Unset = UNSET
        if not isinstance(self.migration_state, Unset):
            migration_state = self.migration_state.value

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if migration_state is not UNSET:
            field_dict["migrationState"] = migration_state
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_migration_repository_repository import RestMigrationRepositoryRepository

        d = dict(src_dict)
        _migration_state = d.pop("migrationState", UNSET)
        migration_state: RestMigrationRepositoryMigrationState | Unset
        if isinstance(_migration_state, Unset):
            migration_state = UNSET
        else:
            migration_state = RestMigrationRepositoryMigrationState(_migration_state)

        _repository = d.pop("repository", UNSET)
        repository: RestMigrationRepositoryRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RestMigrationRepositoryRepository.from_dict(_repository)

        rest_migration_repository = cls(
            migration_state=migration_state,
            repository=repository,
        )

        rest_migration_repository.additional_properties = d
        return rest_migration_repository

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
