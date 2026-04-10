from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_pull_request_suggestion_from_ref import RestPullRequestSuggestionFromRef
    from ..models.rest_pull_request_suggestion_ref_change import RestPullRequestSuggestionRefChange
    from ..models.rest_pull_request_suggestion_repository import RestPullRequestSuggestionRepository
    from ..models.rest_pull_request_suggestion_to_ref import RestPullRequestSuggestionToRef


T = TypeVar("T", bound="RestPullRequestSuggestion")


@_attrs_define
class RestPullRequestSuggestion:
    change_tme: int | Unset = UNSET
    from_ref: RestPullRequestSuggestionFromRef | Unset = UNSET
    ref_change: RestPullRequestSuggestionRefChange | Unset = UNSET
    repository: RestPullRequestSuggestionRepository | Unset = UNSET
    to_ref: RestPullRequestSuggestionToRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_tme = self.change_tme

        from_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_ref, Unset):
            from_ref = self.from_ref.to_dict()

        ref_change: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ref_change, Unset):
            ref_change = self.ref_change.to_dict()

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        to_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to_ref, Unset):
            to_ref = self.to_ref.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change_tme is not UNSET:
            field_dict["changeTme"] = change_tme
        if from_ref is not UNSET:
            field_dict["fromRef"] = from_ref
        if ref_change is not UNSET:
            field_dict["refChange"] = ref_change
        if repository is not UNSET:
            field_dict["repository"] = repository
        if to_ref is not UNSET:
            field_dict["toRef"] = to_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_pull_request_suggestion_from_ref import RestPullRequestSuggestionFromRef
        from ..models.rest_pull_request_suggestion_ref_change import RestPullRequestSuggestionRefChange
        from ..models.rest_pull_request_suggestion_repository import RestPullRequestSuggestionRepository
        from ..models.rest_pull_request_suggestion_to_ref import RestPullRequestSuggestionToRef

        d = dict(src_dict)
        change_tme = d.pop("changeTme", UNSET)

        _from_ref = d.pop("fromRef", UNSET)
        from_ref: RestPullRequestSuggestionFromRef | Unset
        if isinstance(_from_ref, Unset):
            from_ref = UNSET
        else:
            from_ref = RestPullRequestSuggestionFromRef.from_dict(_from_ref)

        _ref_change = d.pop("refChange", UNSET)
        ref_change: RestPullRequestSuggestionRefChange | Unset
        if isinstance(_ref_change, Unset):
            ref_change = UNSET
        else:
            ref_change = RestPullRequestSuggestionRefChange.from_dict(_ref_change)

        _repository = d.pop("repository", UNSET)
        repository: RestPullRequestSuggestionRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RestPullRequestSuggestionRepository.from_dict(_repository)

        _to_ref = d.pop("toRef", UNSET)
        to_ref: RestPullRequestSuggestionToRef | Unset
        if isinstance(_to_ref, Unset):
            to_ref = UNSET
        else:
            to_ref = RestPullRequestSuggestionToRef.from_dict(_to_ref)

        rest_pull_request_suggestion = cls(
            change_tme=change_tme,
            from_ref=from_ref,
            ref_change=ref_change,
            repository=repository,
            to_ref=to_ref,
        )

        rest_pull_request_suggestion.additional_properties = d
        return rest_pull_request_suggestion

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
