from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_bulk_user_rate_limit_settings_update_request_settings import (
        RestBulkUserRateLimitSettingsUpdateRequestSettings,
    )


T = TypeVar("T", bound="RestBulkUserRateLimitSettingsUpdateRequest")


@_attrs_define
class RestBulkUserRateLimitSettingsUpdateRequest:
    usernames: list[str]
    settings: RestBulkUserRateLimitSettingsUpdateRequestSettings | Unset = UNSET
    whitelisted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usernames = self.usernames

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        whitelisted = self.whitelisted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "usernames": usernames,
            }
        )
        if settings is not UNSET:
            field_dict["settings"] = settings
        if whitelisted is not UNSET:
            field_dict["whitelisted"] = whitelisted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_bulk_user_rate_limit_settings_update_request_settings import (
            RestBulkUserRateLimitSettingsUpdateRequestSettings,
        )

        d = dict(src_dict)
        usernames = cast(list[str], d.pop("usernames"))

        _settings = d.pop("settings", UNSET)
        settings: RestBulkUserRateLimitSettingsUpdateRequestSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = RestBulkUserRateLimitSettingsUpdateRequestSettings.from_dict(_settings)

        whitelisted = d.pop("whitelisted", UNSET)

        rest_bulk_user_rate_limit_settings_update_request = cls(
            usernames=usernames,
            settings=settings,
            whitelisted=whitelisted,
        )

        rest_bulk_user_rate_limit_settings_update_request.additional_properties = d
        return rest_bulk_user_rate_limit_settings_update_request

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
