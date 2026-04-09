from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pipeline_state_completed_error_name import PipelineStateCompletedErrorName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_error import PipelineError


T = TypeVar("T", bound="PipelineStateCompletedError")


@_attrs_define
class PipelineStateCompletedError:
    type_: str
    name: PipelineStateCompletedErrorName | Unset = UNSET
    """ The name of the result (ERROR) """
    error: PipelineError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_error import PipelineError

        d = dict(src_dict)
        type_ = d.pop("type")

        _name = d.pop("name", UNSET)
        name: PipelineStateCompletedErrorName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = PipelineStateCompletedErrorName(_name)

        _error = d.pop("error", UNSET)
        error: PipelineError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = PipelineError.from_dict(_error)

        pipeline_state_completed_error = cls(
            type_=type_,
            name=name,
            error=error,
        )

        pipeline_state_completed_error.additional_properties = d
        return pipeline_state_completed_error

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
