from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_allowlist_rule_response_401 import DeleteAllowlistRuleResponse401
from ...types import Response


def _get_kwargs(
    project_key: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/secret-scanning/allowlist/{id}".format(
            project_key=quote(str(project_key), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteAllowlistRuleResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteAllowlistRuleResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteAllowlistRuleResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteAllowlistRuleResponse401]:
    """Delete a project secret scanning allowlist rule

     Delete a project secret scanning allowlist rule with the provided ID.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAllowlistRuleResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteAllowlistRuleResponse401 | None:
    """Delete a project secret scanning allowlist rule

     Delete a project secret scanning allowlist rule with the provided ID.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAllowlistRuleResponse401
    """

    return sync_detailed(
        project_key=project_key,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteAllowlistRuleResponse401]:
    """Delete a project secret scanning allowlist rule

     Delete a project secret scanning allowlist rule with the provided ID.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAllowlistRuleResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteAllowlistRuleResponse401 | None:
    """Delete a project secret scanning allowlist rule

     Delete a project secret scanning allowlist rule with the provided ID.

    Project **Admin** is required

    Args:
        project_key (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAllowlistRuleResponse401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            id=id,
            client=client,
        )
    ).parsed
