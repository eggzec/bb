from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestJiraBackfillError")


@_attrs_define
class RestJiraBackfillError:
    error: str | Unset = UNSET
    project_key: str | Unset = UNSET
    repo_slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        project_key = self.project_key

        repo_slug = self.repo_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if project_key is not UNSET:
            field_dict["projectKey"] = project_key
        if repo_slug is not UNSET:
            field_dict["repoSlug"] = repo_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        project_key = d.pop("projectKey", UNSET)

        repo_slug = d.pop("repoSlug", UNSET)

        rest_jira_backfill_error = cls(
            error=error,
            project_key=project_key,
            repo_slug=repo_slug,
        )

        rest_jira_backfill_error.additional_properties = d
        return rest_jira_backfill_error

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
