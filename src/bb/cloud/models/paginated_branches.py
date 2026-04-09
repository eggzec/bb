from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch import Branch


T = TypeVar("T", bound="PaginatedBranches")


@_attrs_define
class PaginatedBranches:
    """A paginated list of branches."""

    size: int | Unset = UNSET
    """ Total number of objects in the response. This is an optional element that is not provided in all responses,
    as it can be expensive to compute. """
    page: int | Unset = UNSET
    """ Page number of the current results. This is an optional element that is not provided in all responses. """
    pagelen: int | Unset = UNSET
    """ Current number of objects on the existing page. The default value is 10 with 100 being the maximum allowed
    value. Individual APIs may enforce different values. """
    next_: str | Unset = UNSET
    """ Link to the next page if it exists. The last page of a collection does not have this value. Use this link to
    navigate the result set and refrain from constructing your own URLs. """
    previous: str | Unset = UNSET
    """ Link to previous page if it exists. A collections first page does not have this value. This is an optional
    element that is not provided in all responses. Some result sets strictly support forward navigation and never
    provide previous links. Clients must anticipate that backwards navigation is not always available. Use this link
    to navigate the result set and refrain from constructing your own URLs. """
    values: list[Branch] | Unset = UNSET

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
        from ..models.branch import Branch

        d = dict(src_dict)
        size = d.pop("size", UNSET)

        page = d.pop("page", UNSET)

        pagelen = d.pop("pagelen", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        _values = d.pop("values", UNSET)
        values: list[Branch] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = Branch.from_dict(values_item_data)

                values.append(values_item)

        paginated_branches = cls(
            size=size,
            page=page,
            pagelen=pagelen,
            next_=next_,
            previous=previous,
            values=values,
        )

        return paginated_branches
