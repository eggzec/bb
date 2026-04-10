from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_rejected_ref_state import RestRejectedRefState
from ..models.rest_rejected_ref_type import RestRejectedRefType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestRejectedRef")


@_attrs_define
class RestRejectedRef:
    display_id: str | Unset = UNSET
    id: str | Unset = UNSET
    state: RestRejectedRefState | Unset = UNSET
    tag: bool | Unset = UNSET
    type_: RestRejectedRefType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_id = self.display_id

        id = self.id

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        tag = self.tag

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_id is not UNSET:
            field_dict["displayId"] = display_id
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if tag is not UNSET:
            field_dict["tag"] = tag
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_id = d.pop("displayId", UNSET)

        id = d.pop("id", UNSET)

        _state = d.pop("state", UNSET)
        state: RestRejectedRefState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestRejectedRefState(_state)

        tag = d.pop("tag", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RestRejectedRefType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestRejectedRefType(_type_)

        rest_rejected_ref = cls(
            display_id=display_id,
            id=id,
            state=state,
            tag=tag,
            type_=type_,
        )

        rest_rejected_ref.additional_properties = d
        return rest_rejected_ref

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
