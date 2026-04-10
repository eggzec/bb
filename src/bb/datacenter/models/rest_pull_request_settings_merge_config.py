from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_pull_request_merge_strategy import RestPullRequestMergeStrategy
    from ..models.rest_pull_request_settings_merge_config_commit_message_template import (
        RestPullRequestSettingsMergeConfigCommitMessageTemplate,
    )
    from ..models.rest_pull_request_settings_merge_config_default_strategy import (
        RestPullRequestSettingsMergeConfigDefaultStrategy,
    )


T = TypeVar("T", bound="RestPullRequestSettingsMergeConfig")


@_attrs_define
class RestPullRequestSettingsMergeConfig:
    strategies: list[RestPullRequestMergeStrategy]
    commit_message_template: RestPullRequestSettingsMergeConfigCommitMessageTemplate | Unset = UNSET
    commit_summaries: int | Unset = UNSET
    default_strategy: RestPullRequestSettingsMergeConfigDefaultStrategy | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        strategies = []
        for strategies_item_data in self.strategies:
            strategies_item = strategies_item_data.to_dict()
            strategies.append(strategies_item)

        commit_message_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit_message_template, Unset):
            commit_message_template = self.commit_message_template.to_dict()

        commit_summaries = self.commit_summaries

        default_strategy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_strategy, Unset):
            default_strategy = self.default_strategy.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "strategies": strategies,
            }
        )
        if commit_message_template is not UNSET:
            field_dict["commitMessageTemplate"] = commit_message_template
        if commit_summaries is not UNSET:
            field_dict["commitSummaries"] = commit_summaries
        if default_strategy is not UNSET:
            field_dict["defaultStrategy"] = default_strategy
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_pull_request_merge_strategy import RestPullRequestMergeStrategy
        from ..models.rest_pull_request_settings_merge_config_commit_message_template import (
            RestPullRequestSettingsMergeConfigCommitMessageTemplate,
        )
        from ..models.rest_pull_request_settings_merge_config_default_strategy import (
            RestPullRequestSettingsMergeConfigDefaultStrategy,
        )

        d = dict(src_dict)
        strategies = []
        _strategies = d.pop("strategies")
        for strategies_item_data in _strategies:
            strategies_item = RestPullRequestMergeStrategy.from_dict(strategies_item_data)

            strategies.append(strategies_item)

        _commit_message_template = d.pop("commitMessageTemplate", UNSET)
        commit_message_template: RestPullRequestSettingsMergeConfigCommitMessageTemplate | Unset
        if isinstance(_commit_message_template, Unset):
            commit_message_template = UNSET
        else:
            commit_message_template = RestPullRequestSettingsMergeConfigCommitMessageTemplate.from_dict(
                _commit_message_template
            )

        commit_summaries = d.pop("commitSummaries", UNSET)

        _default_strategy = d.pop("defaultStrategy", UNSET)
        default_strategy: RestPullRequestSettingsMergeConfigDefaultStrategy | Unset
        if isinstance(_default_strategy, Unset):
            default_strategy = UNSET
        else:
            default_strategy = RestPullRequestSettingsMergeConfigDefaultStrategy.from_dict(_default_strategy)

        type_ = d.pop("type", UNSET)

        rest_pull_request_settings_merge_config = cls(
            strategies=strategies,
            commit_message_template=commit_message_template,
            commit_summaries=commit_summaries,
            default_strategy=default_strategy,
            type_=type_,
        )

        rest_pull_request_settings_merge_config.additional_properties = d
        return rest_pull_request_settings_merge_config

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
