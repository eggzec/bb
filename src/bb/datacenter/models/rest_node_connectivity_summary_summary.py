from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestNodeConnectivitySummarySummary")


@_attrs_define
class RestNodeConnectivitySummarySummary:
    error_message: str | Unset = UNSET
    reachable: bool | Unset = UNSET
    round_trip_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        reachable = self.reachable

        round_trip_time = self.round_trip_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if reachable is not UNSET:
            field_dict["reachable"] = reachable
        if round_trip_time is not UNSET:
            field_dict["roundTripTime"] = round_trip_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error_message = d.pop("errorMessage", UNSET)

        reachable = d.pop("reachable", UNSET)

        round_trip_time = d.pop("roundTripTime", UNSET)

        rest_node_connectivity_summary_summary = cls(
            error_message=error_message,
            reachable=reachable,
            round_trip_time=round_trip_time,
        )

        rest_node_connectivity_summary_summary.additional_properties = d
        return rest_node_connectivity_summary_summary

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
