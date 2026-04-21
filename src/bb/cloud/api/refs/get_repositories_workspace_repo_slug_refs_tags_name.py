from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.tag import Tag
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/refs/tags/{name}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | Tag
type ParseResult = Error | Tag | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = Tag.from_dict(response.json())

        return response_200

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
    repo_slug: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""Get a tag

     Returns the specified tag.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq .
    {
      \"name\": \"3.8\",
      \"links\": {
        \"commits\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8\"
        },
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8\"
        },
        \"html\": {
          \"href\": \"https://bitbucket.org/seanfarley/hg/commits/tag/3.8\"
        }
      },
      \"tagger\": {
        \"raw\": \"Matt Mackall <mpm@selenic.com>\",
        \"type\": \"author\",
        \"user\": {
          \"username\": \"mpmselenic\",
          \"nickname\": \"mpmselenic\",
          \"display_name\": \"Matt Mackall\",
          \"type\": \"user\",
          \"uuid\": \"{a4934530-db4c-419c-a478-9ab4964c2ee7}\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/users/mpmselenic\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/mpmselenic/\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/account/mpmselenic/avatar/32/\"
            }
          }
        }
      },
      \"date\": \"2016-05-01T18:52:25+00:00\",
      \"message\": \"Added tag 3.8 for changeset f85de28eae32\",
      \"type\": \"tag\",
      \"target\": {
        \"hash\": \"f85de28eae32e7d3064b1a1321309071bbaaa069\",
        \"repository\": {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg/avatar/32/\"
            }
          },
          \"type\": \"repository\",
          \"name\": \"hg\",
          \"full_name\": \"seanfarley/hg\",
          \"uuid\": \"{c75687fb-e99d-4579-9087-190dbd406d30}\"
        },
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069\"
          },
          \"comments\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/comments\"
          },
          \"patch\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d30
    64b1a1321309071bbaaa069\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069\"
          },
          \"diff\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d306
    4b1a1321309071bbaaa069\"
          },
          \"approve\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/approve\"
          },
          \"statuses\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/statuses\"
          }
        },
        \"author\": {
          \"raw\": \"Sean Farley <sean@farley.io>\",
          \"type\": \"author\",
          \"user\": {
            \"username\": \"seanfarley\",
            \"nickname\": \"seanfarley\",
            \"display_name\": \"Sean Farley\",
            \"type\": \"user\",
            \"uuid\": \"{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/seanfarley\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/seanfarley/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/seanfarley/avatar/32/\"
              }
            }
          }
        },
        \"parents\": [
          {
            \"hash\": \"9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\",
            \"type\": \"commit\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07f
    c60887f9d3d34d9ac7d536f470d2\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"
              }
            }
          }
        ],
        \"date\": \"2016-05-01T04:21:17+00:00\",
        \"message\": \"debian: alphabetize build deps\",
        \"type\": \"commit\"
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Tag]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""Get a tag

     Returns the specified tag.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq .
    {
      \"name\": \"3.8\",
      \"links\": {
        \"commits\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8\"
        },
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8\"
        },
        \"html\": {
          \"href\": \"https://bitbucket.org/seanfarley/hg/commits/tag/3.8\"
        }
      },
      \"tagger\": {
        \"raw\": \"Matt Mackall <mpm@selenic.com>\",
        \"type\": \"author\",
        \"user\": {
          \"username\": \"mpmselenic\",
          \"nickname\": \"mpmselenic\",
          \"display_name\": \"Matt Mackall\",
          \"type\": \"user\",
          \"uuid\": \"{a4934530-db4c-419c-a478-9ab4964c2ee7}\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/users/mpmselenic\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/mpmselenic/\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/account/mpmselenic/avatar/32/\"
            }
          }
        }
      },
      \"date\": \"2016-05-01T18:52:25+00:00\",
      \"message\": \"Added tag 3.8 for changeset f85de28eae32\",
      \"type\": \"tag\",
      \"target\": {
        \"hash\": \"f85de28eae32e7d3064b1a1321309071bbaaa069\",
        \"repository\": {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg/avatar/32/\"
            }
          },
          \"type\": \"repository\",
          \"name\": \"hg\",
          \"full_name\": \"seanfarley/hg\",
          \"uuid\": \"{c75687fb-e99d-4579-9087-190dbd406d30}\"
        },
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069\"
          },
          \"comments\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/comments\"
          },
          \"patch\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d30
    64b1a1321309071bbaaa069\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069\"
          },
          \"diff\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d306
    4b1a1321309071bbaaa069\"
          },
          \"approve\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/approve\"
          },
          \"statuses\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/statuses\"
          }
        },
        \"author\": {
          \"raw\": \"Sean Farley <sean@farley.io>\",
          \"type\": \"author\",
          \"user\": {
            \"username\": \"seanfarley\",
            \"nickname\": \"seanfarley\",
            \"display_name\": \"Sean Farley\",
            \"type\": \"user\",
            \"uuid\": \"{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/seanfarley\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/seanfarley/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/seanfarley/avatar/32/\"
              }
            }
          }
        },
        \"parents\": [
          {
            \"hash\": \"9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\",
            \"type\": \"commit\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07f
    c60887f9d3d34d9ac7d536f470d2\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"
              }
            }
          }
        ],
        \"date\": \"2016-05-01T04:21:17+00:00\",
        \"message\": \"debian: alphabetize build deps\",
        \"type\": \"commit\"
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Tag
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""Get a tag

     Returns the specified tag.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq .
    {
      \"name\": \"3.8\",
      \"links\": {
        \"commits\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8\"
        },
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8\"
        },
        \"html\": {
          \"href\": \"https://bitbucket.org/seanfarley/hg/commits/tag/3.8\"
        }
      },
      \"tagger\": {
        \"raw\": \"Matt Mackall <mpm@selenic.com>\",
        \"type\": \"author\",
        \"user\": {
          \"username\": \"mpmselenic\",
          \"nickname\": \"mpmselenic\",
          \"display_name\": \"Matt Mackall\",
          \"type\": \"user\",
          \"uuid\": \"{a4934530-db4c-419c-a478-9ab4964c2ee7}\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/users/mpmselenic\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/mpmselenic/\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/account/mpmselenic/avatar/32/\"
            }
          }
        }
      },
      \"date\": \"2016-05-01T18:52:25+00:00\",
      \"message\": \"Added tag 3.8 for changeset f85de28eae32\",
      \"type\": \"tag\",
      \"target\": {
        \"hash\": \"f85de28eae32e7d3064b1a1321309071bbaaa069\",
        \"repository\": {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg/avatar/32/\"
            }
          },
          \"type\": \"repository\",
          \"name\": \"hg\",
          \"full_name\": \"seanfarley/hg\",
          \"uuid\": \"{c75687fb-e99d-4579-9087-190dbd406d30}\"
        },
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069\"
          },
          \"comments\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/comments\"
          },
          \"patch\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d30
    64b1a1321309071bbaaa069\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069\"
          },
          \"diff\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d306
    4b1a1321309071bbaaa069\"
          },
          \"approve\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/approve\"
          },
          \"statuses\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/statuses\"
          }
        },
        \"author\": {
          \"raw\": \"Sean Farley <sean@farley.io>\",
          \"type\": \"author\",
          \"user\": {
            \"username\": \"seanfarley\",
            \"nickname\": \"seanfarley\",
            \"display_name\": \"Sean Farley\",
            \"type\": \"user\",
            \"uuid\": \"{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/seanfarley\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/seanfarley/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/seanfarley/avatar/32/\"
              }
            }
          }
        },
        \"parents\": [
          {
            \"hash\": \"9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\",
            \"type\": \"commit\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07f
    c60887f9d3d34d9ac7d536f470d2\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"
              }
            }
          }
        ],
        \"date\": \"2016-05-01T04:21:17+00:00\",
        \"message\": \"debian: alphabetize build deps\",
        \"type\": \"commit\"
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Tag]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""Get a tag

     Returns the specified tag.

    ```
    $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq .
    {
      \"name\": \"3.8\",
      \"links\": {
        \"commits\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8\"
        },
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8\"
        },
        \"html\": {
          \"href\": \"https://bitbucket.org/seanfarley/hg/commits/tag/3.8\"
        }
      },
      \"tagger\": {
        \"raw\": \"Matt Mackall <mpm@selenic.com>\",
        \"type\": \"author\",
        \"user\": {
          \"username\": \"mpmselenic\",
          \"nickname\": \"mpmselenic\",
          \"display_name\": \"Matt Mackall\",
          \"type\": \"user\",
          \"uuid\": \"{a4934530-db4c-419c-a478-9ab4964c2ee7}\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/users/mpmselenic\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/mpmselenic/\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/account/mpmselenic/avatar/32/\"
            }
          }
        }
      },
      \"date\": \"2016-05-01T18:52:25+00:00\",
      \"message\": \"Added tag 3.8 for changeset f85de28eae32\",
      \"type\": \"tag\",
      \"target\": {
        \"hash\": \"f85de28eae32e7d3064b1a1321309071bbaaa069\",
        \"repository\": {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg\"
            },
            \"html\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg\"
            },
            \"avatar\": {
              \"href\": \"https://bitbucket.org/seanfarley/hg/avatar/32/\"
            }
          },
          \"type\": \"repository\",
          \"name\": \"hg\",
          \"full_name\": \"seanfarley/hg\",
          \"uuid\": \"{c75687fb-e99d-4579-9087-190dbd406d30}\"
        },
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069\"
          },
          \"comments\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/comments\"
          },
          \"patch\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d30
    64b1a1321309071bbaaa069\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069\"
          },
          \"diff\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d306
    4b1a1321309071bbaaa069\"
          },
          \"approve\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/approve\"
          },
          \"statuses\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3
    064b1a1321309071bbaaa069/statuses\"
          }
        },
        \"author\": {
          \"raw\": \"Sean Farley <sean@farley.io>\",
          \"type\": \"author\",
          \"user\": {
            \"username\": \"seanfarley\",
            \"nickname\": \"seanfarley\",
            \"display_name\": \"Sean Farley\",
            \"type\": \"user\",
            \"uuid\": \"{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/users/seanfarley\"
              },
              \"html\": {
                \"href\": \"https://bitbucket.org/seanfarley/\"
              },
              \"avatar\": {
                \"href\": \"https://bitbucket.org/account/seanfarley/avatar/32/\"
              }
            }
          }
        },
        \"parents\": [
          {
            \"hash\": \"9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\",
            \"type\": \"commit\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07f
    c60887f9d3d34d9ac7d536f470d2\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2\"
              }
            }
          }
        ],
        \"date\": \"2016-05-01T04:21:17+00:00\",
        \"message\": \"debian: alphabetize build deps\",
        \"type\": \"commit\"
      }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Tag
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            name=name,
            client=client,
        )
    ).parsed
