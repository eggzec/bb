from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_bearer_token_credentials import RestBearerTokenCredentials
    from ..models.rest_ssh_credentials import RestSshCredentials
    from ..models.rest_username_password_credentials import RestUsernamePasswordCredentials


T = TypeVar("T", bound="RestAuthenticationRequest")


@_attrs_define
class RestAuthenticationRequest:
    credentials: RestBearerTokenCredentials | RestSshCredentials | RestUsernamePasswordCredentials
    repository_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_bearer_token_credentials import RestBearerTokenCredentials
        from ..models.rest_username_password_credentials import RestUsernamePasswordCredentials

        credentials: dict[str, Any]
        if isinstance(self.credentials, RestUsernamePasswordCredentials):
            credentials = self.credentials.to_dict()
        elif isinstance(self.credentials, RestBearerTokenCredentials):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials.to_dict()

        repository_id = self.repository_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
            }
        )
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_bearer_token_credentials import RestBearerTokenCredentials
        from ..models.rest_ssh_credentials import RestSshCredentials
        from ..models.rest_username_password_credentials import RestUsernamePasswordCredentials

        d = dict(src_dict)

        def _parse_credentials(
            data: object,
        ) -> RestBearerTokenCredentials | RestSshCredentials | RestUsernamePasswordCredentials:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_credentials_type_0 = RestUsernamePasswordCredentials.from_dict(data)

                return componentsschemas_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_credentials_type_1 = RestBearerTokenCredentials.from_dict(data)

                return componentsschemas_credentials_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_credentials_type_2 = RestSshCredentials.from_dict(data)

            return componentsschemas_credentials_type_2

        credentials = _parse_credentials(d.pop("credentials"))

        repository_id = d.pop("repositoryId", UNSET)

        rest_authentication_request = cls(
            credentials=credentials,
            repository_id=repository_id,
        )

        rest_authentication_request.additional_properties = d
        return rest_authentication_request

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
