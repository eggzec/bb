from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_state import RestJobState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_job_initiator import RestJobInitiator
    from ..models.rest_job_progress import RestJobProgress


T = TypeVar("T", bound="RestJob")


@_attrs_define
class RestJob:
    end_date: int | Unset = UNSET
    id: int | Unset = UNSET
    initiator: RestJobInitiator | Unset = UNSET
    node_id: str | Unset = UNSET
    progress: RestJobProgress | Unset = UNSET
    start_date: int | Unset = UNSET
    state: RestJobState | Unset = UNSET
    type_: str | Unset = UNSET
    updated_date: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date = self.end_date

        id = self.id

        initiator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.initiator, Unset):
            initiator = self.initiator.to_dict()

        node_id = self.node_id

        progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        start_date = self.start_date

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        type_ = self.type_

        updated_date = self.updated_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if id is not UNSET:
            field_dict["id"] = id
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if progress is not UNSET:
            field_dict["progress"] = progress
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if state is not UNSET:
            field_dict["state"] = state
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_date is not UNSET:
            field_dict["updatedDate"] = updated_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_initiator import RestJobInitiator
        from ..models.rest_job_progress import RestJobProgress

        d = dict(src_dict)
        end_date = d.pop("endDate", UNSET)

        id = d.pop("id", UNSET)

        _initiator = d.pop("initiator", UNSET)
        initiator: RestJobInitiator | Unset
        if isinstance(_initiator, Unset):
            initiator = UNSET
        else:
            initiator = RestJobInitiator.from_dict(_initiator)

        node_id = d.pop("nodeId", UNSET)

        _progress = d.pop("progress", UNSET)
        progress: RestJobProgress | Unset
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = RestJobProgress.from_dict(_progress)

        start_date = d.pop("startDate", UNSET)

        _state = d.pop("state", UNSET)
        state: RestJobState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestJobState(_state)

        type_ = d.pop("type", UNSET)

        updated_date = d.pop("updatedDate", UNSET)

        rest_job = cls(
            end_date=end_date,
            id=id,
            initiator=initiator,
            node_id=node_id,
            progress=progress,
            start_date=start_date,
            state=state,
            type_=type_,
            updated_date=updated_date,
        )

        rest_job.additional_properties = d
        return rest_job

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
