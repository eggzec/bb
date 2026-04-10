from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestBuildStats")


@_attrs_define
class RestBuildStats:
    cancelled: int | Unset = UNSET
    failed: int | Unset = UNSET
    in_progress: int | Unset = UNSET
    successful: int | Unset = UNSET
    unknown: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancelled = self.cancelled

        failed = self.failed

        in_progress = self.in_progress

        successful = self.successful

        unknown = self.unknown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if failed is not UNSET:
            field_dict["failed"] = failed
        if in_progress is not UNSET:
            field_dict["inProgress"] = in_progress
        if successful is not UNSET:
            field_dict["successful"] = successful
        if unknown is not UNSET:
            field_dict["unknown"] = unknown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancelled = d.pop("cancelled", UNSET)

        failed = d.pop("failed", UNSET)

        in_progress = d.pop("inProgress", UNSET)

        successful = d.pop("successful", UNSET)

        unknown = d.pop("unknown", UNSET)

        rest_build_stats = cls(
            cancelled=cancelled,
            failed=failed,
            in_progress=in_progress,
            successful=successful,
            unknown=unknown,
        )

        rest_build_stats.additional_properties = d
        return rest_build_stats

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
