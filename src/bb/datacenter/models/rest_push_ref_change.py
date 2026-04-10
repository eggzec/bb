from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_push_ref_change_type import RestPushRefChangeType
from ..models.rest_push_ref_change_updated_type import RestPushRefChangeUpdatedType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_push_ref_change_ref import RestPushRefChangeRef


T = TypeVar("T", bound="RestPushRefChange")


@_attrs_define
class RestPushRefChange:
    from_hash: str | Unset = UNSET
    ref: RestPushRefChangeRef | Unset = UNSET
    ref_id: str | Unset = UNSET
    to_hash: str | Unset = UNSET
    type_: RestPushRefChangeType | Unset = UNSET
    updated_type: RestPushRefChangeUpdatedType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_hash = self.from_hash

        ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ref, Unset):
            ref = self.ref.to_dict()

        ref_id = self.ref_id

        to_hash = self.to_hash

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_type: str | Unset = UNSET
        if not isinstance(self.updated_type, Unset):
            updated_type = self.updated_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_hash is not UNSET:
            field_dict["fromHash"] = from_hash
        if ref is not UNSET:
            field_dict["ref"] = ref
        if ref_id is not UNSET:
            field_dict["refId"] = ref_id
        if to_hash is not UNSET:
            field_dict["toHash"] = to_hash
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_type is not UNSET:
            field_dict["updatedType"] = updated_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_push_ref_change_ref import RestPushRefChangeRef

        d = dict(src_dict)
        from_hash = d.pop("fromHash", UNSET)

        _ref = d.pop("ref", UNSET)
        ref: RestPushRefChangeRef | Unset
        if isinstance(_ref, Unset):
            ref = UNSET
        else:
            ref = RestPushRefChangeRef.from_dict(_ref)

        ref_id = d.pop("refId", UNSET)

        to_hash = d.pop("toHash", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RestPushRefChangeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestPushRefChangeType(_type_)

        _updated_type = d.pop("updatedType", UNSET)
        updated_type: RestPushRefChangeUpdatedType | Unset
        if isinstance(_updated_type, Unset):
            updated_type = UNSET
        else:
            updated_type = RestPushRefChangeUpdatedType(_updated_type)

        rest_push_ref_change = cls(
            from_hash=from_hash,
            ref=ref,
            ref_id=ref_id,
            to_hash=to_hash,
            type_=type_,
            updated_type=updated_type,
        )

        rest_push_ref_change.additional_properties = d
        return rest_push_ref_change

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
