from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.application_property_attributes_item import ApplicationPropertyAttributesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationProperty")


@_attrs_define
class ApplicationProperty:
    """An application property. It is a caller defined JSON object that Bitbucket will store and return.
    The `_attributes` field at its top level can be used to control who is allowed to read and update the property.
    The keys of the JSON object must match an allowed pattern. For details,
    see [Application properties](/cloud/bitbucket/application-properties/).

    """

    field_attributes: list[ApplicationPropertyAttributesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_attributes: list[str] | Unset = UNSET
        if not isinstance(self.field_attributes, Unset):
            field_attributes = []
            for field_attributes_item_data in self.field_attributes:
                field_attributes_item = field_attributes_item_data.value
                field_attributes.append(field_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_attributes is not UNSET:
            field_dict["_attributes"] = field_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _field_attributes = d.pop("_attributes", UNSET)
        field_attributes: list[ApplicationPropertyAttributesItem] | Unset = UNSET
        if _field_attributes is not UNSET:
            field_attributes = []
            for field_attributes_item_data in _field_attributes:
                field_attributes_item = ApplicationPropertyAttributesItem(field_attributes_item_data)

                field_attributes.append(field_attributes_item)

        application_property = cls(
            field_attributes=field_attributes,
        )

        application_property.additional_properties = d
        return application_property

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
