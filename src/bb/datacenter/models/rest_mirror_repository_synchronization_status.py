from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_mirror_repository_synchronization_status_hashes import (
        RestMirrorRepositorySynchronizationStatusHashes,
    )


T = TypeVar("T", bound="RestMirrorRepositorySynchronizationStatus")


@_attrs_define
class RestMirrorRepositorySynchronizationStatus:
    external_repo_id: str | Unset = UNSET
    failed_sync_count: int | Unset = UNSET
    hashes: RestMirrorRepositorySynchronizationStatusHashes | Unset = UNSET
    initial_sync_date: datetime.datetime | Unset = UNSET
    last_sync_date: datetime.datetime | Unset = UNSET
    local_project_id: int | Unset = UNSET
    local_repo_id: int | Unset = UNSET
    upstream_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_repo_id = self.external_repo_id

        failed_sync_count = self.failed_sync_count

        hashes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hashes, Unset):
            hashes = self.hashes.to_dict()

        initial_sync_date: str | Unset = UNSET
        if not isinstance(self.initial_sync_date, Unset):
            initial_sync_date = self.initial_sync_date.isoformat()

        last_sync_date: str | Unset = UNSET
        if not isinstance(self.last_sync_date, Unset):
            last_sync_date = self.last_sync_date.isoformat()

        local_project_id = self.local_project_id

        local_repo_id = self.local_repo_id

        upstream_id = self.upstream_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_repo_id is not UNSET:
            field_dict["externalRepoId"] = external_repo_id
        if failed_sync_count is not UNSET:
            field_dict["failedSyncCount"] = failed_sync_count
        if hashes is not UNSET:
            field_dict["hashes"] = hashes
        if initial_sync_date is not UNSET:
            field_dict["initialSyncDate"] = initial_sync_date
        if last_sync_date is not UNSET:
            field_dict["lastSyncDate"] = last_sync_date
        if local_project_id is not UNSET:
            field_dict["localProjectId"] = local_project_id
        if local_repo_id is not UNSET:
            field_dict["localRepoId"] = local_repo_id
        if upstream_id is not UNSET:
            field_dict["upstreamId"] = upstream_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_mirror_repository_synchronization_status_hashes import (
            RestMirrorRepositorySynchronizationStatusHashes,
        )

        d = dict(src_dict)
        external_repo_id = d.pop("externalRepoId", UNSET)

        failed_sync_count = d.pop("failedSyncCount", UNSET)

        _hashes = d.pop("hashes", UNSET)
        hashes: RestMirrorRepositorySynchronizationStatusHashes | Unset
        if isinstance(_hashes, Unset):
            hashes = UNSET
        else:
            hashes = RestMirrorRepositorySynchronizationStatusHashes.from_dict(_hashes)

        _initial_sync_date = d.pop("initialSyncDate", UNSET)
        initial_sync_date: datetime.datetime | Unset
        if isinstance(_initial_sync_date, Unset):
            initial_sync_date = UNSET
        else:
            initial_sync_date = isoparse(_initial_sync_date)

        _last_sync_date = d.pop("lastSyncDate", UNSET)
        last_sync_date: datetime.datetime | Unset
        if isinstance(_last_sync_date, Unset):
            last_sync_date = UNSET
        else:
            last_sync_date = isoparse(_last_sync_date)

        local_project_id = d.pop("localProjectId", UNSET)

        local_repo_id = d.pop("localRepoId", UNSET)

        upstream_id = d.pop("upstreamId", UNSET)

        rest_mirror_repository_synchronization_status = cls(
            external_repo_id=external_repo_id,
            failed_sync_count=failed_sync_count,
            hashes=hashes,
            initial_sync_date=initial_sync_date,
            last_sync_date=last_sync_date,
            local_project_id=local_project_id,
            local_repo_id=local_repo_id,
            upstream_id=upstream_id,
        )

        rest_mirror_repository_synchronization_status.additional_properties = d
        return rest_mirror_repository_synchronization_status

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
