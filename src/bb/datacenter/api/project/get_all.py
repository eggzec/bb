from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_response_200 import GetAllResponse200
from ...models.get_all_response_400 import GetAllResponse400
from ...models.get_all_response_401 import GetAllResponse401
from ...models.get_all_response_404 import GetAllResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    namespace: str,
    feature_key: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["namespace"] = namespace

    params["featureKey"] = feature_key

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/settings-restriction/all".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404 | None:
    if response.status_code == 200:
        response_200 = GetAllResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAllResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAllResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetAllResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    namespace: str,
    feature_key: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404]:
    """Get all enforcing project settings

     Get all project settings restrictions for the given namespace and feature key, including those with
    a component key set.

    The authenticated user must have **PROJECT_VIEW** permission for the target project to retrieve a
    settings restrictions.

    Args:
        project_key (str):
        namespace (str):
        feature_key (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        namespace=namespace,
        feature_key=feature_key,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    namespace: str,
    feature_key: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404 | None:
    """Get all enforcing project settings

     Get all project settings restrictions for the given namespace and feature key, including those with
    a component key set.

    The authenticated user must have **PROJECT_VIEW** permission for the target project to retrieve a
    settings restrictions.

    Args:
        project_key (str):
        namespace (str):
        feature_key (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        namespace=namespace,
        feature_key=feature_key,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    namespace: str,
    feature_key: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404]:
    """Get all enforcing project settings

     Get all project settings restrictions for the given namespace and feature key, including those with
    a component key set.

    The authenticated user must have **PROJECT_VIEW** permission for the target project to retrieve a
    settings restrictions.

    Args:
        project_key (str):
        namespace (str):
        feature_key (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        namespace=namespace,
        feature_key=feature_key,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    namespace: str,
    feature_key: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404 | None:
    """Get all enforcing project settings

     Get all project settings restrictions for the given namespace and feature key, including those with
    a component key set.

    The authenticated user must have **PROJECT_VIEW** permission for the target project to retrieve a
    settings restrictions.

    Args:
        project_key (str):
        namespace (str):
        feature_key (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllResponse200 | GetAllResponse400 | GetAllResponse401 | GetAllResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            namespace=namespace,
            feature_key=feature_key,
            start=start,
            limit=limit,
        )
    ).parsed
