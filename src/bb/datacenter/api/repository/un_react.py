from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
    emoticon: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/comment-likes/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/comments/{comment_id}/reactions/{emoticon}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
            emoticon=quote(str(emoticon), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
    emoticon: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Remove a reaction from comment

     Remove an emoticon reaction from a comment

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):
        emoticon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        comment_id=comment_id,
        emoticon=emoticon,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    comment_id: str,
    emoticon: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Remove a reaction from comment

     Remove an emoticon reaction from a comment

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        comment_id (str):
        emoticon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        comment_id=comment_id,
        emoticon=emoticon,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
