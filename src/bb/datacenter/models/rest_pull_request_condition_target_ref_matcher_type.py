from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_pull_request_condition_target_ref_matcher_type_id import (
    RestPullRequestConditionTargetRefMatcherTypeId,
)

T = TypeVar("T", bound="RestPullRequestConditionTargetRefMatcherType")


@_attrs_define
class RestPullRequestConditionTargetRefMatcherType:
    id: RestPullRequestConditionTargetRefMatcherTypeId
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = RestPullRequestConditionTargetRefMatcherTypeId(d.pop("id"))

        name = d.pop("name")

        rest_pull_request_condition_target_ref_matcher_type = cls(
            id=id,
            name=name,
        )

        rest_pull_request_condition_target_ref_matcher_type.additional_properties = d
        return rest_pull_request_condition_target_ref_matcher_type

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
