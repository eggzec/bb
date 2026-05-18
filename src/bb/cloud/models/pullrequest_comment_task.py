from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_state import TaskState
from ..models.task_type import TaskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.comment import Comment
    from ..models.task_content import TaskContent
    from ..models.task_links import TaskLinks


T = TypeVar("T", bound="PullrequestCommentTask")


@_attrs_define
class PullrequestCommentTask:
    created_on: datetime.datetime
    updated_on: datetime.datetime
    state: TaskState
    content: TaskContent
    creator: Account
    id: int | Unset = UNSET
    pending: bool | Unset = UNSET
    resolved_on: datetime.datetime | None | Unset = UNSET
    """ The ISO8601 timestamp for when the task was resolved. """
    resolved_by: Account | None | Unset = UNSET
    links: TaskLinks | Unset = UNSET
    """ Navigation links for this task """
    type_: TaskType | Unset = UNSET
    """ The type discriminator for this object. """
    comment: Comment | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.account import Account

        created_on = self.created_on.isoformat()

        updated_on = self.updated_on.isoformat()

        state = self.state.value

        content = self.content.to_dict()

        creator = self.creator.to_dict()

        id = self.id

        pending = self.pending

        resolved_on: None | str | Unset
        if isinstance(self.resolved_on, Unset):
            resolved_on = UNSET
        elif isinstance(self.resolved_on, datetime.datetime):
            resolved_on = self.resolved_on.isoformat()
        else:
            resolved_on = self.resolved_on

        resolved_by: dict[str, Any] | None | Unset
        if isinstance(self.resolved_by, Unset):
            resolved_by = UNSET
        elif isinstance(self.resolved_by, Account):
            resolved_by = self.resolved_by.to_dict()
        else:
            resolved_by = self.resolved_by

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if links is not UNSET:
            field_dict["links"] = links
        if type_ is not UNSET:
            field_dict["type"] = type_
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.comment import Comment
        from ..models.task_content import TaskContent
        from ..models.task_links import TaskLinks

        d = dict(src_dict)
        created_on = isoparse(d.pop("created_on"))

        updated_on = isoparse(d.pop("updated_on"))

        state = TaskState(d.pop("state"))

        content = TaskContent.from_dict(d.pop("content"))

        creator = Account.from_dict(d.pop("creator"))

        id = d.pop("id", UNSET)

        pending = d.pop("pending", UNSET)

        def _parse_resolved_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_on_type_0 = isoparse(data)

                return resolved_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_on = _parse_resolved_on(d.pop("resolved_on", UNSET))

        def _parse_resolved_by(data: object) -> Account | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolved_by_type_0 = Account.from_dict(data)

                return resolved_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Account | None | Unset, data)

        resolved_by = _parse_resolved_by(d.pop("resolved_by", UNSET))

        _links = d.pop("links", UNSET)
        links: TaskLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TaskLinks.from_dict(_links)

        _type_ = d.pop("type", UNSET)
        type_: TaskType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TaskType(_type_)

        _comment = d.pop("comment", UNSET)
        comment: Comment | Unset
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = Comment.from_dict(_comment)

        pullrequest_comment_task = cls(
            created_on=created_on,
            updated_on=updated_on,
            state=state,
            content=content,
            creator=creator,
            id=id,
            pending=pending,
            resolved_on=resolved_on,
            resolved_by=resolved_by,
            links=links,
            type_=type_,
            comment=comment,
        )

        pullrequest_comment_task.additional_properties = d
        return pullrequest_comment_task

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
