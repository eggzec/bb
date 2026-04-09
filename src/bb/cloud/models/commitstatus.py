from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.commitstatus_state import CommitstatusState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commitstatus_links import CommitstatusLinks


T = TypeVar("T", bound="Commitstatus")


@_attrs_define
class Commitstatus:
    type_: str
    key: str
    """ An identifier for the status that's unique to
            its type (current "build" is the only supported type) and the vendor,
            e.g. BB-DEPLOY """
    state: CommitstatusState
    """ Provides some indication of the status of this commit """
    links: CommitstatusLinks | Unset = UNSET
    refname: str | Unset = UNSET
    """
    The name of the ref that pointed to this commit at the time the status
    object was created. Note that this the ref may since have moved off of
    the commit. This optional field can be useful for build systems whose
    build triggers and configuration are branch-dependent (e.g. a Pipeline
    build).
    It is legitimate for this field to not be set, or even apply (e.g. a
    static linting job). """
    url: str | Unset = UNSET
    """ A URL linking back to the vendor or build system, for providing more information about whatever process
    produced this status. Accepts context variables `repository` and `commit` that Bitbucket will evaluate at
    runtime whenever at runtime. For example, one could use https://foo.com/builds/{repository.full_name} which
    Bitbucket will turn into https://foo.com/builds/foo/bar at render time. """
    name: str | Unset = UNSET
    """ An identifier for the build itself, e.g. BB-DEPLOY-1 """
    description: str | Unset = UNSET
    """ A description of the build (e.g. "Unit tests in Bamboo") """
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        key = self.key

        state = self.state.value

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        refname = self.refname

        url = self.url

        name = self.name

        description = self.description

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "key": key,
                "state": state,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if refname is not UNSET:
            field_dict["refname"] = refname
        if url is not UNSET:
            field_dict["url"] = url
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commitstatus_links import CommitstatusLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        key = d.pop("key")

        state = CommitstatusState(d.pop("state"))

        _links = d.pop("links", UNSET)
        links: CommitstatusLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CommitstatusLinks.from_dict(_links)

        refname = d.pop("refname", UNSET)

        url = d.pop("url", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

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

        commitstatus = cls(
            type_=type_,
            key=key,
            state=state,
            links=links,
            refname=refname,
            url=url,
            name=name,
            description=description,
            created_on=created_on,
            updated_on=updated_on,
        )

        commitstatus.additional_properties = d
        return commitstatus

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
