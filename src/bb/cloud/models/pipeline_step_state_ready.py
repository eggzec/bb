from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_step_state_ready_name import PipelineStepStateReadyName
from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineStepStateReady")


@_attrs_define
class PipelineStepStateReady:
    type_: str
    name: PipelineStepStateReadyName | Unset = UNSET
    """ The name of pipeline step state (READY). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        _name = d.pop("name", UNSET)
        name: PipelineStepStateReadyName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PipelineStepStateReadyName(_name)

        pipeline_step_state_ready = cls(
            type_=type_,
            name=name,
        )

        pipeline_step_state_ready.additional_properties = d
        return pipeline_step_state_ready

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
