from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExampleSettings")


@_attrs_define
class ExampleSettings:
    boolean_value: bool | Unset = UNSET
    double_value: float | Unset = UNSET
    integer_value: int | Unset = UNSET
    long_value: int | Unset = UNSET
    string_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        boolean_value = self.boolean_value

        double_value = self.double_value

        integer_value = self.integer_value

        long_value = self.long_value

        string_value = self.string_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boolean_value is not UNSET:
            field_dict["booleanValue"] = boolean_value
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if integer_value is not UNSET:
            field_dict["integerValue"] = integer_value
        if long_value is not UNSET:
            field_dict["longValue"] = long_value
        if string_value is not UNSET:
            field_dict["stringValue"] = string_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        boolean_value = d.pop("booleanValue", UNSET)

        double_value = d.pop("doubleValue", UNSET)

        integer_value = d.pop("integerValue", UNSET)

        long_value = d.pop("longValue", UNSET)

        string_value = d.pop("stringValue", UNSET)

        example_settings = cls(
            boolean_value=boolean_value,
            double_value=double_value,
            integer_value=integer_value,
            long_value=long_value,
            string_value=string_value,
        )

        example_settings.additional_properties = d
        return example_settings

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
