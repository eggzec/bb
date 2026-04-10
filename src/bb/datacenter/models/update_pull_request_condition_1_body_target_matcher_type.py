from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_pull_request_condition_1_body_target_matcher_type_id import (
    UpdatePullRequestCondition1BodyTargetMatcherTypeId,
)

T = TypeVar("T", bound="UpdatePullRequestCondition1BodyTargetMatcherType")


@_attrs_define
class UpdatePullRequestCondition1BodyTargetMatcherType:
    id: UpdatePullRequestCondition1BodyTargetMatcherTypeId
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
        id = UpdatePullRequestCondition1BodyTargetMatcherTypeId(d.pop("id"))

        name = d.pop("name")

        update_pull_request_condition_1_body_target_matcher_type = cls(
            id=id,
            name=name,
        )

        update_pull_request_condition_1_body_target_matcher_type.additional_properties = d
        return update_pull_request_condition_1_body_target_matcher_type

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
