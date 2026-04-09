from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.author import Author
    from ..models.commit import Commit
    from ..models.ref_links import RefLinks


T = TypeVar("T", bound="Tag")


@_attrs_define
class Tag:
    type_: str
    links: RefLinks | Unset = UNSET
    name: str | Unset = UNSET
    """ The name of the ref. """
    target: Commit | Unset = UNSET
    message: str | Unset = UNSET
    """ The message associated with the tag, if available. """
    date: datetime.datetime | Unset = UNSET
    """ The date that the tag was created, if available """
    tagger: Author | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        message = self.message

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        tagger: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tagger, Unset):
            tagger = self.tagger.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if target is not UNSET:
            field_dict["target"] = target
        if message is not UNSET:
            field_dict["message"] = message
        if date is not UNSET:
            field_dict["date"] = date
        if tagger is not UNSET:
            field_dict["tagger"] = tagger

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.author import Author
        from ..models.commit import Commit
        from ..models.ref_links import RefLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: RefLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RefLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        _target = d.pop("target", UNSET)
        target: Commit | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = Commit.from_dict(_target)

        message = d.pop("message", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _tagger = d.pop("tagger", UNSET)
        tagger: Author | Unset
        if isinstance(_tagger, Unset):
            tagger = UNSET
        else:
            tagger = Author.from_dict(_tagger)

        tag = cls(
            type_=type_,
            links=links,
            name=name,
            target=target,
            message=message,
            date=date,
            tagger=tagger,
        )

        tag.additional_properties = d
        return tag

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
