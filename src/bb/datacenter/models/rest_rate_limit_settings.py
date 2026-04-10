from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_rate_limit_settings_default_settings import RestRateLimitSettingsDefaultSettings


T = TypeVar("T", bound="RestRateLimitSettings")


@_attrs_define
class RestRateLimitSettings:
    default_settings: RestRateLimitSettingsDefaultSettings | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_settings, Unset):
            default_settings = self.default_settings.to_dict()

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_settings is not UNSET:
            field_dict["defaultSettings"] = default_settings
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_rate_limit_settings_default_settings import RestRateLimitSettingsDefaultSettings

        d = dict(src_dict)
        _default_settings = d.pop("defaultSettings", UNSET)
        default_settings: RestRateLimitSettingsDefaultSettings | Unset
        if isinstance(_default_settings, Unset):
            default_settings = UNSET
        else:
            default_settings = RestRateLimitSettingsDefaultSettings.from_dict(_default_settings)

        enabled = d.pop("enabled", UNSET)

        rest_rate_limit_settings = cls(
            default_settings=default_settings,
            enabled=enabled,
        )

        rest_rate_limit_settings.additional_properties = d
        return rest_rate_limit_settings

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
