from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_scopes_example_links import RestScopesExampleLinks
    from ..models.rest_scopes_example_scopes_item import RestScopesExampleScopesItem


T = TypeVar("T", bound="RestScopesExample")


@_attrs_define
class RestScopesExample:
    links: RestScopesExampleLinks | Unset = UNSET
    scopes: list[RestScopesExampleScopesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        scopes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()
                scopes.append(scopes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_scopes_example_links import RestScopesExampleLinks
        from ..models.rest_scopes_example_scopes_item import RestScopesExampleScopesItem

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: RestScopesExampleLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestScopesExampleLinks.from_dict(_links)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[RestScopesExampleScopesItem] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = RestScopesExampleScopesItem.from_dict(scopes_item_data)

                scopes.append(scopes_item)

        rest_scopes_example = cls(
            links=links,
            scopes=scopes,
        )

        rest_scopes_example.additional_properties = d
        return rest_scopes_example

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
