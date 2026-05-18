from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipelines_links_section_href import PipelinesLinksSectionHref


T = TypeVar("T", bound="PipelinesPipelineLinks")


@_attrs_define
class PipelinesPipelineLinks:
    type_: str | Unset = UNSET
    self_: PipelinesLinksSectionHref | Unset = UNSET
    steps: PipelinesLinksSectionHref | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        self_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        steps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = self.steps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if self_ is not UNSET:
            field_dict["self"] = self_
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipelines_links_section_href import PipelinesLinksSectionHref

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _self_ = d.pop("self", UNSET)
        self_: PipelinesLinksSectionHref | Unset
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = PipelinesLinksSectionHref.from_dict(_self_)

        _steps = d.pop("steps", UNSET)
        steps: PipelinesLinksSectionHref | Unset
        if isinstance(_steps, Unset):
            steps = UNSET
        else:
            steps = PipelinesLinksSectionHref.from_dict(_steps)

        pipelines_pipeline_links = cls(
            type_=type_,
            self_=self_,
            steps=steps,
        )

        pipelines_pipeline_links.additional_properties = d
        return pipelines_pipeline_links

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
