from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit import Commit


T = TypeVar("T", bound="PaginatedCommits")


@_attrs_define
class PaginatedCommits:
    """A paginated list of commits."""

    size: int | Unset = UNSET
    """ Total number of objects in the response. """
    page: int | Unset = UNSET
    """ Page number of the current results. """
    pagelen: int | Unset = UNSET
    """ Current number of objects on the existing page. """
    next_: str | Unset = UNSET
    """ Link to the next page if it exists. """
    previous: str | Unset = UNSET
    """ Link to previous page if it exists. """
    values: list[Commit] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        page = self.page

        pagelen = self.pagelen

        next_ = self.next_

        previous = self.previous

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if page is not UNSET:
            field_dict["page"] = page
        if pagelen is not UNSET:
            field_dict["pagelen"] = pagelen
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit import Commit

        d = dict(src_dict)
        size = d.pop("size", UNSET)

        page = d.pop("page", UNSET)

        pagelen = d.pop("pagelen", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        _values = d.pop("values", UNSET)
        values: list[Commit] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = Commit.from_dict(values_item_data)

                values.append(values_item)

        paginated_commits = cls(
            size=size,
            page=page,
            pagelen=pagelen,
            next_=next_,
            previous=previous,
            values=values,
        )

        paginated_commits.additional_properties = d
        return paginated_commits

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
