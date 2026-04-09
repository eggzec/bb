from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline import Pipeline


T = TypeVar("T", bound="PipelineScheduleExecutionExecuted")


@_attrs_define
class PipelineScheduleExecutionExecuted:
    type_: str
    pipeline: Pipeline | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline, Unset):
            pipeline = self.pipeline.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline import Pipeline

        d = dict(src_dict)
        type_ = d.pop("type")

        _pipeline = d.pop("pipeline", UNSET)
        pipeline: Pipeline | Unset
        if isinstance(_pipeline, Unset):
            pipeline = UNSET
        else:
            pipeline = Pipeline.from_dict(_pipeline)

        pipeline_schedule_execution_executed = cls(
            type_=type_,
            pipeline=pipeline,
        )

        pipeline_schedule_execution_executed.additional_properties = d
        return pipeline_schedule_execution_executed

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
