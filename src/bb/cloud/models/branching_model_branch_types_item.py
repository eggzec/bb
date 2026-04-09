from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.branching_model_branch_types_item_kind import BranchingModelBranchTypesItemKind

T = TypeVar("T", bound="BranchingModelBranchTypesItem")


@_attrs_define
class BranchingModelBranchTypesItem:
    kind: BranchingModelBranchTypesItemKind
    """ The kind of branch. """
    prefix: str
    """ The prefix for this branch type. A branch with this prefix will be classified as per `kind`. The prefix must
    be a valid prefix for a branch and must always exist. It cannot be blank, empty or `null`. """

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        prefix = self.prefix

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "prefix": prefix,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = BranchingModelBranchTypesItemKind(d.pop("kind"))

        prefix = d.pop("prefix")

        branching_model_branch_types_item = cls(
            kind=kind,
            prefix=prefix,
        )

        return branching_model_branch_types_item
