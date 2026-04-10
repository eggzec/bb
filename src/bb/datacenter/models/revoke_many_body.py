from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_project import RestProject
    from ..models.rest_repository import RestRepository


T = TypeVar("T", bound="RevokeManyBody")


@_attrs_define
class RevokeManyBody:
    projects: RestProject | Unset = UNSET
    repositories: RestRepository | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects: dict[str, Any] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = self.projects.to_dict()

        repositories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = self.repositories.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if projects is not UNSET:
            field_dict["projects"] = projects
        if repositories is not UNSET:
            field_dict["repositories"] = repositories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_project import RestProject
        from ..models.rest_repository import RestRepository

        d = dict(src_dict)
        _projects = d.pop("projects", UNSET)
        projects: RestProject | Unset
        if isinstance(_projects, Unset):
            projects = UNSET
        else:
            projects = RestProject.from_dict(_projects)

        _repositories = d.pop("repositories", UNSET)
        repositories: RestRepository | Unset
        if isinstance(_repositories, Unset):
            repositories = UNSET
        else:
            repositories = RestRepository.from_dict(_repositories)

        revoke_many_body = cls(
            projects=projects,
            repositories=repositories,
        )

        revoke_many_body.additional_properties = d
        return revoke_many_body

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
