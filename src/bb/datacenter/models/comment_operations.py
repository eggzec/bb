from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentOperations")


@_attrs_define
class CommentOperations:
    deletable: bool | Unset = UNSET
    editable: bool | Unset = UNSET
    transitionable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deletable = self.deletable

        editable = self.editable

        transitionable = self.transitionable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deletable is not UNSET:
            field_dict["deletable"] = deletable
        if editable is not UNSET:
            field_dict["editable"] = editable
        if transitionable is not UNSET:
            field_dict["transitionable"] = transitionable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deletable = d.pop("deletable", UNSET)

        editable = d.pop("editable", UNSET)

        transitionable = d.pop("transitionable", UNSET)

        comment_operations = cls(
            deletable=deletable,
            editable=editable,
            transitionable=transitionable,
        )

        comment_operations.additional_properties = d
        return comment_operations

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
