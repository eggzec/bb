from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.example_avatar_multipart_form_data import ExampleAvatarMultipartFormData
from ...models.upload_avatar_1_response_401 import UploadAvatar1Response401
from ...models.upload_avatar_1_response_404 import UploadAvatar1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_slug: str,
    *,
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
    x_atlassian_token: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_atlassian_token, Unset):
        headers["X-Atlassian-Token"] = x_atlassian_token

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/users/{user_slug}/avatar.png".format(
            user_slug=quote(str(user_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UploadAvatar1Response401 | UploadAvatar1Response404 | None:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = UploadAvatar1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UploadAvatar1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | UploadAvatar1Response401 | UploadAvatar1Response404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
    x_atlassian_token: str | Unset = UNSET,
) -> Response[Any | UploadAvatar1Response401 | UploadAvatar1Response404]:
    r"""Update user avatar

     Update the avatar for the user with the supplied <strong>slug</strong>.


    This resource accepts POST multipart form data, containing a single image in a form-field named
    'avatar'.


    There are configurable server limits on both the dimensions (1024x1024 pixels by default) and
    uploaded
    file size (1MB by default). Several different image formats are supported, but <strong>PNG</strong>
    and
    <strong>JPEG</strong> are preferred due to the file size limit.


    This resource has Cross-Site Request Forgery (XSRF) protection. To allow the request to
    pass the XSRF check the caller needs to send an <code>X-Atlassian-Token</code> HTTP header with the
    value <code>no-check</code>.


    An example <a href=\"http://curl.haxx.se/\">curl</a> request to upload an image name 'avatar.png'
    would be:
    ```
    curl -X POST -u username:password -H \"X-Atlassian-Token: no-check\"
    http://example.com/rest/api/latest/users/jdoe/avatar.png -F avatar=@avatar.png
    ```


    Users are always allowed to update their own avatar. To update someone else's avatar the
    authenticated user must
    have global <strong>ADMIN</strong> permission, or global <strong>SYS_ADMIN</strong> permission to
    update a
    <strong>SYS_ADMIN</strong> user's avatar.

    Args:
        user_slug (str):
        x_atlassian_token (str | Unset):
        body (ExampleAvatarMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UploadAvatar1Response401 | UploadAvatar1Response404]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
        body=body,
        x_atlassian_token=x_atlassian_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
    x_atlassian_token: str | Unset = UNSET,
) -> Any | UploadAvatar1Response401 | UploadAvatar1Response404 | None:
    r"""Update user avatar

     Update the avatar for the user with the supplied <strong>slug</strong>.


    This resource accepts POST multipart form data, containing a single image in a form-field named
    'avatar'.


    There are configurable server limits on both the dimensions (1024x1024 pixels by default) and
    uploaded
    file size (1MB by default). Several different image formats are supported, but <strong>PNG</strong>
    and
    <strong>JPEG</strong> are preferred due to the file size limit.


    This resource has Cross-Site Request Forgery (XSRF) protection. To allow the request to
    pass the XSRF check the caller needs to send an <code>X-Atlassian-Token</code> HTTP header with the
    value <code>no-check</code>.


    An example <a href=\"http://curl.haxx.se/\">curl</a> request to upload an image name 'avatar.png'
    would be:
    ```
    curl -X POST -u username:password -H \"X-Atlassian-Token: no-check\"
    http://example.com/rest/api/latest/users/jdoe/avatar.png -F avatar=@avatar.png
    ```


    Users are always allowed to update their own avatar. To update someone else's avatar the
    authenticated user must
    have global <strong>ADMIN</strong> permission, or global <strong>SYS_ADMIN</strong> permission to
    update a
    <strong>SYS_ADMIN</strong> user's avatar.

    Args:
        user_slug (str):
        x_atlassian_token (str | Unset):
        body (ExampleAvatarMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UploadAvatar1Response401 | UploadAvatar1Response404
    """

    return sync_detailed(
        user_slug=user_slug,
        client=client,
        body=body,
        x_atlassian_token=x_atlassian_token,
    ).parsed


async def asyncio_detailed(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
    x_atlassian_token: str | Unset = UNSET,
) -> Response[Any | UploadAvatar1Response401 | UploadAvatar1Response404]:
    r"""Update user avatar

     Update the avatar for the user with the supplied <strong>slug</strong>.


    This resource accepts POST multipart form data, containing a single image in a form-field named
    'avatar'.


    There are configurable server limits on both the dimensions (1024x1024 pixels by default) and
    uploaded
    file size (1MB by default). Several different image formats are supported, but <strong>PNG</strong>
    and
    <strong>JPEG</strong> are preferred due to the file size limit.


    This resource has Cross-Site Request Forgery (XSRF) protection. To allow the request to
    pass the XSRF check the caller needs to send an <code>X-Atlassian-Token</code> HTTP header with the
    value <code>no-check</code>.


    An example <a href=\"http://curl.haxx.se/\">curl</a> request to upload an image name 'avatar.png'
    would be:
    ```
    curl -X POST -u username:password -H \"X-Atlassian-Token: no-check\"
    http://example.com/rest/api/latest/users/jdoe/avatar.png -F avatar=@avatar.png
    ```


    Users are always allowed to update their own avatar. To update someone else's avatar the
    authenticated user must
    have global <strong>ADMIN</strong> permission, or global <strong>SYS_ADMIN</strong> permission to
    update a
    <strong>SYS_ADMIN</strong> user's avatar.

    Args:
        user_slug (str):
        x_atlassian_token (str | Unset):
        body (ExampleAvatarMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UploadAvatar1Response401 | UploadAvatar1Response404]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
        body=body,
        x_atlassian_token=x_atlassian_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
    x_atlassian_token: str | Unset = UNSET,
) -> Any | UploadAvatar1Response401 | UploadAvatar1Response404 | None:
    r"""Update user avatar

     Update the avatar for the user with the supplied <strong>slug</strong>.


    This resource accepts POST multipart form data, containing a single image in a form-field named
    'avatar'.


    There are configurable server limits on both the dimensions (1024x1024 pixels by default) and
    uploaded
    file size (1MB by default). Several different image formats are supported, but <strong>PNG</strong>
    and
    <strong>JPEG</strong> are preferred due to the file size limit.


    This resource has Cross-Site Request Forgery (XSRF) protection. To allow the request to
    pass the XSRF check the caller needs to send an <code>X-Atlassian-Token</code> HTTP header with the
    value <code>no-check</code>.


    An example <a href=\"http://curl.haxx.se/\">curl</a> request to upload an image name 'avatar.png'
    would be:
    ```
    curl -X POST -u username:password -H \"X-Atlassian-Token: no-check\"
    http://example.com/rest/api/latest/users/jdoe/avatar.png -F avatar=@avatar.png
    ```


    Users are always allowed to update their own avatar. To update someone else's avatar the
    authenticated user must
    have global <strong>ADMIN</strong> permission, or global <strong>SYS_ADMIN</strong> permission to
    update a
    <strong>SYS_ADMIN</strong> user's avatar.

    Args:
        user_slug (str):
        x_atlassian_token (str | Unset):
        body (ExampleAvatarMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UploadAvatar1Response401 | UploadAvatar1Response404
    """

    return (
        await asyncio_detailed(
            user_slug=user_slug,
            client=client,
            body=body,
            x_atlassian_token=x_atlassian_token,
        )
    ).parsed
