from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rest_indexing_process_event import RestIndexingProcessEvent


T = TypeVar("T", bound="RestIndexingProcess")


@_attrs_define
class RestIndexingProcess:
    """A snapshot of the current process being executed by the indexing worker."""

    current_task: str
    """ The current task description that the indexing worker is executing. """
    event: RestIndexingProcessEvent
    """ The event that is currently being processed by the indexing worker. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_task = self.current_task

        event = self.event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currentTask": current_task,
                "event": event,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_indexing_process_event import RestIndexingProcessEvent

        d = dict(src_dict)
        current_task = d.pop("currentTask")

        event = RestIndexingProcessEvent.from_dict(d.pop("event"))

        rest_indexing_process = cls(
            current_task=current_task,
            event=event,
        )

        rest_indexing_process.additional_properties = d
        return rest_indexing_process

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
