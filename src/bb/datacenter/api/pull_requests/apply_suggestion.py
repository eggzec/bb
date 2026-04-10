from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apply_suggestion_response_400 import ApplySuggestionResponse400
from ...models.apply_suggestion_response_401 import ApplySuggestionResponse401
from ...models.apply_suggestion_response_404 import ApplySuggestionResponse404
from ...models.apply_suggestion_response_409 import ApplySuggestionResponse409
from ...models.rest_apply_suggestion_request import RestApplySuggestionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    comment_id: str,
    *,
    body: RestApplySuggestionRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/comments/{comment_id}/apply-suggestion".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ApplySuggestionResponse400
    | ApplySuggestionResponse401
    | ApplySuggestionResponse404
    | ApplySuggestionResponse409
    | None
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ApplySuggestionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApplySuggestionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ApplySuggestionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApplySuggestionResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ApplySuggestionResponse400
    | ApplySuggestionResponse401
    | ApplySuggestionResponse404
    | ApplySuggestionResponse409
]:
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
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestApplySuggestionRequest | Unset = UNSET,
) -> Response[
    Any
    | ApplySuggestionResponse400
    | ApplySuggestionResponse401
    | ApplySuggestionResponse404
    | ApplySuggestionResponse409
]:
    """Apply pull request suggestion

     Apply a suggestion contained within a comment.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        body (RestApplySuggestionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApplySuggestionResponse400 | ApplySuggestionResponse401 | ApplySuggestionResponse404 | ApplySuggestionResponse409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        comment_id=comment_id,
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
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestApplySuggestionRequest | Unset = UNSET,
) -> (
    Any
    | ApplySuggestionResponse400
    | ApplySuggestionResponse401
    | ApplySuggestionResponse404
    | ApplySuggestionResponse409
    | None
):
    """Apply pull request suggestion

     Apply a suggestion contained within a comment.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        body (RestApplySuggestionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApplySuggestionResponse400 | ApplySuggestionResponse401 | ApplySuggestionResponse404 | ApplySuggestionResponse409
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestApplySuggestionRequest | Unset = UNSET,
) -> Response[
    Any
    | ApplySuggestionResponse400
    | ApplySuggestionResponse401
    | ApplySuggestionResponse404
    | ApplySuggestionResponse409
]:
    """Apply pull request suggestion

     Apply a suggestion contained within a comment.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        body (RestApplySuggestionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApplySuggestionResponse400 | ApplySuggestionResponse401 | ApplySuggestionResponse404 | ApplySuggestionResponse409]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestApplySuggestionRequest | Unset = UNSET,
) -> (
    Any
    | ApplySuggestionResponse400
    | ApplySuggestionResponse401
    | ApplySuggestionResponse404
    | ApplySuggestionResponse409
    | None
):
    """Apply pull request suggestion

     Apply a suggestion contained within a comment.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        body (RestApplySuggestionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApplySuggestionResponse400 | ApplySuggestionResponse401 | ApplySuggestionResponse404 | ApplySuggestionResponse409
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
