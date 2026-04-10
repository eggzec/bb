from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_permitted_group_group import RestPermittedGroupGroup


T = TypeVar("T", bound="RestPermittedGroup")


@_attrs_define
class RestPermittedGroup:
    group: RestPermittedGroupGroup | Unset = UNSET
    permission: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        permission = self.permission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group is not UNSET:
            field_dict["group"] = group
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_permitted_group_group import RestPermittedGroupGroup

        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: RestPermittedGroupGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = RestPermittedGroupGroup.from_dict(_group)

        permission = d.pop("permission", UNSET)

        rest_permitted_group = cls(
            group=group,
            permission=permission,
        )

        rest_permitted_group.additional_properties = d
        return rest_permitted_group

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
