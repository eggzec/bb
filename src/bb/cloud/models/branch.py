from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.branch_merge_strategies_item import BranchMergeStrategiesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit import Commit
    from ..models.ref_links import RefLinks


T = TypeVar("T", bound="Branch")


@_attrs_define
class Branch:
    type_: str
    links: RefLinks | Unset = UNSET
    name: str | Unset = UNSET
    """ The name of the ref. """
    target: Commit | Unset = UNSET
    merge_strategies: list[BranchMergeStrategiesItem] | Unset = UNSET
    """ Available merge strategies for pull requests targeting this branch. """
    default_merge_strategy: str | Unset = UNSET
    """ The default merge strategy for pull requests targeting this branch. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        merge_strategies: list[str] | Unset = UNSET
        if not isinstance(self.merge_strategies, Unset):
            merge_strategies = []
            for merge_strategies_item_data in self.merge_strategies:
                merge_strategies_item = merge_strategies_item_data.value
                merge_strategies.append(merge_strategies_item)

        default_merge_strategy = self.default_merge_strategy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target
        if merge_strategies is not UNSET:
            field_dict["merge_strategies"] = merge_strategies
        if default_merge_strategy is not UNSET:
            field_dict["default_merge_strategy"] = default_merge_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit import Commit
        from ..models.ref_links import RefLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: RefLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RefLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        _target = d.pop("target", UNSET)
        target: Commit | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = Commit.from_dict(_target)

        _merge_strategies = d.pop("merge_strategies", UNSET)
        merge_strategies: list[BranchMergeStrategiesItem] | Unset = UNSET
        if _merge_strategies is not UNSET:
            merge_strategies = []
            for merge_strategies_item_data in _merge_strategies:
                merge_strategies_item = BranchMergeStrategiesItem(merge_strategies_item_data)

                merge_strategies.append(merge_strategies_item)

        default_merge_strategy = d.pop("default_merge_strategy", UNSET)

        branch = cls(
            type_=type_,
            links=links,
            name=name,
            target=target,
            merge_strategies=merge_strategies,
            default_merge_strategy=default_merge_strategy,
        )

        branch.additional_properties = d
        return branch

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
