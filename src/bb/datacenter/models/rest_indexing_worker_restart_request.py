from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestIndexingWorkerRestartRequest")


@_attrs_define
class RestIndexingWorkerRestartRequest:
    graceful_shutdown: bool | Unset = False
    """ Should the indexing thread terminate immediately """
    wait_for_restart: bool | Unset = False
    """ Should the response wait until the worker has been restarted """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        graceful_shutdown = self.graceful_shutdown

        wait_for_restart = self.wait_for_restart

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if graceful_shutdown is not UNSET:
            field_dict["gracefulShutdown"] = graceful_shutdown
        if wait_for_restart is not UNSET:
            field_dict["waitForRestart"] = wait_for_restart

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        graceful_shutdown = d.pop("gracefulShutdown", UNSET)

        wait_for_restart = d.pop("waitForRestart", UNSET)

        rest_indexing_worker_restart_request = cls(
            graceful_shutdown=graceful_shutdown,
            wait_for_restart=wait_for_restart,
        )

        rest_indexing_worker_restart_request.additional_properties = d
        return rest_indexing_worker_restart_request

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
