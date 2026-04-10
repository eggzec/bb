from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_ref_sync_request import RestRefSyncRequest
from ...models.rest_rejected_ref import RestRejectedRef
from ...models.synchronize_response_400 import SynchronizeResponse400
from ...models.synchronize_response_401 import SynchronizeResponse401
from ...models.synchronize_response_404 import SynchronizeResponse404
from ...models.synchronize_response_409 import SynchronizeResponse409
from ...models.synchronize_response_501 import SynchronizeResponse501
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestRefSyncRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sync/latest/projects/{project_key}/repos/{repository_slug}/synchronize".format(
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
) -> (
    Any
    | RestRejectedRef
    | SynchronizeResponse400
    | SynchronizeResponse401
    | SynchronizeResponse404
    | SynchronizeResponse409
    | SynchronizeResponse501
    | None
):
    if response.status_code == 200:
        response_200 = RestRejectedRef.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = SynchronizeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SynchronizeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SynchronizeResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = SynchronizeResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 501:
        response_501 = SynchronizeResponse501.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | RestRejectedRef
    | SynchronizeResponse400
    | SynchronizeResponse401
    | SynchronizeResponse404
    | SynchronizeResponse409
    | SynchronizeResponse501
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
    *,
    client: AuthenticatedClient | Client,
    body: RestRefSyncRequest | Unset = UNSET,
) -> Response[
    Any
    | RestRejectedRef
    | SynchronizeResponse400
    | SynchronizeResponse401
    | SynchronizeResponse404
    | SynchronizeResponse409
    | SynchronizeResponse501
]:
    r"""Manual synchronization

     Allows developers to apply a manual operation to bring a ref back in sync with upstream when it
    becomes out of sync due to conflicting changes. The following actions are supported:

    - <tt>MERGE</tt>: Merges in commits from the upstream ref. After applying this action, the
    synchronized ref will be <tt>AHEAD</tt> (as it still includes commits that do not exist   upstream.
       - This action is only supported for <tt>DIVERGED</tt> refs
       - If a \"commitMessage\" is provided in the context, it will be used on the merge commit.
    Otherwise a default message is used.
    - <tt>DISCARD</tt>: <i>Throws away</i> local changes in favour of those made upstream. This is a
    <i>destructive</i> operation where commits in the local repository are lost.
       - No context entries are supported for this action
       - If the upstream ref has been deleted, the local ref is deleted as well
       - Otherwise, the local ref is updated to reference the same commit as upstream, even if      the
    update is not fast-forward (similar to a forced push)


    The authenticated user must have <b>REPO_WRITE</b> permission for the specified repository.
    Anonymous users cannot synchronize refs, even on public repositories. Additionally, synchronization
    must be <i>enabled</i> and <i>available</i> for the specified repository.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRefSyncRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RestRejectedRef | SynchronizeResponse400 | SynchronizeResponse401 | SynchronizeResponse404 | SynchronizeResponse409 | SynchronizeResponse501]
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
    body: RestRefSyncRequest | Unset = UNSET,
) -> (
    Any
    | RestRejectedRef
    | SynchronizeResponse400
    | SynchronizeResponse401
    | SynchronizeResponse404
    | SynchronizeResponse409
    | SynchronizeResponse501
    | None
):
    r"""Manual synchronization

     Allows developers to apply a manual operation to bring a ref back in sync with upstream when it
    becomes out of sync due to conflicting changes. The following actions are supported:

    - <tt>MERGE</tt>: Merges in commits from the upstream ref. After applying this action, the
    synchronized ref will be <tt>AHEAD</tt> (as it still includes commits that do not exist   upstream.
       - This action is only supported for <tt>DIVERGED</tt> refs
       - If a \"commitMessage\" is provided in the context, it will be used on the merge commit.
    Otherwise a default message is used.
    - <tt>DISCARD</tt>: <i>Throws away</i> local changes in favour of those made upstream. This is a
    <i>destructive</i> operation where commits in the local repository are lost.
       - No context entries are supported for this action
       - If the upstream ref has been deleted, the local ref is deleted as well
       - Otherwise, the local ref is updated to reference the same commit as upstream, even if      the
    update is not fast-forward (similar to a forced push)


    The authenticated user must have <b>REPO_WRITE</b> permission for the specified repository.
    Anonymous users cannot synchronize refs, even on public repositories. Additionally, synchronization
    must be <i>enabled</i> and <i>available</i> for the specified repository.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRefSyncRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RestRejectedRef | SynchronizeResponse400 | SynchronizeResponse401 | SynchronizeResponse404 | SynchronizeResponse409 | SynchronizeResponse501
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
    body: RestRefSyncRequest | Unset = UNSET,
) -> Response[
    Any
    | RestRejectedRef
    | SynchronizeResponse400
    | SynchronizeResponse401
    | SynchronizeResponse404
    | SynchronizeResponse409
    | SynchronizeResponse501
]:
    r"""Manual synchronization

     Allows developers to apply a manual operation to bring a ref back in sync with upstream when it
    becomes out of sync due to conflicting changes. The following actions are supported:

    - <tt>MERGE</tt>: Merges in commits from the upstream ref. After applying this action, the
    synchronized ref will be <tt>AHEAD</tt> (as it still includes commits that do not exist   upstream.
       - This action is only supported for <tt>DIVERGED</tt> refs
       - If a \"commitMessage\" is provided in the context, it will be used on the merge commit.
    Otherwise a default message is used.
    - <tt>DISCARD</tt>: <i>Throws away</i> local changes in favour of those made upstream. This is a
    <i>destructive</i> operation where commits in the local repository are lost.
       - No context entries are supported for this action
       - If the upstream ref has been deleted, the local ref is deleted as well
       - Otherwise, the local ref is updated to reference the same commit as upstream, even if      the
    update is not fast-forward (similar to a forced push)


    The authenticated user must have <b>REPO_WRITE</b> permission for the specified repository.
    Anonymous users cannot synchronize refs, even on public repositories. Additionally, synchronization
    must be <i>enabled</i> and <i>available</i> for the specified repository.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRefSyncRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RestRejectedRef | SynchronizeResponse400 | SynchronizeResponse401 | SynchronizeResponse404 | SynchronizeResponse409 | SynchronizeResponse501]
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
    body: RestRefSyncRequest | Unset = UNSET,
) -> (
    Any
    | RestRejectedRef
    | SynchronizeResponse400
    | SynchronizeResponse401
    | SynchronizeResponse404
    | SynchronizeResponse409
    | SynchronizeResponse501
    | None
):
    r"""Manual synchronization

     Allows developers to apply a manual operation to bring a ref back in sync with upstream when it
    becomes out of sync due to conflicting changes. The following actions are supported:

    - <tt>MERGE</tt>: Merges in commits from the upstream ref. After applying this action, the
    synchronized ref will be <tt>AHEAD</tt> (as it still includes commits that do not exist   upstream.
       - This action is only supported for <tt>DIVERGED</tt> refs
       - If a \"commitMessage\" is provided in the context, it will be used on the merge commit.
    Otherwise a default message is used.
    - <tt>DISCARD</tt>: <i>Throws away</i> local changes in favour of those made upstream. This is a
    <i>destructive</i> operation where commits in the local repository are lost.
       - No context entries are supported for this action
       - If the upstream ref has been deleted, the local ref is deleted as well
       - Otherwise, the local ref is updated to reference the same commit as upstream, even if      the
    update is not fast-forward (similar to a forced push)


    The authenticated user must have <b>REPO_WRITE</b> permission for the specified repository.
    Anonymous users cannot synchronize refs, even on public repositories. Additionally, synchronization
    must be <i>enabled</i> and <i>available</i> for the specified repository.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRefSyncRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RestRejectedRef | SynchronizeResponse400 | SynchronizeResponse401 | SynchronizeResponse404 | SynchronizeResponse409 | SynchronizeResponse501
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
