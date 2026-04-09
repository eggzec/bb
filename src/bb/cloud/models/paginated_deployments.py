from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment import Deployment


T = TypeVar("T", bound="PaginatedDeployments")


@_attrs_define
class PaginatedDeployments:
    """A paged list of deployments"""

    page: int | Unset = UNSET
    """ Page number of the current results. This is an optional element that is not provided in all responses. """
    values: list[Deployment] | Unset = UNSET
    """ The values of the current page. """
    size: int | Unset = UNSET
    """ Total number of objects in the response. This is an optional element that is not provided in all responses,
    as it can be expensive to compute. """
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        size = self.size

        pagelen = self.pagelen

        next_ = self.next_

        previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if values is not UNSET:
            field_dict["values"] = values
        if size is not UNSET:
            field_dict["size"] = size
        if pagelen is not UNSET:
            field_dict["pagelen"] = pagelen
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment import Deployment

        d = dict(src_dict)
        page = d.pop("page", UNSET)

        _values = d.pop("values", UNSET)
        values: list[Deployment] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = Deployment.from_dict(values_item_data)

                values.append(values_item)

        size = d.pop("size", UNSET)

        pagelen = d.pop("pagelen", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        paginated_deployments = cls(
            page=page,
            values=values,
            size=size,
            pagelen=pagelen,
            next_=next_,
            previous=previous,
        )

        paginated_deployments.additional_properties = d
        return paginated_deployments

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
