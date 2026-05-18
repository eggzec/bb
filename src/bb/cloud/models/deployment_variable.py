from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentVariable")


@_attrs_define
class DeploymentVariable:
    type_: str | Unset = UNSET
    uuid: str | Unset = UNSET
    """ The UUID identifying the variable. """
    key: str | Unset = UNSET
    """ The unique name of the variable. """
    value: str | Unset = UNSET
    """ The value of the variable. If the variable is secured, this will be empty. """
    secured: bool | Unset = UNSET
    """ If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST
    API. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        key = self.key

        value = self.value

        secured = self.secured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if secured is not UNSET:
            field_dict["secured"] = secured

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        uuid = d.pop("uuid", UNSET)

        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        secured = d.pop("secured", UNSET)

        deployment_variable = cls(
            type_=type_,
            uuid=uuid,
            key=key,
            value=value,
            secured=secured,
        )

        deployment_variable.additional_properties = d
        return deployment_variable

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
