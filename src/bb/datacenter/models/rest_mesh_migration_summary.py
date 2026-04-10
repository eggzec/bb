from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_mesh_migration_summary_queue import RestMeshMigrationSummaryQueue


T = TypeVar("T", bound="RestMeshMigrationSummary")


@_attrs_define
class RestMeshMigrationSummary:
    end_time: int | Unset = UNSET
    job_id: int | Unset = UNSET
    progress: int | Unset = UNSET
    queue: RestMeshMigrationSummaryQueue | Unset = UNSET
    start_time: int | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time = self.end_time

        job_id = self.job_id

        progress = self.progress

        queue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.queue, Unset):
            queue = self.queue.to_dict()

        start_time = self.start_time

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if progress is not UNSET:
            field_dict["progress"] = progress
        if queue is not UNSET:
            field_dict["queue"] = queue
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_mesh_migration_summary_queue import RestMeshMigrationSummaryQueue

        d = dict(src_dict)
        end_time = d.pop("endTime", UNSET)

        job_id = d.pop("jobId", UNSET)

        progress = d.pop("progress", UNSET)

        _queue = d.pop("queue", UNSET)
        queue: RestMeshMigrationSummaryQueue | Unset
        if isinstance(_queue, Unset):
            queue = UNSET
        else:
            queue = RestMeshMigrationSummaryQueue.from_dict(_queue)

        start_time = d.pop("startTime", UNSET)

        state = d.pop("state", UNSET)

        rest_mesh_migration_summary = cls(
            end_time=end_time,
            job_id=job_id,
            progress=progress,
            queue=queue,
            start_time=start_time,
            state=state,
        )

        rest_mesh_migration_summary.additional_properties = d
        return rest_mesh_migration_summary

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
