from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.author import Author
    from ..models.base_commit import BaseCommit
    from ..models.base_commit_summary import BaseCommitSummary
    from ..models.committer import Committer
    from ..models.snippet import Snippet
    from ..models.snippet_commit_links import SnippetCommitLinks


T = TypeVar("T", bound="SnippetCommit")


@_attrs_define
class SnippetCommit:
    type_: str
    hash_: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    author: Author | Unset = UNSET
    committer: Committer | Unset = UNSET
    message: str | Unset = UNSET
    summary: BaseCommitSummary | Unset = UNSET
    parents: list[BaseCommit] | Unset = UNSET
    links: SnippetCommitLinks | Unset = UNSET
    snippet: Snippet | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        hash_ = self.hash_

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        committer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        message = self.message

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        parents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parents, Unset):
            parents = []
            for parents_item_data in self.parents:
                parents_item = parents_item_data.to_dict()
                parents.append(parents_item)

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        snippet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snippet, Unset):
            snippet = self.snippet.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if date is not UNSET:
            field_dict["date"] = date
        if author is not UNSET:
            field_dict["author"] = author
        if committer is not UNSET:
            field_dict["committer"] = committer
        if message is not UNSET:
            field_dict["message"] = message
        if summary is not UNSET:
            field_dict["summary"] = summary
        if parents is not UNSET:
            field_dict["parents"] = parents
        if links is not UNSET:
            field_dict["links"] = links
        if snippet is not UNSET:
            field_dict["snippet"] = snippet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.author import Author
        from ..models.base_commit import BaseCommit
        from ..models.base_commit_summary import BaseCommitSummary
        from ..models.committer import Committer
        from ..models.snippet import Snippet
        from ..models.snippet_commit_links import SnippetCommitLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        hash_ = d.pop("hash", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _author = d.pop("author", UNSET)
        author: Author | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = Author.from_dict(_author)

        _committer = d.pop("committer", UNSET)
        committer: Committer | Unset
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = Committer.from_dict(_committer)

        message = d.pop("message", UNSET)

        _summary = d.pop("summary", UNSET)
        summary: BaseCommitSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = BaseCommitSummary.from_dict(_summary)

        _parents = d.pop("parents", UNSET)
        parents: list[BaseCommit] | Unset = UNSET
        if _parents is not UNSET:
            parents = []
            for parents_item_data in _parents:
                parents_item = BaseCommit.from_dict(parents_item_data)

                parents.append(parents_item)

        _links = d.pop("links", UNSET)
        links: SnippetCommitLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SnippetCommitLinks.from_dict(_links)

        _snippet = d.pop("snippet", UNSET)
        snippet: Snippet | Unset
        if isinstance(_snippet, Unset):
            snippet = UNSET
        else:
            snippet = Snippet.from_dict(_snippet)

        snippet_commit = cls(
            type_=type_,
            hash_=hash_,
            date=date,
            author=author,
            committer=committer,
            message=message,
            summary=summary,
            parents=parents,
            links=links,
            snippet=snippet,
        )

        snippet_commit.additional_properties = d
        return snippet_commit

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
