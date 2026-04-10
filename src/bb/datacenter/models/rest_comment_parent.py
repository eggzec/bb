from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_comment import RestComment
    from ..models.rest_comment_parent_anchor import RestCommentParentAnchor
    from ..models.rest_comment_parent_author import RestCommentParentAuthor
    from ..models.rest_comment_parent_properties import RestCommentParentProperties
    from ..models.rest_comment_parent_resolver import RestCommentParentResolver
    from ..models.rest_comment_parent_thread_resolver import RestCommentParentThreadResolver


T = TypeVar("T", bound="RestCommentParent")


@_attrs_define
class RestCommentParent:
    anchor: RestCommentParentAnchor | Unset = UNSET
    anchored: bool | Unset = UNSET
    author: RestCommentParentAuthor | Unset = UNSET
    comments: list[RestComment] | Unset = UNSET
    created_date: int | Unset = UNSET
    html: str | Unset = UNSET
    id: int | Unset = UNSET
    pending: bool | Unset = UNSET
    properties: RestCommentParentProperties | Unset = UNSET
    reply: bool | Unset = UNSET
    resolved_date: int | Unset = UNSET
    resolver: RestCommentParentResolver | Unset = UNSET
    severity: str | Unset = UNSET
    state: str | Unset = UNSET
    text: str | Unset = UNSET
    thread_resolved: bool | Unset = UNSET
    """ Indicates if this comment thread has been marked as resolved or not """
    thread_resolved_date: int | Unset = UNSET
    thread_resolver: RestCommentParentThreadResolver | Unset = UNSET
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
        from ..models.rest_comment_parent_anchor import RestCommentParentAnchor
        from ..models.rest_comment_parent_author import RestCommentParentAuthor
        from ..models.rest_comment_parent_properties import RestCommentParentProperties
        from ..models.rest_comment_parent_resolver import RestCommentParentResolver
        from ..models.rest_comment_parent_thread_resolver import RestCommentParentThreadResolver

        d = dict(src_dict)
        _anchor = d.pop("anchor", UNSET)
        anchor: RestCommentParentAnchor | Unset
        if isinstance(_anchor, Unset):
            anchor = UNSET
        else:
            anchor = RestCommentParentAnchor.from_dict(_anchor)

        anchored = d.pop("anchored", UNSET)

        _author = d.pop("author", UNSET)
        author: RestCommentParentAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = RestCommentParentAuthor.from_dict(_author)

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

        pending = d.pop("pending", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: RestCommentParentProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = RestCommentParentProperties.from_dict(_properties)

        reply = d.pop("reply", UNSET)

        resolved_date = d.pop("resolvedDate", UNSET)

        _resolver = d.pop("resolver", UNSET)
        resolver: RestCommentParentResolver | Unset
        if isinstance(_resolver, Unset):
            resolver = UNSET
        else:
            resolver = RestCommentParentResolver.from_dict(_resolver)

        severity = d.pop("severity", UNSET)

        state = d.pop("state", UNSET)

        text = d.pop("text", UNSET)

        thread_resolved = d.pop("threadResolved", UNSET)

        thread_resolved_date = d.pop("threadResolvedDate", UNSET)

        _thread_resolver = d.pop("threadResolver", UNSET)
        thread_resolver: RestCommentParentThreadResolver | Unset
        if isinstance(_thread_resolver, Unset):
            thread_resolver = UNSET
        else:
            thread_resolver = RestCommentParentThreadResolver.from_dict(_thread_resolver)

        updated_date = d.pop("updatedDate", UNSET)

        version = d.pop("version", UNSET)

        rest_comment_parent = cls(
            anchor=anchor,
            anchored=anchored,
            author=author,
            comments=comments,
            created_date=created_date,
            html=html,
            id=id,
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

        rest_comment_parent.additional_properties = d
        return rest_comment_parent

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
