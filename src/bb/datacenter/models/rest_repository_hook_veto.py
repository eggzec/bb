from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRepositoryHookVeto")


@_attrs_define
class RestRepositoryHookVeto:
    detailed_message: str | Unset = UNSET
    summary_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detailed_message = self.detailed_message

        summary_message = self.summary_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detailed_message is not UNSET:
            field_dict["detailedMessage"] = detailed_message
        if summary_message is not UNSET:
            field_dict["summaryMessage"] = summary_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detailed_message = d.pop("detailedMessage", UNSET)

        summary_message = d.pop("summaryMessage", UNSET)

        rest_repository_hook_veto = cls(
            detailed_message=detailed_message,
            summary_message=summary_message,
        )

        rest_repository_hook_veto.additional_properties = d
        return rest_repository_hook_veto

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
