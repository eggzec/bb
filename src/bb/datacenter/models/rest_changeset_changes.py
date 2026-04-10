from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_changeset_changes_values import RestChangesetChangesValues


T = TypeVar("T", bound="RestChangesetChanges")


@_attrs_define
class RestChangesetChanges:
    is_last_page: bool | Unset = UNSET
    limit: int | Unset = UNSET
    next_page_start: int | Unset = UNSET
    size: int | Unset = UNSET
    start: int | Unset = UNSET
    values: RestChangesetChangesValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_last_page = self.is_last_page

        limit = self.limit

        next_page_start = self.next_page_start

        size = self.size

        start = self.start

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

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
        from ..models.rest_changeset_changes_values import RestChangesetChangesValues

        d = dict(src_dict)
        is_last_page = d.pop("isLastPage", UNSET)

        limit = d.pop("limit", UNSET)

        next_page_start = d.pop("nextPageStart", UNSET)

        size = d.pop("size", UNSET)

        start = d.pop("start", UNSET)

        _values = d.pop("values", UNSET)
        values: RestChangesetChangesValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = RestChangesetChangesValues.from_dict(_values)

        rest_changeset_changes = cls(
            is_last_page=is_last_page,
            limit=limit,
            next_page_start=next_page_start,
            size=size,
            start=start,
            values=values,
        )

        rest_changeset_changes.additional_properties = d
        return rest_changeset_changes

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
