from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_default_reviewers_request import RestDefaultReviewersRequest
from ...models.rest_pull_request_condition import RestPullRequestCondition
from ...models.update_pull_request_condition_response_400 import UpdatePullRequestConditionResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    id: str,
    *,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/default-reviewers/latest/projects/{project_key}/condition/{id}".format(
            project_key=quote(str(project_key), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestPullRequestCondition | UpdatePullRequestConditionResponse400 | None:
    if response.status_code == 200:
        response_200 = RestPullRequestCondition.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdatePullRequestConditionResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestPullRequestCondition | UpdatePullRequestConditionResponse400]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> Response[RestPullRequestCondition | UpdatePullRequestConditionResponse400]:
    """Update default reviewer condition

     Update the default reviewer pull request condition for the given ID.

    Args:
        project_key (str):
        id (str):
        body (RestDefaultReviewersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestCondition | UpdatePullRequestConditionResponse400]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> RestPullRequestCondition | UpdatePullRequestConditionResponse400 | None:
    """Update default reviewer condition

     Update the default reviewer pull request condition for the given ID.

    Args:
        project_key (str):
        id (str):
        body (RestDefaultReviewersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestCondition | UpdatePullRequestConditionResponse400
    """

    return sync_detailed(
        project_key=project_key,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> Response[RestPullRequestCondition | UpdatePullRequestConditionResponse400]:
    """Update default reviewer condition

     Update the default reviewer pull request condition for the given ID.

    Args:
        project_key (str):
        id (str):
        body (RestDefaultReviewersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestPullRequestCondition | UpdatePullRequestConditionResponse400]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestDefaultReviewersRequest | Unset = UNSET,
) -> RestPullRequestCondition | UpdatePullRequestConditionResponse400 | None:
    """Update default reviewer condition

     Update the default reviewer pull request condition for the given ID.

    Args:
        project_key (str):
        id (str):
        body (RestDefaultReviewersRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestPullRequestCondition | UpdatePullRequestConditionResponse400
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
