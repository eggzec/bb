from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_schedule_post_request_body_target_ref_type import PipelineSchedulePostRequestBodyTargetRefType

if TYPE_CHECKING:
    from ..models.pipeline_selector import PipelineSelector


T = TypeVar("T", bound="PipelineSchedulePostRequestBodyTarget")


@_attrs_define
class PipelineSchedulePostRequestBodyTarget:
    """The target on which the schedule will be executed."""

    selector: PipelineSelector
    ref_name: str
    """ The name of the reference. """
    ref_type: PipelineSchedulePostRequestBodyTargetRefType
    """ The type of reference (branch only). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selector = self.selector.to_dict()

        ref_name = self.ref_name

        ref_type = self.ref_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selector": selector,
                "ref_name": ref_name,
                "ref_type": ref_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_selector import PipelineSelector

        d = dict(src_dict)
        selector = PipelineSelector.from_dict(d.pop("selector"))

        ref_name = d.pop("ref_name")

        ref_type = PipelineSchedulePostRequestBodyTargetRefType(d.pop("ref_type"))

        pipeline_schedule_post_request_body_target = cls(
            selector=selector,
            ref_name=ref_name,
            ref_type=ref_type,
        )

        pipeline_schedule_post_request_body_target.additional_properties = d
        return pipeline_schedule_post_request_body_target

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
