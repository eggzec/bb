from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssh_key_links import SshKeyLinks


T = TypeVar("T", bound="SshKey")


@_attrs_define
class SshKey:
    type_: str
    uuid: str | Unset = UNSET
    """ The SSH key's immutable ID. """
    key: str | Unset = UNSET
    """ The SSH public key value in OpenSSH format. """
    comment: str | Unset = UNSET
    """ The comment parsed from the SSH key (if present) """
    label: str | Unset = UNSET
    """ The user-defined label for the SSH key """
    created_on: datetime.datetime | Unset = UNSET
    last_used: datetime.datetime | Unset = UNSET
    links: SshKeyLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        key = self.key

        comment = self.comment

        label = self.label

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        last_used: str | Unset = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if key is not UNSET:
            field_dict["key"] = key
        if comment is not UNSET:
            field_dict["comment"] = comment
        if label is not UNSET:
            field_dict["label"] = label
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ssh_key_links import SshKeyLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        key = d.pop("key", UNSET)

        comment = d.pop("comment", UNSET)

        label = d.pop("label", UNSET)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _last_used = d.pop("last_used", UNSET)
        last_used: datetime.datetime | Unset
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        _links = d.pop("links", UNSET)
        links: SshKeyLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SshKeyLinks.from_dict(_links)

        ssh_key = cls(
            type_=type_,
            uuid=uuid,
            key=key,
            comment=comment,
            label=label,
            created_on=created_on,
            last_used=last_used,
            links=links,
        )

        ssh_key.additional_properties = d
        return ssh_key

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
