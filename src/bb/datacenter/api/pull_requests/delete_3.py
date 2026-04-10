from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_3_response_401 import Delete3Response401
from ...models.delete_3_response_404 import Delete3Response404
from ...models.delete_3_response_409 import Delete3Response409
from ...models.rest_pull_request_delete_request import RestPullRequestDeleteRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    body: RestPullRequestDeleteRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Delete3Response401 | Delete3Response404 | Delete3Response409 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = Delete3Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Delete3Response404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Delete3Response409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Delete3Response401 | Delete3Response404 | Delete3Response409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestDeleteRequest | Unset = UNSET,
) -> Response[Any | Delete3Response401 | Delete3Response404 | Delete3Response409]:
    r"""Delete pull request

     Deletes a pull request.

    To call this resource, users must be authenticated and have permission to view the pull request.
    Additionally, they must:

    - be the pull request author, if the system is configured to allow authors to delete their own
    pull requests (this is the default) OR
    - have repository administrator permission for the repository the pull request is targeting


    A body containing the version of the pull request must be provided with this request.

    `{ \"version\": 1 }`

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestDeleteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Delete3Response401 | Delete3Response404 | Delete3Response409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestDeleteRequest | Unset = UNSET,
) -> Any | Delete3Response401 | Delete3Response404 | Delete3Response409 | None:
    r"""Delete pull request

     Deletes a pull request.

    To call this resource, users must be authenticated and have permission to view the pull request.
    Additionally, they must:

    - be the pull request author, if the system is configured to allow authors to delete their own
    pull requests (this is the default) OR
    - have repository administrator permission for the repository the pull request is targeting


    A body containing the version of the pull request must be provided with this request.

    `{ \"version\": 1 }`

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestDeleteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Delete3Response401 | Delete3Response404 | Delete3Response409
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestDeleteRequest | Unset = UNSET,
) -> Response[Any | Delete3Response401 | Delete3Response404 | Delete3Response409]:
    r"""Delete pull request

     Deletes a pull request.

    To call this resource, users must be authenticated and have permission to view the pull request.
    Additionally, they must:

    - be the pull request author, if the system is configured to allow authors to delete their own
    pull requests (this is the default) OR
    - have repository administrator permission for the repository the pull request is targeting


    A body containing the version of the pull request must be provided with this request.

    `{ \"version\": 1 }`

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestDeleteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Delete3Response401 | Delete3Response404 | Delete3Response409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestDeleteRequest | Unset = UNSET,
) -> Any | Delete3Response401 | Delete3Response404 | Delete3Response409 | None:
    r"""Delete pull request

     Deletes a pull request.

    To call this resource, users must be authenticated and have permission to view the pull request.
    Additionally, they must:

    - be the pull request author, if the system is configured to allow authors to delete their own
    pull requests (this is the default) OR
    - have repository administrator permission for the repository the pull request is targeting


    A body containing the version of the pull request must be provided with this request.

    `{ \"version\": 1 }`

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestPullRequestDeleteRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Delete3Response401 | Delete3Response404 | Delete3Response409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
            body=body,
        )
    ).parsed
