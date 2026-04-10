from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_ref_sync_request_action import RestRefSyncRequestAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.context import Context


T = TypeVar("T", bound="RestRefSyncRequest")


@_attrs_define
class RestRefSyncRequest:
    action: RestRefSyncRequestAction | Unset = UNSET
    context: Context | Unset = UNSET
    ref_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        ref_id = self.ref_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if context is not UNSET:
            field_dict["context"] = context
        if ref_id is not UNSET:
            field_dict["refId"] = ref_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context import Context

        d = dict(src_dict)
        _action = d.pop("action", UNSET)
        action: RestRefSyncRequestAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = RestRefSyncRequestAction(_action)

        _context = d.pop("context", UNSET)
        context: Context | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = Context.from_dict(_context)

        ref_id = d.pop("refId", UNSET)

        rest_ref_sync_request = cls(
            action=action,
            context=context,
            ref_id=ref_id,
        )

        rest_ref_sync_request.additional_properties = d
        return rest_ref_sync_request

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
