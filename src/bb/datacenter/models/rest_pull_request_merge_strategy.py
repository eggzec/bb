from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_pull_request_merge_strategy_links import RestPullRequestMergeStrategyLinks


T = TypeVar("T", bound="RestPullRequestMergeStrategy")


@_attrs_define
class RestPullRequestMergeStrategy:
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    flag: str | Unset = UNSET
    id: str | Unset = UNSET
    links: RestPullRequestMergeStrategyLinks | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        enabled = self.enabled

        flag = self.flag

        id = self.id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if flag is not UNSET:
            field_dict["flag"] = flag
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_pull_request_merge_strategy_links import RestPullRequestMergeStrategyLinks

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        flag = d.pop("flag", UNSET)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: RestPullRequestMergeStrategyLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestPullRequestMergeStrategyLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        rest_pull_request_merge_strategy = cls(
            description=description,
            enabled=enabled,
            flag=flag,
            id=id,
            links=links,
            name=name,
        )

        rest_pull_request_merge_strategy.additional_properties = d
        return rest_pull_request_merge_strategy

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
