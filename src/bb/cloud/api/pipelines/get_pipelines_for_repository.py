import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_pipelines_for_repository_sort import GetPipelinesForRepositorySort
from ...models.get_pipelines_for_repository_status import GetPipelinesForRepositoryStatus
from ...models.get_pipelines_for_repository_target_ref_type import GetPipelinesForRepositoryTargetRefType
from ...models.get_pipelines_for_repository_target_selector_type import GetPipelinesForRepositoryTargetSelectorType
from ...models.get_pipelines_for_repository_trigger_type import GetPipelinesForRepositoryTriggerType
from ...models.paginated_pipelines import PaginatedPipelines
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    creator_uuid: UUID | Unset = UNSET,
    target_ref_type: GetPipelinesForRepositoryTargetRefType | Unset = UNSET,
    target_ref_name: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    target_commit_hash: str | Unset = UNSET,
    target_selector_pattern: str | Unset = UNSET,
    target_selector_type: GetPipelinesForRepositoryTargetSelectorType | Unset = UNSET,
    created_on: datetime.datetime | Unset = UNSET,
    trigger_type: GetPipelinesForRepositoryTriggerType | Unset = UNSET,
    status: GetPipelinesForRepositoryStatus | Unset = UNSET,
    sort: GetPipelinesForRepositorySort | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_creator_uuid: str | Unset = UNSET
    if not isinstance(creator_uuid, Unset):
        json_creator_uuid = str(creator_uuid)
    params["creator.uuid"] = json_creator_uuid

    json_target_ref_type: str | Unset = UNSET
    if not isinstance(target_ref_type, Unset):
        json_target_ref_type = target_ref_type.value

    params["target.ref_type"] = json_target_ref_type

    params["target.ref_name"] = target_ref_name

    params["target.branch"] = target_branch

    params["target.commit.hash"] = target_commit_hash

    params["target.selector.pattern"] = target_selector_pattern

    json_target_selector_type: str | Unset = UNSET
    if not isinstance(target_selector_type, Unset):
        json_target_selector_type = target_selector_type.value

    params["target.selector.type"] = json_target_selector_type

    json_created_on: str | Unset = UNSET
    if not isinstance(created_on, Unset):
        json_created_on = created_on.isoformat()
    params["created_on"] = json_created_on

    json_trigger_type: str | Unset = UNSET
    if not isinstance(trigger_type, Unset):
        json_trigger_type = trigger_type.value

    params["trigger_type"] = json_trigger_type

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/pipelines".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = PaginatedPipelines
type ParseResult = PaginatedPipelines | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedPipelines.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    creator_uuid: UUID | Unset = UNSET,
    target_ref_type: GetPipelinesForRepositoryTargetRefType | Unset = UNSET,
    target_ref_name: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    target_commit_hash: str | Unset = UNSET,
    target_selector_pattern: str | Unset = UNSET,
    target_selector_type: GetPipelinesForRepositoryTargetSelectorType | Unset = UNSET,
    created_on: datetime.datetime | Unset = UNSET,
    trigger_type: GetPipelinesForRepositoryTriggerType | Unset = UNSET,
    status: GetPipelinesForRepositoryStatus | Unset = UNSET,
    sort: GetPipelinesForRepositorySort | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    """List pipelines

     Find pipelines in a repository.

    Note that unlike other endpoints in the Bitbucket API, this endpoint utilizes query parameters to
    allow filtering
    and sorting of returned results. See [query parameters](#api-repositories-workspace-repo-slug-
    pipelines-get-request-Query%20parameters)
    for specific details.

    Args:
        workspace (str):
        repo_slug (str):
        creator_uuid (UUID | Unset):
        target_ref_type (GetPipelinesForRepositoryTargetRefType | Unset):
        target_ref_name (str | Unset):
        target_branch (str | Unset):
        target_commit_hash (str | Unset):
        target_selector_pattern (str | Unset):
        target_selector_type (GetPipelinesForRepositoryTargetSelectorType | Unset):
        created_on (datetime.datetime | Unset):
        trigger_type (GetPipelinesForRepositoryTriggerType | Unset):
        status (GetPipelinesForRepositoryStatus | Unset):
        sort (GetPipelinesForRepositorySort | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPipelines]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        creator_uuid=creator_uuid,
        target_ref_type=target_ref_type,
        target_ref_name=target_ref_name,
        target_branch=target_branch,
        target_commit_hash=target_commit_hash,
        target_selector_pattern=target_selector_pattern,
        target_selector_type=target_selector_type,
        created_on=created_on,
        trigger_type=trigger_type,
        status=status,
        sort=sort,
        page=page,
        pagelen=pagelen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    creator_uuid: UUID | Unset = UNSET,
    target_ref_type: GetPipelinesForRepositoryTargetRefType | Unset = UNSET,
    target_ref_name: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    target_commit_hash: str | Unset = UNSET,
    target_selector_pattern: str | Unset = UNSET,
    target_selector_type: GetPipelinesForRepositoryTargetSelectorType | Unset = UNSET,
    created_on: datetime.datetime | Unset = UNSET,
    trigger_type: GetPipelinesForRepositoryTriggerType | Unset = UNSET,
    status: GetPipelinesForRepositoryStatus | Unset = UNSET,
    sort: GetPipelinesForRepositorySort | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    """List pipelines

     Find pipelines in a repository.

    Note that unlike other endpoints in the Bitbucket API, this endpoint utilizes query parameters to
    allow filtering
    and sorting of returned results. See [query parameters](#api-repositories-workspace-repo-slug-
    pipelines-get-request-Query%20parameters)
    for specific details.

    Args:
        workspace (str):
        repo_slug (str):
        creator_uuid (UUID | Unset):
        target_ref_type (GetPipelinesForRepositoryTargetRefType | Unset):
        target_ref_name (str | Unset):
        target_branch (str | Unset):
        target_commit_hash (str | Unset):
        target_selector_pattern (str | Unset):
        target_selector_type (GetPipelinesForRepositoryTargetSelectorType | Unset):
        created_on (datetime.datetime | Unset):
        trigger_type (GetPipelinesForRepositoryTriggerType | Unset):
        status (GetPipelinesForRepositoryStatus | Unset):
        sort (GetPipelinesForRepositorySort | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPipelines
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        creator_uuid=creator_uuid,
        target_ref_type=target_ref_type,
        target_ref_name=target_ref_name,
        target_branch=target_branch,
        target_commit_hash=target_commit_hash,
        target_selector_pattern=target_selector_pattern,
        target_selector_type=target_selector_type,
        created_on=created_on,
        trigger_type=trigger_type,
        status=status,
        sort=sort,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    creator_uuid: UUID | Unset = UNSET,
    target_ref_type: GetPipelinesForRepositoryTargetRefType | Unset = UNSET,
    target_ref_name: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    target_commit_hash: str | Unset = UNSET,
    target_selector_pattern: str | Unset = UNSET,
    target_selector_type: GetPipelinesForRepositoryTargetSelectorType | Unset = UNSET,
    created_on: datetime.datetime | Unset = UNSET,
    trigger_type: GetPipelinesForRepositoryTriggerType | Unset = UNSET,
    status: GetPipelinesForRepositoryStatus | Unset = UNSET,
    sort: GetPipelinesForRepositorySort | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    """List pipelines

     Find pipelines in a repository.

    Note that unlike other endpoints in the Bitbucket API, this endpoint utilizes query parameters to
    allow filtering
    and sorting of returned results. See [query parameters](#api-repositories-workspace-repo-slug-
    pipelines-get-request-Query%20parameters)
    for specific details.

    Args:
        workspace (str):
        repo_slug (str):
        creator_uuid (UUID | Unset):
        target_ref_type (GetPipelinesForRepositoryTargetRefType | Unset):
        target_ref_name (str | Unset):
        target_branch (str | Unset):
        target_commit_hash (str | Unset):
        target_selector_pattern (str | Unset):
        target_selector_type (GetPipelinesForRepositoryTargetSelectorType | Unset):
        created_on (datetime.datetime | Unset):
        trigger_type (GetPipelinesForRepositoryTriggerType | Unset):
        status (GetPipelinesForRepositoryStatus | Unset):
        sort (GetPipelinesForRepositorySort | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPipelines]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        creator_uuid=creator_uuid,
        target_ref_type=target_ref_type,
        target_ref_name=target_ref_name,
        target_branch=target_branch,
        target_commit_hash=target_commit_hash,
        target_selector_pattern=target_selector_pattern,
        target_selector_type=target_selector_type,
        created_on=created_on,
        trigger_type=trigger_type,
        status=status,
        sort=sort,
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    creator_uuid: UUID | Unset = UNSET,
    target_ref_type: GetPipelinesForRepositoryTargetRefType | Unset = UNSET,
    target_ref_name: str | Unset = UNSET,
    target_branch: str | Unset = UNSET,
    target_commit_hash: str | Unset = UNSET,
    target_selector_pattern: str | Unset = UNSET,
    target_selector_type: GetPipelinesForRepositoryTargetSelectorType | Unset = UNSET,
    created_on: datetime.datetime | Unset = UNSET,
    trigger_type: GetPipelinesForRepositoryTriggerType | Unset = UNSET,
    status: GetPipelinesForRepositoryStatus | Unset = UNSET,
    sort: GetPipelinesForRepositorySort | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    """List pipelines

     Find pipelines in a repository.

    Note that unlike other endpoints in the Bitbucket API, this endpoint utilizes query parameters to
    allow filtering
    and sorting of returned results. See [query parameters](#api-repositories-workspace-repo-slug-
    pipelines-get-request-Query%20parameters)
    for specific details.

    Args:
        workspace (str):
        repo_slug (str):
        creator_uuid (UUID | Unset):
        target_ref_type (GetPipelinesForRepositoryTargetRefType | Unset):
        target_ref_name (str | Unset):
        target_branch (str | Unset):
        target_commit_hash (str | Unset):
        target_selector_pattern (str | Unset):
        target_selector_type (GetPipelinesForRepositoryTargetSelectorType | Unset):
        created_on (datetime.datetime | Unset):
        trigger_type (GetPipelinesForRepositoryTriggerType | Unset):
        status (GetPipelinesForRepositoryStatus | Unset):
        sort (GetPipelinesForRepositorySort | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPipelines
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            creator_uuid=creator_uuid,
            target_ref_type=target_ref_type,
            target_ref_name=target_ref_name,
            target_branch=target_branch,
            target_commit_hash=target_commit_hash,
            target_selector_pattern=target_selector_pattern,
            target_selector_type=target_selector_type,
            created_on=created_on,
            trigger_type=trigger_type,
            status=status,
            sort=sort,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
