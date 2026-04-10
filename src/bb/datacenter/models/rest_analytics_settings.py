from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestAnalyticsSettings")


@_attrs_define
class RestAnalyticsSettings:
    can_collect_analytics: bool | Unset = UNSET
    server_time: int | Unset = UNSET
    support_entitlement_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_collect_analytics = self.can_collect_analytics

        server_time = self.server_time

        support_entitlement_number = self.support_entitlement_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_collect_analytics is not UNSET:
            field_dict["canCollectAnalytics"] = can_collect_analytics
        if server_time is not UNSET:
            field_dict["serverTime"] = server_time
        if support_entitlement_number is not UNSET:
            field_dict["supportEntitlementNumber"] = support_entitlement_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_collect_analytics = d.pop("canCollectAnalytics", UNSET)

        server_time = d.pop("serverTime", UNSET)

        support_entitlement_number = d.pop("supportEntitlementNumber", UNSET)

        rest_analytics_settings = cls(
            can_collect_analytics=can_collect_analytics,
            server_time=server_time,
            support_entitlement_number=support_entitlement_number,
        )

        rest_analytics_settings.additional_properties = d
        return rest_analytics_settings

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
