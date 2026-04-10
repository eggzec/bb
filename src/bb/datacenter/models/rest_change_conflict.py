from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_change_conflict_our_change import RestChangeConflictOurChange
    from ..models.rest_change_conflict_their_change import RestChangeConflictTheirChange


T = TypeVar("T", bound="RestChangeConflict")


@_attrs_define
class RestChangeConflict:
    our_change: RestChangeConflictOurChange | Unset = UNSET
    their_change: RestChangeConflictTheirChange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        our_change: dict[str, Any] | Unset = UNSET
        if not isinstance(self.our_change, Unset):
            our_change = self.our_change.to_dict()

        their_change: dict[str, Any] | Unset = UNSET
        if not isinstance(self.their_change, Unset):
            their_change = self.their_change.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if our_change is not UNSET:
            field_dict["ourChange"] = our_change
        if their_change is not UNSET:
            field_dict["theirChange"] = their_change

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_change_conflict_our_change import RestChangeConflictOurChange
        from ..models.rest_change_conflict_their_change import RestChangeConflictTheirChange

        d = dict(src_dict)
        _our_change = d.pop("ourChange", UNSET)
        our_change: RestChangeConflictOurChange | Unset
        if isinstance(_our_change, Unset):
            our_change = UNSET
        else:
            our_change = RestChangeConflictOurChange.from_dict(_our_change)

        _their_change = d.pop("theirChange", UNSET)
        their_change: RestChangeConflictTheirChange | Unset
        if isinstance(_their_change, Unset):
            their_change = UNSET
        else:
            their_change = RestChangeConflictTheirChange.from_dict(_their_change)

        rest_change_conflict = cls(
            our_change=our_change,
            their_change=their_change,
        )

        rest_change_conflict.additional_properties = d
        return rest_change_conflict

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
