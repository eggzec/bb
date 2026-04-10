from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_pull_request_settings import RestPullRequestSettings
from ...models.update_pull_request_settings_response_400 import UpdatePullRequestSettingsResponse400
from ...models.update_pull_request_settings_response_401 import UpdatePullRequestSettingsResponse401
from ...models.update_pull_request_settings_response_404 import UpdatePullRequestSettingsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    scm_id: str,
    *,
    body: RestPullRequestSettings | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/settings/pull-requests/{scm_id}".format(
            project_key=quote(str(project_key), safe=""),
            scm_id=quote(str(scm_id), safe=""),
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
    RestPullRequestSettings
    | UpdatePullRequestSettingsResponse400
    | UpdatePullRequestSettingsResponse401
    | UpdatePullRequestSettingsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = RestPullRequestSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdatePullRequestSettingsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdatePullRequestSettingsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdatePullRequestSettingsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestPullRequestSettings
    | UpdatePullRequestSettingsResponse400
    | UpdatePullRequestSettingsResponse401
    | UpdatePullRequestSettingsResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestSettings | Unset = UNSET,
) -> Response[
    RestPullRequestSettings
    | UpdatePullRequestSettingsResponse400
    | UpdatePullRequestSettingsResponse401
    | UpdatePullRequestSettingsResponse404
]:
    r"""Update merge strategy

     Update the pull request merge strategy configuration for this project and SCM.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the context
    repository to call this resource.

    Only the strategies provided will be enabled, the default must be set and included in the set of
    strategies.

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty \"mergeConfig\" attribute. i.e:
    <pre>{
        \"mergeConfig\": {}
    }
    </pre>

    Upon completion of this request, the effective configuration will be the configuration explicitly
    set for the SCM, or if no such explicit configuration is set then the default configuration will be
    used.

    Args:
        project_key (str):
        scm_id (str):
        body (RestPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestSettings | UpdatePullRequestSettingsResponse400 | UpdatePullRequestSettingsResponse401 | UpdatePullRequestSettingsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        scm_id=scm_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestSettings | Unset = UNSET,
) -> (
    RestPullRequestSettings
    | UpdatePullRequestSettingsResponse400
    | UpdatePullRequestSettingsResponse401
    | UpdatePullRequestSettingsResponse404
    | None
):
    r"""Update merge strategy

     Update the pull request merge strategy configuration for this project and SCM.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the context
    repository to call this resource.

    Only the strategies provided will be enabled, the default must be set and included in the set of
    strategies.

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty \"mergeConfig\" attribute. i.e:
    <pre>{
        \"mergeConfig\": {}
    }
    </pre>

    Upon completion of this request, the effective configuration will be the configuration explicitly
    set for the SCM, or if no such explicit configuration is set then the default configuration will be
    used.

    Args:
        project_key (str):
        scm_id (str):
        body (RestPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestSettings | UpdatePullRequestSettingsResponse400 | UpdatePullRequestSettingsResponse401 | UpdatePullRequestSettingsResponse404
    """

    return sync_detailed(
        project_key=project_key,
        scm_id=scm_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestSettings | Unset = UNSET,
) -> Response[
    RestPullRequestSettings
    | UpdatePullRequestSettingsResponse400
    | UpdatePullRequestSettingsResponse401
    | UpdatePullRequestSettingsResponse404
]:
    r"""Update merge strategy

     Update the pull request merge strategy configuration for this project and SCM.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the context
    repository to call this resource.

    Only the strategies provided will be enabled, the default must be set and included in the set of
    strategies.

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty \"mergeConfig\" attribute. i.e:
    <pre>{
        \"mergeConfig\": {}
    }
    </pre>

    Upon completion of this request, the effective configuration will be the configuration explicitly
    set for the SCM, or if no such explicit configuration is set then the default configuration will be
    used.

    Args:
        project_key (str):
        scm_id (str):
        body (RestPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestSettings | UpdatePullRequestSettingsResponse400 | UpdatePullRequestSettingsResponse401 | UpdatePullRequestSettingsResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        scm_id=scm_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestSettings | Unset = UNSET,
) -> (
    RestPullRequestSettings
    | UpdatePullRequestSettingsResponse400
    | UpdatePullRequestSettingsResponse401
    | UpdatePullRequestSettingsResponse404
    | None
):
    r"""Update merge strategy

     Update the pull request merge strategy configuration for this project and SCM.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the context
    repository to call this resource.

    Only the strategies provided will be enabled, the default must be set and included in the set of
    strategies.

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty \"mergeConfig\" attribute. i.e:
    <pre>{
        \"mergeConfig\": {}
    }
    </pre>

    Upon completion of this request, the effective configuration will be the configuration explicitly
    set for the SCM, or if no such explicit configuration is set then the default configuration will be
    used.

    Args:
        project_key (str):
        scm_id (str):
        body (RestPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestSettings | UpdatePullRequestSettingsResponse400 | UpdatePullRequestSettingsResponse401 | UpdatePullRequestSettingsResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            scm_id=scm_id,
            client=client,
            body=body,
        )
    ).parsed
