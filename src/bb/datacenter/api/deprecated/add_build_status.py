from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.add_build_status_response_400 import AddBuildStatusResponse400
from ...models.add_build_status_response_401 import AddBuildStatusResponse401
from ...models.rest_build_status import RestBuildStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    commit_id: str,
    *,
    body: RestBuildStatus | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/build-status/latest/commits/{commit_id}".format(
            commit_id=quote(str(commit_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = AddBuildStatusResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddBuildStatusResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated_endpoint(None)
def sync_detailed(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBuildStatus | Unset = UNSET,
) -> Response[AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any]:
    """Create build status for commit

     Associates a build status with a commit.The <code>state</code>, the <code>key</code> and the
    <code>url</code> fields are mandatory. The <code>name</code> and<code>description</code> fields are
    optional.All fields (mandatory or optional) are limited to 255 characters, except for the
    <code>url</code>,which is limited to 450 characters.Supported values for the <code>state</code> are
    <code>SUCCESSFUL</code>, <code>FAILED</code>and <code>INPROGRESS</code>.The authenticated user must
    have <strong>LICENSED</strong> permission or higher to call this resource.

    <strong>Deprecated in 7.14, please use the repository based builds resource instead.</strong>

    Args:
        commit_id (str):
        body (RestBuildStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any]
    """

    kwargs = _get_kwargs(
        commit_id=commit_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBuildStatus | Unset = UNSET,
) -> AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any | None:
    """Create build status for commit

     Associates a build status with a commit.The <code>state</code>, the <code>key</code> and the
    <code>url</code> fields are mandatory. The <code>name</code> and<code>description</code> fields are
    optional.All fields (mandatory or optional) are limited to 255 characters, except for the
    <code>url</code>,which is limited to 450 characters.Supported values for the <code>state</code> are
    <code>SUCCESSFUL</code>, <code>FAILED</code>and <code>INPROGRESS</code>.The authenticated user must
    have <strong>LICENSED</strong> permission or higher to call this resource.

    <strong>Deprecated in 7.14, please use the repository based builds resource instead.</strong>

    Args:
        commit_id (str):
        body (RestBuildStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any
    """

    return sync_detailed(
        commit_id=commit_id,
        client=client,
        body=body,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBuildStatus | Unset = UNSET,
) -> Response[AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any]:
    """Create build status for commit

     Associates a build status with a commit.The <code>state</code>, the <code>key</code> and the
    <code>url</code> fields are mandatory. The <code>name</code> and<code>description</code> fields are
    optional.All fields (mandatory or optional) are limited to 255 characters, except for the
    <code>url</code>,which is limited to 450 characters.Supported values for the <code>state</code> are
    <code>SUCCESSFUL</code>, <code>FAILED</code>and <code>INPROGRESS</code>.The authenticated user must
    have <strong>LICENSED</strong> permission or higher to call this resource.

    <strong>Deprecated in 7.14, please use the repository based builds resource instead.</strong>

    Args:
        commit_id (str):
        body (RestBuildStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any]
    """

    kwargs = _get_kwargs(
        commit_id=commit_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBuildStatus | Unset = UNSET,
) -> AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any | None:
    """Create build status for commit

     Associates a build status with a commit.The <code>state</code>, the <code>key</code> and the
    <code>url</code> fields are mandatory. The <code>name</code> and<code>description</code> fields are
    optional.All fields (mandatory or optional) are limited to 255 characters, except for the
    <code>url</code>,which is limited to 450 characters.Supported values for the <code>state</code> are
    <code>SUCCESSFUL</code>, <code>FAILED</code>and <code>INPROGRESS</code>.The authenticated user must
    have <strong>LICENSED</strong> permission or higher to call this resource.

    <strong>Deprecated in 7.14, please use the repository based builds resource instead.</strong>

    Args:
        commit_id (str):
        body (RestBuildStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddBuildStatusResponse400 | AddBuildStatusResponse401 | Any
    """

    return (
        await asyncio_detailed(
            commit_id=commit_id,
            client=client,
            body=body,
        )
    ).parsed
