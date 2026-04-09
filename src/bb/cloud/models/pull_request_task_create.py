from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment import Comment
    from ..models.pull_request_task_create_task_raw_content import PullRequestTaskCreateTaskRawContent


T = TypeVar("T", bound="PullRequestTaskCreate")


@_attrs_define
class PullRequestTaskCreate:
    """A pullrequest task create"""

    content: PullRequestTaskCreateTaskRawContent
    """ task raw content """
    comment: Comment | Unset = UNSET
    pending: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        content = self.content.to_dict()

        comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        pending = self.pending

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content": content,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if pending is not UNSET:
            field_dict["pending"] = pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment import Comment
        from ..models.pull_request_task_create_task_raw_content import PullRequestTaskCreateTaskRawContent

        d = dict(src_dict)
        content = PullRequestTaskCreateTaskRawContent.from_dict(d.pop("content"))

        _comment = d.pop("comment", UNSET)
        comment: Comment | Unset
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = Comment.from_dict(_comment)

        pending = d.pop("pending", UNSET)

        pull_request_task_create = cls(
            content=content,
            comment=comment,
            pending=pending,
        )

        return pull_request_task_create
