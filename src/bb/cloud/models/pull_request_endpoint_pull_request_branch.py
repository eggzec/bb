from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.pull_request_endpoint_pull_request_branch_merge_strategies_item import (
    PullRequestEndpointPullRequestBranchMergeStrategiesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullRequestEndpointPullRequestBranch")


@_attrs_define
class PullRequestEndpointPullRequestBranch:
    name: str | Unset = UNSET
    merge_strategies: list[PullRequestEndpointPullRequestBranchMergeStrategiesItem] | Unset = UNSET
    """ Available merge strategies, when this endpoint is the destination of the pull request. """
    default_merge_strategy: str | Unset = UNSET
    """ The default merge strategy, when this endpoint is the destination of the pull request. """

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        merge_strategies: list[str] | Unset = UNSET
        if not isinstance(self.merge_strategies, Unset):
            merge_strategies = []
            for merge_strategies_item_data in self.merge_strategies:
                merge_strategies_item = merge_strategies_item_data.value
                merge_strategies.append(merge_strategies_item)

        default_merge_strategy = self.default_merge_strategy

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if merge_strategies is not UNSET:
            field_dict["merge_strategies"] = merge_strategies
        if default_merge_strategy is not UNSET:
            field_dict["default_merge_strategy"] = default_merge_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _merge_strategies = d.pop("merge_strategies", UNSET)
        merge_strategies: list[PullRequestEndpointPullRequestBranchMergeStrategiesItem] | Unset = UNSET
        if _merge_strategies is not UNSET:
            merge_strategies = []
            for merge_strategies_item_data in _merge_strategies:
                merge_strategies_item = PullRequestEndpointPullRequestBranchMergeStrategiesItem(
                    merge_strategies_item_data
                )

                merge_strategies.append(merge_strategies_item)

        default_merge_strategy = d.pop("default_merge_strategy", UNSET)

        pull_request_endpoint_pull_request_branch = cls(
            name=name,
            merge_strategies=merge_strategies,
            default_merge_strategy=default_merge_strategy,
        )

        return pull_request_endpoint_pull_request_branch
