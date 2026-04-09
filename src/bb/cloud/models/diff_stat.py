from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.diff_stat_status import DiffStatStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_file import CommitFile


T = TypeVar("T", bound="DiffStat")


@_attrs_define
class DiffStat:
    """A diffstat object that includes a summary of changes made to a file between two commits."""

    type_: str
    status: DiffStatStatus | Unset = UNSET
    lines_added: int | Unset = UNSET
    lines_removed: int | Unset = UNSET
    old: CommitFile | Unset = UNSET
    """ A file object, representing a file at a commit in a repository """
    new: CommitFile | Unset = UNSET
    """ A file object, representing a file at a commit in a repository """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        lines_added = self.lines_added

        lines_removed = self.lines_removed

        old: dict[str, Any] | Unset = UNSET
        if not isinstance(self.old, Unset):
            old = self.old.to_dict()

        new: dict[str, Any] | Unset = UNSET
        if not isinstance(self.new, Unset):
            new = self.new.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if lines_added is not UNSET:
            field_dict["lines_added"] = lines_added
        if lines_removed is not UNSET:
            field_dict["lines_removed"] = lines_removed
        if old is not UNSET:
            field_dict["old"] = old
        if new is not UNSET:
            field_dict["new"] = new

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit_file import CommitFile

        d = dict(src_dict)
        type_ = d.pop("type")

        _status = d.pop("status", UNSET)
        status: DiffStatStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DiffStatStatus(_status)

        lines_added = d.pop("lines_added", UNSET)

        lines_removed = d.pop("lines_removed", UNSET)

        _old = d.pop("old", UNSET)
        old: CommitFile | Unset
        if isinstance(_old, Unset):
            old = UNSET
        else:
            old = CommitFile.from_dict(_old)

        _new = d.pop("new", UNSET)
        new: CommitFile | Unset
        if isinstance(_new, Unset):
            new = UNSET
        else:
            new = CommitFile.from_dict(_new)

        diff_stat = cls(
            type_=type_,
            status=status,
            lines_added=lines_added,
            lines_removed=lines_removed,
            old=old,
            new=new,
        )

        diff_stat.additional_properties = d
        return diff_stat

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
