from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_ref_target_ref_type import PipelineRefTargetRefType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit import Commit
    from ..models.pipeline_selector import PipelineSelector


T = TypeVar("T", bound="PipelineRefTarget")


@_attrs_define
class PipelineRefTarget:
    type_: str | Unset = UNSET
    ref_type: PipelineRefTargetRefType | Unset = UNSET
    """ The type of reference (branch/tag). """
    ref_name: str | Unset = UNSET
    """ The name of the reference. """
    commit: Commit | Unset = UNSET
    selector: PipelineSelector | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ref_type: str | Unset = UNSET
        if not isinstance(self.ref_type, Unset):
            ref_type = self.ref_type.value

        ref_name = self.ref_name

        commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        selector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selector, Unset):
            selector = self.selector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ref_type is not UNSET:
            field_dict["ref_type"] = ref_type
        if ref_name is not UNSET:
            field_dict["ref_name"] = ref_name
        if commit is not UNSET:
            field_dict["commit"] = commit
        if selector is not UNSET:
            field_dict["selector"] = selector

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commit import Commit
        from ..models.pipeline_selector import PipelineSelector

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _ref_type = d.pop("ref_type", UNSET)
        ref_type: PipelineRefTargetRefType | Unset
        if isinstance(_ref_type, Unset):
            ref_type = UNSET
        else:
            ref_type = PipelineRefTargetRefType(_ref_type)

        ref_name = d.pop("ref_name", UNSET)

        _commit = d.pop("commit", UNSET)
        commit: Commit | Unset
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = Commit.from_dict(_commit)

        _selector = d.pop("selector", UNSET)
        selector: PipelineSelector | Unset
        if isinstance(_selector, Unset):
            selector = UNSET
        else:
            selector = PipelineSelector.from_dict(_selector)

        pipeline_ref_target = cls(
            type_=type_,
            ref_type=ref_type,
            ref_name=ref_name,
            commit=commit,
            selector=selector,
        )

        pipeline_ref_target.additional_properties = d
        return pipeline_ref_target

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
