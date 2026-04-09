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
        "method": "get",
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
        response_200 = Snippet.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())

        return response_410

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
    r"""Get a snippet

     Retrieves a single snippet.

    Snippets support multiple content types:

    * application/json
    * multipart/related
    * multipart/form-data


    application/json
    ----------------

    The default content type of the response is `application/json`.
    Since JSON is always `utf-8`, it cannot reliably contain file contents
    for files that are not text. Therefore, JSON snippet documents only
    contain the filename and links to the file contents.

    This means that in order to retrieve all parts of a snippet, N+1
    requests need to be made (where N is the number of files in the
    snippet).


    multipart/related
    -----------------

    To retrieve an entire snippet in a single response, use the
    `Accept: multipart/related` HTTP request header.

        $ curl -H \"Accept: multipart/related\" https://api.bitbucket.org/2.0/snippets/evzijst/1

    Response:

        HTTP/1.1 200 OK
        Content-Length: 2214
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/snippets/evzijst/kypj\"
            },
            \"comments\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/comments\"
            },
            \"watchers\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/watchers\"
            },
            \"commits\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/commits\"
            }
          },
          \"id\": kypj,
          \"title\": \"My snippet\",
          \"created_on\": \"2014-12-29T22:22:04.790331+00:00\",
          \"updated_on\": \"2014-12-29T22:22:04.790331+00:00\",
          \"is_private\": false,
          \"files\": {
            \"foo.txt\": {
              \"links\": {
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/foo.txt\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-foo.txt\"
                }
              }
            },
            \"image.png\": {
              \"links\": {
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/image.png\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-image.png\"
                }
              }
            }
          ],
          \"owner\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket-staging-
    assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"
              }
            }
          },
          \"creator\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket-staging-
    assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"
              }
            }
          }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        foo

        --===============1438169132528273974==
        Content-Type: image/png
        MIME-Version: 1.0
        Content-Transfer-Encoding: base64
        Content-ID: \"image.png\"
        Content-Disposition: attachment; filename=\"image.png\"

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        --===============1438169132528273974==--

    multipart/form-data
    -------------------

    As with creating new snippets, `multipart/form-data` can be used as an
    alternative to `multipart/related`. However, the inherently flat
    structure of form-data means that only basic, root-level properties
    can be returned, while nested elements like `links` are omitted:

        $ curl -H \"Accept: multipart/form-data\" https://api.bitbucket.org/2.0/snippets/evzijst/kypj

    Response:

        HTTP/1.1 200 OK
        Content-Length: 951
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"
        Content-Type: text/plain; charset=\"utf-8\"

        My snippet
        ------------------------------63a4b224c59f--
        Content-Disposition: attachment; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: attachment; name=\"file\"; filename=\"image.png\"
        Content-Transfer-Encoding: base64
        Content-Type: application/octet-stream

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        ------------------------------5957323a6b76--

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
    r"""Get a snippet

     Retrieves a single snippet.

    Snippets support multiple content types:

    * application/json
    * multipart/related
    * multipart/form-data


    application/json
    ----------------

    The default content type of the response is `application/json`.
    Since JSON is always `utf-8`, it cannot reliably contain file contents
    for files that are not text. Therefore, JSON snippet documents only
    contain the filename and links to the file contents.

    This means that in order to retrieve all parts of a snippet, N+1
    requests need to be made (where N is the number of files in the
    snippet).


    multipart/related
    -----------------

    To retrieve an entire snippet in a single response, use the
    `Accept: multipart/related` HTTP request header.

        $ curl -H \"Accept: multipart/related\" https://api.bitbucket.org/2.0/snippets/evzijst/1

    Response:

        HTTP/1.1 200 OK
        Content-Length: 2214
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/snippets/evzijst/kypj\"
            },
            \"comments\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/comments\"
            },
            \"watchers\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/watchers\"
            },
            \"commits\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/commits\"
            }
          },
          \"id\": kypj,
          \"title\": \"My snippet\",
          \"created_on\": \"2014-12-29T22:22:04.790331+00:00\",
          \"updated_on\": \"2014-12-29T22:22:04.790331+00:00\",
          \"is_private\": false,
          \"files\": {
            \"foo.txt\": {
              \"links\": {
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/foo.txt\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-foo.txt\"
                }
              }
            },
            \"image.png\": {
              \"links\": {
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/image.png\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-image.png\"
                }
              }
            }
          ],
          \"owner\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket-staging-
    assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"
              }
            }
          },
          \"creator\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket-staging-
    assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"
              }
            }
          }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        foo

        --===============1438169132528273974==
        Content-Type: image/png
        MIME-Version: 1.0
        Content-Transfer-Encoding: base64
        Content-ID: \"image.png\"
        Content-Disposition: attachment; filename=\"image.png\"

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        --===============1438169132528273974==--

    multipart/form-data
    -------------------

    As with creating new snippets, `multipart/form-data` can be used as an
    alternative to `multipart/related`. However, the inherently flat
    structure of form-data means that only basic, root-level properties
    can be returned, while nested elements like `links` are omitted:

        $ curl -H \"Accept: multipart/form-data\" https://api.bitbucket.org/2.0/snippets/evzijst/kypj

    Response:

        HTTP/1.1 200 OK
        Content-Length: 951
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"
        Content-Type: text/plain; charset=\"utf-8\"

        My snippet
        ------------------------------63a4b224c59f--
        Content-Disposition: attachment; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: attachment; name=\"file\"; filename=\"image.png\"
        Content-Transfer-Encoding: base64
        Content-Type: application/octet-stream

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        ------------------------------5957323a6b76--

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
    r"""Get a snippet

     Retrieves a single snippet.

    Snippets support multiple content types:

    * application/json
    * multipart/related
    * multipart/form-data


    application/json
    ----------------

    The default content type of the response is `application/json`.
    Since JSON is always `utf-8`, it cannot reliably contain file contents
    for files that are not text. Therefore, JSON snippet documents only
    contain the filename and links to the file contents.

    This means that in order to retrieve all parts of a snippet, N+1
    requests need to be made (where N is the number of files in the
    snippet).


    multipart/related
    -----------------

    To retrieve an entire snippet in a single response, use the
    `Accept: multipart/related` HTTP request header.

        $ curl -H \"Accept: multipart/related\" https://api.bitbucket.org/2.0/snippets/evzijst/1

    Response:

        HTTP/1.1 200 OK
        Content-Length: 2214
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/snippets/evzijst/kypj\"
            },
            \"comments\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/comments\"
            },
            \"watchers\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/watchers\"
            },
            \"commits\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/commits\"
            }
          },
          \"id\": kypj,
          \"title\": \"My snippet\",
          \"created_on\": \"2014-12-29T22:22:04.790331+00:00\",
          \"updated_on\": \"2014-12-29T22:22:04.790331+00:00\",
          \"is_private\": false,
          \"files\": {
            \"foo.txt\": {
              \"links\": {
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/foo.txt\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-foo.txt\"
                }
              }
            },
            \"image.png\": {
              \"links\": {
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/image.png\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-image.png\"
                }
              }
            }
          ],
          \"owner\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket-staging-
    assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"
              }
            }
          },
          \"creator\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket-staging-
    assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"
              }
            }
          }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        foo

        --===============1438169132528273974==
        Content-Type: image/png
        MIME-Version: 1.0
        Content-Transfer-Encoding: base64
        Content-ID: \"image.png\"
        Content-Disposition: attachment; filename=\"image.png\"

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        --===============1438169132528273974==--

    multipart/form-data
    -------------------

    As with creating new snippets, `multipart/form-data` can be used as an
    alternative to `multipart/related`. However, the inherently flat
    structure of form-data means that only basic, root-level properties
    can be returned, while nested elements like `links` are omitted:

        $ curl -H \"Accept: multipart/form-data\" https://api.bitbucket.org/2.0/snippets/evzijst/kypj

    Response:

        HTTP/1.1 200 OK
        Content-Length: 951
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"
        Content-Type: text/plain; charset=\"utf-8\"

        My snippet
        ------------------------------63a4b224c59f--
        Content-Disposition: attachment; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: attachment; name=\"file\"; filename=\"image.png\"
        Content-Transfer-Encoding: base64
        Content-Type: application/octet-stream

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        ------------------------------5957323a6b76--

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
    r"""Get a snippet

     Retrieves a single snippet.

    Snippets support multiple content types:

    * application/json
    * multipart/related
    * multipart/form-data


    application/json
    ----------------

    The default content type of the response is `application/json`.
    Since JSON is always `utf-8`, it cannot reliably contain file contents
    for files that are not text. Therefore, JSON snippet documents only
    contain the filename and links to the file contents.

    This means that in order to retrieve all parts of a snippet, N+1
    requests need to be made (where N is the number of files in the
    snippet).


    multipart/related
    -----------------

    To retrieve an entire snippet in a single response, use the
    `Accept: multipart/related` HTTP request header.

        $ curl -H \"Accept: multipart/related\" https://api.bitbucket.org/2.0/snippets/evzijst/1

    Response:

        HTTP/1.1 200 OK
        Content-Length: 2214
        Content-Type: multipart/related; start=\"snippet\";
    boundary=\"===============1438169132528273974==\"
        MIME-Version: 1.0

        --===============1438169132528273974==
        Content-Type: application/json; charset=\"utf-8\"
        MIME-Version: 1.0
        Content-ID: snippet

        {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/snippets/evzijst/kypj\"
            },
            \"comments\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/comments\"
            },
            \"watchers\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/watchers\"
            },
            \"commits\": {
              \"href\": \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/commits\"
            }
          },
          \"id\": kypj,
          \"title\": \"My snippet\",
          \"created_on\": \"2014-12-29T22:22:04.790331+00:00\",
          \"updated_on\": \"2014-12-29T22:22:04.790331+00:00\",
          \"is_private\": false,
          \"files\": {
            \"foo.txt\": {
              \"links\": {
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/foo.txt\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-foo.txt\"
                }
              }
            },
            \"image.png\": {
              \"links\": {
                \"self\": {
                  \"href\":
    \"https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/image.png\"
                },
                \"html\": {
                  \"href\": \"https://bitbucket.org/snippets/evzijst/kypj#file-image.png\"
                }
              }
            }
          ],
          \"owner\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket-staging-
    assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"
              }
            }
          },
          \"creator\": {
            \"username\": \"evzijst\",
            \"nickname\": \"evzijst\",
            \"display_name\": \"Erik van Zijst\",
            \"uuid\": \"{d301aafa-d676-4ee0-88be-962be7417567}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/evzijst\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/evzijst\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket-staging-
    assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png\"
              }
            }
          }
        }

        --===============1438169132528273974==
        Content-Type: text/plain; charset=\"us-ascii\"
        MIME-Version: 1.0
        Content-Transfer-Encoding: 7bit
        Content-ID: \"foo.txt\"
        Content-Disposition: attachment; filename=\"foo.txt\"

        foo

        --===============1438169132528273974==
        Content-Type: image/png
        MIME-Version: 1.0
        Content-Transfer-Encoding: base64
        Content-ID: \"image.png\"
        Content-Disposition: attachment; filename=\"image.png\"

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        --===============1438169132528273974==--

    multipart/form-data
    -------------------

    As with creating new snippets, `multipart/form-data` can be used as an
    alternative to `multipart/related`. However, the inherently flat
    structure of form-data means that only basic, root-level properties
    can be returned, while nested elements like `links` are omitted:

        $ curl -H \"Accept: multipart/form-data\" https://api.bitbucket.org/2.0/snippets/evzijst/kypj

    Response:

        HTTP/1.1 200 OK
        Content-Length: 951
        Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f

        ------------------------------63a4b224c59f
        Content-Disposition: form-data; name=\"title\"
        Content-Type: text/plain; charset=\"utf-8\"

        My snippet
        ------------------------------63a4b224c59f--
        Content-Disposition: attachment; name=\"file\"; filename=\"foo.txt\"
        Content-Type: text/plain

        foo

        ------------------------------63a4b224c59f
        Content-Disposition: attachment; name=\"file\"; filename=\"image.png\"
        Content-Transfer-Encoding: base64
        Content-Type: application/octet-stream

        iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m
        TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB
        cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5
        EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ
        73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN
        AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==
        ------------------------------5957323a6b76--

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
