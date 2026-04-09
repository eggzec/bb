from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_ref_target import PipelineRefTarget


T = TypeVar("T", bound="PipelineSchedule")


@_attrs_define
class PipelineSchedule:
    type_: str
    uuid: str | Unset = UNSET
    """ The UUID identifying the schedule. """
    enabled: bool | Unset = UNSET
    """ Whether the schedule is enabled. """
    target: PipelineRefTarget | Unset = UNSET
    cron_pattern: str | Unset = UNSET
    """ The cron expression with second precision (7 fields) that the schedule applies. For example, for expression:
    0 0 12 * * ? *, will execute at 12pm UTC every day. """
    created_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the schedule was created. """
    updated_on: datetime.datetime | Unset = UNSET
    """ The timestamp when the schedule was updated. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        enabled = self.enabled

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        cron_pattern = self.cron_pattern

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if target is not UNSET:
            field_dict["target"] = target
        if cron_pattern is not UNSET:
            field_dict["cron_pattern"] = cron_pattern
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_ref_target import PipelineRefTarget

        d = dict(src_dict)
        type_ = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        enabled = d.pop("enabled", UNSET)

        _target = d.pop("target", UNSET)
        target: PipelineRefTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = PipelineRefTarget.from_dict(_target)

        cron_pattern = d.pop("cron_pattern", UNSET)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _updated_on = d.pop("updated_on", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        pipeline_schedule = cls(
            type_=type_,
            uuid=uuid,
            enabled=enabled,
            target=target,
            cron_pattern=cron_pattern,
            created_on=created_on,
            updated_on=updated_on,
        )

        pipeline_schedule.additional_properties = d
        return pipeline_schedule

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
