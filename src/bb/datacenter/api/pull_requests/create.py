from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_response_400 import CreateResponse400
from ...models.create_response_401 import CreateResponse401
from ...models.create_response_404 import CreateResponse404
from ...models.create_response_409 import CreateResponse409
from ...models.rest_pull_request import RestPullRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestPullRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest | None:
    if response.status_code == 201:
        response_201 = RestPullRequest.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequest | Unset = UNSET,
) -> Response[CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest]:
    """Create pull request

     Create a new pull request from a source branch or tag to a target branch. The source and target may
    be in the same repository, or different ones. (Note that different repositories must belong to the
    same <code>Repository#getHierarchyId()</code> hierarchy.)

    The <code>fromRef</code> may be a branch or a tag. The <code>toRef</code> is required to be a
    branch. Tags are not allowed as targets because tags are intended to be immutable and should not be
    changed after they are created.

    The authenticated user must have <strong>REPO_READ</strong> permission for the <code>fromRef</code>
    and <code>toRef</code> repositories to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestPullRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequest | Unset = UNSET,
) -> CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest | None:
    """Create pull request

     Create a new pull request from a source branch or tag to a target branch. The source and target may
    be in the same repository, or different ones. (Note that different repositories must belong to the
    same <code>Repository#getHierarchyId()</code> hierarchy.)

    The <code>fromRef</code> may be a branch or a tag. The <code>toRef</code> is required to be a
    branch. Tags are not allowed as targets because tags are intended to be immutable and should not be
    changed after they are created.

    The authenticated user must have <strong>REPO_READ</strong> permission for the <code>fromRef</code>
    and <code>toRef</code> repositories to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestPullRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequest | Unset = UNSET,
) -> Response[CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest]:
    """Create pull request

     Create a new pull request from a source branch or tag to a target branch. The source and target may
    be in the same repository, or different ones. (Note that different repositories must belong to the
    same <code>Repository#getHierarchyId()</code> hierarchy.)

    The <code>fromRef</code> may be a branch or a tag. The <code>toRef</code> is required to be a
    branch. Tags are not allowed as targets because tags are intended to be immutable and should not be
    changed after they are created.

    The authenticated user must have <strong>REPO_READ</strong> permission for the <code>fromRef</code>
    and <code>toRef</code> repositories to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestPullRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequest | Unset = UNSET,
) -> CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest | None:
    """Create pull request

     Create a new pull request from a source branch or tag to a target branch. The source and target may
    be in the same repository, or different ones. (Note that different repositories must belong to the
    same <code>Repository#getHierarchyId()</code> hierarchy.)

    The <code>fromRef</code> may be a branch or a tag. The <code>toRef</code> is required to be a
    branch. Tags are not allowed as targets because tags are intended to be immutable and should not be
    changed after they are created.

    The authenticated user must have <strong>REPO_READ</strong> permission for the <code>fromRef</code>
    and <code>toRef</code> repositories to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestPullRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateResponse400 | CreateResponse401 | CreateResponse404 | CreateResponse409 | RestPullRequest
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
