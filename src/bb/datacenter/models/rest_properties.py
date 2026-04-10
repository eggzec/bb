from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestProperties")


@_attrs_define
class RestProperties:
    content_hash: str | Unset = UNSET
    default_branch_id: str | Unset = UNSET
    metadata_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_hash = self.content_hash

        default_branch_id = self.default_branch_id

        metadata_hash = self.metadata_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content_hash is not UNSET:
            field_dict["contentHash"] = content_hash
        if default_branch_id is not UNSET:
            field_dict["defaultBranchId"] = default_branch_id
        if metadata_hash is not UNSET:
            field_dict["metadataHash"] = metadata_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_hash = d.pop("contentHash", UNSET)

        default_branch_id = d.pop("defaultBranchId", UNSET)

        metadata_hash = d.pop("metadataHash", UNSET)

        rest_properties = cls(
            content_hash=content_hash,
            default_branch_id=default_branch_id,
            metadata_hash=metadata_hash,
        )

        rest_properties.additional_properties = d
        return rest_properties

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
