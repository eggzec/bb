from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_comment import RestComment
from ...models.update_comment_2_response_400 import UpdateComment2Response400
from ...models.update_comment_2_response_401 import UpdateComment2Response401
from ...models.update_comment_2_response_404 import UpdateComment2Response404
from ...models.update_comment_2_response_409 import UpdateComment2Response409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    comment_id: str,
    *,
    body: RestComment | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/comments/{comment_id}".format(
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
    RestComment
    | UpdateComment2Response400
    | UpdateComment2Response401
    | UpdateComment2Response404
    | UpdateComment2Response409
    | None
):
    if response.status_code == 200:
        response_200 = RestComment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateComment2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateComment2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateComment2Response404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = UpdateComment2Response409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestComment
    | UpdateComment2Response400
    | UpdateComment2Response401
    | UpdateComment2Response404
    | UpdateComment2Response409
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
    body: RestComment | Unset = UNSET,
) -> Response[
    RestComment
    | UpdateComment2Response400
    | UpdateComment2Response401
    | UpdateComment2Response404
    | UpdateComment2Response409
]:
    r"""Update pull request comment

     Update a comment, with the following restrictions:

    - only the author of the comment may update the <i>text</i> of the comment
    - only the author of the comment, the author of the pull request or repository admins and above may
    update the other fields of a comment
    </ul>

    Convert a comment to a task or vice versa.

    Comments can be converted to tasks by setting the 'severity' attribute to 'BLOCKER':
     <pre> {
     \"severity\": \"BLOCKER\"
     }
     </pre>

    Tasks can be converted to comments by setting the 'severity' attribute to 'NORMAL':  <pre> {
     \"severity\": \"NORMAL\"
     }
     </pre>

    Resolve a task.

    Tasks can be resolved by setting the 'state' attribute to 'RESOLVED':  <pre> {
     \"state\": \"RESOLVED\"
     }
     </pre>

    <strong>Note:</strong> the supplied JSON object must contain a <code>version</code> that must match
    the server's version of the comment or the update will fail. To determine the current version of the
    comment, the comment should be fetched from the server prior to the update. Look for the 'version'
    attribute in the returned JSON structure.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        body (RestComment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestComment | UpdateComment2Response400 | UpdateComment2Response401 | UpdateComment2Response404 | UpdateComment2Response409]
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
    body: RestComment | Unset = UNSET,
) -> (
    RestComment
    | UpdateComment2Response400
    | UpdateComment2Response401
    | UpdateComment2Response404
    | UpdateComment2Response409
    | None
):
    r"""Update pull request comment

     Update a comment, with the following restrictions:

    - only the author of the comment may update the <i>text</i> of the comment
    - only the author of the comment, the author of the pull request or repository admins and above may
    update the other fields of a comment
    </ul>

    Convert a comment to a task or vice versa.

    Comments can be converted to tasks by setting the 'severity' attribute to 'BLOCKER':
     <pre> {
     \"severity\": \"BLOCKER\"
     }
     </pre>

    Tasks can be converted to comments by setting the 'severity' attribute to 'NORMAL':  <pre> {
     \"severity\": \"NORMAL\"
     }
     </pre>

    Resolve a task.

    Tasks can be resolved by setting the 'state' attribute to 'RESOLVED':  <pre> {
     \"state\": \"RESOLVED\"
     }
     </pre>

    <strong>Note:</strong> the supplied JSON object must contain a <code>version</code> that must match
    the server's version of the comment or the update will fail. To determine the current version of the
    comment, the comment should be fetched from the server prior to the update. Look for the 'version'
    attribute in the returned JSON structure.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        body (RestComment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestComment | UpdateComment2Response400 | UpdateComment2Response401 | UpdateComment2Response404 | UpdateComment2Response409
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
    body: RestComment | Unset = UNSET,
) -> Response[
    RestComment
    | UpdateComment2Response400
    | UpdateComment2Response401
    | UpdateComment2Response404
    | UpdateComment2Response409
]:
    r"""Update pull request comment

     Update a comment, with the following restrictions:

    - only the author of the comment may update the <i>text</i> of the comment
    - only the author of the comment, the author of the pull request or repository admins and above may
    update the other fields of a comment
    </ul>

    Convert a comment to a task or vice versa.

    Comments can be converted to tasks by setting the 'severity' attribute to 'BLOCKER':
     <pre> {
     \"severity\": \"BLOCKER\"
     }
     </pre>

    Tasks can be converted to comments by setting the 'severity' attribute to 'NORMAL':  <pre> {
     \"severity\": \"NORMAL\"
     }
     </pre>

    Resolve a task.

    Tasks can be resolved by setting the 'state' attribute to 'RESOLVED':  <pre> {
     \"state\": \"RESOLVED\"
     }
     </pre>

    <strong>Note:</strong> the supplied JSON object must contain a <code>version</code> that must match
    the server's version of the comment or the update will fail. To determine the current version of the
    comment, the comment should be fetched from the server prior to the update. Look for the 'version'
    attribute in the returned JSON structure.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        body (RestComment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestComment | UpdateComment2Response400 | UpdateComment2Response401 | UpdateComment2Response404 | UpdateComment2Response409]
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
    body: RestComment | Unset = UNSET,
) -> (
    RestComment
    | UpdateComment2Response400
    | UpdateComment2Response401
    | UpdateComment2Response404
    | UpdateComment2Response409
    | None
):
    r"""Update pull request comment

     Update a comment, with the following restrictions:

    - only the author of the comment may update the <i>text</i> of the comment
    - only the author of the comment, the author of the pull request or repository admins and above may
    update the other fields of a comment
    </ul>

    Convert a comment to a task or vice versa.

    Comments can be converted to tasks by setting the 'severity' attribute to 'BLOCKER':
     <pre> {
     \"severity\": \"BLOCKER\"
     }
     </pre>

    Tasks can be converted to comments by setting the 'severity' attribute to 'NORMAL':  <pre> {
     \"severity\": \"NORMAL\"
     }
     </pre>

    Resolve a task.

    Tasks can be resolved by setting the 'state' attribute to 'RESOLVED':  <pre> {
     \"state\": \"RESOLVED\"
     }
     </pre>

    <strong>Note:</strong> the supplied JSON object must contain a <code>version</code> that must match
    the server's version of the comment or the update will fail. To determine the current version of the
    comment, the comment should be fetched from the server prior to the update. Look for the 'version'
    attribute in the returned JSON structure.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        comment_id (str):
        body (RestComment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestComment | UpdateComment2Response400 | UpdateComment2Response401 | UpdateComment2Response404 | UpdateComment2Response409
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
