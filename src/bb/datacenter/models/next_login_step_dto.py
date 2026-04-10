from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.next_login_step_dto_next_login_step import NextLoginStepDTONextLoginStep
from ..types import UNSET, Unset

T = TypeVar("T", bound="NextLoginStepDTO")


@_attrs_define
class NextLoginStepDTO:
    conversation_id: str | Unset = UNSET
    next_login_step: NextLoginStepDTONextLoginStep | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        next_login_step: str | Unset = UNSET
        if not isinstance(self.next_login_step, Unset):
            next_login_step = self.next_login_step.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation_id is not UNSET:
            field_dict["conversationId"] = conversation_id
        if next_login_step is not UNSET:
            field_dict["nextLoginStep"] = next_login_step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversationId", UNSET)

        _next_login_step = d.pop("nextLoginStep", UNSET)
        next_login_step: NextLoginStepDTONextLoginStep | Unset
        if isinstance(_next_login_step, Unset):
            next_login_step = UNSET
        else:
            next_login_step = NextLoginStepDTONextLoginStep(_next_login_step)

        next_login_step_dto = cls(
            conversation_id=conversation_id,
            next_login_step=next_login_step,
        )

        next_login_step_dto.additional_properties = d
        return next_login_step_dto

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
