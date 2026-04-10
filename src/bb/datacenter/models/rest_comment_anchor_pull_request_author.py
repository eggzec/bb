from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_comment_anchor_pull_request_author_role import RestCommentAnchorPullRequestAuthorRole
from ..models.rest_comment_anchor_pull_request_author_status import RestCommentAnchorPullRequestAuthorStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_comment_anchor_pull_request_author_user import RestCommentAnchorPullRequestAuthorUser


T = TypeVar("T", bound="RestCommentAnchorPullRequestAuthor")


@_attrs_define
class RestCommentAnchorPullRequestAuthor:
    approved: bool | Unset = UNSET
    last_reviewed_commit: str | Unset = UNSET
    role: RestCommentAnchorPullRequestAuthorRole | Unset = UNSET
    status: RestCommentAnchorPullRequestAuthorStatus | Unset = UNSET
    user: RestCommentAnchorPullRequestAuthorUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approved = self.approved

        last_reviewed_commit = self.last_reviewed_commit

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approved is not UNSET:
            field_dict["approved"] = approved
        if last_reviewed_commit is not UNSET:
            field_dict["lastReviewedCommit"] = last_reviewed_commit
        if role is not UNSET:
            field_dict["role"] = role
        if status is not UNSET:
            field_dict["status"] = status
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_comment_anchor_pull_request_author_user import RestCommentAnchorPullRequestAuthorUser

        d = dict(src_dict)
        approved = d.pop("approved", UNSET)

        last_reviewed_commit = d.pop("lastReviewedCommit", UNSET)

        _role = d.pop("role", UNSET)
        role: RestCommentAnchorPullRequestAuthorRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RestCommentAnchorPullRequestAuthorRole(_role)

        _status = d.pop("status", UNSET)
        status: RestCommentAnchorPullRequestAuthorStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RestCommentAnchorPullRequestAuthorStatus(_status)

        _user = d.pop("user", UNSET)
        user: RestCommentAnchorPullRequestAuthorUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RestCommentAnchorPullRequestAuthorUser.from_dict(_user)

        rest_comment_anchor_pull_request_author = cls(
            approved=approved,
            last_reviewed_commit=last_reviewed_commit,
            role=role,
            status=status,
            user=user,
        )

        rest_comment_anchor_pull_request_author.additional_properties = d
        return rest_comment_anchor_pull_request_author

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
