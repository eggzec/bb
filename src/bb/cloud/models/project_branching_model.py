from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_branching_model_branch_types_item import ProjectBranchingModelBranchTypesItem
    from ..models.project_branching_model_development import ProjectBranchingModelDevelopment
    from ..models.project_branching_model_production import ProjectBranchingModelProduction


T = TypeVar("T", bound="ProjectBranchingModel")


@_attrs_define
class ProjectBranchingModel:
    type_: str
    branch_types: list[ProjectBranchingModelBranchTypesItem] | Unset = UNSET
    """ The active branch types. """
    development: ProjectBranchingModelDevelopment | Unset = UNSET
    production: ProjectBranchingModelProduction | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        branch_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.branch_types, Unset):
            branch_types = []
            for branch_types_item_data in self.branch_types:
                branch_types_item = branch_types_item_data.to_dict()
                branch_types.append(branch_types_item)

        development: dict[str, Any] | Unset = UNSET
        if not isinstance(self.development, Unset):
            development = self.development.to_dict()

        production: dict[str, Any] | Unset = UNSET
        if not isinstance(self.production, Unset):
            production = self.production.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if branch_types is not UNSET:
            field_dict["branch_types"] = branch_types
        if development is not UNSET:
            field_dict["development"] = development
        if production is not UNSET:
            field_dict["production"] = production

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_branching_model_branch_types_item import ProjectBranchingModelBranchTypesItem
        from ..models.project_branching_model_development import ProjectBranchingModelDevelopment
        from ..models.project_branching_model_production import ProjectBranchingModelProduction

        d = dict(src_dict)
        type_ = d.pop("type")

        _branch_types = d.pop("branch_types", UNSET)
        branch_types: list[ProjectBranchingModelBranchTypesItem] | Unset = UNSET
        if _branch_types is not UNSET:
            branch_types = []
            for branch_types_item_data in _branch_types:
                branch_types_item = ProjectBranchingModelBranchTypesItem.from_dict(branch_types_item_data)

                branch_types.append(branch_types_item)

        _development = d.pop("development", UNSET)
        development: ProjectBranchingModelDevelopment | Unset
        if isinstance(_development, Unset):
            development = UNSET
        else:
            development = ProjectBranchingModelDevelopment.from_dict(_development)

        _production = d.pop("production", UNSET)
        production: ProjectBranchingModelProduction | Unset
        if isinstance(_production, Unset):
            production = UNSET
        else:
            production = ProjectBranchingModelProduction.from_dict(_production)

        project_branching_model = cls(
            type_=type_,
            branch_types=branch_types,
            development=development,
            production=production,
        )

        project_branching_model.additional_properties = d
        return project_branching_model

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
