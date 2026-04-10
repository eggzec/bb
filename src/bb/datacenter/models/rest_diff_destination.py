from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestDiffDestination")


@_attrs_define
class RestDiffDestination:
    components: list[str] | Unset = UNSET
    extension: str | Unset = UNSET
    name: str | Unset = UNSET
    parent: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        components: list[str] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components

        extension = self.extension

        name = self.name

        parent = self.parent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if components is not UNSET:
            field_dict["components"] = components
        if extension is not UNSET:
            field_dict["extension"] = extension
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        components = cast(list[str], d.pop("components", UNSET))

        extension = d.pop("extension", UNSET)

        name = d.pop("name", UNSET)

        parent = d.pop("parent", UNSET)

        rest_diff_destination = cls(
            components=components,
            extension=extension,
            name=name,
            parent=parent,
        )

        rest_diff_destination.additional_properties = d
        return rest_diff_destination

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
