from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_environment_category import DeploymentEnvironmentCategory
    from ..models.deployment_environment_lock import DeploymentEnvironmentLock
    from ..models.deployment_environment_restrictions import DeploymentEnvironmentRestrictions
    from ..models.deployment_environment_type import DeploymentEnvironmentType


T = TypeVar("T", bound="DeploymentEnvironment")


@_attrs_define
class DeploymentEnvironment:
    type_: str | Unset = UNSET
    """ The type discriminator for this object. """
    uuid: str | Unset = UNSET
    """ The UUID identifying the environment. """
    name: str | Unset = UNSET
    """ The name of the environment. """
    environment_type: DeploymentEnvironmentType | Unset = UNSET
    """ The type of a deployment environment (Test, Staging, Production). """
    slug: str | Unset = UNSET
    """ URL-safe environment name. """
    rank: int | Unset = UNSET
    """ Sort order for the environment (0=Test, 1=Staging, 2=Production). """
    hidden: bool | Unset = UNSET
    """ Whether the environment is hidden in the UI. """
    deployment_gate_enabled: bool | Unset = UNSET
    """ Whether deployment gates are enabled for this environment. """
    environment_lock_enabled: bool | Unset = UNSET
    """ Whether the environment has a deployment lock enabled. """
    category: DeploymentEnvironmentCategory | Unset = UNSET
    """ The category of this environment (e.g. Test, Staging, Production). """
    lock: DeploymentEnvironmentLock | Unset = UNSET
    """ Current lock state of this environment, including lock opener and triggerer. """
    restrictions: DeploymentEnvironmentRestrictions | Unset = UNSET
    """ Deployment restrictions configuration for this environment. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        name = self.name

        environment_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment_type, Unset):
            environment_type = self.environment_type.to_dict()

        slug = self.slug

        rank = self.rank

        hidden = self.hidden

        deployment_gate_enabled = self.deployment_gate_enabled

        environment_lock_enabled = self.environment_lock_enabled

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        lock: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lock, Unset):
            lock = self.lock.to_dict()

        restrictions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if environment_type is not UNSET:
            field_dict["environment_type"] = environment_type
        if slug is not UNSET:
            field_dict["slug"] = slug
        if rank is not UNSET:
            field_dict["rank"] = rank
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if deployment_gate_enabled is not UNSET:
            field_dict["deployment_gate_enabled"] = deployment_gate_enabled
        if environment_lock_enabled is not UNSET:
            field_dict["environment_lock_enabled"] = environment_lock_enabled
        if category is not UNSET:
            field_dict["category"] = category
        if lock is not UNSET:
            field_dict["lock"] = lock
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_environment_category import DeploymentEnvironmentCategory
        from ..models.deployment_environment_lock import DeploymentEnvironmentLock
        from ..models.deployment_environment_restrictions import DeploymentEnvironmentRestrictions
        from ..models.deployment_environment_type import DeploymentEnvironmentType

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        _environment_type = d.pop("environment_type", UNSET)
        environment_type: DeploymentEnvironmentType | Unset
        if isinstance(_environment_type, Unset):
            environment_type = UNSET
        else:
            environment_type = DeploymentEnvironmentType.from_dict(_environment_type)

        slug = d.pop("slug", UNSET)

        rank = d.pop("rank", UNSET)

        hidden = d.pop("hidden", UNSET)

        deployment_gate_enabled = d.pop("deployment_gate_enabled", UNSET)

        environment_lock_enabled = d.pop("environment_lock_enabled", UNSET)

        _category = d.pop("category", UNSET)
        category: DeploymentEnvironmentCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = DeploymentEnvironmentCategory.from_dict(_category)

        _lock = d.pop("lock", UNSET)
        lock: DeploymentEnvironmentLock | Unset
        if isinstance(_lock, Unset):
            lock = UNSET
        else:
            lock = DeploymentEnvironmentLock.from_dict(_lock)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: DeploymentEnvironmentRestrictions | Unset
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = DeploymentEnvironmentRestrictions.from_dict(_restrictions)

        deployment_environment = cls(
            type_=type_,
            uuid=uuid,
            name=name,
            environment_type=environment_type,
            slug=slug,
            rank=rank,
            hidden=hidden,
            deployment_gate_enabled=deployment_gate_enabled,
            environment_lock_enabled=environment_lock_enabled,
            category=category,
            lock=lock,
            restrictions=restrictions,
        )

        deployment_environment.additional_properties = d
        return deployment_environment

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
