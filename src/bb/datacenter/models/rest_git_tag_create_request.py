from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_git_tag_create_request_type import RestGitTagCreateRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestGitTagCreateRequest")


@_attrs_define
class RestGitTagCreateRequest:
    force: bool | Unset = UNSET
    message: str | Unset = UNSET
    name: str | Unset = UNSET
    start_point: str | Unset = UNSET
    type_: RestGitTagCreateRequestType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        force = self.force

        message = self.message

        name = self.name

        start_point = self.start_point

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if force is not UNSET:
            field_dict["force"] = force
        if message is not UNSET:
            field_dict["message"] = message
        if name is not UNSET:
            field_dict["name"] = name
        if start_point is not UNSET:
            field_dict["startPoint"] = start_point
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        force = d.pop("force", UNSET)

        message = d.pop("message", UNSET)

        name = d.pop("name", UNSET)

        start_point = d.pop("startPoint", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RestGitTagCreateRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestGitTagCreateRequestType(_type_)

        rest_git_tag_create_request = cls(
            force=force,
            message=message,
            name=name,
            start_point=start_point,
            type_=type_,
        )

        rest_git_tag_create_request.additional_properties = d
        return rest_git_tag_create_request

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
