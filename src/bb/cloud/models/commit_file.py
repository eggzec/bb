from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.commit_file_attributes_item import CommitFileAttributesItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit import Commit


T = TypeVar("T", bound="CommitFile")


@_attrs_define
class CommitFile:
    """A file object, representing a file at a commit in a repository"""

    type_: str
    path: str | Unset = UNSET
    """ The path in the repository """
    commit: Commit | Unset = UNSET
    attributes: list[CommitFileAttributesItem] | Unset = UNSET
    escaped_path: str | Unset = UNSET
    """ The escaped version of the path as it appears in a diff. If the path does not require escaping this will be
    the same as path. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        path = self.path

        commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        attributes: list[str] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.value
                attributes.append(attributes_item)

        escaped_path = self.escaped_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if commit is not UNSET:
            field_dict["commit"] = commit
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if escaped_path is not UNSET:
            field_dict["escaped_path"] = escaped_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit import Commit

        d = dict(src_dict)
        type_ = d.pop("type")

        path = d.pop("path", UNSET)

        _commit = d.pop("commit", UNSET)
        commit: Commit | Unset
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = Commit.from_dict(_commit)

        _attributes = d.pop("attributes", UNSET)
        attributes: list[CommitFileAttributesItem] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = CommitFileAttributesItem(attributes_item_data)

                attributes.append(attributes_item)

        escaped_path = d.pop("escaped_path", UNSET)

        commit_file = cls(
            type_=type_,
            path=path,
            commit=commit,
            attributes=attributes,
            escaped_path=escaped_path,
        )

        commit_file.additional_properties = d
        return commit_file

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
