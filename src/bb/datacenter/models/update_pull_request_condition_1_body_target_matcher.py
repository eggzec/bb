from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_pull_request_condition_1_body_target_matcher_type import (
        UpdatePullRequestCondition1BodyTargetMatcherType,
    )


T = TypeVar("T", bound="UpdatePullRequestCondition1BodyTargetMatcher")


@_attrs_define
class UpdatePullRequestCondition1BodyTargetMatcher:
    display_id: str | Unset = UNSET
    id: str | Unset = UNSET
    type_: UpdatePullRequestCondition1BodyTargetMatcherType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_id = self.display_id

        id = self.id

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_id is not UNSET:
            field_dict["displayId"] = display_id
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_pull_request_condition_1_body_target_matcher_type import (
            UpdatePullRequestCondition1BodyTargetMatcherType,
        )

        d = dict(src_dict)
        display_id = d.pop("displayId", UNSET)

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: UpdatePullRequestCondition1BodyTargetMatcherType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UpdatePullRequestCondition1BodyTargetMatcherType.from_dict(_type_)

        update_pull_request_condition_1_body_target_matcher = cls(
            display_id=display_id,
            id=id,
            type_=type_,
        )

        update_pull_request_condition_1_body_target_matcher.additional_properties = d
        return update_pull_request_condition_1_body_target_matcher

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
