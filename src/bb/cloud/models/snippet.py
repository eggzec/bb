from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.snippet_scm import SnippetScm
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="Snippet")


@_attrs_define
class Snippet:
    type_: str
    id: int | Unset = UNSET
    title: str | Unset = UNSET
    scm: SnippetScm | Unset = UNSET
    """ The DVCS used to store the snippet. """
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    owner: Account | Unset = UNSET
    creator: Account | Unset = UNSET
    is_private: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        title = self.title

        scm: str | Unset = UNSET
        if not isinstance(self.scm, Unset):
            scm = self.scm.value

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        is_private = self.is_private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if scm is not UNSET:
            field_dict["scm"] = scm
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on
        if owner is not UNSET:
            field_dict["owner"] = owner
        if creator is not UNSET:
            field_dict["creator"] = creator
        if is_private is not UNSET:
            field_dict["is_private"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account

        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        _scm = d.pop("scm", UNSET)
        scm: SnippetScm | Unset
        if isinstance(_scm, Unset):
            scm = UNSET
        else:
            scm = SnippetScm(_scm)

        _created_on = d.pop("created_on", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)

        _updated_on = d.pop("updated_on", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)

        _owner = d.pop("owner", UNSET)
        owner: Account | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = Account.from_dict(_owner)

        _creator = d.pop("creator", UNSET)
        creator: Account | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = Account.from_dict(_creator)

        is_private = d.pop("is_private", UNSET)

        snippet = cls(
            type_=type_,
            id=id,
            title=title,
            scm=scm,
            created_on=created_on,
            updated_on=updated_on,
            owner=owner,
            creator=creator,
            is_private=is_private,
        )

        snippet.additional_properties = d
        return snippet

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
