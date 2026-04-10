from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.elevation_method_rest_dto_elevation_methods_item import ElevationMethodRestDTOElevationMethodsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ElevationMethodRestDTO")


@_attrs_define
class ElevationMethodRestDTO:
    elevation_methods: list[ElevationMethodRestDTOElevationMethodsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        elevation_methods: list[str] | Unset = UNSET
        if not isinstance(self.elevation_methods, Unset):
            elevation_methods = []
            for elevation_methods_item_data in self.elevation_methods:
                elevation_methods_item = elevation_methods_item_data.value
                elevation_methods.append(elevation_methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elevation_methods is not UNSET:
            field_dict["elevationMethods"] = elevation_methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _elevation_methods = d.pop("elevationMethods", UNSET)
        elevation_methods: list[ElevationMethodRestDTOElevationMethodsItem] | Unset = UNSET
        if _elevation_methods is not UNSET:
            elevation_methods = []
            for elevation_methods_item_data in _elevation_methods:
                elevation_methods_item = ElevationMethodRestDTOElevationMethodsItem(elevation_methods_item_data)

                elevation_methods.append(elevation_methods_item)

        elevation_method_rest_dto = cls(
            elevation_methods=elevation_methods,
        )

        elevation_method_rest_dto.additional_properties = d
        return elevation_method_rest_dto

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
