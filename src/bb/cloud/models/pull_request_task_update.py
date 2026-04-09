from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.pull_request_task_update_state import PullRequestTaskUpdateState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pull_request_task_update_task_raw_content import PullRequestTaskUpdateTaskRawContent


T = TypeVar("T", bound="PullRequestTaskUpdate")


@_attrs_define
class PullRequestTaskUpdate:
    """A pullrequest task update"""

    content: PullRequestTaskUpdateTaskRawContent | Unset = UNSET
    """ task raw content """
    state: PullRequestTaskUpdateState | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pull_request_task_update_task_raw_content import PullRequestTaskUpdateTaskRawContent

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: PullRequestTaskUpdateTaskRawContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = PullRequestTaskUpdateTaskRawContent.from_dict(_content)

        _state = d.pop("state", UNSET)
        state: PullRequestTaskUpdateState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PullRequestTaskUpdateState(_state)

        pull_request_task_update = cls(
            content=content,
            state=state,
        )

        return pull_request_task_update
