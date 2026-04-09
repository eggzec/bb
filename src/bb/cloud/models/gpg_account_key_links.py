from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="GPGAccountKeyLinks")


@_attrs_define
class GPGAccountKeyLinks:
    self_: Link | Unset = UNSET
    """ A link to a resource related to this object. """

    def to_dict(self) -> dict[str, Any]:
        self_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Link | Unset
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = Link.from_dict(_self_)

        gpg_account_key_links = cls(
            self_=self_,
        )

        return gpg_account_key_links
