from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.issue_kind import IssueKind
from ..models.issue_priority import IssuePriority
from ..models.issue_state import IssueState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.component import Component
    from ..models.issue_content import IssueContent
    from ..models.issue_links import IssueLinks
    from ..models.milestone import Milestone
    from ..models.repository import Repository
    from ..models.version import Version


T = TypeVar("T", bound="Issue")


@_attrs_define
class Issue:
    type_: str
    links: IssueLinks | Unset = UNSET
    id: int | Unset = UNSET
    repository: Repository | Unset = UNSET
    title: str | Unset = UNSET
    reporter: Account | Unset = UNSET
    assignee: Account | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    edited_on: datetime.datetime | Unset = UNSET
    state: IssueState | Unset = UNSET
    kind: IssueKind | Unset = UNSET
    priority: IssuePriority | Unset = UNSET
    milestone: Milestone | Unset = UNSET
    version: Version | Unset = UNSET
    component: Component | Unset = UNSET
    votes: int | Unset = UNSET
    content: IssueContent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        id = self.id

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        title = self.title

        reporter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reporter, Unset):
            reporter = self.reporter.to_dict()

        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        edited_on: str | Unset = UNSET
        if not isinstance(self.edited_on, Unset):
            edited_on = self.edited_on.isoformat()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        milestone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.milestone, Unset):
            milestone = self.milestone.to_dict()

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.to_dict()

        votes = self.votes

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if id is not UNSET:
            field_dict["id"] = id
        if repository is not UNSET:
            field_dict["repository"] = repository
        if title is not UNSET:
            field_dict["title"] = title
        if reporter is not UNSET:
            field_dict["reporter"] = reporter
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if edited_on is not UNSET:
            field_dict["edited_on"] = edited_on
        if state is not UNSET:
            field_dict["state"] = state
        if kind is not UNSET:
            field_dict["kind"] = kind
        if priority is not UNSET:
            field_dict["priority"] = priority
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if version is not UNSET:
            field_dict["version"] = version
        if component is not UNSET:
            field_dict["component"] = component
        if votes is not UNSET:
            field_dict["votes"] = votes
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.component import Component
        from ..models.issue_content import IssueContent
        from ..models.issue_links import IssueLinks
        from ..models.milestone import Milestone
        from ..models.repository import Repository
        from ..models.version import Version

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: IssueLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = IssueLinks.from_dict(_links)

        id = d.pop("id", UNSET)

        _repository = d.pop("repository", UNSET)
        repository: Repository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        title = d.pop("title", UNSET)

        _reporter = d.pop("reporter", UNSET)
        reporter: Account | Unset
        if isinstance(_reporter, Unset):
            reporter = UNSET
        else:
            reporter = Account.from_dict(_reporter)

        _assignee = d.pop("assignee", UNSET)
        assignee: Account | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = Account.from_dict(_assignee)

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

        _edited_on = d.pop("edited_on", UNSET)
        edited_on: datetime.datetime | Unset
        if isinstance(_edited_on, Unset):
            edited_on = UNSET
        else:
            edited_on = isoparse(_edited_on)

        _state = d.pop("state", UNSET)
        state: IssueState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = IssueState(_state)

        _kind = d.pop("kind", UNSET)
        kind: IssueKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = IssueKind(_kind)

        _priority = d.pop("priority", UNSET)
        priority: IssuePriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = IssuePriority(_priority)

        _milestone = d.pop("milestone", UNSET)
        milestone: Milestone | Unset
        if isinstance(_milestone, Unset):
            milestone = UNSET
        else:
            milestone = Milestone.from_dict(_milestone)

        _version = d.pop("version", UNSET)
        version: Version | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = Version.from_dict(_version)

        _component = d.pop("component", UNSET)
        component: Component | Unset
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = Component.from_dict(_component)

        votes = d.pop("votes", UNSET)

        _content = d.pop("content", UNSET)
        content: IssueContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = IssueContent.from_dict(_content)

        issue = cls(
            type_=type_,
            links=links,
            id=id,
            repository=repository,
            title=title,
            reporter=reporter,
            assignee=assignee,
            created_on=created_on,
            updated_on=updated_on,
            edited_on=edited_on,
            state=state,
            kind=kind,
            priority=priority,
            milestone=milestone,
            version=version,
            component=component,
            votes=votes,
            content=content,
        )

        issue.additional_properties = d
        return issue

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
