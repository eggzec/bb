from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGroupsResponse200")


@_attrs_define
class GetGroupsResponse200:
    is_last_page: bool | Unset = UNSET
    limit: float | Unset = UNSET
    next_page_start: int | Unset = UNSET
    size: float | Unset = UNSET
    start: int | Unset = UNSET
    values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_last_page = self.is_last_page

        limit = self.limit

        next_page_start = self.next_page_start

        size = self.size

        start = self.start

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_last_page is not UNSET:
            field_dict["isLastPage"] = is_last_page
        if limit is not UNSET:
            field_dict["limit"] = limit
        if next_page_start is not UNSET:
            field_dict["nextPageStart"] = next_page_start
        if size is not UNSET:
            field_dict["size"] = size
        if start is not UNSET:
            field_dict["start"] = start
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_last_page = d.pop("isLastPage", UNSET)

        limit = d.pop("limit", UNSET)

        next_page_start = d.pop("nextPageStart", UNSET)

        size = d.pop("size", UNSET)

        start = d.pop("start", UNSET)

        values = cast(list[str], d.pop("values", UNSET))

        get_groups_response_200 = cls(
            is_last_page=is_last_page,
            limit=limit,
            next_page_start=next_page_start,
            size=size,
            start=start,
            values=values,
        )

        get_groups_response_200.additional_properties = d
        return get_groups_response_200

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
