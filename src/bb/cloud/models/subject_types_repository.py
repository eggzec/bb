from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="SubjectTypesRepository")


@_attrs_define
class SubjectTypesRepository:
    events: Link | Unset = UNSET
    """ A link to a resource related to this object. """

    def to_dict(self) -> dict[str, Any]:
        events: dict[str, Any] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link

        d = dict(src_dict)
        _events = d.pop("events", UNSET)
        events: Link | Unset
        if isinstance(_events, Unset):
            events = UNSET
        else:
            events = Link.from_dict(_events)

        subject_types_repository = cls(
            events=events,
        )

        return subject_types_repository
