from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_broken_index_status_repository_details_status import RestBrokenIndexStatusRepositoryDetailsStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestBrokenIndexStatusRepositoryDetails")


@_attrs_define
class RestBrokenIndexStatusRepositoryDetails:
    """Details about the last index attempt for the given repository"""

    project_key: str
    """ The project key that the repository belongs to """
    repository_slug: str
    """ The repository slug """
    status: RestBrokenIndexStatusRepositoryDetailsStatus
    """ The current indexing status of the repository. """
    indexing_error: str | Unset = UNSET
    """ Additional detail about the <b>BROKEN</b> status if available, meant for informational purposes only. This
    nullable, free-form text field should not be used for automation; rely on status instead. """
    last_indexed_commit_id: str | Unset = UNSET
    """ The commit hash of the last indexed commit in the repository. """
    last_indexed_timestamp: int | Unset = UNSET
    """ The timestamp in epoch milliseconds of the last time the repository successfully was indexed """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_key = self.project_key

        repository_slug = self.repository_slug

        status = self.status.value

        indexing_error = self.indexing_error

        last_indexed_commit_id = self.last_indexed_commit_id

        last_indexed_timestamp = self.last_indexed_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projectKey": project_key,
                "repositorySlug": repository_slug,
                "status": status,
            }
        )
        if indexing_error is not UNSET:
            field_dict["indexingError"] = indexing_error
        if last_indexed_commit_id is not UNSET:
            field_dict["lastIndexedCommitId"] = last_indexed_commit_id
        if last_indexed_timestamp is not UNSET:
            field_dict["lastIndexedTimestamp"] = last_indexed_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_key = d.pop("projectKey")

        repository_slug = d.pop("repositorySlug")

        status = RestBrokenIndexStatusRepositoryDetailsStatus(d.pop("status"))

        indexing_error = d.pop("indexingError", UNSET)

        last_indexed_commit_id = d.pop("lastIndexedCommitId", UNSET)

        last_indexed_timestamp = d.pop("lastIndexedTimestamp", UNSET)

        rest_broken_index_status_repository_details = cls(
            project_key=project_key,
            repository_slug=repository_slug,
            status=status,
            indexing_error=indexing_error,
            last_indexed_commit_id=last_indexed_commit_id,
            last_indexed_timestamp=last_indexed_timestamp,
        )

        rest_broken_index_status_repository_details.additional_properties = d
        return rest_broken_index_status_repository_details

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
