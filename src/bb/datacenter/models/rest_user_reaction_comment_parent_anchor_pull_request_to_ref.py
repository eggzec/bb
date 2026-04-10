from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_user_reaction_comment_parent_anchor_pull_request_to_ref_type import (
    RestUserReactionCommentParentAnchorPullRequestToRefType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_user_reaction_comment_parent_anchor_pull_request_to_ref_repository import (
        RestUserReactionCommentParentAnchorPullRequestToRefRepository,
    )


T = TypeVar("T", bound="RestUserReactionCommentParentAnchorPullRequestToRef")


@_attrs_define
class RestUserReactionCommentParentAnchorPullRequestToRef:
    display_id: str
    id: str
    latest_commit: str
    repository: RestUserReactionCommentParentAnchorPullRequestToRefRepository | Unset = UNSET
    type_: RestUserReactionCommentParentAnchorPullRequestToRefType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_id = self.display_id

        id = self.id

        latest_commit = self.latest_commit

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayId": display_id,
                "id": id,
                "latestCommit": latest_commit,
            }
        )
        if repository is not UNSET:
            field_dict["repository"] = repository
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_user_reaction_comment_parent_anchor_pull_request_to_ref_repository import (
            RestUserReactionCommentParentAnchorPullRequestToRefRepository,
        )

        d = dict(src_dict)
        display_id = d.pop("displayId")

        id = d.pop("id")

        latest_commit = d.pop("latestCommit")

        _repository = d.pop("repository", UNSET)
        repository: RestUserReactionCommentParentAnchorPullRequestToRefRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RestUserReactionCommentParentAnchorPullRequestToRefRepository.from_dict(_repository)

        _type_ = d.pop("type", UNSET)
        type_: RestUserReactionCommentParentAnchorPullRequestToRefType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestUserReactionCommentParentAnchorPullRequestToRefType(_type_)

        rest_user_reaction_comment_parent_anchor_pull_request_to_ref = cls(
            display_id=display_id,
            id=id,
            latest_commit=latest_commit,
            repository=repository,
            type_=type_,
        )

        rest_user_reaction_comment_parent_anchor_pull_request_to_ref.additional_properties = d
        return rest_user_reaction_comment_parent_anchor_pull_request_to_ref

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
