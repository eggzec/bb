from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_pull_request_settings_merge_config import RestPullRequestSettingsMergeConfig


T = TypeVar("T", bound="RestPullRequestSettings")


@_attrs_define
class RestPullRequestSettings:
    merge_config: RestPullRequestSettingsMergeConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merge_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge_config, Unset):
            merge_config = self.merge_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merge_config is not UNSET:
            field_dict["mergeConfig"] = merge_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_pull_request_settings_merge_config import RestPullRequestSettingsMergeConfig

        d = dict(src_dict)
        _merge_config = d.pop("mergeConfig", UNSET)
        merge_config: RestPullRequestSettingsMergeConfig | Unset
        if isinstance(_merge_config, Unset):
            merge_config = UNSET
        else:
            merge_config = RestPullRequestSettingsMergeConfig.from_dict(_merge_config)

        rest_pull_request_settings = cls(
            merge_config=merge_config,
        )

        rest_pull_request_settings.additional_properties = d
        return rest_pull_request_settings

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
