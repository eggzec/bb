from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExampleMultipartFormData")


@_attrs_define
class ExampleMultipartFormData:
    branch: str | Unset = UNSET
    """ The branch on which the <code>path</code> should be modified or created. """
    content: str | Unset = UNSET
    """ The full content of the file at <code>path</code>. """
    message: str | Unset = UNSET
    """ The message associated with this change, to be used as the commit message. Or null if the default message
    should be used. """
    source_branch: str | Unset = UNSET
    """ The starting point for <code>branch</code>. If provided and different from <code>branch</code>,
    <code>branch</code> will be created as a new branch, branching off from <code>sourceBranch</code>. """
    source_commit_id: str | Unset = UNSET
    """ The commit ID of the file before it was edited, used to identify if content has changed. Or null if this is
    a new file """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        content = self.content

        message = self.message

        source_branch = self.source_branch

        source_commit_id = self.source_commit_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["branch"] = branch
        if content is not UNSET:
            field_dict["content"] = content
        if message is not UNSET:
            field_dict["message"] = message
        if source_branch is not UNSET:
            field_dict["sourceBranch"] = source_branch
        if source_commit_id is not UNSET:
            field_dict["sourceCommitId"] = source_commit_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.branch, Unset):
            files.append(("branch", (None, str(self.branch).encode(), "text/plain")))

        if not isinstance(self.content, Unset):
            files.append(("content", (None, str(self.content).encode(), "text/plain")))

        if not isinstance(self.message, Unset):
            files.append(("message", (None, str(self.message).encode(), "text/plain")))

        if not isinstance(self.source_branch, Unset):
            files.append(("sourceBranch", (None, str(self.source_branch).encode(), "text/plain")))

        if not isinstance(self.source_commit_id, Unset):
            files.append(("sourceCommitId", (None, str(self.source_commit_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = d.pop("branch", UNSET)

        content = d.pop("content", UNSET)

        message = d.pop("message", UNSET)

        source_branch = d.pop("sourceBranch", UNSET)

        source_commit_id = d.pop("sourceCommitId", UNSET)

        example_multipart_form_data = cls(
            branch=branch,
            content=content,
            message=message,
            source_branch=source_branch,
            source_commit_id=source_commit_id,
        )

        example_multipart_form_data.additional_properties = d
        return example_multipart_form_data

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
