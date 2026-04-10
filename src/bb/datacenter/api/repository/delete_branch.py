from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_branch_response_400 import DeleteBranchResponse400
from ...models.delete_branch_response_401 import DeleteBranchResponse401
from ...models.rest_branch_delete_request import RestBranchDeleteRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestBranchDeleteRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/branch-utils/latest/projects/{project_key}/repos/{repository_slug}/branches".format(
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
) -> Any | DeleteBranchResponse400 | DeleteBranchResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteBranchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteBranchResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteBranchResponse400 | DeleteBranchResponse401]:
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
    body: RestBranchDeleteRequest | Unset = UNSET,
) -> Response[Any | DeleteBranchResponse400 | DeleteBranchResponse401]:
    """Delete branch

      Deletes a branch in the specified repository.


     If the branch does not exist, this operation will not raise an error. In other words after calling
    this resource
     and receiving a 204 response the branch provided in the request is guaranteed to not exist in the
    specified
     repository any more, regardless of its existence beforehand.


     The optional 'endPoint' parameter of the request may contain a commit ID that the provided ref name
    is
     expected to point to. Should the ref point to a different commit ID, a 400 response will be
    returned with
     appropriate error details.


     The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource. If
     branch permissions are set up in the repository, the authenticated user must also have access to
    the branch name
     that is to be deleted.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestBranchDeleteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteBranchResponse400 | DeleteBranchResponse401]
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
    body: RestBranchDeleteRequest | Unset = UNSET,
) -> Any | DeleteBranchResponse400 | DeleteBranchResponse401 | None:
    """Delete branch

      Deletes a branch in the specified repository.


     If the branch does not exist, this operation will not raise an error. In other words after calling
    this resource
     and receiving a 204 response the branch provided in the request is guaranteed to not exist in the
    specified
     repository any more, regardless of its existence beforehand.


     The optional 'endPoint' parameter of the request may contain a commit ID that the provided ref name
    is
     expected to point to. Should the ref point to a different commit ID, a 400 response will be
    returned with
     appropriate error details.


     The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource. If
     branch permissions are set up in the repository, the authenticated user must also have access to
    the branch name
     that is to be deleted.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestBranchDeleteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteBranchResponse400 | DeleteBranchResponse401
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
    body: RestBranchDeleteRequest | Unset = UNSET,
) -> Response[Any | DeleteBranchResponse400 | DeleteBranchResponse401]:
    """Delete branch

      Deletes a branch in the specified repository.


     If the branch does not exist, this operation will not raise an error. In other words after calling
    this resource
     and receiving a 204 response the branch provided in the request is guaranteed to not exist in the
    specified
     repository any more, regardless of its existence beforehand.


     The optional 'endPoint' parameter of the request may contain a commit ID that the provided ref name
    is
     expected to point to. Should the ref point to a different commit ID, a 400 response will be
    returned with
     appropriate error details.


     The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource. If
     branch permissions are set up in the repository, the authenticated user must also have access to
    the branch name
     that is to be deleted.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestBranchDeleteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteBranchResponse400 | DeleteBranchResponse401]
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
    body: RestBranchDeleteRequest | Unset = UNSET,
) -> Any | DeleteBranchResponse400 | DeleteBranchResponse401 | None:
    """Delete branch

      Deletes a branch in the specified repository.


     If the branch does not exist, this operation will not raise an error. In other words after calling
    this resource
     and receiving a 204 response the branch provided in the request is guaranteed to not exist in the
    specified
     repository any more, regardless of its existence beforehand.


     The optional 'endPoint' parameter of the request may contain a commit ID that the provided ref name
    is
     expected to point to. Should the ref point to a different commit ID, a 400 response will be
    returned with
     appropriate error details.


     The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource. If
     branch permissions are set up in the repository, the authenticated user must also have access to
    the branch name
     that is to be deleted.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestBranchDeleteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteBranchResponse400 | DeleteBranchResponse401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
