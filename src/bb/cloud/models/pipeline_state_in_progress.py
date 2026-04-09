from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_state_in_progress_name import PipelineStateInProgressName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_state_in_progress_stage import PipelineStateInProgressStage


T = TypeVar("T", bound="PipelineStateInProgress")


@_attrs_define
class PipelineStateInProgress:
    type_: str
    name: PipelineStateInProgressName | Unset = UNSET
    """ The name of pipeline state (IN_PROGRESS). """
    stage: PipelineStateInProgressStage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        stage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if stage is not UNSET:
            field_dict["stage"] = stage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_state_in_progress_stage import PipelineStateInProgressStage

        d = dict(src_dict)
        type_ = d.pop("type")

        _name = d.pop("name", UNSET)
        name: PipelineStateInProgressName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PipelineStateInProgressName(_name)

        _stage = d.pop("stage", UNSET)
        stage: PipelineStateInProgressStage | Unset
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = PipelineStateInProgressStage.from_dict(_stage)

        pipeline_state_in_progress = cls(
            type_=type_,
            name=name,
            stage=stage,
        )

        pipeline_state_in_progress.additional_properties = d
        return pipeline_state_in_progress

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
