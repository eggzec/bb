from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_auto_merge_project_settings_request_restriction_action import (
    RestAutoMergeProjectSettingsRequestRestrictionAction,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestAutoMergeProjectSettingsRequest")


@_attrs_define
class RestAutoMergeProjectSettingsRequest:
    enabled: bool | Unset = UNSET
    restriction_action: RestAutoMergeProjectSettingsRequestRestrictionAction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        restriction_action: str | Unset = UNSET
        if not isinstance(self.restriction_action, Unset):
            restriction_action = self.restriction_action.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if restriction_action is not UNSET:
            field_dict["restrictionAction"] = restriction_action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _restriction_action = d.pop("restrictionAction", UNSET)
        restriction_action: RestAutoMergeProjectSettingsRequestRestrictionAction | Unset
        if isinstance(_restriction_action, Unset):
            restriction_action = UNSET
        else:
            restriction_action = RestAutoMergeProjectSettingsRequestRestrictionAction(_restriction_action)

        rest_auto_merge_project_settings_request = cls(
            enabled=enabled,
            restriction_action=restriction_action,
        )

        rest_auto_merge_project_settings_request.additional_properties = d
        return rest_auto_merge_project_settings_request

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
