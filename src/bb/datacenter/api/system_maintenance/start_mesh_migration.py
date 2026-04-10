from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_job import RestJob
from ...models.start_mesh_migration_body import StartMeshMigrationBody
from ...models.start_mesh_migration_response_400 import StartMeshMigrationResponse400
from ...models.start_mesh_migration_response_401 import StartMeshMigrationResponse401
from ...models.start_mesh_migration_response_503 import StartMeshMigrationResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: StartMeshMigrationBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/migration/mesh",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503 | None:
    if response.status_code == 200:
        response_200 = RestJob.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StartMeshMigrationResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StartMeshMigrationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 503:
        response_503 = StartMeshMigrationResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartMeshMigrationBody | Unset = UNSET,
) -> Response[RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503]:
    r"""Start Mesh migration job

     Starts a background job that migrates selected projects/repositories to Mesh.

    Only 1 job is supported _per cluster_.

    The response includes a description of the job that has been started, and its ID can be used to
    query these details again, including the current progress, and to interrupt and cancel the execution
    of this job.

    The request to start a migration is similar to the one for previewing a migration.

    There are essentially three ways to select repositories for migration. Regardless of which you use,
    a few general rules apply:

        - You can supply a list of repository IDs and project IDs. The selection will be additive. All
    repositories     in the system are migrated if both lists are empty.     - Repositories that are
    selected more than once due to overlapping IDs will be de-duplicated and     effectively migrated
    only once.     - For every selected repository, its full fork hierarchy will be considered selected,
    even if parts of that     hierarchy would otherwise not be matched by the provided IDs. For example,
    when you explicitly     select a single repository only, but that repository is a fork, then its
    origin will be migrated too.

    Now, a single repository can be selected like this:

    ```

         {
         \"repositoryIds\": [1]
         }
    ```

    Multiple repositories can be selected like this:



    ```

         {
         \"repositoryIds\": [1, 2]
         }
    ```

    Second, all repositories in a specific project can be selected like this:



    ```

         {
         \"projectIds\": [1]
         }
    ```

    And third, all projects and repositories in the system would be selected like this:



    ```

         {
         \"projectIds\": [],
         \"repositoryIds\": []
         }
    ```

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        body (StartMeshMigrationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: StartMeshMigrationBody | Unset = UNSET,
) -> RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503 | None:
    r"""Start Mesh migration job

     Starts a background job that migrates selected projects/repositories to Mesh.

    Only 1 job is supported _per cluster_.

    The response includes a description of the job that has been started, and its ID can be used to
    query these details again, including the current progress, and to interrupt and cancel the execution
    of this job.

    The request to start a migration is similar to the one for previewing a migration.

    There are essentially three ways to select repositories for migration. Regardless of which you use,
    a few general rules apply:

        - You can supply a list of repository IDs and project IDs. The selection will be additive. All
    repositories     in the system are migrated if both lists are empty.     - Repositories that are
    selected more than once due to overlapping IDs will be de-duplicated and     effectively migrated
    only once.     - For every selected repository, its full fork hierarchy will be considered selected,
    even if parts of that     hierarchy would otherwise not be matched by the provided IDs. For example,
    when you explicitly     select a single repository only, but that repository is a fork, then its
    origin will be migrated too.

    Now, a single repository can be selected like this:

    ```

         {
         \"repositoryIds\": [1]
         }
    ```

    Multiple repositories can be selected like this:



    ```

         {
         \"repositoryIds\": [1, 2]
         }
    ```

    Second, all repositories in a specific project can be selected like this:



    ```

         {
         \"projectIds\": [1]
         }
    ```

    And third, all projects and repositories in the system would be selected like this:



    ```

         {
         \"projectIds\": [],
         \"repositoryIds\": []
         }
    ```

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        body (StartMeshMigrationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartMeshMigrationBody | Unset = UNSET,
) -> Response[RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503]:
    r"""Start Mesh migration job

     Starts a background job that migrates selected projects/repositories to Mesh.

    Only 1 job is supported _per cluster_.

    The response includes a description of the job that has been started, and its ID can be used to
    query these details again, including the current progress, and to interrupt and cancel the execution
    of this job.

    The request to start a migration is similar to the one for previewing a migration.

    There are essentially three ways to select repositories for migration. Regardless of which you use,
    a few general rules apply:

        - You can supply a list of repository IDs and project IDs. The selection will be additive. All
    repositories     in the system are migrated if both lists are empty.     - Repositories that are
    selected more than once due to overlapping IDs will be de-duplicated and     effectively migrated
    only once.     - For every selected repository, its full fork hierarchy will be considered selected,
    even if parts of that     hierarchy would otherwise not be matched by the provided IDs. For example,
    when you explicitly     select a single repository only, but that repository is a fork, then its
    origin will be migrated too.

    Now, a single repository can be selected like this:

    ```

         {
         \"repositoryIds\": [1]
         }
    ```

    Multiple repositories can be selected like this:



    ```

         {
         \"repositoryIds\": [1, 2]
         }
    ```

    Second, all repositories in a specific project can be selected like this:



    ```

         {
         \"projectIds\": [1]
         }
    ```

    And third, all projects and repositories in the system would be selected like this:



    ```

         {
         \"projectIds\": [],
         \"repositoryIds\": []
         }
    ```

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        body (StartMeshMigrationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StartMeshMigrationBody | Unset = UNSET,
) -> RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503 | None:
    r"""Start Mesh migration job

     Starts a background job that migrates selected projects/repositories to Mesh.

    Only 1 job is supported _per cluster_.

    The response includes a description of the job that has been started, and its ID can be used to
    query these details again, including the current progress, and to interrupt and cancel the execution
    of this job.

    The request to start a migration is similar to the one for previewing a migration.

    There are essentially three ways to select repositories for migration. Regardless of which you use,
    a few general rules apply:

        - You can supply a list of repository IDs and project IDs. The selection will be additive. All
    repositories     in the system are migrated if both lists are empty.     - Repositories that are
    selected more than once due to overlapping IDs will be de-duplicated and     effectively migrated
    only once.     - For every selected repository, its full fork hierarchy will be considered selected,
    even if parts of that     hierarchy would otherwise not be matched by the provided IDs. For example,
    when you explicitly     select a single repository only, but that repository is a fork, then its
    origin will be migrated too.

    Now, a single repository can be selected like this:

    ```

         {
         \"repositoryIds\": [1]
         }
    ```

    Multiple repositories can be selected like this:



    ```

         {
         \"repositoryIds\": [1, 2]
         }
    ```

    Second, all repositories in a specific project can be selected like this:



    ```

         {
         \"projectIds\": [1]
         }
    ```

    And third, all projects and repositories in the system would be selected like this:



    ```

         {
         \"projectIds\": [],
         \"repositoryIds\": []
         }
    ```

    The authenticated user must have **SYS_ADMIN** permission to call this resource.

    Args:
        body (StartMeshMigrationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestJob | StartMeshMigrationResponse400 | StartMeshMigrationResponse401 | StartMeshMigrationResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
