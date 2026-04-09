from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.issue_change_message_markup import IssueChangeMessageMarkup
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueChangeMessage")


@_attrs_define
class IssueChangeMessage:
    raw: str | Unset = UNSET
    """ The text as it was typed by a user. """
    markup: IssueChangeMessageMarkup | Unset = UNSET
    """ The type of markup language the raw content is to be interpreted in. """
    html: str | Unset = UNSET
    """ The user's content rendered as HTML. """

    def to_dict(self) -> dict[str, Any]:
        raw = self.raw

        markup: str | Unset = UNSET
        if not isinstance(self.markup, Unset):
            markup = self.markup.value

        html = self.html

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if raw is not UNSET:
            field_dict["raw"] = raw
        if markup is not UNSET:
            field_dict["markup"] = markup
        if html is not UNSET:
            field_dict["html"] = html

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        raw = d.pop("raw", UNSET)

        _markup = d.pop("markup", UNSET)
        markup: IssueChangeMessageMarkup | Unset
        if isinstance(_markup, Unset):
            markup = UNSET
        else:
            markup = IssueChangeMessageMarkup(_markup)

        html = d.pop("html", UNSET)

        issue_change_message = cls(
            raw=raw,
            markup=markup,
            html=html,
        )

        return issue_change_message
