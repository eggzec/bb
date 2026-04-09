from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.hook_event_event import HookEventEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="HookEvent")


@_attrs_define
class HookEvent:
    """An event, associated with a resource or subject type."""

    event: HookEventEvent | Unset = UNSET
    """ The event identifier. """
    category: str | Unset = UNSET
    """ The category this event belongs to. """
    label: str | Unset = UNSET
    """ Summary of the webhook event type. """
    description: str | Unset = UNSET
    """ More detailed description of the webhook event type. """

    def to_dict(self) -> dict[str, Any]:
        event: str | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value

        category = self.category

        label = self.label

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if category is not UNSET:
            field_dict["category"] = category
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _event = d.pop("event", UNSET)
        event: HookEventEvent | Unset
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = HookEventEvent(_event)

        category = d.pop("category", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        hook_event = cls(
            event=event,
            category=category,
            label=label,
            description=description,
        )

        return hook_event
