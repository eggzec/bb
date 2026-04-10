from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_build_status_state import RestBuildStatusState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_build_status_test_results import RestBuildStatusTestResults


T = TypeVar("T", bound="RestBuildStatus")


@_attrs_define
class RestBuildStatus:
    build_number: str | Unset = UNSET
    created_date: int | Unset = UNSET
    description: str | Unset = UNSET
    duration: int | Unset = UNSET
    key: str | Unset = UNSET
    name: str | Unset = UNSET
    parent: str | Unset = UNSET
    project_key: str | Unset = UNSET
    ref: str | Unset = UNSET
    repository_slug: str | Unset = UNSET
    state: RestBuildStatusState | Unset = UNSET
    test_results: RestBuildStatusTestResults | Unset = UNSET
    updated_date: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        build_number = self.build_number

        created_date = self.created_date

        description = self.description

        duration = self.duration

        key = self.key

        name = self.name

        parent = self.parent

        project_key = self.project_key

        ref = self.ref

        repository_slug = self.repository_slug

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        test_results: dict[str, Any] | Unset = UNSET
        if not isinstance(self.test_results, Unset):
            test_results = self.test_results.to_dict()

        updated_date = self.updated_date

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if build_number is not UNSET:
            field_dict["buildNumber"] = build_number
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if project_key is not UNSET:
            field_dict["projectKey"] = project_key
        if ref is not UNSET:
            field_dict["ref"] = ref
        if repository_slug is not UNSET:
            field_dict["repositorySlug"] = repository_slug
        if state is not UNSET:
            field_dict["state"] = state
        if test_results is not UNSET:
            field_dict["testResults"] = test_results
        if updated_date is not UNSET:
            field_dict["updatedDate"] = updated_date
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_build_status_test_results import RestBuildStatusTestResults

        d = dict(src_dict)
        build_number = d.pop("buildNumber", UNSET)

        created_date = d.pop("createdDate", UNSET)

        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        parent = d.pop("parent", UNSET)

        project_key = d.pop("projectKey", UNSET)

        ref = d.pop("ref", UNSET)

        repository_slug = d.pop("repositorySlug", UNSET)

        _state = d.pop("state", UNSET)
        state: RestBuildStatusState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RestBuildStatusState(_state)

        _test_results = d.pop("testResults", UNSET)
        test_results: RestBuildStatusTestResults | Unset
        if isinstance(_test_results, Unset):
            test_results = UNSET
        else:
            test_results = RestBuildStatusTestResults.from_dict(_test_results)

        updated_date = d.pop("updatedDate", UNSET)

        url = d.pop("url", UNSET)

        rest_build_status = cls(
            build_number=build_number,
            created_date=created_date,
            description=description,
            duration=duration,
            key=key,
            name=name,
            parent=parent,
            project_key=project_key,
            ref=ref,
            repository_slug=repository_slug,
            state=state,
            test_results=test_results,
            updated_date=updated_date,
            url=url,
        )

        rest_build_status.additional_properties = d
        return rest_build_status

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
