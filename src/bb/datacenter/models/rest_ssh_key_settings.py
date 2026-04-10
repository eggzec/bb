from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_ssh_key_type_restriction import RestSshKeyTypeRestriction


T = TypeVar("T", bound="RestSshKeySettings")


@_attrs_define
class RestSshKeySettings:
    key_type_restrictions: list[RestSshKeyTypeRestriction] | Unset = UNSET
    max_expiry_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_type_restrictions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.key_type_restrictions, Unset):
            key_type_restrictions = []
            for key_type_restrictions_item_data in self.key_type_restrictions:
                key_type_restrictions_item = key_type_restrictions_item_data.to_dict()
                key_type_restrictions.append(key_type_restrictions_item)

        max_expiry_days = self.max_expiry_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_type_restrictions is not UNSET:
            field_dict["keyTypeRestrictions"] = key_type_restrictions
        if max_expiry_days is not UNSET:
            field_dict["maxExpiryDays"] = max_expiry_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_ssh_key_type_restriction import RestSshKeyTypeRestriction

        d = dict(src_dict)
        _key_type_restrictions = d.pop("keyTypeRestrictions", UNSET)
        key_type_restrictions: list[RestSshKeyTypeRestriction] | Unset = UNSET
        if _key_type_restrictions is not UNSET:
            key_type_restrictions = []
            for key_type_restrictions_item_data in _key_type_restrictions:
                key_type_restrictions_item = RestSshKeyTypeRestriction.from_dict(key_type_restrictions_item_data)

                key_type_restrictions.append(key_type_restrictions_item)

        max_expiry_days = d.pop("maxExpiryDays", UNSET)

        rest_ssh_key_settings = cls(
            key_type_restrictions=key_type_restrictions,
            max_expiry_days=max_expiry_days,
        )

        rest_ssh_key_settings.additional_properties = d
        return rest_ssh_key_settings

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
