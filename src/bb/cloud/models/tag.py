from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
    date: datetime.datetime | None | Unset = UNSET
    """ The date that the tag was created, if available """
    tagger: Author | None | Unset = UNSET
    """ The author that tagged this commit, if available. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.author import Author

        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        message = self.message

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        tagger: dict[str, Any] | None | Unset
        if isinstance(self.tagger, Unset):
            tagger = UNSET
        elif isinstance(self.tagger, Author):
            tagger = self.tagger.to_dict()
        else:
            tagger = self.tagger

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

        def _parse_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_tagger(data: object) -> Author | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tagger_type_0 = Author.from_dict(data)

                return tagger_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Author | None | Unset, data)

        tagger = _parse_tagger(d.pop("tagger", UNSET))

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
