from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_repository_ref_change_activity_ref_change import RestRepositoryRefChangeActivityRefChange
    from ..models.rest_repository_ref_change_activity_repository import RestRepositoryRefChangeActivityRepository
    from ..models.rest_repository_ref_change_activity_user import RestRepositoryRefChangeActivityUser


T = TypeVar("T", bound="RestRepositoryRefChangeActivity")


@_attrs_define
class RestRepositoryRefChangeActivity:
    created_date: int | Unset = UNSET
    id: int | Unset = UNSET
    ref_change: RestRepositoryRefChangeActivityRefChange | Unset = UNSET
    repository: RestRepositoryRefChangeActivityRepository | Unset = UNSET
    trigger: str | Unset = UNSET
    user: RestRepositoryRefChangeActivityUser | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_date = self.created_date

        id = self.id

        ref_change: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ref_change, Unset):
            ref_change = self.ref_change.to_dict()

        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        trigger = self.trigger

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if id is not UNSET:
            field_dict["id"] = id
        if ref_change is not UNSET:
            field_dict["refChange"] = ref_change
        if repository is not UNSET:
            field_dict["repository"] = repository
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_repository_ref_change_activity_ref_change import RestRepositoryRefChangeActivityRefChange
        from ..models.rest_repository_ref_change_activity_repository import RestRepositoryRefChangeActivityRepository
        from ..models.rest_repository_ref_change_activity_user import RestRepositoryRefChangeActivityUser

        d = dict(src_dict)
        created_date = d.pop("createdDate", UNSET)

        id = d.pop("id", UNSET)

        _ref_change = d.pop("refChange", UNSET)
        ref_change: RestRepositoryRefChangeActivityRefChange | Unset
        if isinstance(_ref_change, Unset):
            ref_change = UNSET
        else:
            ref_change = RestRepositoryRefChangeActivityRefChange.from_dict(_ref_change)

        _repository = d.pop("repository", UNSET)
        repository: RestRepositoryRefChangeActivityRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = RestRepositoryRefChangeActivityRepository.from_dict(_repository)

        trigger = d.pop("trigger", UNSET)

        _user = d.pop("user", UNSET)
        user: RestRepositoryRefChangeActivityUser | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = RestRepositoryRefChangeActivityUser.from_dict(_user)

        rest_repository_ref_change_activity = cls(
            created_date=created_date,
            id=id,
            ref_change=ref_change,
            repository=repository,
            trigger=trigger,
            user=user,
        )

        rest_repository_ref_change_activity.additional_properties = d
        return rest_repository_ref_change_activity

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
