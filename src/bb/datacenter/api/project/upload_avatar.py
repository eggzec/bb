from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.example_avatar_multipart_form_data import ExampleAvatarMultipartFormData
from ...models.upload_avatar_response_401 import UploadAvatarResponse401
from ...models.upload_avatar_response_404 import UploadAvatarResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/avatar.png".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | UploadAvatarResponse401 | UploadAvatarResponse404 | None:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = UploadAvatarResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UploadAvatarResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | UploadAvatarResponse401 | UploadAvatarResponse404]:
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
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
) -> Response[Any | UploadAvatarResponse401 | UploadAvatarResponse404]:
    r"""Update project avatar

     Update the avatar for the project matching the supplied <strong>projectKey</strong>.

    This resource accepts POST multipart form data, containing a single image in a form-field named
    'avatar'.

    There are configurable server limits on both the dimensions (1024x1024 pixels by default) and
    uploaded file size (1MB by default). Several different image formats are supported, but
    <strong>PNG</strong> and <strong>JPEG</strong> are preferred due to the file size limit.

    This resource has Cross-Site Request Forgery (XSRF) protection. To allow the request to pass the
    XSRF check the caller needs to send an <code>X-Atlassian-Token</code> HTTP header with the value
    <code>no-check</code>.

    An example <a href=\"http://curl.haxx.se/\">curl</a> request to upload an image name 'avatar.png'
    would be: ```curl -X POST -u username:password -H \"X-Atlassian-Token: no-check\"
    http://example.com/rest/api/1.0/projects/STASH/avatar.png -F avatar=@avatar.png ```

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (ExampleAvatarMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UploadAvatarResponse401 | UploadAvatarResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
) -> Any | UploadAvatarResponse401 | UploadAvatarResponse404 | None:
    r"""Update project avatar

     Update the avatar for the project matching the supplied <strong>projectKey</strong>.

    This resource accepts POST multipart form data, containing a single image in a form-field named
    'avatar'.

    There are configurable server limits on both the dimensions (1024x1024 pixels by default) and
    uploaded file size (1MB by default). Several different image formats are supported, but
    <strong>PNG</strong> and <strong>JPEG</strong> are preferred due to the file size limit.

    This resource has Cross-Site Request Forgery (XSRF) protection. To allow the request to pass the
    XSRF check the caller needs to send an <code>X-Atlassian-Token</code> HTTP header with the value
    <code>no-check</code>.

    An example <a href=\"http://curl.haxx.se/\">curl</a> request to upload an image name 'avatar.png'
    would be: ```curl -X POST -u username:password -H \"X-Atlassian-Token: no-check\"
    http://example.com/rest/api/1.0/projects/STASH/avatar.png -F avatar=@avatar.png ```

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (ExampleAvatarMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UploadAvatarResponse401 | UploadAvatarResponse404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
) -> Response[Any | UploadAvatarResponse401 | UploadAvatarResponse404]:
    r"""Update project avatar

     Update the avatar for the project matching the supplied <strong>projectKey</strong>.

    This resource accepts POST multipart form data, containing a single image in a form-field named
    'avatar'.

    There are configurable server limits on both the dimensions (1024x1024 pixels by default) and
    uploaded file size (1MB by default). Several different image formats are supported, but
    <strong>PNG</strong> and <strong>JPEG</strong> are preferred due to the file size limit.

    This resource has Cross-Site Request Forgery (XSRF) protection. To allow the request to pass the
    XSRF check the caller needs to send an <code>X-Atlassian-Token</code> HTTP header with the value
    <code>no-check</code>.

    An example <a href=\"http://curl.haxx.se/\">curl</a> request to upload an image name 'avatar.png'
    would be: ```curl -X POST -u username:password -H \"X-Atlassian-Token: no-check\"
    http://example.com/rest/api/1.0/projects/STASH/avatar.png -F avatar=@avatar.png ```

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (ExampleAvatarMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | UploadAvatarResponse401 | UploadAvatarResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleAvatarMultipartFormData | Unset = UNSET,
) -> Any | UploadAvatarResponse401 | UploadAvatarResponse404 | None:
    r"""Update project avatar

     Update the avatar for the project matching the supplied <strong>projectKey</strong>.

    This resource accepts POST multipart form data, containing a single image in a form-field named
    'avatar'.

    There are configurable server limits on both the dimensions (1024x1024 pixels by default) and
    uploaded file size (1MB by default). Several different image formats are supported, but
    <strong>PNG</strong> and <strong>JPEG</strong> are preferred due to the file size limit.

    This resource has Cross-Site Request Forgery (XSRF) protection. To allow the request to pass the
    XSRF check the caller needs to send an <code>X-Atlassian-Token</code> HTTP header with the value
    <code>no-check</code>.

    An example <a href=\"http://curl.haxx.se/\">curl</a> request to upload an image name 'avatar.png'
    would be: ```curl -X POST -u username:password -H \"X-Atlassian-Token: no-check\"
    http://example.com/rest/api/1.0/projects/STASH/avatar.png -F avatar=@avatar.png ```

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (ExampleAvatarMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | UploadAvatarResponse401 | UploadAvatarResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
