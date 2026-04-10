from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.can_rebase_response_401 import CanRebaseResponse401
from ...models.can_rebase_response_404 import CanRebaseResponse404
from ...models.rest_pull_request_rebaseability import RestPullRequestRebaseability
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/git/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/rebase".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability | None:
    if response.status_code == 200:
        response_200 = RestPullRequestRebaseability.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = CanRebaseResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CanRebaseResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability]:
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
) -> Response[CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability]:
    r"""Check PR rebase precondition

     Checks preconditions to determine whether the pull request can be rebased.

    Some of the preconditions are:

    - The pull request is between Git repositories
    - The pull request is currently open
    - The pull request's {@link PullRequest#getFromRef \"from\" ref} is a <i>branch</i>
       - In other words, the qualified ID for the \"from\" ref must start with <code>refs/heads/</code>
       - Tags, and other non-standard refs, cannot be rebased
    - The current user has an e-mail address
       - Pull requests cannot be rebased anonymously
       - `git rebase` records the current user as the committer for the rebased commits, which
    requires a name and e-mail address
    - The current user has <i>write</i> access to the {@link PullRequest#getFromRef \"from\" ref}'s
    repository
       - Note that in order to <i>view</i> a pull request a user is only required to have <i>read</i>
    access to the {@link PullRequest#getToRef toRef}'s repository, so just because a user can <i>see</i>
    a pull request does not mean they can request a rebase


    This list is not exhaustive, and the exact set of preconditions applied can be extended by third-
    party add-ons.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
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
) -> CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability | None:
    r"""Check PR rebase precondition

     Checks preconditions to determine whether the pull request can be rebased.

    Some of the preconditions are:

    - The pull request is between Git repositories
    - The pull request is currently open
    - The pull request's {@link PullRequest#getFromRef \"from\" ref} is a <i>branch</i>
       - In other words, the qualified ID for the \"from\" ref must start with <code>refs/heads/</code>
       - Tags, and other non-standard refs, cannot be rebased
    - The current user has an e-mail address
       - Pull requests cannot be rebased anonymously
       - `git rebase` records the current user as the committer for the rebased commits, which
    requires a name and e-mail address
    - The current user has <i>write</i> access to the {@link PullRequest#getFromRef \"from\" ref}'s
    repository
       - Note that in order to <i>view</i> a pull request a user is only required to have <i>read</i>
    access to the {@link PullRequest#getToRef toRef}'s repository, so just because a user can <i>see</i>
    a pull request does not mean they can request a rebase


    This list is not exhaustive, and the exact set of preconditions applied can be extended by third-
    party add-ons.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability]:
    r"""Check PR rebase precondition

     Checks preconditions to determine whether the pull request can be rebased.

    Some of the preconditions are:

    - The pull request is between Git repositories
    - The pull request is currently open
    - The pull request's {@link PullRequest#getFromRef \"from\" ref} is a <i>branch</i>
       - In other words, the qualified ID for the \"from\" ref must start with <code>refs/heads/</code>
       - Tags, and other non-standard refs, cannot be rebased
    - The current user has an e-mail address
       - Pull requests cannot be rebased anonymously
       - `git rebase` records the current user as the committer for the rebased commits, which
    requires a name and e-mail address
    - The current user has <i>write</i> access to the {@link PullRequest#getFromRef \"from\" ref}'s
    repository
       - Note that in order to <i>view</i> a pull request a user is only required to have <i>read</i>
    access to the {@link PullRequest#getToRef toRef}'s repository, so just because a user can <i>see</i>
    a pull request does not mean they can request a rebase


    This list is not exhaustive, and the exact set of preconditions applied can be extended by third-
    party add-ons.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability | None:
    r"""Check PR rebase precondition

     Checks preconditions to determine whether the pull request can be rebased.

    Some of the preconditions are:

    - The pull request is between Git repositories
    - The pull request is currently open
    - The pull request's {@link PullRequest#getFromRef \"from\" ref} is a <i>branch</i>
       - In other words, the qualified ID for the \"from\" ref must start with <code>refs/heads/</code>
       - Tags, and other non-standard refs, cannot be rebased
    - The current user has an e-mail address
       - Pull requests cannot be rebased anonymously
       - `git rebase` records the current user as the committer for the rebased commits, which
    requires a name and e-mail address
    - The current user has <i>write</i> access to the {@link PullRequest#getFromRef \"from\" ref}'s
    repository
       - Note that in order to <i>view</i> a pull request a user is only required to have <i>read</i>
    access to the {@link PullRequest#getToRef toRef}'s repository, so just because a user can <i>see</i>
    a pull request does not mean they can request a rebase


    This list is not exhaustive, and the exact set of preconditions applied can be extended by third-
    party add-ons.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CanRebaseResponse401 | CanRebaseResponse404 | RestPullRequestRebaseability
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
        )
    ).parsed
