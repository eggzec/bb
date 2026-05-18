from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_schedule_post_request_body_target import PipelineSchedulePostRequestBodyTarget


T = TypeVar("T", bound="PipelineSchedulePostRequestBody")


@_attrs_define
class PipelineSchedulePostRequestBody:
    target: PipelineSchedulePostRequestBodyTarget
    """ The target on which the schedule will be executed. """
    cron_pattern: str
    """ The cron expression with second precision (7 fields) that the schedule applies. For example, for expression:
    0 0 12 * * ? *, will execute at 12pm UTC every day. """
    type_: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    """ Whether the schedule is enabled. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target = self.target.to_dict()

        cron_pattern = self.cron_pattern

        type_ = self.type_

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
                "cron_pattern": cron_pattern,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_schedule_post_request_body_target import PipelineSchedulePostRequestBodyTarget

        d = dict(src_dict)
        target = PipelineSchedulePostRequestBodyTarget.from_dict(d.pop("target"))

        cron_pattern = d.pop("cron_pattern")

        type_ = d.pop("type", UNSET)

        enabled = d.pop("enabled", UNSET)

        pipeline_schedule_post_request_body = cls(
            target=target,
            cron_pattern=cron_pattern,
            type_=type_,
            enabled=enabled,
        )

        pipeline_schedule_post_request_body.additional_properties = d
        return pipeline_schedule_post_request_body

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
