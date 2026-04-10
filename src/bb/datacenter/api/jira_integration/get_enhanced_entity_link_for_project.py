from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_enhanced_entity_link import RestEnhancedEntityLink
from ...types import Response


def _get_kwargs(
    project_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jira/latest/projects/{project_key}/primary-enhanced-entitylink".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RestEnhancedEntityLink | None:
    if response.status_code == 200:
        response_200 = RestEnhancedEntityLink.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestEnhancedEntityLink]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestEnhancedEntityLink]:
    """Get entity link

     Retrieves the enchanced primary entitylink

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the project having the
    primary enhanced entitylink.


    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestEnhancedEntityLink]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestEnhancedEntityLink | None:
    """Get entity link

     Retrieves the enchanced primary entitylink

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the project having the
    primary enhanced entitylink.


    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestEnhancedEntityLink
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestEnhancedEntityLink]:
    """Get entity link

     Retrieves the enchanced primary entitylink

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the project having the
    primary enhanced entitylink.


    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestEnhancedEntityLink]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestEnhancedEntityLink | None:
    """Get entity link

     Retrieves the enchanced primary entitylink

    The authenticated user must have <strong>PROJECT_READ</strong> permission for the project having the
    primary enhanced entitylink.


    Args:
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestEnhancedEntityLink
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
        )
    ).parsed
