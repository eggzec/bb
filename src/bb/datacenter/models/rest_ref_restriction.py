from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_application_user import RestApplicationUser
    from ..models.rest_ref_restriction_matcher import RestRefRestrictionMatcher
    from ..models.rest_ref_restriction_scope import RestRefRestrictionScope
    from ..models.rest_ssh_access_key import RestSshAccessKey


T = TypeVar("T", bound="RestRefRestriction")


@_attrs_define
class RestRefRestriction:
    access_keys: list[RestSshAccessKey] | Unset = UNSET
    groups: list[str] | Unset = UNSET
    id: int | Unset = UNSET
    matcher: RestRefRestrictionMatcher | Unset = UNSET
    scope: RestRefRestrictionScope | Unset = UNSET
    type_: str | Unset = UNSET
    users: list[RestApplicationUser] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.access_keys, Unset):
            access_keys = []
            for access_keys_item_data in self.access_keys:
                access_keys_item = access_keys_item_data.to_dict()
                access_keys.append(access_keys_item)

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        id = self.id

        matcher: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matcher, Unset):
            matcher = self.matcher.to_dict()

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        type_ = self.type_

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_keys is not UNSET:
            field_dict["accessKeys"] = access_keys
        if groups is not UNSET:
            field_dict["groups"] = groups
        if id is not UNSET:
            field_dict["id"] = id
        if matcher is not UNSET:
            field_dict["matcher"] = matcher
        if scope is not UNSET:
            field_dict["scope"] = scope
        if type_ is not UNSET:
            field_dict["type"] = type_
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_application_user import RestApplicationUser
        from ..models.rest_ref_restriction_matcher import RestRefRestrictionMatcher
        from ..models.rest_ref_restriction_scope import RestRefRestrictionScope
        from ..models.rest_ssh_access_key import RestSshAccessKey

        d = dict(src_dict)
        _access_keys = d.pop("accessKeys", UNSET)
        access_keys: list[RestSshAccessKey] | Unset = UNSET
        if _access_keys is not UNSET:
            access_keys = []
            for access_keys_item_data in _access_keys:
                access_keys_item = RestSshAccessKey.from_dict(access_keys_item_data)

                access_keys.append(access_keys_item)

        groups = cast(list[str], d.pop("groups", UNSET))

        id = d.pop("id", UNSET)

        _matcher = d.pop("matcher", UNSET)
        matcher: RestRefRestrictionMatcher | Unset
        if isinstance(_matcher, Unset):
            matcher = UNSET
        else:
            matcher = RestRefRestrictionMatcher.from_dict(_matcher)

        _scope = d.pop("scope", UNSET)
        scope: RestRefRestrictionScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RestRefRestrictionScope.from_dict(_scope)

        type_ = d.pop("type", UNSET)

        _users = d.pop("users", UNSET)
        users: list[RestApplicationUser] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = RestApplicationUser.from_dict(users_item_data)

                users.append(users_item)

        rest_ref_restriction = cls(
            access_keys=access_keys,
            groups=groups,
            id=id,
            matcher=matcher,
            scope=scope,
            type_=type_,
            users=users,
        )

        rest_ref_restriction.additional_properties = d
        return rest_ref_restriction

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
