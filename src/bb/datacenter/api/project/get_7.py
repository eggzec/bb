from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_7_response_400 import Get7Response400
from ...models.get_7_response_401 import Get7Response401
from ...models.get_7_response_404 import Get7Response404
from ...models.rest_project_settings_restriction import RestProjectSettingsRestriction
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
        "method": "get",
        "url": "/api/latest/projects/{project_key}/settings-restriction".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction | None:
    if response.status_code == 200:
        response_200 = RestProjectSettingsRestriction.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Get7Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Get7Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Get7Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction]:
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
) -> Response[Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction]:
    """Get enforcing project setting

     Get a specified project settings restriction for the given namespace, feature key and component key.
    Note that not providing the component key will **not** return restrictions for the namespace and
    feature key with a component key set.

    The authenticated user must have **PROJECT_VIEW** permission for the target project to retrieve a
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
        Response[Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction]
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
) -> Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction | None:
    """Get enforcing project setting

     Get a specified project settings restriction for the given namespace, feature key and component key.
    Note that not providing the component key will **not** return restrictions for the namespace and
    feature key with a component key set.

    The authenticated user must have **PROJECT_VIEW** permission for the target project to retrieve a
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
        Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction
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
) -> Response[Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction]:
    """Get enforcing project setting

     Get a specified project settings restriction for the given namespace, feature key and component key.
    Note that not providing the component key will **not** return restrictions for the namespace and
    feature key with a component key set.

    The authenticated user must have **PROJECT_VIEW** permission for the target project to retrieve a
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
        Response[Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction]
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
) -> Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction | None:
    """Get enforcing project setting

     Get a specified project settings restriction for the given namespace, feature key and component key.
    Note that not providing the component key will **not** return restrictions for the namespace and
    feature key with a component key set.

    The authenticated user must have **PROJECT_VIEW** permission for the target project to retrieve a
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
        Get7Response400 | Get7Response401 | Get7Response404 | RestProjectSettingsRestriction
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
