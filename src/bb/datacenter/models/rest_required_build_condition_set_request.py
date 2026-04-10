from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_ref_matcher import RestRefMatcher
    from ..models.rest_required_build_condition_set_request_exempt_ref_matcher import (
        RestRequiredBuildConditionSetRequestExemptRefMatcher,
    )


T = TypeVar("T", bound="RestRequiredBuildConditionSetRequest")


@_attrs_define
class RestRequiredBuildConditionSetRequest:
    build_parent_keys: list[str]
    """ A non-empty list of build parent keys that require green builds for this merge check to pass """
    ref_matcher: RestRefMatcher
    exempt_ref_matcher: RestRequiredBuildConditionSetRequestExemptRefMatcher | Unset = UNSET
    required_for_merge_queue: bool | Unset = True
    """ Indicates whether this required build condition is enforced for merges via the merge queue. If not
    specified, defaults to true. """
    required_for_pull_request: bool | Unset = True
    """ Indicates whether this required build condition is enforced for pull requests. If not specified, defaults to
    true. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_parent_keys = self.build_parent_keys

        ref_matcher = self.ref_matcher.to_dict()

        exempt_ref_matcher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exempt_ref_matcher, Unset):
            exempt_ref_matcher = self.exempt_ref_matcher.to_dict()

        required_for_merge_queue = self.required_for_merge_queue

        required_for_pull_request = self.required_for_pull_request

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buildParentKeys": build_parent_keys,
                "refMatcher": ref_matcher,
            }
        )
        if exempt_ref_matcher is not UNSET:
            field_dict["exemptRefMatcher"] = exempt_ref_matcher
        if required_for_merge_queue is not UNSET:
            field_dict["requiredForMergeQueue"] = required_for_merge_queue
        if required_for_pull_request is not UNSET:
            field_dict["requiredForPullRequest"] = required_for_pull_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_ref_matcher import RestRefMatcher
        from ..models.rest_required_build_condition_set_request_exempt_ref_matcher import (
            RestRequiredBuildConditionSetRequestExemptRefMatcher,
        )

        d = dict(src_dict)
        build_parent_keys = cast(list[str], d.pop("buildParentKeys"))

        ref_matcher = RestRefMatcher.from_dict(d.pop("refMatcher"))

        _exempt_ref_matcher = d.pop("exemptRefMatcher", UNSET)
        exempt_ref_matcher: RestRequiredBuildConditionSetRequestExemptRefMatcher | Unset
        if isinstance(_exempt_ref_matcher, Unset):
            exempt_ref_matcher = UNSET
        else:
            exempt_ref_matcher = RestRequiredBuildConditionSetRequestExemptRefMatcher.from_dict(_exempt_ref_matcher)

        required_for_merge_queue = d.pop("requiredForMergeQueue", UNSET)

        required_for_pull_request = d.pop("requiredForPullRequest", UNSET)

        rest_required_build_condition_set_request = cls(
            build_parent_keys=build_parent_keys,
            ref_matcher=ref_matcher,
            exempt_ref_matcher=exempt_ref_matcher,
            required_for_merge_queue=required_for_merge_queue,
            required_for_pull_request=required_for_pull_request,
        )

        rest_required_build_condition_set_request.additional_properties = d
        return rest_required_build_condition_set_request

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
