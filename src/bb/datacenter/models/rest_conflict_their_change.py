from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_conflict_their_change_type import RestConflictTheirChangeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_conflict_their_change_path import RestConflictTheirChangePath
    from ..models.rest_conflict_their_change_src_path import RestConflictTheirChangeSrcPath


T = TypeVar("T", bound="RestConflictTheirChange")


@_attrs_define
class RestConflictTheirChange:
    path: RestConflictTheirChangePath | Unset = UNSET
    src_path: RestConflictTheirChangeSrcPath | Unset = UNSET
    type_: RestConflictTheirChangeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        src_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.src_path, Unset):
            src_path = self.src_path.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if src_path is not UNSET:
            field_dict["srcPath"] = src_path
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_conflict_their_change_path import RestConflictTheirChangePath
        from ..models.rest_conflict_their_change_src_path import RestConflictTheirChangeSrcPath

        d = dict(src_dict)
        _path = d.pop("path", UNSET)
        path: RestConflictTheirChangePath | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = RestConflictTheirChangePath.from_dict(_path)

        _src_path = d.pop("srcPath", UNSET)
        src_path: RestConflictTheirChangeSrcPath | Unset
        if isinstance(_src_path, Unset):
            src_path = UNSET
        else:
            src_path = RestConflictTheirChangeSrcPath.from_dict(_src_path)

        _type_ = d.pop("type", UNSET)
        type_: RestConflictTheirChangeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestConflictTheirChangeType(_type_)

        rest_conflict_their_change = cls(
            path=path,
            src_path=src_path,
            type_=type_,
        )

        rest_conflict_their_change.additional_properties = d
        return rest_conflict_their_change

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
