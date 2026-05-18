from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_ssh_public_key import PipelineSshPublicKey


T = TypeVar("T", bound="PipelineKnownHost")


@_attrs_define
class PipelineKnownHost:
    type_: str | Unset = UNSET
    uuid: str | Unset = UNSET
    """ The UUID identifying the known host. """
    hostname: str | Unset = UNSET
    """ The hostname of the known host. """
    public_key: PipelineSshPublicKey | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        hostname = self.hostname

        public_key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_key, Unset):
            public_key = self.public_key.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if public_key is not UNSET:
            field_dict["public_key"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_ssh_public_key import PipelineSshPublicKey

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        uuid = d.pop("uuid", UNSET)

        hostname = d.pop("hostname", UNSET)

        _public_key = d.pop("public_key", UNSET)
        public_key: PipelineSshPublicKey | Unset
        if isinstance(_public_key, Unset):
            public_key = UNSET
        else:
            public_key = PipelineSshPublicKey.from_dict(_public_key)

        pipeline_known_host = cls(
            type_=type_,
            uuid=uuid,
            hostname=hostname,
            public_key=public_key,
        )

        pipeline_known_host.additional_properties = d
        return pipeline_known_host

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
