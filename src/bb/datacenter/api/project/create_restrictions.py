from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_restrictions_response_400 import CreateRestrictionsResponse400
from ...models.create_restrictions_response_401 import CreateRestrictionsResponse401
from ...models.rest_ref_restriction import RestRefRestriction
from ...models.rest_restriction_request import RestRestrictionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    body: list[RestRestrictionRequest] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/branch-permissions/latest/projects/{project_key}/restrictions".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/vnd.atl.bitbucket.bulk+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction | None:
    if response.status_code == 200:
        response_200 = RestRefRestriction.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateRestrictionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateRestrictionsResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction]:
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
    body: list[RestRestrictionRequest] | Unset = UNSET,
) -> Response[CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction]:
    """Create multiple ref restrictions

     Allows creating multiple restrictions at once.

    Args:
        project_key (str):
        body (list[RestRestrictionRequest] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[RestRestrictionRequest] | Unset = UNSET,
) -> CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction | None:
    """Create multiple ref restrictions

     Allows creating multiple restrictions at once.

    Args:
        project_key (str):
        body (list[RestRestrictionRequest] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[RestRestrictionRequest] | Unset = UNSET,
) -> Response[CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction]:
    """Create multiple ref restrictions

     Allows creating multiple restrictions at once.

    Args:
        project_key (str):
        body (list[RestRestrictionRequest] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[RestRestrictionRequest] | Unset = UNSET,
) -> CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction | None:
    """Create multiple ref restrictions

     Allows creating multiple restrictions at once.

    Args:
        project_key (str):
        body (list[RestRestrictionRequest] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRestrictionsResponse400 | CreateRestrictionsResponse401 | RestRefRestriction
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
