from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExampleSettingsMap")


@_attrs_define
class ExampleSettingsMap:
    boolean_key: bool | Unset = UNSET
    long_key: float | Unset = UNSET
    string_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        boolean_key = self.boolean_key

        long_key = self.long_key

        string_key = self.string_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boolean_key is not UNSET:
            field_dict["boolean key"] = boolean_key
        if long_key is not UNSET:
            field_dict["long key"] = long_key
        if string_key is not UNSET:
            field_dict["string key"] = string_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        boolean_key = d.pop("boolean key", UNSET)

        long_key = d.pop("long key", UNSET)

        string_key = d.pop("string key", UNSET)

        example_settings_map = cls(
            boolean_key=boolean_key,
            long_key=long_key,
            string_key=string_key,
        )

        example_settings_map.additional_properties = d
        return example_settings_map

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
