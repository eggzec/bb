from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit import Commit
    from ..models.ref_links import RefLinks


T = TypeVar("T", bound="Ref")


@_attrs_define
class Ref:
    """A ref object, representing a branch or tag in a repository."""

    type_: str
    links: RefLinks | Unset = UNSET
    name: str | Unset = UNSET
    """ The name of the ref. """
    target: Commit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit import Commit
        from ..models.ref_links import RefLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: RefLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RefLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        _target = d.pop("target", UNSET)
        target: Commit | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = Commit.from_dict(_target)

        ref = cls(
            type_=type_,
            links=links,
            name=name,
            target=target,
        )

        ref.additional_properties = d
        return ref

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
