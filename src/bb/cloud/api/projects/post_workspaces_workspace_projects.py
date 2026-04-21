from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.project import Project
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    *,
    body: Project,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/workspaces/{workspace}/projects".format(
            workspace=quote(str(workspace), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Project
type ParseResult = Error | Project | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_201 = Project.from_dict(response.json())

        return response_201

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    body: Project,
) -> Response[ParsedPayload]:
    r""" Create a project in a workspace

     Creates a new project.

    Note that the avatar has to be embedded as either a data-url
    or a URL to an external image as shown in the examples below:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\":
    \"data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    or even:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\": \"http://i.imgur.com/72tRx4w.gif\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    Args:
        workspace (str):
        body (Project):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Project]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
    body: Project,
) -> ParsedPayload | None:
    r""" Create a project in a workspace

     Creates a new project.

    Note that the avatar has to be embedded as either a data-url
    or a URL to an external image as shown in the examples below:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\":
    \"data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    or even:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\": \"http://i.imgur.com/72tRx4w.gif\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    Args:
        workspace (str):
        body (Project):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Project
     """

    return sync_detailed(
        workspace=workspace,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    body: Project,
) -> Response[ParsedPayload]:
    r""" Create a project in a workspace

     Creates a new project.

    Note that the avatar has to be embedded as either a data-url
    or a URL to an external image as shown in the examples below:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\":
    \"data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    or even:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\": \"http://i.imgur.com/72tRx4w.gif\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    Args:
        workspace (str):
        body (Project):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Project]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    body: Project,
) -> ParsedPayload | None:
    r""" Create a project in a workspace

     Creates a new project.

    Note that the avatar has to be embedded as either a data-url
    or a URL to an external image as shown in the examples below:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\":
    \"data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/...\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    or even:

    ```
    $ body=$(cat << EOF
    {
        \"name\": \"Mars Project\",
        \"key\": \"MARS\",
        \"description\": \"Software for colonizing mars.\",
        \"links\": {
            \"avatar\": {
                \"href\": \"http://i.imgur.com/72tRx4w.gif\"
            }
        },
        \"is_private\": false
    }
    EOF
    )
    $ curl -H \"Content-Type: application/json\" \
           -X POST \
           -d \"$body\" \
           https://api.bitbucket.org/2.0/workspaces/teams-in-space/projects/ | jq .
    {
      // Serialized project document
    }
    ```

    Args:
        workspace (str):
        body (Project):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Project
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            body=body,
        )
    ).parsed
