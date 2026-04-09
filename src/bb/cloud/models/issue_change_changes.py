from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_change_changes_assignee import IssueChangeChangesAssignee
    from ..models.issue_change_changes_component import IssueChangeChangesComponent
    from ..models.issue_change_changes_content import IssueChangeChangesContent
    from ..models.issue_change_changes_kind import IssueChangeChangesKind
    from ..models.issue_change_changes_milestone import IssueChangeChangesMilestone
    from ..models.issue_change_changes_priority import IssueChangeChangesPriority
    from ..models.issue_change_changes_state import IssueChangeChangesState
    from ..models.issue_change_changes_title import IssueChangeChangesTitle
    from ..models.issue_change_changes_version import IssueChangeChangesVersion


T = TypeVar("T", bound="IssueChangeChanges")


@_attrs_define
class IssueChangeChanges:
    assignee: IssueChangeChangesAssignee | Unset = UNSET
    state: IssueChangeChangesState | Unset = UNSET
    title: IssueChangeChangesTitle | Unset = UNSET
    kind: IssueChangeChangesKind | Unset = UNSET
    milestone: IssueChangeChangesMilestone | Unset = UNSET
    component: IssueChangeChangesComponent | Unset = UNSET
    priority: IssueChangeChangesPriority | Unset = UNSET
    version: IssueChangeChangesVersion | Unset = UNSET
    content: IssueChangeChangesContent | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        title: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        kind: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.to_dict()

        milestone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.milestone, Unset):
            milestone = self.milestone.to_dict()

        component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.to_dict()

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        version: dict[str, Any] | Unset = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if state is not UNSET:
            field_dict["state"] = state
        if title is not UNSET:
            field_dict["title"] = title
        if kind is not UNSET:
            field_dict["kind"] = kind
        if milestone is not UNSET:
            field_dict["milestone"] = milestone
        if component is not UNSET:
            field_dict["component"] = component
        if priority is not UNSET:
            field_dict["priority"] = priority
        if version is not UNSET:
            field_dict["version"] = version
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_change_changes_assignee import IssueChangeChangesAssignee
        from ..models.issue_change_changes_component import IssueChangeChangesComponent
        from ..models.issue_change_changes_content import IssueChangeChangesContent
        from ..models.issue_change_changes_kind import IssueChangeChangesKind
        from ..models.issue_change_changes_milestone import IssueChangeChangesMilestone
        from ..models.issue_change_changes_priority import IssueChangeChangesPriority
        from ..models.issue_change_changes_state import IssueChangeChangesState
        from ..models.issue_change_changes_title import IssueChangeChangesTitle
        from ..models.issue_change_changes_version import IssueChangeChangesVersion

        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: IssueChangeChangesAssignee | Unset
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = IssueChangeChangesAssignee.from_dict(_assignee)

        _state = d.pop("state", UNSET)
        state: IssueChangeChangesState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = IssueChangeChangesState.from_dict(_state)

        _title = d.pop("title", UNSET)
        title: IssueChangeChangesTitle | Unset
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = IssueChangeChangesTitle.from_dict(_title)

        _kind = d.pop("kind", UNSET)
        kind: IssueChangeChangesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = IssueChangeChangesKind.from_dict(_kind)

        _milestone = d.pop("milestone", UNSET)
        milestone: IssueChangeChangesMilestone | Unset
        if isinstance(_milestone, Unset):
            milestone = UNSET
        else:
            milestone = IssueChangeChangesMilestone.from_dict(_milestone)

        _component = d.pop("component", UNSET)
        component: IssueChangeChangesComponent | Unset
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = IssueChangeChangesComponent.from_dict(_component)

        _priority = d.pop("priority", UNSET)
        priority: IssueChangeChangesPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = IssueChangeChangesPriority.from_dict(_priority)

        _version = d.pop("version", UNSET)
        version: IssueChangeChangesVersion | Unset
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = IssueChangeChangesVersion.from_dict(_version)

        _content = d.pop("content", UNSET)
        content: IssueChangeChangesContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = IssueChangeChangesContent.from_dict(_content)

        issue_change_changes = cls(
            assignee=assignee,
            state=state,
            title=title,
            kind=kind,
            milestone=milestone,
            component=component,
            priority=priority,
            version=version,
            content=content,
        )

        return issue_change_changes
