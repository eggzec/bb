from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_pull_request_merge_config import RestPullRequestMergeConfig
from ...models.rest_pull_request_settings import RestPullRequestSettings
from ...models.set_merge_config_response_400 import SetMergeConfigResponse400
from ...models.set_merge_config_response_401 import SetMergeConfigResponse401
from ...models.set_merge_config_response_404 import SetMergeConfigResponse404
from ...models.set_merge_config_response_409 import SetMergeConfigResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    scm_id: str,
    *,
    body: RestPullRequestSettings | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/pull-requests/{scm_id}".format(
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
    RestPullRequestMergeConfig
    | SetMergeConfigResponse400
    | SetMergeConfigResponse401
    | SetMergeConfigResponse404
    | SetMergeConfigResponse409
    | None
):
    if response.status_code == 200:
        response_200 = RestPullRequestMergeConfig.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetMergeConfigResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetMergeConfigResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SetMergeConfigResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = SetMergeConfigResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestPullRequestMergeConfig
    | SetMergeConfigResponse400
    | SetMergeConfigResponse401
    | SetMergeConfigResponse404
    | SetMergeConfigResponse409
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestSettings | Unset = UNSET,
) -> Response[
    RestPullRequestMergeConfig
    | SetMergeConfigResponse400
    | SetMergeConfigResponse401
    | SetMergeConfigResponse404
    | SetMergeConfigResponse409
]:
    r"""Update merge strategies

     Update the pull request merge strategies for the context repository.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Only the strategies provided will be enabled, only one may be set to default

    The commit message template will not be updated if not provided, and will be deleted if the
    `commitMessageTemplate` attribute is empty, i.e: `commitMessageTemplate: {}`.

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty `mergeConfig` attribute. i.e:
    ```
    {
        \"mergeConfig\": {}
    }
    ```

    Upon completion of this request, the effective configuration will be the default configuration.

    Args:
        scm_id (str):
        body (RestPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestMergeConfig | SetMergeConfigResponse400 | SetMergeConfigResponse401 | SetMergeConfigResponse404 | SetMergeConfigResponse409]
    """

    kwargs = _get_kwargs(
        scm_id=scm_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestSettings | Unset = UNSET,
) -> (
    RestPullRequestMergeConfig
    | SetMergeConfigResponse400
    | SetMergeConfigResponse401
    | SetMergeConfigResponse404
    | SetMergeConfigResponse409
    | None
):
    r"""Update merge strategies

     Update the pull request merge strategies for the context repository.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Only the strategies provided will be enabled, only one may be set to default

    The commit message template will not be updated if not provided, and will be deleted if the
    `commitMessageTemplate` attribute is empty, i.e: `commitMessageTemplate: {}`.

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty `mergeConfig` attribute. i.e:
    ```
    {
        \"mergeConfig\": {}
    }
    ```

    Upon completion of this request, the effective configuration will be the default configuration.

    Args:
        scm_id (str):
        body (RestPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestMergeConfig | SetMergeConfigResponse400 | SetMergeConfigResponse401 | SetMergeConfigResponse404 | SetMergeConfigResponse409
    """

    return sync_detailed(
        scm_id=scm_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestSettings | Unset = UNSET,
) -> Response[
    RestPullRequestMergeConfig
    | SetMergeConfigResponse400
    | SetMergeConfigResponse401
    | SetMergeConfigResponse404
    | SetMergeConfigResponse409
]:
    r"""Update merge strategies

     Update the pull request merge strategies for the context repository.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Only the strategies provided will be enabled, only one may be set to default

    The commit message template will not be updated if not provided, and will be deleted if the
    `commitMessageTemplate` attribute is empty, i.e: `commitMessageTemplate: {}`.

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty `mergeConfig` attribute. i.e:
    ```
    {
        \"mergeConfig\": {}
    }
    ```

    Upon completion of this request, the effective configuration will be the default configuration.

    Args:
        scm_id (str):
        body (RestPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestMergeConfig | SetMergeConfigResponse400 | SetMergeConfigResponse401 | SetMergeConfigResponse404 | SetMergeConfigResponse409]
    """

    kwargs = _get_kwargs(
        scm_id=scm_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestPullRequestSettings | Unset = UNSET,
) -> (
    RestPullRequestMergeConfig
    | SetMergeConfigResponse400
    | SetMergeConfigResponse401
    | SetMergeConfigResponse404
    | SetMergeConfigResponse409
    | None
):
    r"""Update merge strategies

     Update the pull request merge strategies for the context repository.

    The authenticated user must have <strong>ADMIN</strong> permission to call this resource.

    Only the strategies provided will be enabled, only one may be set to default

    The commit message template will not be updated if not provided, and will be deleted if the
    `commitMessageTemplate` attribute is empty, i.e: `commitMessageTemplate: {}`.

    An explicitly set pull request merge strategy configuration can be deleted by POSTing a document
    with an empty `mergeConfig` attribute. i.e:
    ```
    {
        \"mergeConfig\": {}
    }
    ```

    Upon completion of this request, the effective configuration will be the default configuration.

    Args:
        scm_id (str):
        body (RestPullRequestSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestMergeConfig | SetMergeConfigResponse400 | SetMergeConfigResponse401 | SetMergeConfigResponse404 | SetMergeConfigResponse409
    """

    return (
        await asyncio_detailed(
            scm_id=scm_id,
            client=client,
            body=body,
        )
    ).parsed
