from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestPullRequestMergeRequest")


@_attrs_define
class RestPullRequestMergeRequest:
    auto_merge: bool | Unset = UNSET
    auto_subject: str | Unset = UNSET
    bypass_merge_queue: bool | Unset = UNSET
    message: str | Unset = UNSET
    strategy_id: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_merge = self.auto_merge

        auto_subject = self.auto_subject

        bypass_merge_queue = self.bypass_merge_queue

        message = self.message

        strategy_id = self.strategy_id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_merge is not UNSET:
            field_dict["autoMerge"] = auto_merge
        if auto_subject is not UNSET:
            field_dict["autoSubject"] = auto_subject
        if bypass_merge_queue is not UNSET:
            field_dict["bypassMergeQueue"] = bypass_merge_queue
        if message is not UNSET:
            field_dict["message"] = message
        if strategy_id is not UNSET:
            field_dict["strategyId"] = strategy_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_merge = d.pop("autoMerge", UNSET)

        auto_subject = d.pop("autoSubject", UNSET)

        bypass_merge_queue = d.pop("bypassMergeQueue", UNSET)

        message = d.pop("message", UNSET)

        strategy_id = d.pop("strategyId", UNSET)

        version = d.pop("version", UNSET)

        rest_pull_request_merge_request = cls(
            auto_merge=auto_merge,
            auto_subject=auto_subject,
            bypass_merge_queue=bypass_merge_queue,
            message=message,
            strategy_id=strategy_id,
            version=version,
        )

        rest_pull_request_merge_request.additional_properties = d
        return rest_pull_request_merge_request

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
