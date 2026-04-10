from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestUserRateLimitSettingsSettings")


@_attrs_define
class RestUserRateLimitSettingsSettings:
    capacity: int | Unset = UNSET
    fill_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capacity = self.capacity

        fill_rate = self.fill_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if fill_rate is not UNSET:
            field_dict["fillRate"] = fill_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        capacity = d.pop("capacity", UNSET)

        fill_rate = d.pop("fillRate", UNSET)

        rest_user_rate_limit_settings_settings = cls(
            capacity=capacity,
            fill_rate=fill_rate,
        )

        rest_user_rate_limit_settings_settings.additional_properties = d
        return rest_user_rate_limit_settings_settings

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
