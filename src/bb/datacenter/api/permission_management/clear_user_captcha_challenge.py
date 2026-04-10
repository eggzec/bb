from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clear_user_captcha_challenge_response_400 import ClearUserCaptchaChallengeResponse400
from ...models.clear_user_captcha_challenge_response_401 import ClearUserCaptchaChallengeResponse401
from ...models.clear_user_captcha_challenge_response_403 import ClearUserCaptchaChallengeResponse403
from ...models.clear_user_captcha_challenge_response_404 import ClearUserCaptchaChallengeResponse404
from ...types import UNSET, Response


def _get_kwargs(
    *,
    name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/admin/users/captcha",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ClearUserCaptchaChallengeResponse400
    | ClearUserCaptchaChallengeResponse401
    | ClearUserCaptchaChallengeResponse403
    | ClearUserCaptchaChallengeResponse404
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ClearUserCaptchaChallengeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ClearUserCaptchaChallengeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ClearUserCaptchaChallengeResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ClearUserCaptchaChallengeResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ClearUserCaptchaChallengeResponse400
    | ClearUserCaptchaChallengeResponse401
    | ClearUserCaptchaChallengeResponse403
    | ClearUserCaptchaChallengeResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[
    Any
    | ClearUserCaptchaChallengeResponse400
    | ClearUserCaptchaChallengeResponse401
    | ClearUserCaptchaChallengeResponse403
    | ClearUserCaptchaChallengeResponse404
]:
    """Clear CAPTCHA for user

     Clears any CAPTCHA challenge that may constrain the user with the supplied username when they
    authenticate. Additionally any counter or metric that contributed towards the user being issued the
    CAPTCHA challenge (for instance too many consecutive failed logins) will also be reset.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource, and
    may not clear the CAPTCHA of a user with greater permissions than themselves.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClearUserCaptchaChallengeResponse400 | ClearUserCaptchaChallengeResponse401 | ClearUserCaptchaChallengeResponse403 | ClearUserCaptchaChallengeResponse404]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> (
    Any
    | ClearUserCaptchaChallengeResponse400
    | ClearUserCaptchaChallengeResponse401
    | ClearUserCaptchaChallengeResponse403
    | ClearUserCaptchaChallengeResponse404
    | None
):
    """Clear CAPTCHA for user

     Clears any CAPTCHA challenge that may constrain the user with the supplied username when they
    authenticate. Additionally any counter or metric that contributed towards the user being issued the
    CAPTCHA challenge (for instance too many consecutive failed logins) will also be reset.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource, and
    may not clear the CAPTCHA of a user with greater permissions than themselves.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClearUserCaptchaChallengeResponse400 | ClearUserCaptchaChallengeResponse401 | ClearUserCaptchaChallengeResponse403 | ClearUserCaptchaChallengeResponse404
    """

    return sync_detailed(
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> Response[
    Any
    | ClearUserCaptchaChallengeResponse400
    | ClearUserCaptchaChallengeResponse401
    | ClearUserCaptchaChallengeResponse403
    | ClearUserCaptchaChallengeResponse404
]:
    """Clear CAPTCHA for user

     Clears any CAPTCHA challenge that may constrain the user with the supplied username when they
    authenticate. Additionally any counter or metric that contributed towards the user being issued the
    CAPTCHA challenge (for instance too many consecutive failed logins) will also be reset.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource, and
    may not clear the CAPTCHA of a user with greater permissions than themselves.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ClearUserCaptchaChallengeResponse400 | ClearUserCaptchaChallengeResponse401 | ClearUserCaptchaChallengeResponse403 | ClearUserCaptchaChallengeResponse404]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str,
) -> (
    Any
    | ClearUserCaptchaChallengeResponse400
    | ClearUserCaptchaChallengeResponse401
    | ClearUserCaptchaChallengeResponse403
    | ClearUserCaptchaChallengeResponse404
    | None
):
    """Clear CAPTCHA for user

     Clears any CAPTCHA challenge that may constrain the user with the supplied username when they
    authenticate. Additionally any counter or metric that contributed towards the user being issued the
    CAPTCHA challenge (for instance too many consecutive failed logins) will also be reset.

    The authenticated user must have the <strong>ADMIN</strong> permission to call this resource, and
    may not clear the CAPTCHA of a user with greater permissions than themselves.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ClearUserCaptchaChallengeResponse400 | ClearUserCaptchaChallengeResponse401 | ClearUserCaptchaChallengeResponse403 | ClearUserCaptchaChallengeResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed
