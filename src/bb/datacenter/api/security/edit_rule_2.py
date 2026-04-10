from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_rule_2_response_400 import EditRule2Response400
from ...models.edit_rule_2_response_401 import EditRule2Response401
from ...models.rest_secret_scanning_rule import RestSecretScanningRule
from ...models.rest_secret_scanning_rule_set_request import RestSecretScanningRuleSetRequest
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: RestSecretScanningRuleSetRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/secret-scanning/rules/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule | None:
    if response.status_code == 200:
        response_200 = RestSecretScanningRule.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EditRule2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = EditRule2Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSecretScanningRuleSetRequest,
) -> Response[EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule]:
    """Edit a global secret scanning rule.

     Edit an existing global secret scanning rule

    Args:
        id (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSecretScanningRuleSetRequest,
) -> EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule | None:
    """Edit a global secret scanning rule.

     Edit an existing global secret scanning rule

    Args:
        id (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSecretScanningRuleSetRequest,
) -> Response[EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule]:
    """Edit a global secret scanning rule.

     Edit an existing global secret scanning rule

    Args:
        id (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSecretScanningRuleSetRequest,
) -> EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule | None:
    """Edit a global secret scanning rule.

     Edit an existing global secret scanning rule

    Args:
        id (str):
        body (RestSecretScanningRuleSetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditRule2Response400 | EditRule2Response401 | RestSecretScanningRule
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
