from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.example_json_last_modified_callback_pom_xml_author import ExampleJsonLastModifiedCallbackPomXmlAuthor
    from ..models.example_json_last_modified_callback_pom_xml_committer import (
        ExampleJsonLastModifiedCallbackPomXmlCommitter,
    )
    from ..models.rest_minimal_commit import RestMinimalCommit


T = TypeVar("T", bound="ExampleJsonLastModifiedCallbackPomXml")


@_attrs_define
class ExampleJsonLastModifiedCallbackPomXml:
    author: ExampleJsonLastModifiedCallbackPomXmlAuthor | Unset = UNSET
    author_timestamp: int | Unset = UNSET
    committer: ExampleJsonLastModifiedCallbackPomXmlCommitter | Unset = UNSET
    committer_timestamp: int | Unset = UNSET
    display_id: str | Unset = UNSET
    id: str | Unset = UNSET
    message: str | Unset = UNSET
    parents: list[RestMinimalCommit] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author: dict[str, Any] | Unset = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        author_timestamp = self.author_timestamp

        committer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.committer, Unset):
            committer = self.committer.to_dict()

        committer_timestamp = self.committer_timestamp

        display_id = self.display_id

        id = self.id

        message = self.message

        parents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parents, Unset):
            parents = []
            for parents_item_data in self.parents:
                parents_item = parents_item_data.to_dict()
                parents.append(parents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if author_timestamp is not UNSET:
            field_dict["authorTimestamp"] = author_timestamp
        if committer is not UNSET:
            field_dict["committer"] = committer
        if committer_timestamp is not UNSET:
            field_dict["committerTimestamp"] = committer_timestamp
        if display_id is not UNSET:
            field_dict["displayId"] = display_id
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if parents is not UNSET:
            field_dict["parents"] = parents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.example_json_last_modified_callback_pom_xml_author import (
            ExampleJsonLastModifiedCallbackPomXmlAuthor,
        )
        from ..models.example_json_last_modified_callback_pom_xml_committer import (
            ExampleJsonLastModifiedCallbackPomXmlCommitter,
        )
        from ..models.rest_minimal_commit import RestMinimalCommit

        d = dict(src_dict)
        _author = d.pop("author", UNSET)
        author: ExampleJsonLastModifiedCallbackPomXmlAuthor | Unset
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = ExampleJsonLastModifiedCallbackPomXmlAuthor.from_dict(_author)

        author_timestamp = d.pop("authorTimestamp", UNSET)

        _committer = d.pop("committer", UNSET)
        committer: ExampleJsonLastModifiedCallbackPomXmlCommitter | Unset
        if isinstance(_committer, Unset):
            committer = UNSET
        else:
            committer = ExampleJsonLastModifiedCallbackPomXmlCommitter.from_dict(_committer)

        committer_timestamp = d.pop("committerTimestamp", UNSET)

        display_id = d.pop("displayId", UNSET)

        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        _parents = d.pop("parents", UNSET)
        parents: list[RestMinimalCommit] | Unset = UNSET
        if _parents is not UNSET:
            parents = []
            for parents_item_data in _parents:
                parents_item = RestMinimalCommit.from_dict(parents_item_data)

                parents.append(parents_item)

        example_json_last_modified_callback_pom_xml = cls(
            author=author,
            author_timestamp=author_timestamp,
            committer=committer,
            committer_timestamp=committer_timestamp,
            display_id=display_id,
            id=id,
            message=message,
            parents=parents,
        )

        example_json_last_modified_callback_pom_xml.additional_properties = d
        return example_json_last_modified_callback_pom_xml

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
