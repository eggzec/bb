from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_ref_sync_status_orphaned_refs_state import RestRefSyncStatusOrphanedRefsState
from ..models.rest_ref_sync_status_orphaned_refs_type import RestRefSyncStatusOrphanedRefsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRefSyncStatusOrphanedRefs")


@_attrs_define
class RestRefSyncStatusOrphanedRefs:
    display_id: str
    id: str
    type_: RestRefSyncStatusOrphanedRefsType
    state: RestRefSyncStatusOrphanedRefsState | Unset = UNSET
    tag: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_id = self.display_id

        id = self.id

        type_ = self.type_.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayId": display_id,
                "id": id,
                "type": type_,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_id = d.pop("displayId")

        id = d.pop("id")

        type_ = RestRefSyncStatusOrphanedRefsType(d.pop("type"))

        _state = d.pop("state", UNSET)
        state: RestRefSyncStatusOrphanedRefsState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestRefSyncStatusOrphanedRefsState(_state)

        tag = d.pop("tag", UNSET)

        rest_ref_sync_status_orphaned_refs = cls(
            display_id=display_id,
            id=id,
            type_=type_,
            state=state,
            tag=tag,
        )

        rest_ref_sync_status_orphaned_refs.additional_properties = d
        return rest_ref_sync_status_orphaned_refs

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
