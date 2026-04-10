from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simple_ssh_key_fingerprint import SimpleSshKeyFingerprint


T = TypeVar("T", bound="RestSshSettings")


@_attrs_define
class RestSshSettings:
    access_keys_enabled: bool | Unset = UNSET
    base_url: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    fingerprint: SimpleSshKeyFingerprint | Unset = UNSET
    port: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_keys_enabled = self.access_keys_enabled

        base_url = self.base_url

        enabled = self.enabled

        fingerprint: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fingerprint, Unset):
            fingerprint = self.fingerprint.to_dict()

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_keys_enabled is not UNSET:
            field_dict["accessKeysEnabled"] = access_keys_enabled
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_ssh_key_fingerprint import SimpleSshKeyFingerprint

        d = dict(src_dict)
        access_keys_enabled = d.pop("accessKeysEnabled", UNSET)

        base_url = d.pop("baseUrl", UNSET)

        enabled = d.pop("enabled", UNSET)

        _fingerprint = d.pop("fingerprint", UNSET)
        fingerprint: SimpleSshKeyFingerprint | Unset
        if isinstance(_fingerprint, Unset):
            fingerprint = UNSET
        else:
            fingerprint = SimpleSshKeyFingerprint.from_dict(_fingerprint)

        port = d.pop("port", UNSET)

        rest_ssh_settings = cls(
            access_keys_enabled=access_keys_enabled,
            base_url=base_url,
            enabled=enabled,
            fingerprint=fingerprint,
            port=port,
        )

        rest_ssh_settings.additional_properties = d
        return rest_ssh_settings

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
