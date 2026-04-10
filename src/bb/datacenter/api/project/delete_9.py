from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_9_response_400 import Delete9Response400
from ...models.delete_9_response_401 import Delete9Response401
from ...models.delete_9_response_404 import Delete9Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    namespace: str,
    component_key: str | Unset = UNSET,
    feature_key: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["namespace"] = namespace

    params["componentKey"] = component_key

    params["featureKey"] = feature_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/settings-restriction".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Delete9Response400 | Delete9Response401 | Delete9Response404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Delete9Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Delete9Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Delete9Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Delete9Response400 | Delete9Response401 | Delete9Response404]:
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
    component_key: str | Unset = UNSET,
    feature_key: str,
) -> Response[Any | Delete9Response400 | Delete9Response401 | Delete9Response404]:
    """Stop enforcing project restriction

     Delete a specified project settings restriction.

    If a restriction does not exist for the specified project, namespace, featureKey, and componentKey,
    the request will be ignored and a 204 response will be returned.

    The authenticated user must have **PROJECT_ADMIN** permission for the target project to delete a
    settings restriction.

    Args:
        project_key (str):
        namespace (str):
        component_key (str | Unset):
        feature_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Delete9Response400 | Delete9Response401 | Delete9Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        namespace=namespace,
        component_key=component_key,
        feature_key=feature_key,
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
    component_key: str | Unset = UNSET,
    feature_key: str,
) -> Any | Delete9Response400 | Delete9Response401 | Delete9Response404 | None:
    """Stop enforcing project restriction

     Delete a specified project settings restriction.

    If a restriction does not exist for the specified project, namespace, featureKey, and componentKey,
    the request will be ignored and a 204 response will be returned.

    The authenticated user must have **PROJECT_ADMIN** permission for the target project to delete a
    settings restriction.

    Args:
        project_key (str):
        namespace (str):
        component_key (str | Unset):
        feature_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Delete9Response400 | Delete9Response401 | Delete9Response404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        namespace=namespace,
        component_key=component_key,
        feature_key=feature_key,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    namespace: str,
    component_key: str | Unset = UNSET,
    feature_key: str,
) -> Response[Any | Delete9Response400 | Delete9Response401 | Delete9Response404]:
    """Stop enforcing project restriction

     Delete a specified project settings restriction.

    If a restriction does not exist for the specified project, namespace, featureKey, and componentKey,
    the request will be ignored and a 204 response will be returned.

    The authenticated user must have **PROJECT_ADMIN** permission for the target project to delete a
    settings restriction.

    Args:
        project_key (str):
        namespace (str):
        component_key (str | Unset):
        feature_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Delete9Response400 | Delete9Response401 | Delete9Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        namespace=namespace,
        component_key=component_key,
        feature_key=feature_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    namespace: str,
    component_key: str | Unset = UNSET,
    feature_key: str,
) -> Any | Delete9Response400 | Delete9Response401 | Delete9Response404 | None:
    """Stop enforcing project restriction

     Delete a specified project settings restriction.

    If a restriction does not exist for the specified project, namespace, featureKey, and componentKey,
    the request will be ignored and a 204 response will be returned.

    The authenticated user must have **PROJECT_ADMIN** permission for the target project to delete a
    settings restriction.

    Args:
        project_key (str):
        namespace (str):
        component_key (str | Unset):
        feature_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Delete9Response400 | Delete9Response401 | Delete9Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            namespace=namespace,
            component_key=component_key,
            feature_key=feature_key,
        )
    ).parsed
