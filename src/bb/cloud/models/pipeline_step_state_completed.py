from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_step_state_completed_name import PipelineStepStateCompletedName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_step_state_completed_result import PipelineStepStateCompletedResult


T = TypeVar("T", bound="PipelineStepStateCompleted")


@_attrs_define
class PipelineStepStateCompleted:
    type_: str
    name: PipelineStepStateCompletedName | Unset = UNSET
    """ The name of pipeline step state (COMPLETED). """
    result: PipelineStepStateCompletedResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_step_state_completed_result import PipelineStepStateCompletedResult

        d = dict(src_dict)
        type_ = d.pop("type")

        _name = d.pop("name", UNSET)
        name: PipelineStepStateCompletedName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PipelineStepStateCompletedName(_name)

        _result = d.pop("result", UNSET)
        result: PipelineStepStateCompletedResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = PipelineStepStateCompletedResult.from_dict(_result)

        pipeline_step_state_completed = cls(
            type_=type_,
            name=name,
            result=result,
        )

        pipeline_step_state_completed.additional_properties = d
        return pipeline_step_state_completed

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
