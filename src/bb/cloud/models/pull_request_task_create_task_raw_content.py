from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PullRequestTaskCreateTaskRawContent")


@_attrs_define
class PullRequestTaskCreateTaskRawContent:
    """task raw content"""

    raw: str
    """ The task contents """

    def to_dict(self) -> dict[str, Any]:
        raw = self.raw

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "raw": raw,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        raw = d.pop("raw")

        pull_request_task_create_task_raw_content = cls(
            raw=raw,
        )

        return pull_request_task_create_task_raw_content
