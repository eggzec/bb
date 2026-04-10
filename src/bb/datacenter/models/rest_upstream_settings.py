from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_upstream_settings_mode import RestUpstreamSettingsMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestUpstreamSettings")


@_attrs_define
class RestUpstreamSettings:
    mode: RestUpstreamSettingsMode | Unset = UNSET
    project_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        project_ids: list[str] | Unset = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if project_ids is not UNSET:
            field_dict["projectIds"] = project_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: RestUpstreamSettingsMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = RestUpstreamSettingsMode(_mode)

        project_ids = cast(list[str], d.pop("projectIds", UNSET))

        rest_upstream_settings = cls(
            mode=mode,
            project_ids=project_ids,
        )

        rest_upstream_settings.additional_properties = d
        return rest_upstream_settings

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
