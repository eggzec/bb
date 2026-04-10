from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineNumberRange")


@_attrs_define
class LineNumberRange:
    maximum: int | Unset = UNSET
    minimum: int | Unset = UNSET
    single_line: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maximum = self.maximum

        minimum = self.minimum

        single_line = self.single_line

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if single_line is not UNSET:
            field_dict["singleLine"] = single_line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        maximum = d.pop("maximum", UNSET)

        minimum = d.pop("minimum", UNSET)

        single_line = d.pop("singleLine", UNSET)

        line_number_range = cls(
            maximum=maximum,
            minimum=minimum,
            single_line=single_line,
        )

        line_number_range.additional_properties = d
        return line_number_range

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
