from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_broken_index_status_repository_details import RestBrokenIndexStatusRepositoryDetails
    from ..models.rest_broken_index_status_repository_repository import RestBrokenIndexStatusRepositoryRepository


T = TypeVar("T", bound="RestBrokenIndexStatusRepository")


@_attrs_define
class RestBrokenIndexStatusRepository:
    details: RestBrokenIndexStatusRepositoryDetails | Unset = UNSET
    """ Details about the last index attempt for the given repository """
    repository: RestBrokenIndexStatusRepositoryRepository | Unset = UNSET
    """ The repository which has entered a broken status """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if repository is not UNSET:
            field_dict["repository"] = repository

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_broken_index_status_repository_details import RestBrokenIndexStatusRepositoryDetails
        from ..models.rest_broken_index_status_repository_repository import RestBrokenIndexStatusRepositoryRepository

        d = dict(src_dict)
        _details = d.pop("details", UNSET)
        details: RestBrokenIndexStatusRepositoryDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = RestBrokenIndexStatusRepositoryDetails.from_dict(_details)

        _repository = d.pop("repository", UNSET)
        repository: RestBrokenIndexStatusRepositoryRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RestBrokenIndexStatusRepositoryRepository.from_dict(_repository)

        rest_broken_index_status_repository = cls(
            details=details,
            repository=repository,
        )

        rest_broken_index_status_repository.additional_properties = d
        return rest_broken_index_status_repository

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
