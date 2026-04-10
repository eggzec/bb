from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_auto_merge_processing_result_auto_merge_processing_status import (
    RestAutoMergeProcessingResultAutoMergeProcessingStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_auto_merge_processing_result_pull_request import RestAutoMergeProcessingResultPullRequest


T = TypeVar("T", bound="RestAutoMergeProcessingResult")


@_attrs_define
class RestAutoMergeProcessingResult:
    auto_merge_processing_status: RestAutoMergeProcessingResultAutoMergeProcessingStatus | Unset = UNSET
    pull_request: RestAutoMergeProcessingResultPullRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_merge_processing_status: str | Unset = UNSET
        if not isinstance(self.auto_merge_processing_status, Unset):
            auto_merge_processing_status = self.auto_merge_processing_status.value

        pull_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pull_request, Unset):
            pull_request = self.pull_request.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_merge_processing_status is not UNSET:
            field_dict["autoMergeProcessingStatus"] = auto_merge_processing_status
        if pull_request is not UNSET:
            field_dict["pullRequest"] = pull_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_auto_merge_processing_result_pull_request import RestAutoMergeProcessingResultPullRequest

        d = dict(src_dict)
        _auto_merge_processing_status = d.pop("autoMergeProcessingStatus", UNSET)
        auto_merge_processing_status: RestAutoMergeProcessingResultAutoMergeProcessingStatus | Unset
        if isinstance(_auto_merge_processing_status, Unset):
            auto_merge_processing_status = UNSET
        else:
            auto_merge_processing_status = RestAutoMergeProcessingResultAutoMergeProcessingStatus(
                _auto_merge_processing_status
            )

        _pull_request = d.pop("pullRequest", UNSET)
        pull_request: RestAutoMergeProcessingResultPullRequest | Unset
        if isinstance(_pull_request, Unset):
            pull_request = UNSET
        else:
            pull_request = RestAutoMergeProcessingResultPullRequest.from_dict(_pull_request)

        rest_auto_merge_processing_result = cls(
            auto_merge_processing_status=auto_merge_processing_status,
            pull_request=pull_request,
        )

        rest_auto_merge_processing_result.additional_properties = d
        return rest_auto_merge_processing_result

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
