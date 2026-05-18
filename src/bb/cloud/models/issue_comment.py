from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.comment import Comment
    from ..models.comment_content import CommentContent
    from ..models.comment_inline import CommentInline
    from ..models.comment_links import CommentLinks
    from ..models.issue import Issue


T = TypeVar("T", bound="IssueComment")


@_attrs_define
class IssueComment:
    type_: str | Unset = UNSET
    id: int | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    content: CommentContent | Unset = UNSET
    user: Account | Unset = UNSET
    deleted: bool | Unset = UNSET
    parent: Comment | Unset = UNSET
    inline: CommentInline | Unset = UNSET
    links: CommentLinks | Unset = UNSET
    issue: Issue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        deleted = self.deleted

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        inline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inline, Unset):
            inline = self.inline.to_dict()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if content is not UNSET:
            field_dict["content"] = content
        if user is not UNSET:
            field_dict["user"] = user
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if parent is not UNSET:
            field_dict["parent"] = parent
        if inline is not UNSET:
            field_dict["inline"] = inline
        if links is not UNSET:
            field_dict["links"] = links
        if issue is not UNSET:
            field_dict["issue"] = issue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.comment import Comment
        from ..models.comment_content import CommentContent
        from ..models.comment_inline import CommentInline
        from ..models.comment_links import CommentLinks
        from ..models.issue import Issue

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _updated_on = d.pop("updated_on", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        _content = d.pop("content", UNSET)
        content: CommentContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = CommentContent.from_dict(_content)

        _user = d.pop("user", UNSET)
        user: Account | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Account.from_dict(_user)

        deleted = d.pop("deleted", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Comment | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = Comment.from_dict(_parent)

        _inline = d.pop("inline", UNSET)
        inline: CommentInline | Unset
        if isinstance(_inline, Unset):
            inline = UNSET
        else:
            inline = CommentInline.from_dict(_inline)

        _links = d.pop("links", UNSET)
        links: CommentLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CommentLinks.from_dict(_links)

        _issue = d.pop("issue", UNSET)
        issue: Issue | Unset
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = Issue.from_dict(_issue)

        issue_comment = cls(
            type_=type_,
            id=id,
            created_on=created_on,
            updated_on=updated_on,
            content=content,
            user=user,
            deleted=deleted,
            parent=parent,
            inline=inline,
            links=links,
            issue=issue,
        )

        issue_comment.additional_properties = d
        return issue_comment

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
