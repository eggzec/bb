from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="IssueLinks")


@_attrs_define
class IssueLinks:
    self_: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    html: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    comments: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    attachments: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    watch: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    vote: Link | Unset = UNSET
    """ A link to a resource related to this object. """

    def to_dict(self) -> dict[str, Any]:
        self_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        html: dict[str, Any] | Unset = UNSET
        if not isinstance(self.html, Unset):
            html = self.html.to_dict()

        comments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = self.comments.to_dict()

        attachments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        watch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.watch, Unset):
            watch = self.watch.to_dict()

        vote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vote, Unset):
            vote = self.vote.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if html is not UNSET:
            field_dict["html"] = html
        if comments is not UNSET:
            field_dict["comments"] = comments
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if watch is not UNSET:
            field_dict["watch"] = watch
        if vote is not UNSET:
            field_dict["vote"] = vote

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Link | Unset
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = Link.from_dict(_self_)

        _html = d.pop("html", UNSET)
        html: Link | Unset
        if isinstance(_html, Unset):
            html = UNSET
        else:
            html = Link.from_dict(_html)

        _comments = d.pop("comments", UNSET)
        comments: Link | Unset
        if isinstance(_comments, Unset):
            comments = UNSET
        else:
            comments = Link.from_dict(_comments)

        _attachments = d.pop("attachments", UNSET)
        attachments: Link | Unset
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = Link.from_dict(_attachments)

        _watch = d.pop("watch", UNSET)
        watch: Link | Unset
        if isinstance(_watch, Unset):
            watch = UNSET
        else:
            watch = Link.from_dict(_watch)

        _vote = d.pop("vote", UNSET)
        vote: Link | Unset
        if isinstance(_vote, Unset):
            vote = UNSET
        else:
            vote = Link.from_dict(_vote)

        issue_links = cls(
            self_=self_,
            html=html,
            comments=comments,
            attachments=attachments,
            watch=watch,
            vote=vote,
        )

        return issue_links
