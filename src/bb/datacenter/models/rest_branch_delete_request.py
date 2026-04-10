from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestBranchDeleteRequest")


@_attrs_define
class RestBranchDeleteRequest:
    dry_run: bool | Unset = UNSET
    """ Don't actually delete the ref name, just do a dry run """
    end_point: str | Unset = UNSET
    """ Commit ID that the provided ref name is expected to point to """
    name: str | Unset = UNSET
    """ Name of the ref to be deleted """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        end_point = self.end_point

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if end_point is not UNSET:
            field_dict["endPoint"] = end_point
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dry_run = d.pop("dryRun", UNSET)

        end_point = d.pop("endPoint", UNSET)

        name = d.pop("name", UNSET)

        rest_branch_delete_request = cls(
            dry_run=dry_run,
            end_point=end_point,
            name=name,
        )

        rest_branch_delete_request.additional_properties = d
        return rest_branch_delete_request

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
