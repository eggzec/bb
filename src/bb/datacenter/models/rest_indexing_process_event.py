from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_indexing_process_event_event_type import RestIndexingProcessEventEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_indexing_process_event_event_metadata import RestIndexingProcessEventEventMetadata


T = TypeVar("T", bound="RestIndexingProcessEvent")


@_attrs_define
class RestIndexingProcessEvent:
    """The event that is currently being processed by the indexing worker."""

    event_type: RestIndexingProcessEventEventType
    """ Retrieves the type of the event, indicating the entity (such as project, repository, or user) that triggered
    the indexing operation. """
    retries: int
    """ Retrieves the count of how many times this event has been retried due to previous failures or exceptions.
    """
    event_metadata: RestIndexingProcessEventEventMetadata | Unset = UNSET
    """ Retrieves the metadata associated with the index event. The content of this metadata is variable and depends
    on the event type. It may include identifiers such as repository ID, project ID, or user ID, among other
    relevant details. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        retries = self.retries

        event_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_metadata, Unset):
            event_metadata = self.event_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "retries": retries,
            }
        )
        if event_metadata is not UNSET:
            field_dict["eventMetadata"] = event_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_indexing_process_event_event_metadata import RestIndexingProcessEventEventMetadata

        d = dict(src_dict)
        event_type = RestIndexingProcessEventEventType(d.pop("eventType"))

        retries = d.pop("retries")

        _event_metadata = d.pop("eventMetadata", UNSET)
        event_metadata: RestIndexingProcessEventEventMetadata | Unset
        if isinstance(_event_metadata, Unset):
            event_metadata = UNSET
        else:
            event_metadata = RestIndexingProcessEventEventMetadata.from_dict(_event_metadata)

        rest_indexing_process_event = cls(
            event_type=event_type,
            retries=retries,
            event_metadata=event_metadata,
        )

        rest_indexing_process_event.additional_properties = d
        return rest_indexing_process_event

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
