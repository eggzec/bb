from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_repository_pull_request_settings_merge_config import RestRepositoryPullRequestSettingsMergeConfig
    from ..models.rest_repository_pull_request_settings_required_approvers import (
        RestRepositoryPullRequestSettingsRequiredApprovers,
    )
    from ..models.rest_repository_pull_request_settings_required_successful_builds import (
        RestRepositoryPullRequestSettingsRequiredSuccessfulBuilds,
    )


T = TypeVar("T", bound="RestRepositoryPullRequestSettings")


@_attrs_define
class RestRepositoryPullRequestSettings:
    merge_config: RestRepositoryPullRequestSettingsMergeConfig | Unset = UNSET
    required_all_approvers: bool | Unset = UNSET
    required_all_tasks_complete: bool | Unset = UNSET
    required_approvers: RestRepositoryPullRequestSettingsRequiredApprovers | Unset = UNSET
    required_approvers_deprecated: int | Unset = UNSET
    required_successful_builds: RestRepositoryPullRequestSettingsRequiredSuccessfulBuilds | Unset = UNSET
    required_successful_builds_deprecated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        merge_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge_config, Unset):
            merge_config = self.merge_config.to_dict()

        required_all_approvers = self.required_all_approvers

        required_all_tasks_complete = self.required_all_tasks_complete

        required_approvers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required_approvers, Unset):
            required_approvers = self.required_approvers.to_dict()

        required_approvers_deprecated = self.required_approvers_deprecated

        required_successful_builds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.required_successful_builds, Unset):
            required_successful_builds = self.required_successful_builds.to_dict()

        required_successful_builds_deprecated = self.required_successful_builds_deprecated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if merge_config is not UNSET:
            field_dict["mergeConfig"] = merge_config
        if required_all_approvers is not UNSET:
            field_dict["requiredAllApprovers"] = required_all_approvers
        if required_all_tasks_complete is not UNSET:
            field_dict["requiredAllTasksComplete"] = required_all_tasks_complete
        if required_approvers is not UNSET:
            field_dict["requiredApprovers"] = required_approvers
        if required_approvers_deprecated is not UNSET:
            field_dict["requiredApproversDeprecated"] = required_approvers_deprecated
        if required_successful_builds is not UNSET:
            field_dict["requiredSuccessfulBuilds"] = required_successful_builds
        if required_successful_builds_deprecated is not UNSET:
            field_dict["requiredSuccessfulBuildsDeprecated"] = required_successful_builds_deprecated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_repository_pull_request_settings_merge_config import (
            RestRepositoryPullRequestSettingsMergeConfig,
        )
        from ..models.rest_repository_pull_request_settings_required_approvers import (
            RestRepositoryPullRequestSettingsRequiredApprovers,
        )
        from ..models.rest_repository_pull_request_settings_required_successful_builds import (
            RestRepositoryPullRequestSettingsRequiredSuccessfulBuilds,
        )

        d = dict(src_dict)
        _merge_config = d.pop("mergeConfig", UNSET)
        merge_config: RestRepositoryPullRequestSettingsMergeConfig | Unset
        if isinstance(_merge_config, Unset):
            merge_config = UNSET
        else:
            merge_config = RestRepositoryPullRequestSettingsMergeConfig.from_dict(_merge_config)

        required_all_approvers = d.pop("requiredAllApprovers", UNSET)

        required_all_tasks_complete = d.pop("requiredAllTasksComplete", UNSET)

        _required_approvers = d.pop("requiredApprovers", UNSET)
        required_approvers: RestRepositoryPullRequestSettingsRequiredApprovers | Unset
        if isinstance(_required_approvers, Unset):
            required_approvers = UNSET
        else:
            required_approvers = RestRepositoryPullRequestSettingsRequiredApprovers.from_dict(_required_approvers)

        required_approvers_deprecated = d.pop("requiredApproversDeprecated", UNSET)

        _required_successful_builds = d.pop("requiredSuccessfulBuilds", UNSET)
        required_successful_builds: RestRepositoryPullRequestSettingsRequiredSuccessfulBuilds | Unset
        if isinstance(_required_successful_builds, Unset):
            required_successful_builds = UNSET
        else:
            required_successful_builds = RestRepositoryPullRequestSettingsRequiredSuccessfulBuilds.from_dict(
                _required_successful_builds
            )

        required_successful_builds_deprecated = d.pop("requiredSuccessfulBuildsDeprecated", UNSET)

        rest_repository_pull_request_settings = cls(
            merge_config=merge_config,
            required_all_approvers=required_all_approvers,
            required_all_tasks_complete=required_all_tasks_complete,
            required_approvers=required_approvers,
            required_approvers_deprecated=required_approvers_deprecated,
            required_successful_builds=required_successful_builds,
            required_successful_builds_deprecated=required_successful_builds_deprecated,
        )

        rest_repository_pull_request_settings.additional_properties = d
        return rest_repository_pull_request_settings

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
