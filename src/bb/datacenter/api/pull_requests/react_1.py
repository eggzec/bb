from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_user_reaction import RestUserReaction
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    comment_id: str,
    emoticon: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/comment-likes/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/comments/{comment_id}/reactions/{emoticon}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
            emoticon=quote(str(emoticon), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RestUserReaction | None:
    if response.status_code == 200:
        response_200 = RestUserReaction.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RestUserReaction]:
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
    emoticon: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestUserReaction]:
    """React to a PR comment

     Add an emoticon reaction to a pull request comment

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        emoticon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestUserReaction]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        comment_id=comment_id,
        emoticon=emoticon,
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
    emoticon: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestUserReaction | None:
    """React to a PR comment

     Add an emoticon reaction to a pull request comment

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        emoticon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestUserReaction
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        comment_id=comment_id,
        emoticon=emoticon,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    comment_id: str,
    emoticon: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestUserReaction]:
    """React to a PR comment

     Add an emoticon reaction to a pull request comment

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        emoticon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestUserReaction]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        comment_id=comment_id,
        emoticon=emoticon,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    comment_id: str,
    emoticon: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestUserReaction | None:
    """React to a PR comment

     Add an emoticon reaction to a pull request comment

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        emoticon (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestUserReaction
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            comment_id=comment_id,
            emoticon=emoticon,
            client=client,
        )
    ).parsed
