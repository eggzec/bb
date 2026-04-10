from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_option_entity import LoginOptionEntity


T = TypeVar("T", bound="RestPageLoginOptionEntity")


@_attrs_define
class RestPageLoginOptionEntity:
    is_last_page: bool | Unset = UNSET
    limit: int | Unset = UNSET
    results: list[LoginOptionEntity] | Unset = UNSET
    size: int | Unset = UNSET
    start: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_last_page = self.is_last_page

        limit = self.limit

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        size = self.size

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_last_page is not UNSET:
            field_dict["isLastPage"] = is_last_page
        if limit is not UNSET:
            field_dict["limit"] = limit
        if results is not UNSET:
            field_dict["results"] = results
        if size is not UNSET:
            field_dict["size"] = size
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login_option_entity import LoginOptionEntity

        d = dict(src_dict)
        is_last_page = d.pop("isLastPage", UNSET)

        limit = d.pop("limit", UNSET)

        _results = d.pop("results", UNSET)
        results: list[LoginOptionEntity] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = LoginOptionEntity.from_dict(results_item_data)

                results.append(results_item)

        size = d.pop("size", UNSET)

        start = d.pop("start", UNSET)

        rest_page_login_option_entity = cls(
            is_last_page=is_last_page,
            limit=limit,
            results=results,
            size=size,
            start=start,
        )

        rest_page_login_option_entity.additional_properties = d
        return rest_page_login_option_entity

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
