from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExampleStatus")


@_attrs_define
class ExampleStatus:
    current_number_of_users: int | Unset = UNSET
    server_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_number_of_users = self.current_number_of_users

        server_id = self.server_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_number_of_users is not UNSET:
            field_dict["currentNumberOfUsers"] = current_number_of_users
        if server_id is not UNSET:
            field_dict["serverId"] = server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_number_of_users = d.pop("currentNumberOfUsers", UNSET)

        server_id = d.pop("serverId", UNSET)

        example_status = cls(
            current_number_of_users=current_number_of_users,
            server_id=server_id,
        )

        example_status.additional_properties = d
        return example_status

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
