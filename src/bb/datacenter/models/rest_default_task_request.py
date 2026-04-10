from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_default_task_request_source_matcher import RestDefaultTaskRequestSourceMatcher
    from ..models.rest_default_task_request_target_matcher import RestDefaultTaskRequestTargetMatcher


T = TypeVar("T", bound="RestDefaultTaskRequest")


@_attrs_define
class RestDefaultTaskRequest:
    description: str
    source_matcher: RestDefaultTaskRequestSourceMatcher | Unset = UNSET
    target_matcher: RestDefaultTaskRequestTargetMatcher | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        source_matcher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_matcher, Unset):
            source_matcher = self.source_matcher.to_dict()

        target_matcher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_matcher, Unset):
            target_matcher = self.target_matcher.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
            }
        )
        if source_matcher is not UNSET:
            field_dict["sourceMatcher"] = source_matcher
        if target_matcher is not UNSET:
            field_dict["targetMatcher"] = target_matcher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_default_task_request_source_matcher import RestDefaultTaskRequestSourceMatcher
        from ..models.rest_default_task_request_target_matcher import RestDefaultTaskRequestTargetMatcher

        d = dict(src_dict)
        description = d.pop("description")

        _source_matcher = d.pop("sourceMatcher", UNSET)
        source_matcher: RestDefaultTaskRequestSourceMatcher | Unset
        if isinstance(_source_matcher, Unset):
            source_matcher = UNSET
        else:
            source_matcher = RestDefaultTaskRequestSourceMatcher.from_dict(_source_matcher)

        _target_matcher = d.pop("targetMatcher", UNSET)
        target_matcher: RestDefaultTaskRequestTargetMatcher | Unset
        if isinstance(_target_matcher, Unset):
            target_matcher = UNSET
        else:
            target_matcher = RestDefaultTaskRequestTargetMatcher.from_dict(_target_matcher)

        rest_default_task_request = cls(
            description=description,
            source_matcher=source_matcher,
            target_matcher=target_matcher,
        )

        rest_default_task_request.additional_properties = d
        return rest_default_task_request

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
