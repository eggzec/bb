from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_repository_hook_veto import RestRepositoryHookVeto


T = TypeVar("T", bound="RestPullRequestRebaseability")


@_attrs_define
class RestPullRequestRebaseability:
    vetoes: list[RestRepositoryHookVeto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vetoes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vetoes, Unset):
            vetoes = []
            for vetoes_item_data in self.vetoes:
                vetoes_item = vetoes_item_data.to_dict()
                vetoes.append(vetoes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vetoes is not UNSET:
            field_dict["vetoes"] = vetoes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_repository_hook_veto import RestRepositoryHookVeto

        d = dict(src_dict)
        _vetoes = d.pop("vetoes", UNSET)
        vetoes: list[RestRepositoryHookVeto] | Unset = UNSET
        if _vetoes is not UNSET:
            vetoes = []
            for vetoes_item_data in _vetoes:
                vetoes_item = RestRepositoryHookVeto.from_dict(vetoes_item_data)

                vetoes.append(vetoes_item)

        rest_pull_request_rebaseability = cls(
            vetoes=vetoes,
        )

        rest_pull_request_rebaseability.additional_properties = d
        return rest_pull_request_rebaseability

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
