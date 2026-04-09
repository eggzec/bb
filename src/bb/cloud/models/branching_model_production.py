from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch import Branch


T = TypeVar("T", bound="BranchingModelProduction")


@_attrs_define
class BranchingModelProduction:
    name: str
    """ Name of the target branch. Will be listed here even when the target branch does not exist. Will be `null` if
    targeting the main branch and the repository is empty. """
    use_mainbranch: bool
    """ Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). """
    branch: Branch | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        use_mainbranch = self.use_mainbranch

        branch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branch, Unset):
            branch = self.branch.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "use_mainbranch": use_mainbranch,
            }
        )
        if branch is not UNSET:
            field_dict["branch"] = branch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.branch import Branch

        d = dict(src_dict)
        name = d.pop("name")

        use_mainbranch = d.pop("use_mainbranch")

        _branch = d.pop("branch", UNSET)
        branch: Branch | Unset
        if isinstance(_branch, Unset):
            branch = UNSET
        else:
            branch = Branch.from_dict(_branch)

        branching_model_production = cls(
            name=name,
            use_mainbranch=use_mainbranch,
            branch=branch,
        )

        return branching_model_production
