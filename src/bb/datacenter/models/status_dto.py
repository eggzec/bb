from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.method_state_dto import MethodStateDTO


T = TypeVar("T", bound="StatusDTO")


@_attrs_define
class StatusDTO:
    is_two_sv_active: bool | Unset = UNSET
    methods: list[MethodStateDTO] | Unset = UNSET
    two_sv_active: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_two_sv_active = self.is_two_sv_active

        methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)

        two_sv_active = self.two_sv_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_two_sv_active is not UNSET:
            field_dict["isTwoSVActive"] = is_two_sv_active
        if methods is not UNSET:
            field_dict["methods"] = methods
        if two_sv_active is not UNSET:
            field_dict["twoSVActive"] = two_sv_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.method_state_dto import MethodStateDTO

        d = dict(src_dict)
        is_two_sv_active = d.pop("isTwoSVActive", UNSET)

        _methods = d.pop("methods", UNSET)
        methods: list[MethodStateDTO] | Unset = UNSET
        if _methods is not UNSET:
            methods = []
            for methods_item_data in _methods:
                methods_item = MethodStateDTO.from_dict(methods_item_data)

                methods.append(methods_item)

        two_sv_active = d.pop("twoSVActive", UNSET)

        status_dto = cls(
            is_two_sv_active=is_two_sv_active,
            methods=methods,
            two_sv_active=two_sv_active,
        )

        status_dto.additional_properties = d
        return status_dto

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
