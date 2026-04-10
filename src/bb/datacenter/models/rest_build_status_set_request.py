from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_build_status_set_request_state import RestBuildStatusSetRequestState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_build_status_set_request_test_results import RestBuildStatusSetRequestTestResults


T = TypeVar("T", bound="RestBuildStatusSetRequest")


@_attrs_define
class RestBuildStatusSetRequest:
    key: str
    state: RestBuildStatusSetRequestState
    url: str
    build_number: str | Unset = UNSET
    description: str | Unset = UNSET
    duration: int | Unset = UNSET
    last_updated: int | Unset = UNSET
    name: str | Unset = UNSET
    parent: str | Unset = UNSET
    ref: str | Unset = UNSET
    test_results: RestBuildStatusSetRequestTestResults | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        state = self.state.value

        url = self.url

        build_number = self.build_number

        description = self.description

        duration = self.duration

        last_updated = self.last_updated

        name = self.name

        parent = self.parent

        ref = self.ref

        test_results: dict[str, Any] | Unset = UNSET
        if not isinstance(self.test_results, Unset):
            test_results = self.test_results.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "state": state,
                "url": url,
            }
        )
        if build_number is not UNSET:
            field_dict["buildNumber"] = build_number
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if ref is not UNSET:
            field_dict["ref"] = ref
        if test_results is not UNSET:
            field_dict["testResults"] = test_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_build_status_set_request_test_results import RestBuildStatusSetRequestTestResults

        d = dict(src_dict)
        key = d.pop("key")

        state = RestBuildStatusSetRequestState(d.pop("state"))

        url = d.pop("url")

        build_number = d.pop("buildNumber", UNSET)

        description = d.pop("description", UNSET)

        duration = d.pop("duration", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        name = d.pop("name", UNSET)

        parent = d.pop("parent", UNSET)

        ref = d.pop("ref", UNSET)

        _test_results = d.pop("testResults", UNSET)
        test_results: RestBuildStatusSetRequestTestResults | Unset
        if isinstance(_test_results, Unset):
            test_results = UNSET
        else:
            test_results = RestBuildStatusSetRequestTestResults.from_dict(_test_results)

        rest_build_status_set_request = cls(
            key=key,
            state=state,
            url=url,
            build_number=build_number,
            description=description,
            duration=duration,
            last_updated=last_updated,
            name=name,
            parent=parent,
            ref=ref,
            test_results=test_results,
        )

        rest_build_status_set_request.additional_properties = d
        return rest_build_status_set_request

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
