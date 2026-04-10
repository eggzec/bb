from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_export_request import RestExportRequest
from ...models.rest_job import RestJob
from ...models.start_export_response_400 import StartExportResponse400
from ...models.start_export_response_401 import StartExportResponse401
from ...models.start_export_response_503 import StartExportResponse503
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestExportRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/migration/exports",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503 | None:
    if response.status_code == 200:
        response_200 = RestJob.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StartExportResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StartExportResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 503:
        response_503 = StartExportResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestExportRequest | Unset = UNSET,
) -> Response[RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503]:
    r"""Start export job

     Starts a background job that exports the selected repositories.

    Only 2 concurrent exports are supported _per cluster node_. If a request ends up on a node that is
    already running that many export jobs, the request will be rejected and an error returned.

    The response includes a description of the job that has been started, and its ID can be used to
    query these details again, including the current progress, warnings and errors that occurred while
    processing the job, and to interrupt and cancel the execution of this job.

    The request to start an export is similar to the one for previewing an export. Additionally, it
    accepts an optional parameter, `exportLocation`, which can be used to specify a _relative_ path
    within `data/migration/export` in the shared home directory. No locations outside of that directory
    will be accepted for exports.

    There are essentially three ways to select repositories for export. Regardless of which you use, a
    few general rules apply:

    - You can supply a list of selectors. The selection will be additive.
    - Repositories that are selected more than once due to overlapping selectors will be de-duplicated
    and effectively exported only once.
    - For every selected repository, its full fork hierarchy will be considered selected, even if parts
    of that hierarchy would otherwise not be matched by the provided selectors. For example, when you
    explicitly select a single repository only, but that repository is a fork, then its origin will be
    exported (and eventually imported), too.

    Now, a single repository can be selected like this:

    ```



    {
          \"projectKey\": \"PRJ\",
          \"slug\": \"my-repo\"
    }

    ```

    Second, all repositories in a specific project can be selected like this:

    ```



    {
          \"projectKey\": \"PRJ\",
          \"slug\": *\"
    }

    ```

    And third, all projects and repositories in the system would be selected like this:

    ```



    {
          \"projectKey\": \"*\",
          \"slug\": *\"
    }

    ```

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        body (RestExportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503]
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
    body: RestExportRequest | Unset = UNSET,
) -> RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503 | None:
    r"""Start export job

     Starts a background job that exports the selected repositories.

    Only 2 concurrent exports are supported _per cluster node_. If a request ends up on a node that is
    already running that many export jobs, the request will be rejected and an error returned.

    The response includes a description of the job that has been started, and its ID can be used to
    query these details again, including the current progress, warnings and errors that occurred while
    processing the job, and to interrupt and cancel the execution of this job.

    The request to start an export is similar to the one for previewing an export. Additionally, it
    accepts an optional parameter, `exportLocation`, which can be used to specify a _relative_ path
    within `data/migration/export` in the shared home directory. No locations outside of that directory
    will be accepted for exports.

    There are essentially three ways to select repositories for export. Regardless of which you use, a
    few general rules apply:

    - You can supply a list of selectors. The selection will be additive.
    - Repositories that are selected more than once due to overlapping selectors will be de-duplicated
    and effectively exported only once.
    - For every selected repository, its full fork hierarchy will be considered selected, even if parts
    of that hierarchy would otherwise not be matched by the provided selectors. For example, when you
    explicitly select a single repository only, but that repository is a fork, then its origin will be
    exported (and eventually imported), too.

    Now, a single repository can be selected like this:

    ```



    {
          \"projectKey\": \"PRJ\",
          \"slug\": \"my-repo\"
    }

    ```

    Second, all repositories in a specific project can be selected like this:

    ```



    {
          \"projectKey\": \"PRJ\",
          \"slug\": *\"
    }

    ```

    And third, all projects and repositories in the system would be selected like this:

    ```



    {
          \"projectKey\": \"*\",
          \"slug\": *\"
    }

    ```

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        body (RestExportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestExportRequest | Unset = UNSET,
) -> Response[RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503]:
    r"""Start export job

     Starts a background job that exports the selected repositories.

    Only 2 concurrent exports are supported _per cluster node_. If a request ends up on a node that is
    already running that many export jobs, the request will be rejected and an error returned.

    The response includes a description of the job that has been started, and its ID can be used to
    query these details again, including the current progress, warnings and errors that occurred while
    processing the job, and to interrupt and cancel the execution of this job.

    The request to start an export is similar to the one for previewing an export. Additionally, it
    accepts an optional parameter, `exportLocation`, which can be used to specify a _relative_ path
    within `data/migration/export` in the shared home directory. No locations outside of that directory
    will be accepted for exports.

    There are essentially three ways to select repositories for export. Regardless of which you use, a
    few general rules apply:

    - You can supply a list of selectors. The selection will be additive.
    - Repositories that are selected more than once due to overlapping selectors will be de-duplicated
    and effectively exported only once.
    - For every selected repository, its full fork hierarchy will be considered selected, even if parts
    of that hierarchy would otherwise not be matched by the provided selectors. For example, when you
    explicitly select a single repository only, but that repository is a fork, then its origin will be
    exported (and eventually imported), too.

    Now, a single repository can be selected like this:

    ```



    {
          \"projectKey\": \"PRJ\",
          \"slug\": \"my-repo\"
    }

    ```

    Second, all repositories in a specific project can be selected like this:

    ```



    {
          \"projectKey\": \"PRJ\",
          \"slug\": *\"
    }

    ```

    And third, all projects and repositories in the system would be selected like this:

    ```



    {
          \"projectKey\": \"*\",
          \"slug\": *\"
    }

    ```

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        body (RestExportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestExportRequest | Unset = UNSET,
) -> RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503 | None:
    r"""Start export job

     Starts a background job that exports the selected repositories.

    Only 2 concurrent exports are supported _per cluster node_. If a request ends up on a node that is
    already running that many export jobs, the request will be rejected and an error returned.

    The response includes a description of the job that has been started, and its ID can be used to
    query these details again, including the current progress, warnings and errors that occurred while
    processing the job, and to interrupt and cancel the execution of this job.

    The request to start an export is similar to the one for previewing an export. Additionally, it
    accepts an optional parameter, `exportLocation`, which can be used to specify a _relative_ path
    within `data/migration/export` in the shared home directory. No locations outside of that directory
    will be accepted for exports.

    There are essentially three ways to select repositories for export. Regardless of which you use, a
    few general rules apply:

    - You can supply a list of selectors. The selection will be additive.
    - Repositories that are selected more than once due to overlapping selectors will be de-duplicated
    and effectively exported only once.
    - For every selected repository, its full fork hierarchy will be considered selected, even if parts
    of that hierarchy would otherwise not be matched by the provided selectors. For example, when you
    explicitly select a single repository only, but that repository is a fork, then its origin will be
    exported (and eventually imported), too.

    Now, a single repository can be selected like this:

    ```



    {
          \"projectKey\": \"PRJ\",
          \"slug\": \"my-repo\"
    }

    ```

    Second, all repositories in a specific project can be selected like this:

    ```



    {
          \"projectKey\": \"PRJ\",
          \"slug\": *\"
    }

    ```

    And third, all projects and repositories in the system would be selected like this:

    ```



    {
          \"projectKey\": \"*\",
          \"slug\": *\"
    }

    ```

    The authenticated user must have **ADMIN** permission or higher to call this resource.

    Args:
        body (RestExportRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestJob | StartExportResponse400 | StartExportResponse401 | StartExportResponse503
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
