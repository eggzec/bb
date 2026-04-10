from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_user_rate_limit_settings_settings import RestUserRateLimitSettingsSettings
    from ..models.rest_user_rate_limit_settings_user import RestUserRateLimitSettingsUser


T = TypeVar("T", bound="RestUserRateLimitSettings")


@_attrs_define
class RestUserRateLimitSettings:
    settings: RestUserRateLimitSettingsSettings | Unset = UNSET
    user: RestUserRateLimitSettingsUser | Unset = UNSET
    whitelisted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        whitelisted = self.whitelisted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if settings is not UNSET:
            field_dict["settings"] = settings
        if user is not UNSET:
            field_dict["user"] = user
        if whitelisted is not UNSET:
            field_dict["whitelisted"] = whitelisted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_user_rate_limit_settings_settings import RestUserRateLimitSettingsSettings
        from ..models.rest_user_rate_limit_settings_user import RestUserRateLimitSettingsUser

        d = dict(src_dict)
        _settings = d.pop("settings", UNSET)
        settings: RestUserRateLimitSettingsSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = RestUserRateLimitSettingsSettings.from_dict(_settings)

        _user = d.pop("user", UNSET)
        user: RestUserRateLimitSettingsUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RestUserRateLimitSettingsUser.from_dict(_user)

        whitelisted = d.pop("whitelisted", UNSET)

        rest_user_rate_limit_settings = cls(
            settings=settings,
            user=user,
            whitelisted=whitelisted,
        )

        rest_user_rate_limit_settings.additional_properties = d
        return rest_user_rate_limit_settings

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
