from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_csp_settings_strictness import RestCspSettingsStrictness
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestCspSettings")


@_attrs_define
class RestCspSettings:
    strictness: RestCspSettingsStrictness | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strictness: str | Unset = UNSET
        if not isinstance(self.strictness, Unset):
            strictness = self.strictness.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if strictness is not UNSET:
            field_dict["strictness"] = strictness

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _strictness = d.pop("strictness", UNSET)
        strictness: RestCspSettingsStrictness | Unset
        if isinstance(_strictness, Unset):
            strictness = UNSET
        else:
            strictness = RestCspSettingsStrictness(_strictness)

        rest_csp_settings = cls(
            strictness=strictness,
        )

        rest_csp_settings.additional_properties = d
        return rest_csp_settings

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
