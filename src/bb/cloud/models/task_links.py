from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="TaskLinks")


@_attrs_define
class TaskLinks:
    """Navigation links for this task"""

    additional_properties: dict[str, Link] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link

        d = dict(src_dict)
        task_links = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Link.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        task_links.additional_properties = additional_properties
        return task_links

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Link:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Link) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
