from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsoConfigEntity")


@_attrs_define
class SsoConfigEntity:
    discovery_refresh_cron: str | Unset = UNSET
    enable_authentication_fallback: bool | Unset = UNSET
    last_updated: datetime.datetime | Unset = UNSET
    show_login_form: bool | Unset = UNSET
    show_login_form_for_jsm: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discovery_refresh_cron = self.discovery_refresh_cron

        enable_authentication_fallback = self.enable_authentication_fallback

        last_updated: str | Unset = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        show_login_form = self.show_login_form

        show_login_form_for_jsm = self.show_login_form_for_jsm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discovery_refresh_cron is not UNSET:
            field_dict["discovery-refresh-cron"] = discovery_refresh_cron
        if enable_authentication_fallback is not UNSET:
            field_dict["enable-authentication-fallback"] = enable_authentication_fallback
        if last_updated is not UNSET:
            field_dict["last-updated"] = last_updated
        if show_login_form is not UNSET:
            field_dict["show-login-form"] = show_login_form
        if show_login_form_for_jsm is not UNSET:
            field_dict["show-login-form-for-jsm"] = show_login_form_for_jsm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discovery_refresh_cron = d.pop("discovery-refresh-cron", UNSET)

        enable_authentication_fallback = d.pop("enable-authentication-fallback", UNSET)

        _last_updated = d.pop("last-updated", UNSET)
        last_updated: datetime.datetime | Unset
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        show_login_form = d.pop("show-login-form", UNSET)

        show_login_form_for_jsm = d.pop("show-login-form-for-jsm", UNSET)

        sso_config_entity = cls(
            discovery_refresh_cron=discovery_refresh_cron,
            enable_authentication_fallback=enable_authentication_fallback,
            last_updated=last_updated,
            show_login_form=show_login_form,
            show_login_form_for_jsm=show_login_form_for_jsm,
        )

        sso_config_entity.additional_properties = d
        return sso_config_entity

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
