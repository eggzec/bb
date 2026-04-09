from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pull_request_merge_parameters_merge_strategy import PullRequestMergeParametersMergeStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="PullRequestMergeParameters")


@_attrs_define
class PullRequestMergeParameters:
    """The metadata that describes a pull request merge."""

    type_: str
    message: str | Unset = UNSET
    """ The commit message that will be used on the resulting commit. Note that the size of the message is limited
    to 128 KiB. """
    close_source_branch: bool | Unset = UNSET
    """ Whether the source branch should be deleted. If this is not provided, we fallback to the value used when the
    pull request was created, which defaults to False """
    merge_strategy: PullRequestMergeParametersMergeStrategy | Unset = (
        PullRequestMergeParametersMergeStrategy.MERGE_COMMIT
    )
    """ The merge strategy that will be used to merge the pull request. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        message = self.message

        close_source_branch = self.close_source_branch

        merge_strategy: str | Unset = UNSET
        if not isinstance(self.merge_strategy, Unset):
            merge_strategy = self.merge_strategy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if close_source_branch is not UNSET:
            field_dict["close_source_branch"] = close_source_branch
        if merge_strategy is not UNSET:
            field_dict["merge_strategy"] = merge_strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        message = d.pop("message", UNSET)

        close_source_branch = d.pop("close_source_branch", UNSET)

        _merge_strategy = d.pop("merge_strategy", UNSET)
        merge_strategy: PullRequestMergeParametersMergeStrategy | Unset
        if isinstance(_merge_strategy, Unset):
            merge_strategy = UNSET
        else:
            merge_strategy = PullRequestMergeParametersMergeStrategy(_merge_strategy)

        pull_request_merge_parameters = cls(
            type_=type_,
            message=message,
            close_source_branch=close_source_branch,
            merge_strategy=merge_strategy,
        )

        pull_request_merge_parameters.additional_properties = d
        return pull_request_merge_parameters

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
