from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.example_json_last_modified_callback_latest_commit import ExampleJsonLastModifiedCallbackLatestCommit
    from ..models.example_json_last_modified_callback_pom_xml import ExampleJsonLastModifiedCallbackPomXml
    from ..models.example_json_last_modified_callback_readme_md import ExampleJsonLastModifiedCallbackReadmeMd


T = TypeVar("T", bound="ExampleJsonLastModifiedCallback")


@_attrs_define
class ExampleJsonLastModifiedCallback:
    latest_commit: ExampleJsonLastModifiedCallbackLatestCommit | Unset = UNSET
    pom_xml: ExampleJsonLastModifiedCallbackPomXml | Unset = UNSET
    readme_md: ExampleJsonLastModifiedCallbackReadmeMd | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_commit, Unset):
            latest_commit = self.latest_commit.to_dict()

        pom_xml: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pom_xml, Unset):
            pom_xml = self.pom_xml.to_dict()

        readme_md: dict[str, Any] | Unset = UNSET
        if not isinstance(self.readme_md, Unset):
            readme_md = self.readme_md.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_commit is not UNSET:
            field_dict["latestCommit"] = latest_commit
        if pom_xml is not UNSET:
            field_dict["pomXml"] = pom_xml
        if readme_md is not UNSET:
            field_dict["readmeMd"] = readme_md

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.example_json_last_modified_callback_latest_commit import (
            ExampleJsonLastModifiedCallbackLatestCommit,
        )
        from ..models.example_json_last_modified_callback_pom_xml import ExampleJsonLastModifiedCallbackPomXml
        from ..models.example_json_last_modified_callback_readme_md import ExampleJsonLastModifiedCallbackReadmeMd

        d = dict(src_dict)
        _latest_commit = d.pop("latestCommit", UNSET)
        latest_commit: ExampleJsonLastModifiedCallbackLatestCommit | Unset
        if isinstance(_latest_commit, Unset):
            latest_commit = UNSET
        else:
            latest_commit = ExampleJsonLastModifiedCallbackLatestCommit.from_dict(_latest_commit)

        _pom_xml = d.pop("pomXml", UNSET)
        pom_xml: ExampleJsonLastModifiedCallbackPomXml | Unset
        if isinstance(_pom_xml, Unset):
            pom_xml = UNSET
        else:
            pom_xml = ExampleJsonLastModifiedCallbackPomXml.from_dict(_pom_xml)

        _readme_md = d.pop("readmeMd", UNSET)
        readme_md: ExampleJsonLastModifiedCallbackReadmeMd | Unset
        if isinstance(_readme_md, Unset):
            readme_md = UNSET
        else:
            readme_md = ExampleJsonLastModifiedCallbackReadmeMd.from_dict(_readme_md)

        example_json_last_modified_callback = cls(
            latest_commit=latest_commit,
            pom_xml=pom_xml,
            readme_md=readme_md,
        )

        example_json_last_modified_callback.additional_properties = d
        return example_json_last_modified_callback

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
