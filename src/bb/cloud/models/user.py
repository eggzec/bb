from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_links import AccountLinks


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    type_: str | Unset = UNSET
    links: AccountLinks | Unset = UNSET
    """ Links related to an Account. """
    created_on: datetime.datetime | Unset = UNSET
    display_name: str | Unset = UNSET
    uuid: str | Unset = UNSET
    account_id: str | Unset = UNSET
    """ The user's Atlassian account ID. """
    account_status: str | Unset = UNSET
    """ The status of the account. Currently the only possible value is "active", but more values may be added in
    the future. """
    has_2fa_enabled: bool | Unset = UNSET
    nickname: str | Unset = UNSET
    """ Account name defined by the owner. Should be used instead of the "username" field. Note that "nickname"
    cannot be used in place of "username" in URLs and queries, as "nickname" is not guaranteed to be unique. """
    is_staff: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        display_name = self.display_name

        uuid = self.uuid

        account_id = self.account_id

        account_status = self.account_status

        has_2fa_enabled = self.has_2fa_enabled

        nickname = self.nickname

        is_staff = self.is_staff

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if links is not UNSET:
            field_dict["links"] = links
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if account_status is not UNSET:
            field_dict["account_status"] = account_status
        if has_2fa_enabled is not UNSET:
            field_dict["has_2fa_enabled"] = has_2fa_enabled
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_links import AccountLinks

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _links = d.pop("links", UNSET)
        links: AccountLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AccountLinks.from_dict(_links)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        display_name = d.pop("display_name", UNSET)

        uuid = d.pop("uuid", UNSET)

        account_id = d.pop("account_id", UNSET)

        account_status = d.pop("account_status", UNSET)

        has_2fa_enabled = d.pop("has_2fa_enabled", UNSET)

        nickname = d.pop("nickname", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        user = cls(
            type_=type_,
            links=links,
            created_on=created_on,
            display_name=display_name,
            uuid=uuid,
            account_id=account_id,
            account_status=account_status,
            has_2fa_enabled=has_2fa_enabled,
            nickname=nickname,
            is_staff=is_staff,
        )

        user.additional_properties = d
        return user

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
