from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueChangeChangesState")


@_attrs_define
class IssueChangeChangesState:
    old: str | Unset = UNSET
    new: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        old = self.old

        new = self.new

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if old is not UNSET:
            field_dict["old"] = old
        if new is not UNSET:
            field_dict["new"] = new

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        old = d.pop("old", UNSET)

        new = d.pop("new", UNSET)

        issue_change_changes_state = cls(
            old=old,
            new=new,
        )

        return issue_change_changes_state
