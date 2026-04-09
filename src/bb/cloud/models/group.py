from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.group_links import GroupLinks
    from ..models.workspace import Workspace


T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    type_: str
    links: GroupLinks | Unset = UNSET
    owner: Account | Unset = UNSET
    workspace: Workspace | Unset = UNSET
    name: str | Unset = UNSET
    slug: str | Unset = UNSET
    """ The "sluggified" version of the group's name. This contains only ASCII
    characters and can therefore be slightly different than the name """
    full_slug: str | Unset = UNSET
    """ The concatenation of the workspace's slug and the group's slug,
    separated with a colon (e.g. `acme:developers`)
     """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        name = self.name

        slug = self.slug

        full_slug = self.full_slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links
        if owner is not UNSET:
            field_dict["owner"] = owner
        if workspace is not UNSET:
            field_dict["workspace"] = workspace
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if full_slug is not UNSET:
            field_dict["full_slug"] = full_slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.group_links import GroupLinks
        from ..models.workspace import Workspace

        d = dict(src_dict)
        type_ = d.pop("type")

        _links = d.pop("links", UNSET)
        links: GroupLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GroupLinks.from_dict(_links)

        _owner = d.pop("owner", UNSET)
        owner: Account | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = Account.from_dict(_owner)

        _workspace = d.pop("workspace", UNSET)
        workspace: Workspace | Unset
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = Workspace.from_dict(_workspace)

        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        full_slug = d.pop("full_slug", UNSET)

        group = cls(
            type_=type_,
            links=links,
            owner=owner,
            workspace=workspace,
            name=name,
            slug=slug,
            full_slug=full_slug,
        )

        group.additional_properties = d
        return group

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
