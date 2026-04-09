from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.issue_job_status_status import IssueJobStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueJobStatus")


@_attrs_define
class IssueJobStatus:
    """The status of an import or export job"""

    type_: str | Unset = UNSET
    status: IssueJobStatusStatus | Unset = UNSET
    """ The status of the import/export job """
    phase: str | Unset = UNSET
    """ The phase of the import/export job """
    total: int | Unset = UNSET
    """ The total number of issues being imported/exported """
    count: int | Unset = UNSET
    """ The total number of issues already imported/exported """
    pct: float | Unset = UNSET
    """ The percentage of issues already imported/exported """

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        phase = self.phase

        total = self.total

        count = self.count

        pct = self.pct

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if phase is not UNSET:
            field_dict["phase"] = phase
        if total is not UNSET:
            field_dict["total"] = total
        if count is not UNSET:
            field_dict["count"] = count
        if pct is not UNSET:
            field_dict["pct"] = pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _status = d.pop("status", UNSET)
        status: IssueJobStatusStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IssueJobStatusStatus(_status)

        phase = d.pop("phase", UNSET)

        total = d.pop("total", UNSET)

        count = d.pop("count", UNSET)

        pct = d.pop("pct", UNSET)

        issue_job_status = cls(
            type_=type_,
            status=status,
            phase=phase,
            total=total,
            count=count,
            pct=pct,
        )

        return issue_job_status
