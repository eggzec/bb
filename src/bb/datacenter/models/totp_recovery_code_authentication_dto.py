from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TotpRecoveryCodeAuthenticationDTO")


@_attrs_define
class TotpRecoveryCodeAuthenticationDTO:
    conversation_id: str | Unset = UNSET
    recovery_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        recovery_code = self.recovery_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if recovery_code is not UNSET:
            field_dict["recoveryCode"] = recovery_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversationId", UNSET)

        recovery_code = d.pop("recoveryCode", UNSET)

        totp_recovery_code_authentication_dto = cls(
            conversation_id=conversation_id,
            recovery_code=recovery_code,
        )

        totp_recovery_code_authentication_dto.additional_properties = d
        return totp_recovery_code_authentication_dto

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
