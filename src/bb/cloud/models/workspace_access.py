from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workspace_base import WorkspaceBase


T = TypeVar("T", bound="WorkspaceAccess")


@_attrs_define
class WorkspaceAccess:
    type_: str | Unset = UNSET
    administrator: bool | Unset = UNSET
    """ The permission level the user has for the workspace. True if the user is an administrator, otherwise False.
    """
    workspace: WorkspaceBase | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        administrator = self.administrator

        workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if administrator is not UNSET:
            field_dict["administrator"] = administrator
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workspace_base import WorkspaceBase

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        administrator = d.pop("administrator", UNSET)

        _workspace = d.pop("workspace", UNSET)
        workspace: WorkspaceBase | Unset
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = WorkspaceBase.from_dict(_workspace)

        workspace_access = cls(
            type_=type_,
            administrator=administrator,
            workspace=workspace,
        )

        workspace_access.additional_properties = d
        return workspace_access

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
