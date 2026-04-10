from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_ref_sync_status_ahead_refs import RestRefSyncStatusAheadRefs
    from ..models.rest_ref_sync_status_diverged_refs import RestRefSyncStatusDivergedRefs
    from ..models.rest_ref_sync_status_orphaned_refs import RestRefSyncStatusOrphanedRefs


T = TypeVar("T", bound="RestRefSyncStatus")


@_attrs_define
class RestRefSyncStatus:
    ahead_refs: RestRefSyncStatusAheadRefs | Unset = UNSET
    available: bool | Unset = UNSET
    diverged_refs: RestRefSyncStatusDivergedRefs | Unset = UNSET
    enabled: bool | Unset = UNSET
    last_sync: float | Unset = UNSET
    orphaned_refs: RestRefSyncStatusOrphanedRefs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ahead_refs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ahead_refs, Unset):
            ahead_refs = self.ahead_refs.to_dict()

        available = self.available

        diverged_refs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.diverged_refs, Unset):
            diverged_refs = self.diverged_refs.to_dict()

        enabled = self.enabled

        last_sync = self.last_sync

        orphaned_refs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.orphaned_refs, Unset):
            orphaned_refs = self.orphaned_refs.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ahead_refs is not UNSET:
            field_dict["aheadRefs"] = ahead_refs
        if available is not UNSET:
            field_dict["available"] = available
        if diverged_refs is not UNSET:
            field_dict["divergedRefs"] = diverged_refs
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if last_sync is not UNSET:
            field_dict["lastSync"] = last_sync
        if orphaned_refs is not UNSET:
            field_dict["orphanedRefs"] = orphaned_refs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_ref_sync_status_ahead_refs import RestRefSyncStatusAheadRefs
        from ..models.rest_ref_sync_status_diverged_refs import RestRefSyncStatusDivergedRefs
        from ..models.rest_ref_sync_status_orphaned_refs import RestRefSyncStatusOrphanedRefs

        d = dict(src_dict)
        _ahead_refs = d.pop("aheadRefs", UNSET)
        ahead_refs: RestRefSyncStatusAheadRefs | Unset
        if isinstance(_ahead_refs, Unset):
            ahead_refs = UNSET
        else:
            ahead_refs = RestRefSyncStatusAheadRefs.from_dict(_ahead_refs)

        available = d.pop("available", UNSET)

        _diverged_refs = d.pop("divergedRefs", UNSET)
        diverged_refs: RestRefSyncStatusDivergedRefs | Unset
        if isinstance(_diverged_refs, Unset):
            diverged_refs = UNSET
        else:
            diverged_refs = RestRefSyncStatusDivergedRefs.from_dict(_diverged_refs)

        enabled = d.pop("enabled", UNSET)

        last_sync = d.pop("lastSync", UNSET)

        _orphaned_refs = d.pop("orphanedRefs", UNSET)
        orphaned_refs: RestRefSyncStatusOrphanedRefs | Unset
        if isinstance(_orphaned_refs, Unset):
            orphaned_refs = UNSET
        else:
            orphaned_refs = RestRefSyncStatusOrphanedRefs.from_dict(_orphaned_refs)

        rest_ref_sync_status = cls(
            ahead_refs=ahead_refs,
            available=available,
            diverged_refs=diverged_refs,
            enabled=enabled,
            last_sync=last_sync,
            orphaned_refs=orphaned_refs,
        )

        rest_ref_sync_status.additional_properties = d
        return rest_ref_sync_status

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
