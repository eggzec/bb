from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_pull_request_condition_scope import RestPullRequestConditionScope
    from ..models.rest_pull_request_condition_source_ref_matcher import RestPullRequestConditionSourceRefMatcher
    from ..models.rest_pull_request_condition_target_ref_matcher import RestPullRequestConditionTargetRefMatcher
    from ..models.rest_reviewer_group import RestReviewerGroup


T = TypeVar("T", bound="RestPullRequestCondition")


@_attrs_define
class RestPullRequestCondition:
    id: int | Unset = UNSET
    required_approvals: int | Unset = UNSET
    reviewer_groups: list[RestReviewerGroup] | Unset = UNSET
    reviewers: list[RestReviewerGroup] | Unset = UNSET
    scope: RestPullRequestConditionScope | Unset = UNSET
    source_ref_matcher: RestPullRequestConditionSourceRefMatcher | Unset = UNSET
    target_ref_matcher: RestPullRequestConditionTargetRefMatcher | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        source_ref_matcher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_ref_matcher, Unset):
            source_ref_matcher = self.source_ref_matcher.to_dict()

        target_ref_matcher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_ref_matcher, Unset):
            target_ref_matcher = self.target_ref_matcher.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if required_approvals is not UNSET:
            field_dict["requiredApprovals"] = required_approvals
        if reviewer_groups is not UNSET:
            field_dict["reviewerGroups"] = reviewer_groups
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if scope is not UNSET:
            field_dict["scope"] = scope
        if source_ref_matcher is not UNSET:
            field_dict["sourceRefMatcher"] = source_ref_matcher
        if target_ref_matcher is not UNSET:
            field_dict["targetRefMatcher"] = target_ref_matcher

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_pull_request_condition_scope import RestPullRequestConditionScope
        from ..models.rest_pull_request_condition_source_ref_matcher import RestPullRequestConditionSourceRefMatcher
        from ..models.rest_pull_request_condition_target_ref_matcher import RestPullRequestConditionTargetRefMatcher
        from ..models.rest_reviewer_group import RestReviewerGroup

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        required_approvals = d.pop("requiredApprovals", UNSET)

        _reviewer_groups = d.pop("reviewerGroups", UNSET)
        reviewer_groups: list[RestReviewerGroup] | Unset = UNSET
        if _reviewer_groups is not UNSET:
            reviewer_groups = []
            for reviewer_groups_item_data in _reviewer_groups:
                reviewer_groups_item = RestReviewerGroup.from_dict(reviewer_groups_item_data)

                reviewer_groups.append(reviewer_groups_item)

        _reviewers = d.pop("reviewers", UNSET)
        reviewers: list[RestReviewerGroup] | Unset = UNSET
        if _reviewers is not UNSET:
            reviewers = []
            for reviewers_item_data in _reviewers:
                reviewers_item = RestReviewerGroup.from_dict(reviewers_item_data)

                reviewers.append(reviewers_item)

        _scope = d.pop("scope", UNSET)
        scope: RestPullRequestConditionScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RestPullRequestConditionScope.from_dict(_scope)

        _source_ref_matcher = d.pop("sourceRefMatcher", UNSET)
        source_ref_matcher: RestPullRequestConditionSourceRefMatcher | Unset
        if isinstance(_source_ref_matcher, Unset):
            source_ref_matcher = UNSET
        else:
            source_ref_matcher = RestPullRequestConditionSourceRefMatcher.from_dict(_source_ref_matcher)

        _target_ref_matcher = d.pop("targetRefMatcher", UNSET)
        target_ref_matcher: RestPullRequestConditionTargetRefMatcher | Unset
        if isinstance(_target_ref_matcher, Unset):
            target_ref_matcher = UNSET
        else:
            target_ref_matcher = RestPullRequestConditionTargetRefMatcher.from_dict(_target_ref_matcher)

        rest_pull_request_condition = cls(
            id=id,
            required_approvals=required_approvals,
            reviewer_groups=reviewer_groups,
            reviewers=reviewers,
            scope=scope,
            source_ref_matcher=source_ref_matcher,
            target_ref_matcher=target_ref_matcher,
        )

        rest_pull_request_condition.additional_properties = d
        return rest_pull_request_condition

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
