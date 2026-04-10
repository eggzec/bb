from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_repository_indexing_details_status import RestRepositoryIndexingDetailsStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRepositoryIndexingDetails")


@_attrs_define
class RestRepositoryIndexingDetails:
    indexing_error: str | Unset = UNSET
    """ Additional detail about the <b>BROKEN</b> status if available, meant for informational purposes only. This
    nullable, free-form text field should not be used for automation; rely on status instead. """
    last_indexed_commit_id: str | Unset = UNSET
    """ The commit hash of the last indexed commit in the repository. """
    last_indexed_timestamp: int | Unset = UNSET
    """ The timestamp in epoch milliseconds of the last time the repository successfully was indexed """
    project_key: str | Unset = UNSET
    """ The project key that the repository belongs to """
    repository_slug: str | Unset = UNSET
    """ The repository slug """
    status: RestRepositoryIndexingDetailsStatus | Unset = UNSET
    """ The current indexing status of the repository. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indexing_error = self.indexing_error

        last_indexed_commit_id = self.last_indexed_commit_id

        last_indexed_timestamp = self.last_indexed_timestamp

        project_key = self.project_key

        repository_slug = self.repository_slug

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if indexing_error is not UNSET:
            field_dict["indexingError"] = indexing_error
        if last_indexed_commit_id is not UNSET:
            field_dict["lastIndexedCommitId"] = last_indexed_commit_id
        if last_indexed_timestamp is not UNSET:
            field_dict["lastIndexedTimestamp"] = last_indexed_timestamp
        if project_key is not UNSET:
            field_dict["projectKey"] = project_key
        if repository_slug is not UNSET:
            field_dict["repositorySlug"] = repository_slug
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        indexing_error = d.pop("indexingError", UNSET)

        last_indexed_commit_id = d.pop("lastIndexedCommitId", UNSET)

        last_indexed_timestamp = d.pop("lastIndexedTimestamp", UNSET)

        project_key = d.pop("projectKey", UNSET)

        repository_slug = d.pop("repositorySlug", UNSET)

        _status = d.pop("status", UNSET)
        status: RestRepositoryIndexingDetailsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RestRepositoryIndexingDetailsStatus(_status)

        rest_repository_indexing_details = cls(
            indexing_error=indexing_error,
            last_indexed_commit_id=last_indexed_commit_id,
            last_indexed_timestamp=last_indexed_timestamp,
            project_key=project_key,
            repository_slug=repository_slug,
            status=status,
        )

        rest_repository_indexing_details.additional_properties = d
        return rest_repository_indexing_details

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
