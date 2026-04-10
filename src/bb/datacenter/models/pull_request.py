from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.pull_request_state import PullRequestState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pull_request_participant import PullRequestParticipant
    from ..models.pull_request_properties import PullRequestProperties
    from ..models.pull_request_ref import PullRequestRef


T = TypeVar("T", bound="PullRequest")


@_attrs_define
class PullRequest:
    author: PullRequestParticipant
    created_date: datetime.datetime
    from_ref: PullRequestRef
    participants: list[PullRequestParticipant]
    properties: PullRequestProperties
    reviewers: list[PullRequestParticipant]
    state: PullRequestState
    title: str
    to_ref: PullRequestRef
    updated_date: datetime.datetime
    closed: bool | Unset = UNSET
    closed_date: datetime.datetime | Unset = UNSET
    cross_repository: bool | Unset = UNSET
    description: str | Unset = UNSET
    draft: bool | Unset = UNSET
    id: int | Unset = UNSET
    locked: bool | Unset = UNSET
    open_: bool | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author.to_dict()

        created_date = self.created_date.isoformat()

        from_ref = self.from_ref.to_dict()

        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()
            participants.append(participants_item)

        properties = self.properties.to_dict()

        reviewers = []
        for reviewers_item_data in self.reviewers:
            reviewers_item = reviewers_item_data.to_dict()
            reviewers.append(reviewers_item)

        state = self.state.value

        title = self.title

        to_ref = self.to_ref.to_dict()

        updated_date = self.updated_date.isoformat()

        closed = self.closed

        closed_date: str | Unset = UNSET
        if not isinstance(self.closed_date, Unset):
            closed_date = self.closed_date.isoformat()

        cross_repository = self.cross_repository

        description = self.description

        draft = self.draft

        id = self.id

        locked = self.locked

        open_ = self.open_

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "createdDate": created_date,
                "fromRef": from_ref,
                "participants": participants,
                "properties": properties,
                "reviewers": reviewers,
                "state": state,
                "title": title,
                "toRef": to_ref,
                "updatedDate": updated_date,
            }
        )
        if closed is not UNSET:
            field_dict["closed"] = closed
        if closed_date is not UNSET:
            field_dict["closedDate"] = closed_date
        if cross_repository is not UNSET:
            field_dict["crossRepository"] = cross_repository
        if description is not UNSET:
            field_dict["description"] = description
        if draft is not UNSET:
            field_dict["draft"] = draft
        if id is not UNSET:
            field_dict["id"] = id
        if locked is not UNSET:
            field_dict["locked"] = locked
        if open_ is not UNSET:
            field_dict["open"] = open_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pull_request_participant import PullRequestParticipant
        from ..models.pull_request_properties import PullRequestProperties
        from ..models.pull_request_ref import PullRequestRef

        d = dict(src_dict)
        author = PullRequestParticipant.from_dict(d.pop("author"))

        created_date = isoparse(d.pop("createdDate"))

        from_ref = PullRequestRef.from_dict(d.pop("fromRef"))

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = PullRequestParticipant.from_dict(participants_item_data)

            participants.append(participants_item)

        properties = PullRequestProperties.from_dict(d.pop("properties"))

        reviewers = []
        _reviewers = d.pop("reviewers")
        for reviewers_item_data in _reviewers:
            reviewers_item = PullRequestParticipant.from_dict(reviewers_item_data)

            reviewers.append(reviewers_item)

        state = PullRequestState(d.pop("state"))

        title = d.pop("title")

        to_ref = PullRequestRef.from_dict(d.pop("toRef"))

        updated_date = isoparse(d.pop("updatedDate"))

        closed = d.pop("closed", UNSET)

        _closed_date = d.pop("closedDate", UNSET)
        closed_date: datetime.datetime | Unset
        if isinstance(_closed_date, Unset):
            closed_date = UNSET
        else:
            closed_date = isoparse(_closed_date)

        cross_repository = d.pop("crossRepository", UNSET)

        description = d.pop("description", UNSET)

        draft = d.pop("draft", UNSET)

        id = d.pop("id", UNSET)

        locked = d.pop("locked", UNSET)

        open_ = d.pop("open", UNSET)

        version = d.pop("version", UNSET)

        pull_request = cls(
            author=author,
            created_date=created_date,
            from_ref=from_ref,
            participants=participants,
            properties=properties,
            reviewers=reviewers,
            state=state,
            title=title,
            to_ref=to_ref,
            updated_date=updated_date,
            closed=closed,
            closed_date=closed_date,
            cross_repository=cross_repository,
            description=description,
            draft=draft,
            id=id,
            locked=locked,
            open_=open_,
            version=version,
        )

        pull_request.additional_properties = d
        return pull_request

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
