from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ProjectBranchingModelProduction")


@_attrs_define
class ProjectBranchingModelProduction:
    name: str
    """ Name of the target branch. If inherited by a repository, it will default to the main branch if the specified
    branch does not exist. """
    use_mainbranch: bool
    """ Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). """

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        use_mainbranch = self.use_mainbranch

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "use_mainbranch": use_mainbranch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        use_mainbranch = d.pop("use_mainbranch")

        project_branching_model_production = cls(
            name=name,
            use_mainbranch=use_mainbranch,
        )

        return project_branching_model_production
