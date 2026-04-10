from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_user_reaction_comment import RestUserReactionComment
    from ..models.rest_user_reaction_emoticon import RestUserReactionEmoticon
    from ..models.rest_user_reaction_user import RestUserReactionUser


T = TypeVar("T", bound="RestUserReaction")


@_attrs_define
class RestUserReaction:
    comment: RestUserReactionComment | Unset = UNSET
    emoticon: RestUserReactionEmoticon | Unset = UNSET
    user: RestUserReactionUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        emoticon: dict[str, Any] | Unset = UNSET
        if not isinstance(self.emoticon, Unset):
            emoticon = self.emoticon.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if emoticon is not UNSET:
            field_dict["emoticon"] = emoticon
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_user_reaction_comment import RestUserReactionComment
        from ..models.rest_user_reaction_emoticon import RestUserReactionEmoticon
        from ..models.rest_user_reaction_user import RestUserReactionUser

        d = dict(src_dict)
        _comment = d.pop("comment", UNSET)
        comment: RestUserReactionComment | Unset
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = RestUserReactionComment.from_dict(_comment)

        _emoticon = d.pop("emoticon", UNSET)
        emoticon: RestUserReactionEmoticon | Unset
        if isinstance(_emoticon, Unset):
            emoticon = UNSET
        else:
            emoticon = RestUserReactionEmoticon.from_dict(_emoticon)

        _user = d.pop("user", UNSET)
        user: RestUserReactionUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RestUserReactionUser.from_dict(_user)

        rest_user_reaction = cls(
            comment=comment,
            emoticon=emoticon,
            user=user,
        )

        rest_user_reaction.additional_properties = d
        return rest_user_reaction

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
