from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_required_build_condition import RestRequiredBuildCondition
from ...models.rest_required_build_condition_set_request import RestRequiredBuildConditionSetRequest
from ...models.update_required_builds_merge_check_response_400 import UpdateRequiredBuildsMergeCheckResponse400
from ...models.update_required_builds_merge_check_response_401 import UpdateRequiredBuildsMergeCheckResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    id: int,
    *,
    body: RestRequiredBuildConditionSetRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/required-builds/latest/projects/{project_key}/repos/{repository_slug}/condition/{id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
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
) -> (
    RestRequiredBuildCondition
    | UpdateRequiredBuildsMergeCheckResponse400
    | UpdateRequiredBuildsMergeCheckResponse401
    | None
):
    if response.status_code == 200:
        response_200 = RestRequiredBuildCondition.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateRequiredBuildsMergeCheckResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateRequiredBuildsMergeCheckResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RestRequiredBuildCondition | UpdateRequiredBuildsMergeCheckResponse400 | UpdateRequiredBuildsMergeCheckResponse401
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RestRequiredBuildConditionSetRequest | Unset = UNSET,
) -> Response[
    RestRequiredBuildCondition | UpdateRequiredBuildsMergeCheckResponse400 | UpdateRequiredBuildsMergeCheckResponse401
]:
    r"""Update a required builds merge check

     Update the required builds merge check for the given ID.

    The authenticated user must have **REPO_ADMIN** permission for the target repository to update a
    required build merge check.

    The contents of the required build merge check request are:

    These fields are **required**:

    - **buildParentKeys**: A non-empty list of build parent keys that require green builds for this
    merge check to pass
    - **refMatcher.id**: The value to match refs against in the target branch
    - **refMatcher.type.id**: The type of ref matcher, one of: \"ANY_REF\", \"BRANCH\", \"PATTERN\",
    \"MODEL_CATEGORY\" or \"MODEL_BRANCH\"


    These fields are optional:

    - **exemptRefMatcher.id** The value to exempt refs in the source branch from this check
    - **exemptRefMatcher.type.id**: The type of exempt ref matcher, one of: \"ANY_REF\", \"BRANCH\",
    \"PATTERN\", \"MODEL_CATEGORY\" or \"MODEL_BRANCH\"



    Args:
        project_key (str):
        repository_slug (str):
        id (int):
        body (RestRequiredBuildConditionSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRequiredBuildCondition | UpdateRequiredBuildsMergeCheckResponse400 | UpdateRequiredBuildsMergeCheckResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RestRequiredBuildConditionSetRequest | Unset = UNSET,
) -> (
    RestRequiredBuildCondition
    | UpdateRequiredBuildsMergeCheckResponse400
    | UpdateRequiredBuildsMergeCheckResponse401
    | None
):
    r"""Update a required builds merge check

     Update the required builds merge check for the given ID.

    The authenticated user must have **REPO_ADMIN** permission for the target repository to update a
    required build merge check.

    The contents of the required build merge check request are:

    These fields are **required**:

    - **buildParentKeys**: A non-empty list of build parent keys that require green builds for this
    merge check to pass
    - **refMatcher.id**: The value to match refs against in the target branch
    - **refMatcher.type.id**: The type of ref matcher, one of: \"ANY_REF\", \"BRANCH\", \"PATTERN\",
    \"MODEL_CATEGORY\" or \"MODEL_BRANCH\"


    These fields are optional:

    - **exemptRefMatcher.id** The value to exempt refs in the source branch from this check
    - **exemptRefMatcher.type.id**: The type of exempt ref matcher, one of: \"ANY_REF\", \"BRANCH\",
    \"PATTERN\", \"MODEL_CATEGORY\" or \"MODEL_BRANCH\"



    Args:
        project_key (str):
        repository_slug (str):
        id (int):
        body (RestRequiredBuildConditionSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRequiredBuildCondition | UpdateRequiredBuildsMergeCheckResponse400 | UpdateRequiredBuildsMergeCheckResponse401
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RestRequiredBuildConditionSetRequest | Unset = UNSET,
) -> Response[
    RestRequiredBuildCondition | UpdateRequiredBuildsMergeCheckResponse400 | UpdateRequiredBuildsMergeCheckResponse401
]:
    r"""Update a required builds merge check

     Update the required builds merge check for the given ID.

    The authenticated user must have **REPO_ADMIN** permission for the target repository to update a
    required build merge check.

    The contents of the required build merge check request are:

    These fields are **required**:

    - **buildParentKeys**: A non-empty list of build parent keys that require green builds for this
    merge check to pass
    - **refMatcher.id**: The value to match refs against in the target branch
    - **refMatcher.type.id**: The type of ref matcher, one of: \"ANY_REF\", \"BRANCH\", \"PATTERN\",
    \"MODEL_CATEGORY\" or \"MODEL_BRANCH\"


    These fields are optional:

    - **exemptRefMatcher.id** The value to exempt refs in the source branch from this check
    - **exemptRefMatcher.type.id**: The type of exempt ref matcher, one of: \"ANY_REF\", \"BRANCH\",
    \"PATTERN\", \"MODEL_CATEGORY\" or \"MODEL_BRANCH\"



    Args:
        project_key (str):
        repository_slug (str):
        id (int):
        body (RestRequiredBuildConditionSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRequiredBuildCondition | UpdateRequiredBuildsMergeCheckResponse400 | UpdateRequiredBuildsMergeCheckResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RestRequiredBuildConditionSetRequest | Unset = UNSET,
) -> (
    RestRequiredBuildCondition
    | UpdateRequiredBuildsMergeCheckResponse400
    | UpdateRequiredBuildsMergeCheckResponse401
    | None
):
    r"""Update a required builds merge check

     Update the required builds merge check for the given ID.

    The authenticated user must have **REPO_ADMIN** permission for the target repository to update a
    required build merge check.

    The contents of the required build merge check request are:

    These fields are **required**:

    - **buildParentKeys**: A non-empty list of build parent keys that require green builds for this
    merge check to pass
    - **refMatcher.id**: The value to match refs against in the target branch
    - **refMatcher.type.id**: The type of ref matcher, one of: \"ANY_REF\", \"BRANCH\", \"PATTERN\",
    \"MODEL_CATEGORY\" or \"MODEL_BRANCH\"


    These fields are optional:

    - **exemptRefMatcher.id** The value to exempt refs in the source branch from this check
    - **exemptRefMatcher.type.id**: The type of exempt ref matcher, one of: \"ANY_REF\", \"BRANCH\",
    \"PATTERN\", \"MODEL_CATEGORY\" or \"MODEL_BRANCH\"



    Args:
        project_key (str):
        repository_slug (str):
        id (int):
        body (RestRequiredBuildConditionSetRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRequiredBuildCondition | UpdateRequiredBuildsMergeCheckResponse400 | UpdateRequiredBuildsMergeCheckResponse401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
