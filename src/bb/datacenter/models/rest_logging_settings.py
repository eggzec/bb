from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestLoggingSettings")


@_attrs_define
class RestLoggingSettings:
    debug_logging_enabled: bool | Unset = UNSET
    profiling_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debug_logging_enabled = self.debug_logging_enabled

        profiling_enabled = self.profiling_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if debug_logging_enabled is not UNSET:
            field_dict["debugLoggingEnabled"] = debug_logging_enabled
        if profiling_enabled is not UNSET:
            field_dict["profilingEnabled"] = profiling_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        debug_logging_enabled = d.pop("debugLoggingEnabled", UNSET)

        profiling_enabled = d.pop("profilingEnabled", UNSET)

        rest_logging_settings = cls(
            debug_logging_enabled=debug_logging_enabled,
            profiling_enabled=profiling_enabled,
        )

        rest_logging_settings.additional_properties = d
        return rest_logging_settings

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
