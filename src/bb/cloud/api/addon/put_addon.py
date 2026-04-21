from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/addon",
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r""" Update an installed app

     Updates the application installation for the user.

    This endpoint is intended to be used by Bitbucket Connect apps
    and only supports JWT authentication -- that is how Bitbucket
    identifies the particular installation of the app. Developers
    with applications registered in the \"Develop Apps\" section
    of Bitbucket need not use this endpoint as updates for those
    applications can be sent out via the UI of that section.

    Passing an empty body will update the installation using the
    existing descriptor URL.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{}'
    ```

    The new `descriptor` for the installation can be also provided
    in the body directly.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor\": $NEW_DESCRIPTOR}'
    ```

    In both these modes the URL of the descriptor cannot be changed. To
    change the descriptor location and upgrade an installation
    the request must be made exclusively with a `descriptor_url`.

     ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor_url\": $NEW_URL}'
    ```

    The `descriptor_url` must exactly match the marketplace registration
    that Atlassian has for the application. Contact your Atlassian
    developer advocate to update this registration. Once the registration
    has been updated you may call this resource for each installation.

    Note that the scopes of the application cannot be increased
    in the new descriptor nor reduced to none.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r""" Update an installed app

     Updates the application installation for the user.

    This endpoint is intended to be used by Bitbucket Connect apps
    and only supports JWT authentication -- that is how Bitbucket
    identifies the particular installation of the app. Developers
    with applications registered in the \"Develop Apps\" section
    of Bitbucket need not use this endpoint as updates for those
    applications can be sent out via the UI of that section.

    Passing an empty body will update the installation using the
    existing descriptor URL.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{}'
    ```

    The new `descriptor` for the installation can be also provided
    in the body directly.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor\": $NEW_DESCRIPTOR}'
    ```

    In both these modes the URL of the descriptor cannot be changed. To
    change the descriptor location and upgrade an installation
    the request must be made exclusively with a `descriptor_url`.

     ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor_url\": $NEW_URL}'
    ```

    The `descriptor_url` must exactly match the marketplace registration
    that Atlassian has for the application. Contact your Atlassian
    developer advocate to update this registration. Once the registration
    has been updated you may call this resource for each installation.

    Note that the scopes of the application cannot be increased
    in the new descriptor nor reduced to none.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r""" Update an installed app

     Updates the application installation for the user.

    This endpoint is intended to be used by Bitbucket Connect apps
    and only supports JWT authentication -- that is how Bitbucket
    identifies the particular installation of the app. Developers
    with applications registered in the \"Develop Apps\" section
    of Bitbucket need not use this endpoint as updates for those
    applications can be sent out via the UI of that section.

    Passing an empty body will update the installation using the
    existing descriptor URL.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{}'
    ```

    The new `descriptor` for the installation can be also provided
    in the body directly.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor\": $NEW_DESCRIPTOR}'
    ```

    In both these modes the URL of the descriptor cannot be changed. To
    change the descriptor location and upgrade an installation
    the request must be made exclusively with a `descriptor_url`.

     ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor_url\": $NEW_URL}'
    ```

    The `descriptor_url` must exactly match the marketplace registration
    that Atlassian has for the application. Contact your Atlassian
    developer advocate to update this registration. Once the registration
    has been updated you may call this resource for each installation.

    Note that the scopes of the application cannot be increased
    in the new descriptor nor reduced to none.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r""" Update an installed app

     Updates the application installation for the user.

    This endpoint is intended to be used by Bitbucket Connect apps
    and only supports JWT authentication -- that is how Bitbucket
    identifies the particular installation of the app. Developers
    with applications registered in the \"Develop Apps\" section
    of Bitbucket need not use this endpoint as updates for those
    applications can be sent out via the UI of that section.

    Passing an empty body will update the installation using the
    existing descriptor URL.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{}'
    ```

    The new `descriptor` for the installation can be also provided
    in the body directly.

    ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor\": $NEW_DESCRIPTOR}'
    ```

    In both these modes the URL of the descriptor cannot be changed. To
    change the descriptor location and upgrade an installation
    the request must be made exclusively with a `descriptor_url`.

     ```
    $ curl -X PUT https://api.bitbucket.org/2.0/addon \
      -H \"Authorization: JWT <JWT Token>\" \
      --header \"Content-Type: application/json\" \
      --data '{\"descriptor_url\": $NEW_URL}'
    ```

    The `descriptor_url` must exactly match the marketplace registration
    that Atlassian has for the application. Contact your Atlassian
    developer advocate to update this registration. Once the registration
    has been updated you may call this resource for each installation.

    Note that the scopes of the application cannot be increased
    in the new descriptor nor reduced to none.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
