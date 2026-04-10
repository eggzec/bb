from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicAuthConfigEntity")


@_attrs_define
class BasicAuthConfigEntity:
    allowed_paths: list[str] | Unset = UNSET
    allowed_users: list[str] | Unset = UNSET
    block_requests: bool | Unset = UNSET
    show_warning_message: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_paths: list[str] | Unset = UNSET
        if not isinstance(self.allowed_paths, Unset):
            allowed_paths = self.allowed_paths

        allowed_users: list[str] | Unset = UNSET
        if not isinstance(self.allowed_users, Unset):
            allowed_users = self.allowed_users

        block_requests = self.block_requests

        show_warning_message = self.show_warning_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_paths is not UNSET:
            field_dict["allowed-paths"] = allowed_paths
        if allowed_users is not UNSET:
            field_dict["allowed-users"] = allowed_users
        if block_requests is not UNSET:
            field_dict["block-requests"] = block_requests
        if show_warning_message is not UNSET:
            field_dict["show-warning-message"] = show_warning_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_paths = cast(list[str], d.pop("allowed-paths", UNSET))

        allowed_users = cast(list[str], d.pop("allowed-users", UNSET))

        block_requests = d.pop("block-requests", UNSET)

        show_warning_message = d.pop("show-warning-message", UNSET)

        basic_auth_config_entity = cls(
            allowed_paths=allowed_paths,
            allowed_users=allowed_users,
            block_requests=block_requests,
            show_warning_message=show_warning_message,
        )

        basic_auth_config_entity.additional_properties = d
        return basic_auth_config_entity

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
