from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_state_dto_type import MethodStateDTOType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodStateDTO")


@_attrs_define
class MethodStateDTO:
    enabled: bool | Unset = UNSET
    enabled_at: datetime.datetime | Unset = UNSET
    enforced: bool | Unset = UNSET
    type_: MethodStateDTOType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        enabled_at: str | Unset = UNSET
        if not isinstance(self.enabled_at, Unset):
            enabled_at = self.enabled_at.isoformat()

        enforced = self.enforced

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if enabled_at is not UNSET:
            field_dict["enabledAt"] = enabled_at
        if enforced is not UNSET:
            field_dict["enforced"] = enforced
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _enabled_at = d.pop("enabledAt", UNSET)
        enabled_at: datetime.datetime | Unset
        if isinstance(_enabled_at, Unset):
            enabled_at = UNSET
        else:
            enabled_at = isoparse(_enabled_at)

        enforced = d.pop("enforced", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: MethodStateDTOType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MethodStateDTOType(_type_)

        method_state_dto = cls(
            enabled=enabled,
            enabled_at=enabled_at,
            enforced=enforced,
            type_=type_,
        )

        method_state_dto.additional_properties = d
        return method_state_dto

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
