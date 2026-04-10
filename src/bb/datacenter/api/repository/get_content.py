from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_content_response_400 import GetContentResponse400
from ...models.get_content_response_401 import GetContentResponse401
from ...models.get_content_response_404 import GetContentResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    no_content: str | Unset = UNSET,
    at: str | Unset = UNSET,
    size: str | Unset = UNSET,
    blame: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["noContent"] = no_content

    params["at"] = at

    params["size"] = size

    params["blame"] = blame

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/browse".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = GetContentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetContentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetContentResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    no_content: str | Unset = UNSET,
    at: str | Unset = UNSET,
    size: str | Unset = UNSET,
    blame: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404]:
    r"""Get file content at revision

     Retrieve a page of content for a file path at a specified revision.

    Responses from this endpoint vary widely depending on the query parameters. The example JSON is for
    a request that does not use size, type, blame or noContent.

    1. size will return a response like {\"size\":10000}
    2. type will return a response like {\"type\":\"FILE\"}, where possible values are    \"DIRECTORY\",
    \"FILE\" and \"SUBMODULE\"
    3. blame <i>without</i> noContent will include blame for the lines of    content returned on the
    page
    4. blame <i>with</i> noContent will omit file contents and only return    blame for the requested
    lines
    5. noContent without blame is ignored and does nothing


    The various parameters are \"processed\" in the above order. That means ?size=true&amp;type=truewill
    return a size response, not a type one; the type parameter will be ignored.

    The blame and noContent query parameters are handled differently from size and type. For blame and
    noContent, the <i>presence</i> of the parameter implies \"true\" if no value is specified; size and
    and type both require an explicit=true or they're treated as \"false\".

    - ?blame is the same as ?blame=true
    - ?blame&amp;noContent is the same as ?blame=true&amp;noContent=true
    - ?size is the same as ?size=false
    - ?type is the same as ?type=false


    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        no_content (str | Unset):
        at (str | Unset):
        size (str | Unset):
        blame (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        no_content=no_content,
        at=at,
        size=size,
        blame=blame,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    no_content: str | Unset = UNSET,
    at: str | Unset = UNSET,
    size: str | Unset = UNSET,
    blame: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404 | None:
    r"""Get file content at revision

     Retrieve a page of content for a file path at a specified revision.

    Responses from this endpoint vary widely depending on the query parameters. The example JSON is for
    a request that does not use size, type, blame or noContent.

    1. size will return a response like {\"size\":10000}
    2. type will return a response like {\"type\":\"FILE\"}, where possible values are    \"DIRECTORY\",
    \"FILE\" and \"SUBMODULE\"
    3. blame <i>without</i> noContent will include blame for the lines of    content returned on the
    page
    4. blame <i>with</i> noContent will omit file contents and only return    blame for the requested
    lines
    5. noContent without blame is ignored and does nothing


    The various parameters are \"processed\" in the above order. That means ?size=true&amp;type=truewill
    return a size response, not a type one; the type parameter will be ignored.

    The blame and noContent query parameters are handled differently from size and type. For blame and
    noContent, the <i>presence</i> of the parameter implies \"true\" if no value is specified; size and
    and type both require an explicit=true or they're treated as \"false\".

    - ?blame is the same as ?blame=true
    - ?blame&amp;noContent is the same as ?blame=true&amp;noContent=true
    - ?size is the same as ?size=false
    - ?type is the same as ?type=false


    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        no_content (str | Unset):
        at (str | Unset):
        size (str | Unset):
        blame (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        no_content=no_content,
        at=at,
        size=size,
        blame=blame,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    no_content: str | Unset = UNSET,
    at: str | Unset = UNSET,
    size: str | Unset = UNSET,
    blame: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404]:
    r"""Get file content at revision

     Retrieve a page of content for a file path at a specified revision.

    Responses from this endpoint vary widely depending on the query parameters. The example JSON is for
    a request that does not use size, type, blame or noContent.

    1. size will return a response like {\"size\":10000}
    2. type will return a response like {\"type\":\"FILE\"}, where possible values are    \"DIRECTORY\",
    \"FILE\" and \"SUBMODULE\"
    3. blame <i>without</i> noContent will include blame for the lines of    content returned on the
    page
    4. blame <i>with</i> noContent will omit file contents and only return    blame for the requested
    lines
    5. noContent without blame is ignored and does nothing


    The various parameters are \"processed\" in the above order. That means ?size=true&amp;type=truewill
    return a size response, not a type one; the type parameter will be ignored.

    The blame and noContent query parameters are handled differently from size and type. For blame and
    noContent, the <i>presence</i> of the parameter implies \"true\" if no value is specified; size and
    and type both require an explicit=true or they're treated as \"false\".

    - ?blame is the same as ?blame=true
    - ?blame&amp;noContent is the same as ?blame=true&amp;noContent=true
    - ?size is the same as ?size=false
    - ?type is the same as ?type=false


    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        no_content (str | Unset):
        at (str | Unset):
        size (str | Unset):
        blame (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        no_content=no_content,
        at=at,
        size=size,
        blame=blame,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    no_content: str | Unset = UNSET,
    at: str | Unset = UNSET,
    size: str | Unset = UNSET,
    blame: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404 | None:
    r"""Get file content at revision

     Retrieve a page of content for a file path at a specified revision.

    Responses from this endpoint vary widely depending on the query parameters. The example JSON is for
    a request that does not use size, type, blame or noContent.

    1. size will return a response like {\"size\":10000}
    2. type will return a response like {\"type\":\"FILE\"}, where possible values are    \"DIRECTORY\",
    \"FILE\" and \"SUBMODULE\"
    3. blame <i>without</i> noContent will include blame for the lines of    content returned on the
    page
    4. blame <i>with</i> noContent will omit file contents and only return    blame for the requested
    lines
    5. noContent without blame is ignored and does nothing


    The various parameters are \"processed\" in the above order. That means ?size=true&amp;type=truewill
    return a size response, not a type one; the type parameter will be ignored.

    The blame and noContent query parameters are handled differently from size and type. For blame and
    noContent, the <i>presence</i> of the parameter implies \"true\" if no value is specified; size and
    and type both require an explicit=true or they're treated as \"false\".

    - ?blame is the same as ?blame=true
    - ?blame&amp;noContent is the same as ?blame=true&amp;noContent=true
    - ?size is the same as ?size=false
    - ?type is the same as ?type=false


    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        no_content (str | Unset):
        at (str | Unset):
        size (str | Unset):
        blame (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetContentResponse400 | GetContentResponse401 | GetContentResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            no_content=no_content,
            at=at,
            size=size,
            blame=blame,
            type_=type_,
        )
    ).parsed
