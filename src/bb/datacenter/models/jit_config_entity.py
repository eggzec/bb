from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JitConfigEntity")


@_attrs_define
class JitConfigEntity:
    additional_openid_scopes: list[str] | Unset = UNSET
    mapping_display_name: str | Unset = UNSET
    mapping_email: str | Unset = UNSET
    mapping_groups: str | Unset = UNSET
    user_provisioning_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_openid_scopes: list[str] | Unset = UNSET
        if not isinstance(self.additional_openid_scopes, Unset):
            additional_openid_scopes = self.additional_openid_scopes

        mapping_display_name = self.mapping_display_name

        mapping_email = self.mapping_email

        mapping_groups = self.mapping_groups

        user_provisioning_enabled = self.user_provisioning_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_openid_scopes is not UNSET:
            field_dict["additional-openid-scopes"] = additional_openid_scopes
        if mapping_display_name is not UNSET:
            field_dict["mapping-display-name"] = mapping_display_name
        if mapping_email is not UNSET:
            field_dict["mapping-email"] = mapping_email
        if mapping_groups is not UNSET:
            field_dict["mapping-groups"] = mapping_groups
        if user_provisioning_enabled is not UNSET:
            field_dict["user-provisioning-enabled"] = user_provisioning_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additional_openid_scopes = cast(list[str], d.pop("additional-openid-scopes", UNSET))

        mapping_display_name = d.pop("mapping-display-name", UNSET)

        mapping_email = d.pop("mapping-email", UNSET)

        mapping_groups = d.pop("mapping-groups", UNSET)

        user_provisioning_enabled = d.pop("user-provisioning-enabled", UNSET)

        jit_config_entity = cls(
            additional_openid_scopes=additional_openid_scopes,
            mapping_display_name=mapping_display_name,
            mapping_email=mapping_email,
            mapping_groups=mapping_groups,
            user_provisioning_enabled=user_provisioning_enabled,
        )

        jit_config_entity.additional_properties = d
        return jit_config_entity

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
