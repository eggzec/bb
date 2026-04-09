from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PipelineRunnerOauthClient")


@_attrs_define
class PipelineRunnerOauthClient:
    type_: str
    id: str | Unset = UNSET
    """ The OAuth client ID. """
    secret: str | Unset = UNSET
    """ The OAuth client secret. This is an optional element that is only provided once. """
    token_endpoint: str | Unset = UNSET
    """ The OAuth token endpoint URL. """
    audience: str | Unset = UNSET
    """ The intended audience for the OAuth token. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        secret = self.secret

        token_endpoint = self.token_endpoint

        audience = self.audience

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if secret is not UNSET:
            field_dict["secret"] = secret
        if token_endpoint is not UNSET:
            field_dict["token_endpoint"] = token_endpoint
        if audience is not UNSET:
            field_dict["audience"] = audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id", UNSET)

        secret = d.pop("secret", UNSET)

        token_endpoint = d.pop("token_endpoint", UNSET)

        audience = d.pop("audience", UNSET)

        pipeline_runner_oauth_client = cls(
            type_=type_,
            id=id,
            secret=secret,
            token_endpoint=token_endpoint,
            audience=audience,
        )

        pipeline_runner_oauth_client.additional_properties = d
        return pipeline_runner_oauth_client

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
