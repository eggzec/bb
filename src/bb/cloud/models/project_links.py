from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="ProjectLinks")


@_attrs_define
class ProjectLinks:
    html: Link | Unset = UNSET
    """ A link to a resource related to this object. """
    avatar: Link | Unset = UNSET
    """ A link to a resource related to this object. """

    def to_dict(self) -> dict[str, Any]:
        html: dict[str, Any] | Unset = UNSET
        if not isinstance(self.html, Unset):
            html = self.html.to_dict()

        avatar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if html is not UNSET:
            field_dict["html"] = html
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link

        d = dict(src_dict)
        _html = d.pop("html", UNSET)
        html: Link | Unset
        if isinstance(_html, Unset):
            html = UNSET
        else:
            html = Link.from_dict(_html)

        _avatar = d.pop("avatar", UNSET)
        avatar: Link | Unset
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Link.from_dict(_avatar)

        project_links = cls(
            html=html,
            avatar=avatar,
        )

        return project_links
