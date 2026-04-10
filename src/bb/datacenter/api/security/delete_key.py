from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_key_response_401 import DeleteKeyResponse401
from ...types import Response


def _get_kwargs(
    fingerprint_or_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/gpg/latest/keys/{fingerprint_or_id}".format(
            fingerprint_or_id=quote(str(fingerprint_or_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteKeyResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteKeyResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteKeyResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fingerprint_or_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteKeyResponse401]:
    """Delete a GPG key

     Delete the GPG key with the specified ID or Key Fingerprint.

    Args:
        fingerprint_or_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteKeyResponse401]
    """

    kwargs = _get_kwargs(
        fingerprint_or_id=fingerprint_or_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fingerprint_or_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteKeyResponse401 | None:
    """Delete a GPG key

     Delete the GPG key with the specified ID or Key Fingerprint.

    Args:
        fingerprint_or_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteKeyResponse401
    """

    return sync_detailed(
        fingerprint_or_id=fingerprint_or_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    fingerprint_or_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteKeyResponse401]:
    """Delete a GPG key

     Delete the GPG key with the specified ID or Key Fingerprint.

    Args:
        fingerprint_or_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteKeyResponse401]
    """

    kwargs = _get_kwargs(
        fingerprint_or_id=fingerprint_or_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fingerprint_or_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteKeyResponse401 | None:
    """Delete a GPG key

     Delete the GPG key with the specified ID or Key Fingerprint.

    Args:
        fingerprint_or_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteKeyResponse401
    """

    return (
        await asyncio_detailed(
            fingerprint_or_id=fingerprint_or_id,
            client=client,
        )
    ).parsed
