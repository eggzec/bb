from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.branching_model_settings_branch_types_item_kind import BranchingModelSettingsBranchTypesItemKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchingModelSettingsBranchTypesItem")


@_attrs_define
class BranchingModelSettingsBranchTypesItem:
    kind: BranchingModelSettingsBranchTypesItemKind
    """ The kind of the branch type. """
    enabled: bool | Unset = UNSET
    """ Whether the branch type is enabled or not. A disabled branch type may contain an invalid `prefix`. """
    prefix: str | Unset = UNSET
    """ The prefix for this branch type. A branch with this prefix will be classified as per `kind`. The `prefix` of
    an enabled branch type must be a valid branch prefix.Additionally, it cannot be blank, empty or `null`. The
    `prefix` for a disabled branch type can be empty or invalid. """

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        enabled = self.enabled

        prefix = self.prefix

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = BranchingModelSettingsBranchTypesItemKind(d.pop("kind"))

        enabled = d.pop("enabled", UNSET)

        prefix = d.pop("prefix", UNSET)

        branching_model_settings_branch_types_item = cls(
            kind=kind,
            enabled=enabled,
            prefix=prefix,
        )

        return branching_model_settings_branch_types_item
