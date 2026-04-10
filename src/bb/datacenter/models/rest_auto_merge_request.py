from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestAutoMergeRequest")


@_attrs_define
class RestAutoMergeRequest:
    auto_subject: bool | Unset = UNSET
    created_date: int | Unset = UNSET
    from_hash: str | Unset = UNSET
    message: str | Unset = UNSET
    strategy_id: str | Unset = UNSET
    to_ref_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_subject = self.auto_subject

        created_date = self.created_date

        from_hash = self.from_hash

        message = self.message

        strategy_id = self.strategy_id

        to_ref_id = self.to_ref_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_subject is not UNSET:
            field_dict["autoSubject"] = auto_subject
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if from_hash is not UNSET:
            field_dict["fromHash"] = from_hash
        if message is not UNSET:
            field_dict["message"] = message
        if strategy_id is not UNSET:
            field_dict["strategyId"] = strategy_id
        if to_ref_id is not UNSET:
            field_dict["toRefId"] = to_ref_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_subject = d.pop("autoSubject", UNSET)

        created_date = d.pop("createdDate", UNSET)

        from_hash = d.pop("fromHash", UNSET)

        message = d.pop("message", UNSET)

        strategy_id = d.pop("strategyId", UNSET)

        to_ref_id = d.pop("toRefId", UNSET)

        rest_auto_merge_request = cls(
            auto_subject=auto_subject,
            created_date=created_date,
            from_hash=from_hash,
            message=message,
            strategy_id=strategy_id,
            to_ref_id=to_ref_id,
        )

        rest_auto_merge_request.additional_properties = d
        return rest_auto_merge_request

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
