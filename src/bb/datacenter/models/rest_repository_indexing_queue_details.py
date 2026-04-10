from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRepositoryIndexingQueueDetails")


@_attrs_define
class RestRepositoryIndexingQueueDetails:
    captured_at: int | Unset = UNSET
    """ The timestamp indicating when the current queue details were captured. """
    node_id: str | Unset = UNSET
    """ The ID of the node associated with the indexing queue. """
    queued: bool | Unset = UNSET
    """ Indicates whether the repository is currently queued for indexing. """
    queued_at: int | Unset = UNSET
    """ Gets the time at which the repository was added to the indexing queue. If the repository is not present in
    the queue, this will be empty. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        captured_at = self.captured_at

        node_id = self.node_id

        queued = self.queued

        queued_at = self.queued_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if captured_at is not UNSET:
            field_dict["capturedAt"] = captured_at
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if queued is not UNSET:
            field_dict["queued"] = queued
        if queued_at is not UNSET:
            field_dict["queuedAt"] = queued_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        captured_at = d.pop("capturedAt", UNSET)

        node_id = d.pop("nodeId", UNSET)

        queued = d.pop("queued", UNSET)

        queued_at = d.pop("queuedAt", UNSET)

        rest_repository_indexing_queue_details = cls(
            captured_at=captured_at,
            node_id=node_id,
            queued=queued,
            queued_at=queued_at,
        )

        rest_repository_indexing_queue_details.additional_properties = d
        return rest_repository_indexing_queue_details

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
