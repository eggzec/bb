from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRepositoryLockOwner")


@_attrs_define
class RestRepositoryLockOwner:
    external_repository_id: str | Unset = UNSET
    """ The repository ID for which the lock is held """
    lock_acquire_time: datetime.datetime | Unset = UNSET
    """ The time at which lock was last acquired """
    node_id: str | Unset = UNSET
    """ The ID of the mirror node on which the lock is being held """
    request_id: str | Unset = UNSET
    """ The unique ID of the request for which the lock is being held """
    thread_name: str | Unset = UNSET
    """ Name of the thread that is holding the lock """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_repository_id = self.external_repository_id

        lock_acquire_time: str | Unset = UNSET
        if not isinstance(self.lock_acquire_time, Unset):
            lock_acquire_time = self.lock_acquire_time.isoformat()

        node_id = self.node_id

        request_id = self.request_id

        thread_name = self.thread_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_repository_id is not UNSET:
            field_dict["externalRepositoryId"] = external_repository_id
        if lock_acquire_time is not UNSET:
            field_dict["lockAcquireTime"] = lock_acquire_time
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if thread_name is not UNSET:
            field_dict["threadName"] = thread_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_repository_id = d.pop("externalRepositoryId", UNSET)

        _lock_acquire_time = d.pop("lockAcquireTime", UNSET)
        lock_acquire_time: datetime.datetime | Unset
        if isinstance(_lock_acquire_time, Unset):
            lock_acquire_time = UNSET
        else:
            lock_acquire_time = isoparse(_lock_acquire_time)

        node_id = d.pop("nodeId", UNSET)

        request_id = d.pop("requestId", UNSET)

        thread_name = d.pop("threadName", UNSET)

        rest_repository_lock_owner = cls(
            external_repository_id=external_repository_id,
            lock_acquire_time=lock_acquire_time,
            node_id=node_id,
            request_id=request_id,
            thread_name=thread_name,
        )

        rest_repository_lock_owner.additional_properties = d
        return rest_repository_lock_owner

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
