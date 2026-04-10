from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_aggregate_reject_counter_user import RestAggregateRejectCounterUser


T = TypeVar("T", bound="RestAggregateRejectCounter")


@_attrs_define
class RestAggregateRejectCounter:
    last_reject_time: float | Unset = UNSET
    reject_count: int | Unset = UNSET
    user: RestAggregateRejectCounterUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_reject_time = self.last_reject_time

        reject_count = self.reject_count

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_reject_time is not UNSET:
            field_dict["lastRejectTime"] = last_reject_time
        if reject_count is not UNSET:
            field_dict["rejectCount"] = reject_count
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_aggregate_reject_counter_user import RestAggregateRejectCounterUser

        d = dict(src_dict)
        last_reject_time = d.pop("lastRejectTime", UNSET)

        reject_count = d.pop("rejectCount", UNSET)

        _user = d.pop("user", UNSET)
        user: RestAggregateRejectCounterUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RestAggregateRejectCounterUser.from_dict(_user)

        rest_aggregate_reject_counter = cls(
            last_reject_time=last_reject_time,
            reject_count=reject_count,
            user=user,
        )

        rest_aggregate_reject_counter.additional_properties = d
        return rest_aggregate_reject_counter

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
