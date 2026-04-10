from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_change_node_type import RestChangeNodeType
from ..models.rest_change_type import RestChangeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_change_conflict import RestChangeConflict
    from ..models.rest_change_links import RestChangeLinks
    from ..models.rest_change_path import RestChangePath
    from ..models.rest_change_src_path import RestChangeSrcPath


T = TypeVar("T", bound="RestChange")


@_attrs_define
class RestChange:
    conflict: RestChangeConflict | Unset = UNSET
    content_id: str | Unset = UNSET
    executable: bool | Unset = UNSET
    from_content_id: str | Unset = UNSET
    links: RestChangeLinks | Unset = UNSET
    node_type: RestChangeNodeType | Unset = UNSET
    path: RestChangePath | Unset = UNSET
    percent_unchanged: int | Unset = UNSET
    src_executable: bool | Unset = UNSET
    src_path: RestChangeSrcPath | Unset = UNSET
    type_: RestChangeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conflict: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conflict, Unset):
            conflict = self.conflict.to_dict()

        content_id = self.content_id

        executable = self.executable

        from_content_id = self.from_content_id

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        node_type: str | Unset = UNSET
        if not isinstance(self.node_type, Unset):
            node_type = self.node_type.value

        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        percent_unchanged = self.percent_unchanged

        src_executable = self.src_executable

        src_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.src_path, Unset):
            src_path = self.src_path.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conflict is not UNSET:
            field_dict["conflict"] = conflict
        if content_id is not UNSET:
            field_dict["contentId"] = content_id
        if executable is not UNSET:
            field_dict["executable"] = executable
        if from_content_id is not UNSET:
            field_dict["fromContentId"] = from_content_id
        if links is not UNSET:
            field_dict["links"] = links
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if path is not UNSET:
            field_dict["path"] = path
        if percent_unchanged is not UNSET:
            field_dict["percentUnchanged"] = percent_unchanged
        if src_executable is not UNSET:
            field_dict["srcExecutable"] = src_executable
        if src_path is not UNSET:
            field_dict["srcPath"] = src_path
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_change_conflict import RestChangeConflict
        from ..models.rest_change_links import RestChangeLinks
        from ..models.rest_change_path import RestChangePath
        from ..models.rest_change_src_path import RestChangeSrcPath

        d = dict(src_dict)
        _conflict = d.pop("conflict", UNSET)
        conflict: RestChangeConflict | Unset
        if isinstance(_conflict, Unset):
            conflict = UNSET
        else:
            conflict = RestChangeConflict.from_dict(_conflict)

        content_id = d.pop("contentId", UNSET)

        executable = d.pop("executable", UNSET)

        from_content_id = d.pop("fromContentId", UNSET)

        _links = d.pop("links", UNSET)
        links: RestChangeLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RestChangeLinks.from_dict(_links)

        _node_type = d.pop("nodeType", UNSET)
        node_type: RestChangeNodeType | Unset
        if isinstance(_node_type, Unset):
            node_type = UNSET
        else:
            node_type = RestChangeNodeType(_node_type)

        _path = d.pop("path", UNSET)
        path: RestChangePath | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = RestChangePath.from_dict(_path)

        percent_unchanged = d.pop("percentUnchanged", UNSET)

        src_executable = d.pop("srcExecutable", UNSET)

        _src_path = d.pop("srcPath", UNSET)
        src_path: RestChangeSrcPath | Unset
        if isinstance(_src_path, Unset):
            src_path = UNSET
        else:
            src_path = RestChangeSrcPath.from_dict(_src_path)

        _type_ = d.pop("type", UNSET)
        type_: RestChangeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RestChangeType(_type_)

        rest_change = cls(
            conflict=conflict,
            content_id=content_id,
            executable=executable,
            from_content_id=from_content_id,
            links=links,
            node_type=node_type,
            path=path,
            percent_unchanged=percent_unchanged,
            src_executable=src_executable,
            src_path=src_path,
            type_=type_,
        )

        rest_change.additional_properties = d
        return rest_change

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
