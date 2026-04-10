from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.comment_severity import CommentSeverity
from ..models.comment_state import CommentState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_user import ApplicationUser
    from ..models.comment_operations import CommentOperations
    from ..models.comment_properties import CommentProperties
    from ..models.comment_thread import CommentThread
    from ..models.comment_thread_diff_anchor import CommentThreadDiffAnchor


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    anchor: CommentThreadDiffAnchor
    author: ApplicationUser
    comments: list[Comment]
    created_date: datetime.datetime
    permitted_operations: CommentOperations
    properties: CommentProperties
    severity: CommentSeverity
    state: CommentState
    text: str
    thread: CommentThread
    updated_date: datetime.datetime
    id: int | Unset = UNSET
    resolved_date: datetime.datetime | Unset = UNSET
    resolver: ApplicationUser | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anchor = self.anchor.to_dict()

        author = self.author.to_dict()

        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        created_date = self.created_date.isoformat()

        permitted_operations = self.permitted_operations.to_dict()

        properties = self.properties.to_dict()

        severity = self.severity.value

        state = self.state.value

        text = self.text

        thread = self.thread.to_dict()

        updated_date = self.updated_date.isoformat()

        id = self.id

        resolved_date: str | Unset = UNSET
        if not isinstance(self.resolved_date, Unset):
            resolved_date = self.resolved_date.isoformat()

        resolver: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolver, Unset):
            resolver = self.resolver.to_dict()

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "anchor": anchor,
                "author": author,
                "comments": comments,
                "createdDate": created_date,
                "permittedOperations": permitted_operations,
                "properties": properties,
                "severity": severity,
                "state": state,
                "text": text,
                "thread": thread,
                "updatedDate": updated_date,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if resolved_date is not UNSET:
            field_dict["resolvedDate"] = resolved_date
        if resolver is not UNSET:
            field_dict["resolver"] = resolver
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_user import ApplicationUser
        from ..models.comment_operations import CommentOperations
        from ..models.comment_properties import CommentProperties
        from ..models.comment_thread import CommentThread
        from ..models.comment_thread_diff_anchor import CommentThreadDiffAnchor

        d = dict(src_dict)
        anchor = CommentThreadDiffAnchor.from_dict(d.pop("anchor"))

        author = ApplicationUser.from_dict(d.pop("author"))

        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = Comment.from_dict(comments_item_data)

            comments.append(comments_item)

        created_date = isoparse(d.pop("createdDate"))

        permitted_operations = CommentOperations.from_dict(d.pop("permittedOperations"))

        properties = CommentProperties.from_dict(d.pop("properties"))

        severity = CommentSeverity(d.pop("severity"))

        state = CommentState(d.pop("state"))

        text = d.pop("text")

        thread = CommentThread.from_dict(d.pop("thread"))

        updated_date = isoparse(d.pop("updatedDate"))

        id = d.pop("id", UNSET)

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

        version = d.pop("version", UNSET)

        comment = cls(
            anchor=anchor,
            author=author,
            comments=comments,
            created_date=created_date,
            permitted_operations=permitted_operations,
            properties=properties,
            severity=severity,
            state=state,
            text=text,
            thread=thread,
            updated_date=updated_date,
            id=id,
            resolved_date=resolved_date,
            resolver=resolver,
            version=version,
        )

        comment.additional_properties = d
        return comment

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
