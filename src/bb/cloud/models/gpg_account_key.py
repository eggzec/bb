from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.gpg_account_key_links import GPGAccountKeyLinks


T = TypeVar("T", bound="GPGAccountKey")


@_attrs_define
class GPGAccountKey:
    type_: str
    owner: Account | Unset = UNSET
    key: str | Unset = UNSET
    """ The GPG key value in X format. """
    key_id: str | Unset = UNSET
    """ The unique identifier for the GPG key """
    fingerprint: str | Unset = UNSET
    """ The GPG key fingerprint. """
    parent_fingerprint: str | Unset = UNSET
    """ The fingerprint of the parent key. This value is null unless the current key is a subkey. """
    comment: str | Unset = UNSET
    """ The comment parsed from the GPG key (if present) """
    name: str | Unset = UNSET
    """ The user-defined label for the GPG key """
    expires_on: datetime.datetime | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    added_on: datetime.datetime | Unset = UNSET
    last_used: datetime.datetime | Unset = UNSET
    subkeys: list[GPGAccountKey] | Unset = UNSET
    links: GPGAccountKeyLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        key = self.key

        key_id = self.key_id

        fingerprint = self.fingerprint

        parent_fingerprint = self.parent_fingerprint

        comment = self.comment

        name = self.name

        expires_on: str | Unset = UNSET
        if not isinstance(self.expires_on, Unset):
            expires_on = self.expires_on.isoformat()

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        added_on: str | Unset = UNSET
        if not isinstance(self.added_on, Unset):
            added_on = self.added_on.isoformat()

        last_used: str | Unset = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        subkeys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subkeys, Unset):
            subkeys = []
            for subkeys_item_data in self.subkeys:
                subkeys_item = subkeys_item_data.to_dict()
                subkeys.append(subkeys_item)

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
        if owner is not UNSET:
            field_dict["owner"] = owner
        if key is not UNSET:
            field_dict["key"] = key
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if parent_fingerprint is not UNSET:
            field_dict["parent_fingerprint"] = parent_fingerprint
        if comment is not UNSET:
            field_dict["comment"] = comment
        if name is not UNSET:
            field_dict["name"] = name
        if expires_on is not UNSET:
            field_dict["expires_on"] = expires_on
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if added_on is not UNSET:
            field_dict["added_on"] = added_on
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if subkeys is not UNSET:
            field_dict["subkeys"] = subkeys
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.gpg_account_key_links import GPGAccountKeyLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        _owner = d.pop("owner", UNSET)
        owner: Account | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = Account.from_dict(_owner)

        key = d.pop("key", UNSET)

        key_id = d.pop("key_id", UNSET)

        fingerprint = d.pop("fingerprint", UNSET)

        parent_fingerprint = d.pop("parent_fingerprint", UNSET)

        comment = d.pop("comment", UNSET)

        name = d.pop("name", UNSET)

        _expires_on = d.pop("expires_on", UNSET)
        expires_on: datetime.datetime | Unset
        if isinstance(_expires_on, Unset):
            expires_on = UNSET
        else:
            expires_on = isoparse(_expires_on)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _added_on = d.pop("added_on", UNSET)
        added_on: datetime.datetime | Unset
        if isinstance(_added_on, Unset):
            added_on = UNSET
        else:
            added_on = isoparse(_added_on)

        _last_used = d.pop("last_used", UNSET)
        last_used: datetime.datetime | Unset
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        _subkeys = d.pop("subkeys", UNSET)
        subkeys: list[GPGAccountKey] | Unset = UNSET
        if _subkeys is not UNSET:
            subkeys = []
            for subkeys_item_data in _subkeys:
                subkeys_item = GPGAccountKey.from_dict(subkeys_item_data)

                subkeys.append(subkeys_item)

        _links = d.pop("links", UNSET)
        links: GPGAccountKeyLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GPGAccountKeyLinks.from_dict(_links)

        gpg_account_key = cls(
            type_=type_,
            owner=owner,
            key=key,
            key_id=key_id,
            fingerprint=fingerprint,
            parent_fingerprint=parent_fingerprint,
            comment=comment,
            name=name,
            expires_on=expires_on,
            created_on=created_on,
            added_on=added_on,
            last_used=last_used,
            subkeys=subkeys,
            links=links,
        )

        gpg_account_key.additional_properties = d
        return gpg_account_key

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
