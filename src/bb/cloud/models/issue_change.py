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
    from ..models.issue import Issue
    from ..models.issue_change_changes import IssueChangeChanges
    from ..models.issue_change_links import IssueChangeLinks
    from ..models.issue_change_message import IssueChangeMessage


T = TypeVar("T", bound="IssueChange")


@_attrs_define
class IssueChange:
    """An issue change."""

    type_: str
    links: IssueChangeLinks | Unset = UNSET
    name: str | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    user: Account | Unset = UNSET
    issue: Issue | Unset = UNSET
    changes: IssueChangeChanges | Unset = UNSET
    message: IssueChangeMessage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.changes, Unset):
            changes = self.changes.to_dict()

        message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if user is not UNSET:
            field_dict["user"] = user
        if issue is not UNSET:
            field_dict["issue"] = issue
        if changes is not UNSET:
            field_dict["changes"] = changes
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.issue import Issue
        from ..models.issue_change_changes import IssueChangeChanges
        from ..models.issue_change_links import IssueChangeLinks
        from ..models.issue_change_message import IssueChangeMessage

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: IssueChangeLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = IssueChangeLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _user = d.pop("user", UNSET)
        user: Account | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Account.from_dict(_user)

        _issue = d.pop("issue", UNSET)
        issue: Issue | Unset
        if isinstance(_issue, Unset):
            issue = UNSET
        else:
            issue = Issue.from_dict(_issue)

        _changes = d.pop("changes", UNSET)
        changes: IssueChangeChanges | Unset
        if isinstance(_changes, Unset):
            changes = UNSET
        else:
            changes = IssueChangeChanges.from_dict(_changes)

        _message = d.pop("message", UNSET)
        message: IssueChangeMessage | Unset
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = IssueChangeMessage.from_dict(_message)

        issue_change = cls(
            type_=type_,
            links=links,
            name=name,
            created_on=created_on,
            user=user,
            issue=issue,
            changes=changes,
            message=message,
        )

        issue_change.additional_properties = d
        return issue_change

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
