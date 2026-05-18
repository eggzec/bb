from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subject_types_workspace_links import SubjectTypesWorkspaceLinks


T = TypeVar("T", bound="SubjectTypesWorkspace")


@_attrs_define
class SubjectTypesWorkspace:
    links: SubjectTypesWorkspaceLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subject_types_workspace_links import SubjectTypesWorkspaceLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: SubjectTypesWorkspaceLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SubjectTypesWorkspaceLinks.from_dict(_links)

        subject_types_workspace = cls(
            links=links,
        )

        subject_types_workspace.additional_properties = d
        return subject_types_workspace

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
