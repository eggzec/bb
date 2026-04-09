from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.task_state import TaskState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.task_content import TaskContent


T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    """A task object."""

    created_on: datetime.datetime
    updated_on: datetime.datetime
    state: TaskState
    content: TaskContent
    creator: Account
    id: int | Unset = UNSET
    pending: bool | Unset = UNSET
    resolved_on: datetime.datetime | Unset = UNSET
    """ The ISO8601 timestamp for when the task was resolved. """
    resolved_by: Account | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_on = self.created_on.isoformat()

        updated_on = self.updated_on.isoformat()

        state = self.state.value

        content = self.content.to_dict()

        creator = self.creator.to_dict()

        id = self.id

        pending = self.pending

        resolved_on: str | Unset = UNSET
        if not isinstance(self.resolved_on, Unset):
            resolved_on = self.resolved_on.isoformat()

        resolved_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolved_by, Unset):
            resolved_by = self.resolved_by.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_on": created_on,
                "updated_on": updated_on,
                "state": state,
                "content": content,
                "creator": creator,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if pending is not UNSET:
            field_dict["pending"] = pending
        if resolved_on is not UNSET:
            field_dict["resolved_on"] = resolved_on
        if resolved_by is not UNSET:
            field_dict["resolved_by"] = resolved_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.task_content import TaskContent

        d = dict(src_dict)
        created_on = isoparse(d.pop("created_on"))

        updated_on = isoparse(d.pop("updated_on"))

        state = TaskState(d.pop("state"))

        content = TaskContent.from_dict(d.pop("content"))

        creator = Account.from_dict(d.pop("creator"))

        id = d.pop("id", UNSET)

        pending = d.pop("pending", UNSET)

        _resolved_on = d.pop("resolved_on", UNSET)
        resolved_on: datetime.datetime | Unset
        if isinstance(_resolved_on, Unset):
            resolved_on = UNSET
        else:
            resolved_on = isoparse(_resolved_on)

        _resolved_by = d.pop("resolved_by", UNSET)
        resolved_by: Account | Unset
        if isinstance(_resolved_by, Unset):
            resolved_by = UNSET
        else:
            resolved_by = Account.from_dict(_resolved_by)

        task = cls(
            created_on=created_on,
            updated_on=updated_on,
            state=state,
            content=content,
            creator=creator,
            id=id,
            pending=pending,
            resolved_on=resolved_on,
            resolved_by=resolved_by,
        )

        return task
