from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.workspace import Workspace
    from ..models.workspace_membership_links import WorkspaceMembershipLinks


T = TypeVar("T", bound="WorkspaceMembership")


@_attrs_define
class WorkspaceMembership:
    type_: str | Unset = UNSET
    links: WorkspaceMembershipLinks | Unset = UNSET
    user: Account | Unset = UNSET
    workspace: Workspace | Unset = UNSET
    permission: str | Unset = UNSET
    """ The workspace permission level (e.g. owner, collaborator, create-project). """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        permission = self.permission

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if links is not UNSET:
            field_dict["links"] = links
        if user is not UNSET:
            field_dict["user"] = user
        if workspace is not UNSET:
            field_dict["workspace"] = workspace
        if permission is not UNSET:
            field_dict["permission"] = permission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.workspace import Workspace
        from ..models.workspace_membership_links import WorkspaceMembershipLinks

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _links = d.pop("links", UNSET)
        links: WorkspaceMembershipLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = WorkspaceMembershipLinks.from_dict(_links)

        _user = d.pop("user", UNSET)
        user: Account | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = Account.from_dict(_user)

        _workspace = d.pop("workspace", UNSET)
        workspace: Workspace | Unset
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = Workspace.from_dict(_workspace)

        permission = d.pop("permission", UNSET)

        workspace_membership = cls(
            type_=type_,
            links=links,
            user=user,
            workspace=workspace,
            permission=permission,
        )

        workspace_membership.additional_properties = d
        return workspace_membership

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
