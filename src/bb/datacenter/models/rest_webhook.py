from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_webhook_configuration import RestWebhookConfiguration
    from ..models.rest_webhook_credentials import RestWebhookCredentials
    from ..models.rest_webhook_statistics import RestWebhookStatistics


T = TypeVar("T", bound="RestWebhook")


@_attrs_define
class RestWebhook:
    active: bool | Unset = UNSET
    configuration: RestWebhookConfiguration | Unset = UNSET
    credentials: RestWebhookCredentials | Unset = UNSET
    events: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    scope_type: str | Unset = UNSET
    ssl_verification_required: bool | Unset = UNSET
    statistics: RestWebhookStatistics | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        name = self.name

        scope_type = self.scope_type

        ssl_verification_required = self.ssl_verification_required

        statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if events is not UNSET:
            field_dict["events"] = events
        if name is not UNSET:
            field_dict["name"] = name
        if scope_type is not UNSET:
            field_dict["scopeType"] = scope_type
        if ssl_verification_required is not UNSET:
            field_dict["sslVerificationRequired"] = ssl_verification_required
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_webhook_configuration import RestWebhookConfiguration
        from ..models.rest_webhook_credentials import RestWebhookCredentials
        from ..models.rest_webhook_statistics import RestWebhookStatistics

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        _configuration = d.pop("configuration", UNSET)
        configuration: RestWebhookConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = RestWebhookConfiguration.from_dict(_configuration)

        _credentials = d.pop("credentials", UNSET)
        credentials: RestWebhookCredentials | Unset
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = RestWebhookCredentials.from_dict(_credentials)

        events = cast(list[str], d.pop("events", UNSET))

        name = d.pop("name", UNSET)

        scope_type = d.pop("scopeType", UNSET)

        ssl_verification_required = d.pop("sslVerificationRequired", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: RestWebhookStatistics | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = RestWebhookStatistics.from_dict(_statistics)

        url = d.pop("url", UNSET)

        rest_webhook = cls(
            active=active,
            configuration=configuration,
            credentials=credentials,
            events=events,
            name=name,
            scope_type=scope_type,
            ssl_verification_required=ssl_verification_required,
            statistics=statistics,
            url=url,
        )

        rest_webhook.additional_properties = d
        return rest_webhook

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
