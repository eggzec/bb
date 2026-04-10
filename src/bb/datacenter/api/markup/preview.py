from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.preview_response_400 import PreviewResponse400
from ...models.preview_response_401 import PreviewResponse401
from ...models.rest_markup import RestMarkup
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    url_mode: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["htmlEscape"] = html_escape

    params["urlMode"] = url_mode

    params["includeHeadingId"] = include_heading_id

    params["hardwrap"] = hardwrap

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/markup/preview",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PreviewResponse400 | PreviewResponse401 | RestMarkup | None:
    if response.status_code == 200:
        response_200 = RestMarkup.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PreviewResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PreviewResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PreviewResponse400 | PreviewResponse401 | RestMarkup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    url_mode: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> Response[PreviewResponse400 | PreviewResponse401 | RestMarkup]:
    """Preview markdown render

     Preview generated HTML for the given markdown content.

    Only authenticated users may call this resource.

    Args:
        html_escape (str | Unset):
        url_mode (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):
        body (str | Unset):  Example: # Hello World!.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PreviewResponse400 | PreviewResponse401 | RestMarkup]
    """

    kwargs = _get_kwargs(
        body=body,
        html_escape=html_escape,
        url_mode=url_mode,
        include_heading_id=include_heading_id,
        hardwrap=hardwrap,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    url_mode: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> PreviewResponse400 | PreviewResponse401 | RestMarkup | None:
    """Preview markdown render

     Preview generated HTML for the given markdown content.

    Only authenticated users may call this resource.

    Args:
        html_escape (str | Unset):
        url_mode (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):
        body (str | Unset):  Example: # Hello World!.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PreviewResponse400 | PreviewResponse401 | RestMarkup
    """

    return sync_detailed(
        client=client,
        body=body,
        html_escape=html_escape,
        url_mode=url_mode,
        include_heading_id=include_heading_id,
        hardwrap=hardwrap,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    url_mode: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> Response[PreviewResponse400 | PreviewResponse401 | RestMarkup]:
    """Preview markdown render

     Preview generated HTML for the given markdown content.

    Only authenticated users may call this resource.

    Args:
        html_escape (str | Unset):
        url_mode (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):
        body (str | Unset):  Example: # Hello World!.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PreviewResponse400 | PreviewResponse401 | RestMarkup]
    """

    kwargs = _get_kwargs(
        body=body,
        html_escape=html_escape,
        url_mode=url_mode,
        include_heading_id=include_heading_id,
        hardwrap=hardwrap,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: str | Unset = UNSET,
    html_escape: str | Unset = UNSET,
    url_mode: str | Unset = UNSET,
    include_heading_id: str | Unset = UNSET,
    hardwrap: str | Unset = UNSET,
) -> PreviewResponse400 | PreviewResponse401 | RestMarkup | None:
    """Preview markdown render

     Preview generated HTML for the given markdown content.

    Only authenticated users may call this resource.

    Args:
        html_escape (str | Unset):
        url_mode (str | Unset):
        include_heading_id (str | Unset):
        hardwrap (str | Unset):
        body (str | Unset):  Example: # Hello World!.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PreviewResponse400 | PreviewResponse401 | RestMarkup
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            html_escape=html_escape,
            url_mode=url_mode,
            include_heading_id=include_heading_id,
            hardwrap=hardwrap,
        )
    ).parsed
