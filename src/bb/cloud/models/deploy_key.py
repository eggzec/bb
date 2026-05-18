from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.deploy_key_links import DeployKeyLinks
    from ..models.repository import Repository


T = TypeVar("T", bound="DeployKey")


@_attrs_define
class DeployKey:
    type_: str | Unset = UNSET
    key: str | Unset = UNSET
    """ The deploy key value. """
    repository: Repository | Unset = UNSET
    comment: str | Unset = UNSET
    """ The comment parsed from the deploy key (if present) """
    label: str | Unset = UNSET
    """ The user-defined label for the deploy key """
    added_on: datetime.datetime | Unset = UNSET
    last_used: datetime.datetime | None | Unset = UNSET
    links: DeployKeyLinks | Unset = UNSET
    owner: Account | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        key = self.key

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        comment = self.comment

        label = self.label

        added_on: str | Unset = UNSET
        if not isinstance(self.added_on, Unset):
            added_on = self.added_on.isoformat()

        last_used: None | str | Unset
        if isinstance(self.last_used, Unset):
            last_used = UNSET
        elif isinstance(self.last_used, datetime.datetime):
            last_used = self.last_used.isoformat()
        else:
            last_used = self.last_used

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if key is not UNSET:
            field_dict["key"] = key
        if repository is not UNSET:
            field_dict["repository"] = repository
        if comment is not UNSET:
            field_dict["comment"] = comment
        if label is not UNSET:
            field_dict["label"] = label
        if added_on is not UNSET:
            field_dict["added_on"] = added_on
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if links is not UNSET:
            field_dict["links"] = links
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.deploy_key_links import DeployKeyLinks
        from ..models.repository import Repository

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        key = d.pop("key", UNSET)

        _repository = d.pop("repository", UNSET)
        repository: Repository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = Repository.from_dict(_repository)

        comment = d.pop("comment", UNSET)

        label = d.pop("label", UNSET)

        _added_on = d.pop("added_on", UNSET)
        added_on: datetime.datetime | Unset
        if isinstance(_added_on, Unset):
            added_on = UNSET
        else:
            added_on = isoparse(_added_on)

        def _parse_last_used(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_type_0 = isoparse(data)

                return last_used_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used = _parse_last_used(d.pop("last_used", UNSET))

        _links = d.pop("links", UNSET)
        links: DeployKeyLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DeployKeyLinks.from_dict(_links)

        _owner = d.pop("owner", UNSET)
        owner: Account | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = Account.from_dict(_owner)

        deploy_key = cls(
            type_=type_,
            key=key,
            repository=repository,
            comment=comment,
            label=label,
            added_on=added_on,
            last_used=last_used,
            links=links,
            owner=owner,
        )

        deploy_key.additional_properties = d
        return deploy_key

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
