from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_repository_pull_request_settings_merge_config_default_strategy_links import (
        RestRepositoryPullRequestSettingsMergeConfigDefaultStrategyLinks,
    )


T = TypeVar("T", bound="RestRepositoryPullRequestSettingsMergeConfigDefaultStrategy")


@_attrs_define
class RestRepositoryPullRequestSettingsMergeConfigDefaultStrategy:
    flag: str
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    id: str | Unset = UNSET
    links: RestRepositoryPullRequestSettingsMergeConfigDefaultStrategyLinks | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flag = self.flag

        description = self.description

        enabled = self.enabled

        id = self.id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "flag": flag,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_repository_pull_request_settings_merge_config_default_strategy_links import (
            RestRepositoryPullRequestSettingsMergeConfigDefaultStrategyLinks,
        )

        d = dict(src_dict)
        flag = d.pop("flag")

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: RestRepositoryPullRequestSettingsMergeConfigDefaultStrategyLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestRepositoryPullRequestSettingsMergeConfigDefaultStrategyLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        rest_repository_pull_request_settings_merge_config_default_strategy = cls(
            flag=flag,
            description=description,
            enabled=enabled,
            id=id,
            links=links,
            name=name,
        )

        rest_repository_pull_request_settings_merge_config_default_strategy.additional_properties = d
        return rest_repository_pull_request_settings_merge_config_default_strategy

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
