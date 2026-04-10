from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_indexing_thread_details_current_process import RestIndexingThreadDetailsCurrentProcess
    from ..models.rest_indexing_thread_details_state import RestIndexingThreadDetailsState


T = TypeVar("T", bound="RestIndexingThreadDetails")


@_attrs_define
class RestIndexingThreadDetails:
    captured_at: int
    """ Returns the timestamp indicating when the current thread details were captured. """
    delayed_queue_size: int
    """ The number of items in the delayed queue. This queue contains retries that have been scheduled with an
    exponential backoff delay. The retries are for operations that previously failed in the main queue. """
    queue_size: int
    """ The number of items currently in the main queue. """
    state: RestIndexingThreadDetailsState
    """ Represents the state of an indexing thread. """
    current_process: RestIndexingThreadDetailsCurrentProcess | Unset = UNSET
    """ A snapshot of the current process being executed by the indexing worker. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        captured_at = self.captured_at

        delayed_queue_size = self.delayed_queue_size

        queue_size = self.queue_size

        state = self.state.to_dict()

        current_process: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_process, Unset):
            current_process = self.current_process.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "capturedAt": captured_at,
                "delayedQueueSize": delayed_queue_size,
                "queueSize": queue_size,
                "state": state,
            }
        )
        if current_process is not UNSET:
            field_dict["currentProcess"] = current_process

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_indexing_thread_details_current_process import RestIndexingThreadDetailsCurrentProcess
        from ..models.rest_indexing_thread_details_state import RestIndexingThreadDetailsState

        d = dict(src_dict)
        captured_at = d.pop("capturedAt")

        delayed_queue_size = d.pop("delayedQueueSize")

        queue_size = d.pop("queueSize")

        state = RestIndexingThreadDetailsState.from_dict(d.pop("state"))

        _current_process = d.pop("currentProcess", UNSET)
        current_process: RestIndexingThreadDetailsCurrentProcess | Unset
        if isinstance(_current_process, Unset):
            current_process = UNSET
        else:
            current_process = RestIndexingThreadDetailsCurrentProcess.from_dict(_current_process)

        rest_indexing_thread_details = cls(
            captured_at=captured_at,
            delayed_queue_size=delayed_queue_size,
            queue_size=queue_size,
            state=state,
            current_process=current_process,
        )

        rest_indexing_thread_details.additional_properties = d
        return rest_indexing_thread_details

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
