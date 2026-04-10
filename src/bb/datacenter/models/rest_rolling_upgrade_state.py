from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRollingUpgradeState")


@_attrs_define
class RestRollingUpgradeState:
    rolling_upgrade_enabled: bool | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rolling_upgrade_enabled = self.rolling_upgrade_enabled

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rolling_upgrade_enabled is not UNSET:
            field_dict["rollingUpgradeEnabled"] = rolling_upgrade_enabled
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rolling_upgrade_enabled = d.pop("rollingUpgradeEnabled", UNSET)

        version = d.pop("version", UNSET)

        rest_rolling_upgrade_state = cls(
            rolling_upgrade_enabled=rolling_upgrade_enabled,
            version=version,
        )

        rest_rolling_upgrade_state.additional_properties = d
        return rest_rolling_upgrade_state

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
