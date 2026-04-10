from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_user import ApplicationUser
    from ..models.comment import Comment
    from ..models.comment_thread_diff_anchor import CommentThreadDiffAnchor
    from ..models.commentable import Commentable


T = TypeVar("T", bound="CommentThread")


@_attrs_define
class CommentThread:
    anchor: CommentThreadDiffAnchor
    commentable: Commentable
    created_date: datetime.datetime
    root_comment: Comment
    updated_date: datetime.datetime
    anchored: bool | Unset = UNSET
    id: int | Unset = UNSET
    resolved: bool | Unset = UNSET
    resolved_date: datetime.datetime | Unset = UNSET
    resolver: ApplicationUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anchor = self.anchor.to_dict()

        commentable = self.commentable.to_dict()

        created_date = self.created_date.isoformat()

        root_comment = self.root_comment.to_dict()

        updated_date = self.updated_date.isoformat()

        anchored = self.anchored

        id = self.id

        resolved = self.resolved

        resolved_date: str | Unset = UNSET
        if not isinstance(self.resolved_date, Unset):
            resolved_date = self.resolved_date.isoformat()

        resolver: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolver, Unset):
            resolver = self.resolver.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anchor": anchor,
                "commentable": commentable,
                "createdDate": created_date,
                "rootComment": root_comment,
                "updatedDate": updated_date,
            }
        )
        if anchored is not UNSET:
            field_dict["anchored"] = anchored
        if id is not UNSET:
            field_dict["id"] = id
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if resolved_date is not UNSET:
            field_dict["resolvedDate"] = resolved_date
        if resolver is not UNSET:
            field_dict["resolver"] = resolver

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_user import ApplicationUser
        from ..models.comment import Comment
        from ..models.comment_thread_diff_anchor import CommentThreadDiffAnchor
        from ..models.commentable import Commentable

        d = dict(src_dict)
        anchor = CommentThreadDiffAnchor.from_dict(d.pop("anchor"))

        commentable = Commentable.from_dict(d.pop("commentable"))

        created_date = isoparse(d.pop("createdDate"))

        root_comment = Comment.from_dict(d.pop("rootComment"))

        updated_date = isoparse(d.pop("updatedDate"))

        anchored = d.pop("anchored", UNSET)

        id = d.pop("id", UNSET)

        resolved = d.pop("resolved", UNSET)

        _resolved_date = d.pop("resolvedDate", UNSET)
        resolved_date: datetime.datetime | Unset
        if isinstance(_resolved_date, Unset):
            resolved_date = UNSET
        else:
            resolved_date = isoparse(_resolved_date)

        _resolver = d.pop("resolver", UNSET)
        resolver: ApplicationUser | Unset
        if isinstance(_resolver, Unset):
            resolver = UNSET
        else:
            resolver = ApplicationUser.from_dict(_resolver)

        comment_thread = cls(
            anchor=anchor,
            commentable=commentable,
            created_date=created_date,
            root_comment=root_comment,
            updated_date=updated_date,
            anchored=anchored,
            id=id,
            resolved=resolved,
            resolved_date=resolved_date,
            resolver=resolver,
        )

        comment_thread.additional_properties = d
        return comment_thread

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
