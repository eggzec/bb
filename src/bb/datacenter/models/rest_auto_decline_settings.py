from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_auto_decline_settings_scope import RestAutoDeclineSettingsScope


T = TypeVar("T", bound="RestAutoDeclineSettings")


@_attrs_define
class RestAutoDeclineSettings:
    enabled: bool | Unset = UNSET
    inactivity_weeks: int | Unset = UNSET
    scope: RestAutoDeclineSettingsScope | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        inactivity_weeks = self.inactivity_weeks

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if inactivity_weeks is not UNSET:
            field_dict["inactivityWeeks"] = inactivity_weeks
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_auto_decline_settings_scope import RestAutoDeclineSettingsScope

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        inactivity_weeks = d.pop("inactivityWeeks", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: RestAutoDeclineSettingsScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RestAutoDeclineSettingsScope.from_dict(_scope)

        rest_auto_decline_settings = cls(
            enabled=enabled,
            inactivity_weeks=inactivity_weeks,
            scope=scope,
        )

        rest_auto_decline_settings.additional_properties = d
        return rest_auto_decline_settings

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
