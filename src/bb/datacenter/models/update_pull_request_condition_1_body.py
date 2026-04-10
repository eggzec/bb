from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_application_user import RestApplicationUser
    from ..models.rest_reviewer_group import RestReviewerGroup
    from ..models.update_pull_request_condition_1_body_source_matcher import (
        UpdatePullRequestCondition1BodySourceMatcher,
    )
    from ..models.update_pull_request_condition_1_body_target_matcher import (
        UpdatePullRequestCondition1BodyTargetMatcher,
    )


T = TypeVar("T", bound="UpdatePullRequestCondition1Body")


@_attrs_define
class UpdatePullRequestCondition1Body:
    required_approvals: int | Unset = UNSET
    reviewer_groups: list[RestReviewerGroup] | Unset = UNSET
    reviewers: list[RestApplicationUser] | Unset = UNSET
    source_matcher: UpdatePullRequestCondition1BodySourceMatcher | Unset = UNSET
    target_matcher: UpdatePullRequestCondition1BodyTargetMatcher | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_approvals = self.required_approvals

        reviewer_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reviewer_groups, Unset):
            reviewer_groups = []
            for reviewer_groups_item_data in self.reviewer_groups:
                reviewer_groups_item = reviewer_groups_item_data.to_dict()
                reviewer_groups.append(reviewer_groups_item)

        reviewers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = []
            for reviewers_item_data in self.reviewers:
                reviewers_item = reviewers_item_data.to_dict()
                reviewers.append(reviewers_item)

        source_matcher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_matcher, Unset):
            source_matcher = self.source_matcher.to_dict()

        target_matcher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_matcher, Unset):
            target_matcher = self.target_matcher.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required_approvals is not UNSET:
            field_dict["requiredApprovals"] = required_approvals
        if reviewer_groups is not UNSET:
            field_dict["reviewerGroups"] = reviewer_groups
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if source_matcher is not UNSET:
            field_dict["sourceMatcher"] = source_matcher
        if target_matcher is not UNSET:
            field_dict["targetMatcher"] = target_matcher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_application_user import RestApplicationUser
        from ..models.rest_reviewer_group import RestReviewerGroup
        from ..models.update_pull_request_condition_1_body_source_matcher import (
            UpdatePullRequestCondition1BodySourceMatcher,
        )
        from ..models.update_pull_request_condition_1_body_target_matcher import (
            UpdatePullRequestCondition1BodyTargetMatcher,
        )

        d = dict(src_dict)
        required_approvals = d.pop("requiredApprovals", UNSET)

        _reviewer_groups = d.pop("reviewerGroups", UNSET)
        reviewer_groups: list[RestReviewerGroup] | Unset = UNSET
        if _reviewer_groups is not UNSET:
            reviewer_groups = []
            for reviewer_groups_item_data in _reviewer_groups:
                reviewer_groups_item = RestReviewerGroup.from_dict(reviewer_groups_item_data)

                reviewer_groups.append(reviewer_groups_item)

        _reviewers = d.pop("reviewers", UNSET)
        reviewers: list[RestApplicationUser] | Unset = UNSET
        if _reviewers is not UNSET:
            reviewers = []
            for reviewers_item_data in _reviewers:
                reviewers_item = RestApplicationUser.from_dict(reviewers_item_data)

                reviewers.append(reviewers_item)

        _source_matcher = d.pop("sourceMatcher", UNSET)
        source_matcher: UpdatePullRequestCondition1BodySourceMatcher | Unset
        if isinstance(_source_matcher, Unset):
            source_matcher = UNSET
        else:
            source_matcher = UpdatePullRequestCondition1BodySourceMatcher.from_dict(_source_matcher)

        _target_matcher = d.pop("targetMatcher", UNSET)
        target_matcher: UpdatePullRequestCondition1BodyTargetMatcher | Unset
        if isinstance(_target_matcher, Unset):
            target_matcher = UNSET
        else:
            target_matcher = UpdatePullRequestCondition1BodyTargetMatcher.from_dict(_target_matcher)

        update_pull_request_condition_1_body = cls(
            required_approvals=required_approvals,
            reviewer_groups=reviewer_groups,
            reviewers=reviewers,
            source_matcher=source_matcher,
            target_matcher=target_matcher,
        )

        update_pull_request_condition_1_body.additional_properties = d
        return update_pull_request_condition_1_body

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
