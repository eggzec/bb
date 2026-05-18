from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.participant_role import ParticipantRole
from ..models.participant_state_type_1 import ParticipantStateType1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="Participant")


@_attrs_define
class Participant:
    type_: str | Unset = UNSET
    user: Account | Unset = UNSET
    role: ParticipantRole | Unset = UNSET
    approved: bool | Unset = UNSET
    state: None | ParticipantStateType1 | Unset = UNSET
    participated_on: datetime.datetime | Unset = UNSET
    """ The ISO8601 timestamp of the participant's action. For approvers, this is the time of their approval. For
    commenters and pull request reviewers who are not approvers, this is the time they last commented, or null if
    they have not commented. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        approved = self.approved

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, ParticipantStateType1):
            state = self.state.value
        else:
            state = self.state

        participated_on: str | Unset = UNSET
        if not isinstance(self.participated_on, Unset):
            participated_on = self.participated_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user is not UNSET:
            field_dict["user"] = user
        if role is not UNSET:
            field_dict["role"] = role
        if approved is not UNSET:
            field_dict["approved"] = approved
        if state is not UNSET:
            field_dict["state"] = state
        if participated_on is not UNSET:
            field_dict["participated_on"] = participated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _user = d.pop("user", UNSET)
        user: Account | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Account.from_dict(_user)

        _role = d.pop("role", UNSET)
        role: ParticipantRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ParticipantRole(_role)

        approved = d.pop("approved", UNSET)

        def _parse_state(data: object) -> None | ParticipantStateType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_1 = ParticipantStateType1(data)

                return state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ParticipantStateType1 | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        _participated_on = d.pop("participated_on", UNSET)
        participated_on: datetime.datetime | Unset
        if isinstance(_participated_on, Unset):
            participated_on = UNSET
        else:
            participated_on = isoparse(_participated_on)

        participant = cls(
            type_=type_,
            user=user,
            role=role,
            approved=approved,
            state=state,
            participated_on=participated_on,
        )

        participant.additional_properties = d
        return participant

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
