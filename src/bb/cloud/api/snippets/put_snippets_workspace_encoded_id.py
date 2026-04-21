from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.snippet import Snippet
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    encoded_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/snippets/{workspace}/{encoded_id}".format(
            workspace=quote(str(workspace), safe=""),
            encoded_id=quote(str(encoded_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | Snippet
type ParseResult = Error | Snippet | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = Snippet.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

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
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""Update a snippet

     Used to update a snippet. Use this to add and delete files and to
    change a snippet's title.

    To update a snippet, one can either PUT a full snapshot, or only the
    parts that need to be changed.

    The contract for PUT on this API is that properties missing from the
    request remain untouched so that snippets can be efficiently
    manipulated with differential payloads.

    To delete a property (e.g. the title, or a file), include its name in
    the request, but omit its value (use `null`).

    As in Git, explicit renaming of files is not supported. Instead, to
    rename a file, delete it and add it again under another name. This can
    be done atomically in a single request. Rename detection is left to
    the SCM.

    PUT supports three different content types for both request and
    response bodies:

    * `application/json`
    * `multipart/related`
    * `multipart/form-data`

    The content type used for the request body can be different than that
    used for the response. Content types are specified using standard HTTP
    headers.

    Use the `Content-Type` and `Accept` headers to select the desired
    request and response format.


    application/json
    ----------------

    As with creation and retrieval, the content type determines what
    properties can be manipulated. `application/json` does not support
    file contents and is therefore limited to a snippet's meta data.

    To update the title, without changing any of its files:

        $ curl -X POST -H \"Content-Type: application/json\"
    https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": \"Updated title\"}'


    To delete the title:

        $ curl -X POST -H \"Content-Type: application/json\"
    https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": null}'

    Not all parts of a snippet can be manipulated. The owner and creator
    for instance are immutable.


    multipart/related
    -----------------

    `multipart/related` can be used to manipulate all of a snippet's
    properties. The body is identical to a POST. properties omitted from
    the request are left unchanged. Since the `start` part contains JSON,
    the mechanism for manipulating the snippet's meta data is identical
    to `application/json` requests.

    To update one of a snippet's file contents, while also changing its
    title:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 288
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"title\": \"My updated snippet\",
          \"files\": {
              \"foo.txt\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        Updated file contents.

        --===============1438169132528273974==--

    Here only the parts that are changed are included in the body. The
    other files remain untouched.

    Note the use of the `files` list in the JSON part. This list contains
    the files that are being manipulated. This list should have
    corresponding multiparts in the request that contain the new contents
    of these files.

    If a filename in the `files` list does not have a corresponding part,
    it will be deleted from the snippet, as shown below:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 188
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"files\": {
            \"image.png\": {}
          }
        }

        --===============1438169132528273974==--

    To simulate a rename, delete a file and add the same file under
    another name:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 212
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
            \"files\": {
              \"foo.txt\": {},
              \"bar.txt\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"bar.txt\"
        Content-Disposition: attachment; filename=\"bar.txt\"

        foo

        --===============1438169132528273974==--


    multipart/form-data
    -----------------

    Again, one can also use `multipart/form-data` to manipulate file
    contents and meta data atomically.

        $ curl -X PUT http://localhost:12345/2.0/snippets/evzijst/kypj             -F title=\"My updated
    snippet\" -F file=@foo.txt

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 351
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"

        My updated snippet
        ------------------------------63a4b224c59f

    To delete a file, omit its contents while including its name in the
    `files` field:

        $ curl -X PUT https://api.bitbucket.org/2.0/snippets/evzijst/kypj -F files=image.png

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 149
        Content-Type: multipart/form-data; boundary=----------------------------ef8871065a86

        ------------------------------ef8871065a86
        Content-Disposition: form-data; name=\"files\"

        image.png
        ------------------------------ef8871065a86--

    The explicit use of the `files` element in `multipart/related` and
    `multipart/form-data` is only required when deleting files.
    The default mode of operation is for file parts to be processed,
    regardless of whether or not they are listed in `files`, as a
    convenience to the client.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Snippet]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""Update a snippet

     Used to update a snippet. Use this to add and delete files and to
    change a snippet's title.

    To update a snippet, one can either PUT a full snapshot, or only the
    parts that need to be changed.

    The contract for PUT on this API is that properties missing from the
    request remain untouched so that snippets can be efficiently
    manipulated with differential payloads.

    To delete a property (e.g. the title, or a file), include its name in
    the request, but omit its value (use `null`).

    As in Git, explicit renaming of files is not supported. Instead, to
    rename a file, delete it and add it again under another name. This can
    be done atomically in a single request. Rename detection is left to
    the SCM.

    PUT supports three different content types for both request and
    response bodies:

    * `application/json`
    * `multipart/related`
    * `multipart/form-data`

    The content type used for the request body can be different than that
    used for the response. Content types are specified using standard HTTP
    headers.

    Use the `Content-Type` and `Accept` headers to select the desired
    request and response format.


    application/json
    ----------------

    As with creation and retrieval, the content type determines what
    properties can be manipulated. `application/json` does not support
    file contents and is therefore limited to a snippet's meta data.

    To update the title, without changing any of its files:

        $ curl -X POST -H \"Content-Type: application/json\"
    https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": \"Updated title\"}'


    To delete the title:

        $ curl -X POST -H \"Content-Type: application/json\"
    https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": null}'

    Not all parts of a snippet can be manipulated. The owner and creator
    for instance are immutable.


    multipart/related
    -----------------

    `multipart/related` can be used to manipulate all of a snippet's
    properties. The body is identical to a POST. properties omitted from
    the request are left unchanged. Since the `start` part contains JSON,
    the mechanism for manipulating the snippet's meta data is identical
    to `application/json` requests.

    To update one of a snippet's file contents, while also changing its
    title:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 288
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"title\": \"My updated snippet\",
          \"files\": {
              \"foo.txt\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        Updated file contents.

        --===============1438169132528273974==--

    Here only the parts that are changed are included in the body. The
    other files remain untouched.

    Note the use of the `files` list in the JSON part. This list contains
    the files that are being manipulated. This list should have
    corresponding multiparts in the request that contain the new contents
    of these files.

    If a filename in the `files` list does not have a corresponding part,
    it will be deleted from the snippet, as shown below:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 188
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"files\": {
            \"image.png\": {}
          }
        }

        --===============1438169132528273974==--

    To simulate a rename, delete a file and add the same file under
    another name:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 212
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
            \"files\": {
              \"foo.txt\": {},
              \"bar.txt\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"bar.txt\"
        Content-Disposition: attachment; filename=\"bar.txt\"

        foo

        --===============1438169132528273974==--


    multipart/form-data
    -----------------

    Again, one can also use `multipart/form-data` to manipulate file
    contents and meta data atomically.

        $ curl -X PUT http://localhost:12345/2.0/snippets/evzijst/kypj             -F title=\"My updated
    snippet\" -F file=@foo.txt

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 351
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"

        My updated snippet
        ------------------------------63a4b224c59f

    To delete a file, omit its contents while including its name in the
    `files` field:

        $ curl -X PUT https://api.bitbucket.org/2.0/snippets/evzijst/kypj -F files=image.png

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 149
        Content-Type: multipart/form-data; boundary=----------------------------ef8871065a86

        ------------------------------ef8871065a86
        Content-Disposition: form-data; name=\"files\"

        image.png
        ------------------------------ef8871065a86--

    The explicit use of the `files` element in `multipart/related` and
    `multipart/form-data` is only required when deleting files.
    The default mode of operation is for file parts to be processed,
    regardless of whether or not they are listed in `files`, as a
    convenience to the client.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Snippet
    """

    return sync_detailed(
        workspace=workspace,
        encoded_id=encoded_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""Update a snippet

     Used to update a snippet. Use this to add and delete files and to
    change a snippet's title.

    To update a snippet, one can either PUT a full snapshot, or only the
    parts that need to be changed.

    The contract for PUT on this API is that properties missing from the
    request remain untouched so that snippets can be efficiently
    manipulated with differential payloads.

    To delete a property (e.g. the title, or a file), include its name in
    the request, but omit its value (use `null`).

    As in Git, explicit renaming of files is not supported. Instead, to
    rename a file, delete it and add it again under another name. This can
    be done atomically in a single request. Rename detection is left to
    the SCM.

    PUT supports three different content types for both request and
    response bodies:

    * `application/json`
    * `multipart/related`
    * `multipart/form-data`

    The content type used for the request body can be different than that
    used for the response. Content types are specified using standard HTTP
    headers.

    Use the `Content-Type` and `Accept` headers to select the desired
    request and response format.


    application/json
    ----------------

    As with creation and retrieval, the content type determines what
    properties can be manipulated. `application/json` does not support
    file contents and is therefore limited to a snippet's meta data.

    To update the title, without changing any of its files:

        $ curl -X POST -H \"Content-Type: application/json\"
    https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": \"Updated title\"}'


    To delete the title:

        $ curl -X POST -H \"Content-Type: application/json\"
    https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": null}'

    Not all parts of a snippet can be manipulated. The owner and creator
    for instance are immutable.


    multipart/related
    -----------------

    `multipart/related` can be used to manipulate all of a snippet's
    properties. The body is identical to a POST. properties omitted from
    the request are left unchanged. Since the `start` part contains JSON,
    the mechanism for manipulating the snippet's meta data is identical
    to `application/json` requests.

    To update one of a snippet's file contents, while also changing its
    title:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 288
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"title\": \"My updated snippet\",
          \"files\": {
              \"foo.txt\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        Updated file contents.

        --===============1438169132528273974==--

    Here only the parts that are changed are included in the body. The
    other files remain untouched.

    Note the use of the `files` list in the JSON part. This list contains
    the files that are being manipulated. This list should have
    corresponding multiparts in the request that contain the new contents
    of these files.

    If a filename in the `files` list does not have a corresponding part,
    it will be deleted from the snippet, as shown below:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 188
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"files\": {
            \"image.png\": {}
          }
        }

        --===============1438169132528273974==--

    To simulate a rename, delete a file and add the same file under
    another name:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 212
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
            \"files\": {
              \"foo.txt\": {},
              \"bar.txt\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"bar.txt\"
        Content-Disposition: attachment; filename=\"bar.txt\"

        foo

        --===============1438169132528273974==--


    multipart/form-data
    -----------------

    Again, one can also use `multipart/form-data` to manipulate file
    contents and meta data atomically.

        $ curl -X PUT http://localhost:12345/2.0/snippets/evzijst/kypj             -F title=\"My updated
    snippet\" -F file=@foo.txt

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 351
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"

        My updated snippet
        ------------------------------63a4b224c59f

    To delete a file, omit its contents while including its name in the
    `files` field:

        $ curl -X PUT https://api.bitbucket.org/2.0/snippets/evzijst/kypj -F files=image.png

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 149
        Content-Type: multipart/form-data; boundary=----------------------------ef8871065a86

        ------------------------------ef8871065a86
        Content-Disposition: form-data; name=\"files\"

        image.png
        ------------------------------ef8871065a86--

    The explicit use of the `files` element in `multipart/related` and
    `multipart/form-data` is only required when deleting files.
    The default mode of operation is for file parts to be processed,
    regardless of whether or not they are listed in `files`, as a
    convenience to the client.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Snippet]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    encoded_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""Update a snippet

     Used to update a snippet. Use this to add and delete files and to
    change a snippet's title.

    To update a snippet, one can either PUT a full snapshot, or only the
    parts that need to be changed.

    The contract for PUT on this API is that properties missing from the
    request remain untouched so that snippets can be efficiently
    manipulated with differential payloads.

    To delete a property (e.g. the title, or a file), include its name in
    the request, but omit its value (use `null`).

    As in Git, explicit renaming of files is not supported. Instead, to
    rename a file, delete it and add it again under another name. This can
    be done atomically in a single request. Rename detection is left to
    the SCM.

    PUT supports three different content types for both request and
    response bodies:

    * `application/json`
    * `multipart/related`
    * `multipart/form-data`

    The content type used for the request body can be different than that
    used for the response. Content types are specified using standard HTTP
    headers.

    Use the `Content-Type` and `Accept` headers to select the desired
    request and response format.


    application/json
    ----------------

    As with creation and retrieval, the content type determines what
    properties can be manipulated. `application/json` does not support
    file contents and is therefore limited to a snippet's meta data.

    To update the title, without changing any of its files:

        $ curl -X POST -H \"Content-Type: application/json\"
    https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": \"Updated title\"}'


    To delete the title:

        $ curl -X POST -H \"Content-Type: application/json\"
    https://api.bitbucket.org/2.0/snippets/evzijst/kypj             -d '{\"title\": null}'

    Not all parts of a snippet can be manipulated. The owner and creator
    for instance are immutable.


    multipart/related
    -----------------

    `multipart/related` can be used to manipulate all of a snippet's
    properties. The body is identical to a POST. properties omitted from
    the request are left unchanged. Since the `start` part contains JSON,
    the mechanism for manipulating the snippet's meta data is identical
    to `application/json` requests.

    To update one of a snippet's file contents, while also changing its
    title:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 288
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"title\": \"My updated snippet\",
          \"files\": {
              \"foo.txt\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        Updated file contents.

        --===============1438169132528273974==--

    Here only the parts that are changed are included in the body. The
    other files remain untouched.

    Note the use of the `files` list in the JSON part. This list contains
    the files that are being manipulated. This list should have
    corresponding multiparts in the request that contain the new contents
    of these files.

    If a filename in the `files` list does not have a corresponding part,
    it will be deleted from the snippet, as shown below:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 188
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"files\": {
            \"image.png\": {}
          }
        }

        --===============1438169132528273974==--

    To simulate a rename, delete a file and add the same file under
    another name:

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 212
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
            \"files\": {
              \"foo.txt\": {},
              \"bar.txt\": {}
            }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"bar.txt\"
        Content-Disposition: attachment; filename=\"bar.txt\"

        foo

        --===============1438169132528273974==--


    multipart/form-data
    -----------------

    Again, one can also use `multipart/form-data` to manipulate file
    contents and meta data atomically.

        $ curl -X PUT http://localhost:12345/2.0/snippets/evzijst/kypj             -F title=\"My updated
    snippet\" -F file=@foo.txt

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 351
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"

        My updated snippet
        ------------------------------63a4b224c59f

    To delete a file, omit its contents while including its name in the
    `files` field:

        $ curl -X PUT https://api.bitbucket.org/2.0/snippets/evzijst/kypj -F files=image.png

        PUT /2.0/snippets/evzijst/kypj HTTP/1.1
        Content-Length: 149
        Content-Type: multipart/form-data; boundary=----------------------------ef8871065a86

        ------------------------------ef8871065a86
        Content-Disposition: form-data; name=\"files\"

        image.png
        ------------------------------ef8871065a86--

    The explicit use of the `files` element in `multipart/related` and
    `multipart/form-data` is only required when deleting files.
    The default mode of operation is for file parts to be processed,
    regardless of whether or not they are listed in `files`, as a
    convenience to the client.

    Args:
        workspace (str):
        encoded_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Snippet
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            client=client,
        )
    ).parsed
