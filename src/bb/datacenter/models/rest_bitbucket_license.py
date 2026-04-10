from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_bitbucket_license_status import RestBitbucketLicenseStatus


T = TypeVar("T", bound="RestBitbucketLicense")


@_attrs_define
class RestBitbucketLicense:
    creation_date: int | Unset = UNSET
    days_before_expiry: int | Unset = UNSET
    expiry_date: int | Unset = UNSET
    grace_period_end_date: int | Unset = UNSET
    license_: str | Unset = UNSET
    maintenance_expiry_date: int | Unset = UNSET
    maximum_number_of_users: int | Unset = UNSET
    number_of_days_before_expiry: int | Unset = UNSET
    number_of_days_before_grace_period_expiry: int | Unset = UNSET
    number_of_days_before_maintenance_expiry: int | Unset = UNSET
    purchase_date: int | Unset = UNSET
    server_id: str | Unset = UNSET
    status: RestBitbucketLicenseStatus | Unset = UNSET
    support_entitlement_number: str | Unset = UNSET
    unlimited_number_of_users: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creation_date = self.creation_date

        days_before_expiry = self.days_before_expiry

        expiry_date = self.expiry_date

        grace_period_end_date = self.grace_period_end_date

        license_ = self.license_

        maintenance_expiry_date = self.maintenance_expiry_date

        maximum_number_of_users = self.maximum_number_of_users

        number_of_days_before_expiry = self.number_of_days_before_expiry

        number_of_days_before_grace_period_expiry = self.number_of_days_before_grace_period_expiry

        number_of_days_before_maintenance_expiry = self.number_of_days_before_maintenance_expiry

        purchase_date = self.purchase_date

        server_id = self.server_id

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        support_entitlement_number = self.support_entitlement_number

        unlimited_number_of_users = self.unlimited_number_of_users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if days_before_expiry is not UNSET:
            field_dict["daysBeforeExpiry"] = days_before_expiry
        if expiry_date is not UNSET:
            field_dict["expiryDate"] = expiry_date
        if grace_period_end_date is not UNSET:
            field_dict["gracePeriodEndDate"] = grace_period_end_date
        if license_ is not UNSET:
            field_dict["license"] = license_
        if maintenance_expiry_date is not UNSET:
            field_dict["maintenanceExpiryDate"] = maintenance_expiry_date
        if maximum_number_of_users is not UNSET:
            field_dict["maximumNumberOfUsers"] = maximum_number_of_users
        if number_of_days_before_expiry is not UNSET:
            field_dict["numberOfDaysBeforeExpiry"] = number_of_days_before_expiry
        if number_of_days_before_grace_period_expiry is not UNSET:
            field_dict["numberOfDaysBeforeGracePeriodExpiry"] = number_of_days_before_grace_period_expiry
        if number_of_days_before_maintenance_expiry is not UNSET:
            field_dict["numberOfDaysBeforeMaintenanceExpiry"] = number_of_days_before_maintenance_expiry
        if purchase_date is not UNSET:
            field_dict["purchaseDate"] = purchase_date
        if server_id is not UNSET:
            field_dict["serverId"] = server_id
        if status is not UNSET:
            field_dict["status"] = status
        if support_entitlement_number is not UNSET:
            field_dict["supportEntitlementNumber"] = support_entitlement_number
        if unlimited_number_of_users is not UNSET:
            field_dict["unlimitedNumberOfUsers"] = unlimited_number_of_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_bitbucket_license_status import RestBitbucketLicenseStatus

        d = dict(src_dict)
        creation_date = d.pop("creationDate", UNSET)

        days_before_expiry = d.pop("daysBeforeExpiry", UNSET)

        expiry_date = d.pop("expiryDate", UNSET)

        grace_period_end_date = d.pop("gracePeriodEndDate", UNSET)

        license_ = d.pop("license", UNSET)

        maintenance_expiry_date = d.pop("maintenanceExpiryDate", UNSET)

        maximum_number_of_users = d.pop("maximumNumberOfUsers", UNSET)

        number_of_days_before_expiry = d.pop("numberOfDaysBeforeExpiry", UNSET)

        number_of_days_before_grace_period_expiry = d.pop("numberOfDaysBeforeGracePeriodExpiry", UNSET)

        number_of_days_before_maintenance_expiry = d.pop("numberOfDaysBeforeMaintenanceExpiry", UNSET)

        purchase_date = d.pop("purchaseDate", UNSET)

        server_id = d.pop("serverId", UNSET)

        _status = d.pop("status", UNSET)
        status: RestBitbucketLicenseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RestBitbucketLicenseStatus.from_dict(_status)

        support_entitlement_number = d.pop("supportEntitlementNumber", UNSET)

        unlimited_number_of_users = d.pop("unlimitedNumberOfUsers", UNSET)

        rest_bitbucket_license = cls(
            creation_date=creation_date,
            days_before_expiry=days_before_expiry,
            expiry_date=expiry_date,
            grace_period_end_date=grace_period_end_date,
            license_=license_,
            maintenance_expiry_date=maintenance_expiry_date,
            maximum_number_of_users=maximum_number_of_users,
            number_of_days_before_expiry=number_of_days_before_expiry,
            number_of_days_before_grace_period_expiry=number_of_days_before_grace_period_expiry,
            number_of_days_before_maintenance_expiry=number_of_days_before_maintenance_expiry,
            purchase_date=purchase_date,
            server_id=server_id,
            status=status,
            support_entitlement_number=support_entitlement_number,
            unlimited_number_of_users=unlimited_number_of_users,
        )

        rest_bitbucket_license.additional_properties = d
        return rest_bitbucket_license

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
