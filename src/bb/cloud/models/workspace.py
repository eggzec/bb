from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.workspace_forking_mode import WorkspaceForkingMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_links import WorkspaceLinks


T = TypeVar("T", bound="Workspace")


@_attrs_define
class Workspace:
    type_: str
    links: WorkspaceLinks | Unset = UNSET
    uuid: str | Unset = UNSET
    """ The workspace's immutable id. """
    name: str | Unset = UNSET
    """ The name of the workspace. """
    slug: str | Unset = UNSET
    """ The short label that identifies this workspace. """
    is_private: bool | Unset = UNSET
    """ Indicates whether the workspace is publicly accessible, or whether it is
    private to the members and consequently only visible to members. """
    is_privacy_enforced: bool | Unset = UNSET
    """ Indicates whether the workspace enforces private content, or whether it allows public content. """
    forking_mode: WorkspaceForkingMode | Unset = UNSET
    """ Controls the rules for forking repositories within this workspace.

    * **allow_forks**: unrestricted forking
    * **internal_only**: prevents forking of private repositories outside the workspace or to public repositories
     """
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        uuid = self.uuid

        name = self.name

        slug = self.slug

        is_private = self.is_private

        is_privacy_enforced = self.is_privacy_enforced

        forking_mode: str | Unset = UNSET
        if not isinstance(self.forking_mode, Unset):
            forking_mode = self.forking_mode.value

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
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if is_private is not UNSET:
            field_dict["is_private"] = is_private
        if is_privacy_enforced is not UNSET:
            field_dict["is_privacy_enforced"] = is_privacy_enforced
        if forking_mode is not UNSET:
            field_dict["forking_mode"] = forking_mode
        if created_on is not UNSET:
            field_dict["created_on"] = created_on
        if updated_on is not UNSET:
            field_dict["updated_on"] = updated_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace_links import WorkspaceLinks

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: WorkspaceLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WorkspaceLinks.from_dict(_links)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        is_private = d.pop("is_private", UNSET)

        is_privacy_enforced = d.pop("is_privacy_enforced", UNSET)

        _forking_mode = d.pop("forking_mode", UNSET)
        forking_mode: WorkspaceForkingMode | Unset
        if isinstance(_forking_mode, Unset):
            forking_mode = UNSET
        else:
            forking_mode = WorkspaceForkingMode(_forking_mode)

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

        workspace = cls(
            type_=type_,
            links=links,
            uuid=uuid,
            name=name,
            slug=slug,
            is_private=is_private,
            is_privacy_enforced=is_privacy_enforced,
            forking_mode=forking_mode,
            created_on=created_on,
            updated_on=updated_on,
        )

        workspace.additional_properties = d
        return workspace

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
