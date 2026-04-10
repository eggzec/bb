from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestApplicationProperties")


@_attrs_define
class RestApplicationProperties:
    build_date: str | Unset = UNSET
    build_number: str | Unset = UNSET
    display_name: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_date = self.build_date

        build_number = self.build_number

        display_name = self.display_name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_date is not UNSET:
            field_dict["buildDate"] = build_date
        if build_number is not UNSET:
            field_dict["buildNumber"] = build_number
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        build_date = d.pop("buildDate", UNSET)

        build_number = d.pop("buildNumber", UNSET)

        display_name = d.pop("displayName", UNSET)

        version = d.pop("version", UNSET)

        rest_application_properties = cls(
            build_date=build_date,
            build_number=build_number,
            display_name=display_name,
            version=version,
        )

        rest_application_properties.additional_properties = d
        return rest_application_properties

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
