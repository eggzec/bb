from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webhook_subscription_events_item import WebhookSubscriptionEventsItem
from ..models.webhook_subscription_subject_type import WebhookSubscriptionSubjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_ import Object


T = TypeVar("T", bound="WebhookSubscription")


@_attrs_define
class WebhookSubscription:
    type_: str
    uuid: str | Unset = UNSET
    """ The webhook's id """
    url: str | Unset = UNSET
    """ The URL events get delivered to. """
    description: str | Unset = UNSET
    """ A user-defined description of the webhook. """
    subject_type: WebhookSubscriptionSubjectType | Unset = UNSET
    """ The type of entity. Set to either `repository` or `workspace` based on where the subscription is defined.
    """
    subject: Object | Unset = UNSET
    """ Base type for most resource objects. It defines the common `type` element that identifies an object's type.
    It also identifies the element as Swagger's `discriminator`. """
    active: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    events: list[WebhookSubscriptionEventsItem] | Unset = UNSET
    """ The events this webhook is subscribed to. """
    secret_set: bool | Unset = UNSET
    """ Indicates whether or not the hook has an associated secret. It is not possible to see the hook's secret.
    This field is ignored during updates. """
    secret: str | Unset = UNSET
    """ The secret to associate with the hook. The secret is never returned via the API. As such, this field is only
    used during updates. The secret can be set to `null` or "" to remove the secret (or create a hook with no
    secret). Leaving out the secret field during updates will leave the secret unchanged. Leaving out the secret
    during creation will create a hook with no secret. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        uuid = self.uuid

        url = self.url

        description = self.description

        subject_type: str | Unset = UNSET
        if not isinstance(self.subject_type, Unset):
            subject_type = self.subject_type.value

        subject: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        active = self.active

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        secret_set = self.secret_set

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if subject_type is not UNSET:
            field_dict["subject_type"] = subject_type
        if subject is not UNSET:
            field_dict["subject"] = subject
        if active is not UNSET:
            field_dict["active"] = active
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if events is not UNSET:
            field_dict["events"] = events
        if secret_set is not UNSET:
            field_dict["secret_set"] = secret_set
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_ import Object

        d = dict(src_dict)
        type_ = d.pop("type")

        uuid = d.pop("uuid", UNSET)

        url = d.pop("url", UNSET)

        description = d.pop("description", UNSET)

        _subject_type = d.pop("subject_type", UNSET)
        subject_type: WebhookSubscriptionSubjectType | Unset
        if isinstance(_subject_type, Unset):
            subject_type = UNSET
        else:
            subject_type = WebhookSubscriptionSubjectType(_subject_type)

        _subject = d.pop("subject", UNSET)
        subject: Object | Unset
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = Object.from_dict(_subject)

        active = d.pop("active", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _events = d.pop("events", UNSET)
        events: list[WebhookSubscriptionEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = WebhookSubscriptionEventsItem(events_item_data)

                events.append(events_item)

        secret_set = d.pop("secret_set", UNSET)

        secret = d.pop("secret", UNSET)

        webhook_subscription = cls(
            type_=type_,
            uuid=uuid,
            url=url,
            description=description,
            subject_type=subject_type,
            subject=subject,
            active=active,
            created_at=created_at,
            events=events,
            secret_set=secret_set,
            secret=secret,
        )

        webhook_subscription.additional_properties = d
        return webhook_subscription

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
