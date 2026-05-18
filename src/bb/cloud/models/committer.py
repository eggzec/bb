from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="Committer")


@_attrs_define
class Committer:
    type_: str | Unset = UNSET
    raw: str | Unset = UNSET
    """ The raw committer value from the repository. This may be the only value available if the committer does not
    match a user in Bitbucket. """
    user: Account | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        raw = self.raw

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if raw is not UNSET:
            field_dict["raw"] = raw
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        raw = d.pop("raw", UNSET)

        _user = d.pop("user", UNSET)
        user: Account | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Account.from_dict(_user)

        committer = cls(
            type_=type_,
            raw=raw,
            user=user,
        )

        committer.additional_properties = d
        return committer

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
