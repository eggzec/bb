from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    permission: str | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["permission"] = permission

    params["filterText"] = filter_text

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/permissions/search".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any:
    return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    permission: str | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[Any]:
    """Search project permissions

     Search direct and implied permissions of principals (users and groups). This endpoint returns a
    superset of the results returned by the /users and /groups endpoints because it allows filtering by
    global permissions too.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    Args:
        project_key (str):
        permission (str | Unset):
        filter_text (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        permission=permission,
        filter_text=filter_text,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    permission: str | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[Any]:
    """Search project permissions

     Search direct and implied permissions of principals (users and groups). This endpoint returns a
    superset of the results returned by the /users and /groups endpoints because it allows filtering by
    global permissions too.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    or a higher global permission to call this resource.

    Args:
        project_key (str):
        permission (str | Unset):
        filter_text (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        permission=permission,
        filter_text=filter_text,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
