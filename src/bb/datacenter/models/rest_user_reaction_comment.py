from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_comment import RestComment
    from ..models.rest_user_reaction_comment_anchor import RestUserReactionCommentAnchor
    from ..models.rest_user_reaction_comment_author import RestUserReactionCommentAuthor
    from ..models.rest_user_reaction_comment_parent import RestUserReactionCommentParent
    from ..models.rest_user_reaction_comment_properties import RestUserReactionCommentProperties
    from ..models.rest_user_reaction_comment_resolver import RestUserReactionCommentResolver
    from ..models.rest_user_reaction_comment_thread_resolver import RestUserReactionCommentThreadResolver


T = TypeVar("T", bound="RestUserReactionComment")


@_attrs_define
class RestUserReactionComment:
    anchor: RestUserReactionCommentAnchor | Unset = UNSET
    anchored: bool | Unset = UNSET
    author: RestUserReactionCommentAuthor | Unset = UNSET
    comments: list[RestComment] | Unset = UNSET
    created_date: int | Unset = UNSET
    html: str | Unset = UNSET
    id: int | Unset = UNSET
    parent: RestUserReactionCommentParent | Unset = UNSET
    pending: bool | Unset = UNSET
    properties: RestUserReactionCommentProperties | Unset = UNSET
    reply: bool | Unset = UNSET
    resolved_date: int | Unset = UNSET
    resolver: RestUserReactionCommentResolver | Unset = UNSET
    severity: str | Unset = UNSET
    state: str | Unset = UNSET
    text: str | Unset = UNSET
    thread_resolved: bool | Unset = UNSET
    """ Indicates if this comment thread has been marked as resolved or not """
    thread_resolved_date: int | Unset = UNSET
    thread_resolver: RestUserReactionCommentThreadResolver | Unset = UNSET
    updated_date: int | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anchor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.anchor, Unset):
            anchor = self.anchor.to_dict()

        anchored = self.anchored

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        created_date = self.created_date

        html = self.html

        id = self.id

        parent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        pending = self.pending

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        reply = self.reply

        resolved_date = self.resolved_date

        resolver: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolver, Unset):
            resolver = self.resolver.to_dict()

        severity = self.severity

        state = self.state

        text = self.text

        thread_resolved = self.thread_resolved

        thread_resolved_date = self.thread_resolved_date

        thread_resolver: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thread_resolver, Unset):
            thread_resolver = self.thread_resolver.to_dict()

        updated_date = self.updated_date

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anchor is not UNSET:
            field_dict["anchor"] = anchor
        if anchored is not UNSET:
            field_dict["anchored"] = anchored
        if author is not UNSET:
            field_dict["author"] = author
        if comments is not UNSET:
            field_dict["comments"] = comments
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if html is not UNSET:
            field_dict["html"] = html
        if id is not UNSET:
            field_dict["id"] = id
        if parent is not UNSET:
            field_dict["parent"] = parent
        if pending is not UNSET:
            field_dict["pending"] = pending
        if properties is not UNSET:
            field_dict["properties"] = properties
        if reply is not UNSET:
            field_dict["reply"] = reply
        if resolved_date is not UNSET:
            field_dict["resolvedDate"] = resolved_date
        if resolver is not UNSET:
            field_dict["resolver"] = resolver
        if severity is not UNSET:
            field_dict["severity"] = severity
        if state is not UNSET:
            field_dict["state"] = state
        if text is not UNSET:
            field_dict["text"] = text
        if thread_resolved is not UNSET:
            field_dict["threadResolved"] = thread_resolved
        if thread_resolved_date is not UNSET:
            field_dict["threadResolvedDate"] = thread_resolved_date
        if thread_resolver is not UNSET:
            field_dict["threadResolver"] = thread_resolver
        if updated_date is not UNSET:
            field_dict["updatedDate"] = updated_date
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_comment import RestComment
        from ..models.rest_user_reaction_comment_anchor import RestUserReactionCommentAnchor
        from ..models.rest_user_reaction_comment_author import RestUserReactionCommentAuthor
        from ..models.rest_user_reaction_comment_parent import RestUserReactionCommentParent
        from ..models.rest_user_reaction_comment_properties import RestUserReactionCommentProperties
        from ..models.rest_user_reaction_comment_resolver import RestUserReactionCommentResolver
        from ..models.rest_user_reaction_comment_thread_resolver import RestUserReactionCommentThreadResolver

        d = dict(src_dict)
        _anchor = d.pop("anchor", UNSET)
        anchor: RestUserReactionCommentAnchor | Unset
        if isinstance(_anchor, Unset):
            anchor = UNSET
        else:
            anchor = RestUserReactionCommentAnchor.from_dict(_anchor)

        anchored = d.pop("anchored", UNSET)

        _author = d.pop("author", UNSET)
        author: RestUserReactionCommentAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = RestUserReactionCommentAuthor.from_dict(_author)

        _comments = d.pop("comments", UNSET)
        comments: list[RestComment] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = RestComment.from_dict(comments_item_data)

                comments.append(comments_item)

        created_date = d.pop("createdDate", UNSET)

        html = d.pop("html", UNSET)

        id = d.pop("id", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: RestUserReactionCommentParent | Unset
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = RestUserReactionCommentParent.from_dict(_parent)

        pending = d.pop("pending", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: RestUserReactionCommentProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = RestUserReactionCommentProperties.from_dict(_properties)

        reply = d.pop("reply", UNSET)

        resolved_date = d.pop("resolvedDate", UNSET)

        _resolver = d.pop("resolver", UNSET)
        resolver: RestUserReactionCommentResolver | Unset
        if isinstance(_resolver, Unset):
            resolver = UNSET
        else:
            resolver = RestUserReactionCommentResolver.from_dict(_resolver)

        severity = d.pop("severity", UNSET)

        state = d.pop("state", UNSET)

        text = d.pop("text", UNSET)

        thread_resolved = d.pop("threadResolved", UNSET)

        thread_resolved_date = d.pop("threadResolvedDate", UNSET)

        _thread_resolver = d.pop("threadResolver", UNSET)
        thread_resolver: RestUserReactionCommentThreadResolver | Unset
        if isinstance(_thread_resolver, Unset):
            thread_resolver = UNSET
        else:
            thread_resolver = RestUserReactionCommentThreadResolver.from_dict(_thread_resolver)

        updated_date = d.pop("updatedDate", UNSET)

        version = d.pop("version", UNSET)

        rest_user_reaction_comment = cls(
            anchor=anchor,
            anchored=anchored,
            author=author,
            comments=comments,
            created_date=created_date,
            html=html,
            id=id,
            parent=parent,
            pending=pending,
            properties=properties,
            reply=reply,
            resolved_date=resolved_date,
            resolver=resolver,
            severity=severity,
            state=state,
            text=text,
            thread_resolved=thread_resolved,
            thread_resolved_date=thread_resolved_date,
            thread_resolver=thread_resolver,
            updated_date=updated_date,
            version=version,
        )

        rest_user_reaction_comment.additional_properties = d
        return rest_user_reaction_comment

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
