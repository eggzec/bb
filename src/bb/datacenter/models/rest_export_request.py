from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_export_request_repositories_request import RestExportRequestRepositoriesRequest


T = TypeVar("T", bound="RestExportRequest")


@_attrs_define
class RestExportRequest:
    repositories_request: RestExportRequestRepositoriesRequest
    export_location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repositories_request = self.repositories_request.to_dict()

        export_location = self.export_location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repositoriesRequest": repositories_request,
            }
        )
        if export_location is not UNSET:
            field_dict["exportLocation"] = export_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_export_request_repositories_request import RestExportRequestRepositoriesRequest

        d = dict(src_dict)
        repositories_request = RestExportRequestRepositoriesRequest.from_dict(d.pop("repositoriesRequest"))

        export_location = d.pop("exportLocation", UNSET)

        rest_export_request = cls(
            repositories_request=repositories_request,
            export_location=export_location,
        )

        rest_export_request.additional_properties = d
        return rest_export_request

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
