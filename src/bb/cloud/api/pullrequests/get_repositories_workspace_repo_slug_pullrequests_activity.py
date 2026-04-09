from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/pullrequests/activity".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
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
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""List a pull request activity log

     Returns a paginated list of the pull request's activity log.

    This handler serves both a v20 and internal endpoint. The v20 endpoint
    returns reviewer comments, updates, approvals and request changes. The internal
    endpoint includes those plus tasks and attachments.

    Comments created on a file or a line of code have an inline property.

    Comment example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"comment\": {
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695/comments/118571088\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695/_/diff#comment-118571088\"
                        }
                    },
                    \"deleted\": false,
                    \"pullrequest\": {
                        \"type\": \"pullrequest\",
                        \"id\": 5695,
                        \"links\": {
                            \"self\": {
                                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                            }
                        },
                        \"title\": \"username/NONE: small change from onFocus to onClick to handle
    tabbing through the page and not expand the editor unless a click event triggers it\"
                    },
                    \"content\": {
                        \"raw\": \"inline with to a dn from lines\",
                        \"markup\": \"markdown\",
                        \"html\": \"<p>inline with to a dn from lines</p>\",
                        \"type\": \"rendered\"
                    },
                    \"created_on\": \"2019-09-27T00:33:46.039178+00:00\",
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"created_on\": \"2019-09-27T00:33:46.039178+00:00\",
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"updated_on\": \"2019-09-27T00:33:46.055384+00:00\",
                    \"inline\": {
                        \"context_lines\": \"\",
                        \"to\": null,
                        \"path\": \"\",
                        \"outdated\": false,
                        \"from\": 211
                    },
                    \"type\": \"pullrequest_comment\",
                    \"id\": 118571088
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Updates include a state property of OPEN, MERGED, or DECLINED.

    Update example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"update\": {
                    \"description\": \"\",
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\",
                    \"destination\": {
                        \"commit\": {
                            \"type\": \"commit\",
                            \"hash\": \"6a2c16e4a152\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/6a2c16e4a152\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-
    mk-2/commits/6a2c16e4a152\"
                                }
                            }
                        },
                        \"branch\": {
                            \"name\": \"master\"
                        },
                        \"repository\": {
                            \"name\": \"Atlaskit-MK-2\",
                            \"type\": \"repository\",
                            \"full_name\": \"atlassian/atlaskit-mk-2\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2\"
                                },
                                \"avatar\": {
                                    \"href\": \"https://bytebucket.org/ravatar/%7B%7D?ts=js\"
                                }
                            },
                            \"uuid\": \"{}\"
                        }
                    },
                    \"reason\": \"\",
                    \"source\": {
                        \"commit\": {
                            \"type\": \"commit\",
                            \"hash\": \"728c8bad1813\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/728c8bad1813\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-
    mk-2/commits/728c8bad1813\"
                                }
                            }
                        },
                        \"branch\": {
                            \"name\": \"username/NONE-add-onClick-prop-for-accessibility\"
                        },
                        \"repository\": {
                            \"name\": \"Atlaskit-MK-2\",
                            \"type\": \"repository\",
                            \"full_name\": \"atlassian/atlaskit-mk-2\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2\"
                                },
                                \"avatar\": {
                                    \"href\": \"https://bytebucket.org/ravatar/%7B%7D?ts=js\"
                                }
                            },
                            \"uuid\": \"{}\"
                        }
                    },
                    \"state\": \"OPEN\",
                    \"author\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"date\": \"2019-05-10T06:48:25.305565+00:00\"
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Approval example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"approval\": {
                    \"date\": \"2019-09-27T00:37:19.849534+00:00\",
                    \"pullrequest\": {
                        \"type\": \"pullrequest\",
                        \"id\": 5695,
                        \"links\": {
                            \"self\": {
                                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                            }
                        },
                        \"title\": \"username/NONE: small change from onFocus to onClick to handle
    tabbing through the page and not expand the editor unless a click event triggers it\"
                    },
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    }
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""List a pull request activity log

     Returns a paginated list of the pull request's activity log.

    This handler serves both a v20 and internal endpoint. The v20 endpoint
    returns reviewer comments, updates, approvals and request changes. The internal
    endpoint includes those plus tasks and attachments.

    Comments created on a file or a line of code have an inline property.

    Comment example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"comment\": {
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695/comments/118571088\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695/_/diff#comment-118571088\"
                        }
                    },
                    \"deleted\": false,
                    \"pullrequest\": {
                        \"type\": \"pullrequest\",
                        \"id\": 5695,
                        \"links\": {
                            \"self\": {
                                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                            }
                        },
                        \"title\": \"username/NONE: small change from onFocus to onClick to handle
    tabbing through the page and not expand the editor unless a click event triggers it\"
                    },
                    \"content\": {
                        \"raw\": \"inline with to a dn from lines\",
                        \"markup\": \"markdown\",
                        \"html\": \"<p>inline with to a dn from lines</p>\",
                        \"type\": \"rendered\"
                    },
                    \"created_on\": \"2019-09-27T00:33:46.039178+00:00\",
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"created_on\": \"2019-09-27T00:33:46.039178+00:00\",
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"updated_on\": \"2019-09-27T00:33:46.055384+00:00\",
                    \"inline\": {
                        \"context_lines\": \"\",
                        \"to\": null,
                        \"path\": \"\",
                        \"outdated\": false,
                        \"from\": 211
                    },
                    \"type\": \"pullrequest_comment\",
                    \"id\": 118571088
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Updates include a state property of OPEN, MERGED, or DECLINED.

    Update example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"update\": {
                    \"description\": \"\",
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\",
                    \"destination\": {
                        \"commit\": {
                            \"type\": \"commit\",
                            \"hash\": \"6a2c16e4a152\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/6a2c16e4a152\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-
    mk-2/commits/6a2c16e4a152\"
                                }
                            }
                        },
                        \"branch\": {
                            \"name\": \"master\"
                        },
                        \"repository\": {
                            \"name\": \"Atlaskit-MK-2\",
                            \"type\": \"repository\",
                            \"full_name\": \"atlassian/atlaskit-mk-2\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2\"
                                },
                                \"avatar\": {
                                    \"href\": \"https://bytebucket.org/ravatar/%7B%7D?ts=js\"
                                }
                            },
                            \"uuid\": \"{}\"
                        }
                    },
                    \"reason\": \"\",
                    \"source\": {
                        \"commit\": {
                            \"type\": \"commit\",
                            \"hash\": \"728c8bad1813\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/728c8bad1813\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-
    mk-2/commits/728c8bad1813\"
                                }
                            }
                        },
                        \"branch\": {
                            \"name\": \"username/NONE-add-onClick-prop-for-accessibility\"
                        },
                        \"repository\": {
                            \"name\": \"Atlaskit-MK-2\",
                            \"type\": \"repository\",
                            \"full_name\": \"atlassian/atlaskit-mk-2\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2\"
                                },
                                \"avatar\": {
                                    \"href\": \"https://bytebucket.org/ravatar/%7B%7D?ts=js\"
                                }
                            },
                            \"uuid\": \"{}\"
                        }
                    },
                    \"state\": \"OPEN\",
                    \"author\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"date\": \"2019-05-10T06:48:25.305565+00:00\"
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Approval example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"approval\": {
                    \"date\": \"2019-09-27T00:37:19.849534+00:00\",
                    \"pullrequest\": {
                        \"type\": \"pullrequest\",
                        \"id\": 5695,
                        \"links\": {
                            \"self\": {
                                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                            }
                        },
                        \"title\": \"username/NONE: small change from onFocus to onClick to handle
    tabbing through the page and not expand the editor unless a click event triggers it\"
                    },
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    }
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""List a pull request activity log

     Returns a paginated list of the pull request's activity log.

    This handler serves both a v20 and internal endpoint. The v20 endpoint
    returns reviewer comments, updates, approvals and request changes. The internal
    endpoint includes those plus tasks and attachments.

    Comments created on a file or a line of code have an inline property.

    Comment example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"comment\": {
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695/comments/118571088\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695/_/diff#comment-118571088\"
                        }
                    },
                    \"deleted\": false,
                    \"pullrequest\": {
                        \"type\": \"pullrequest\",
                        \"id\": 5695,
                        \"links\": {
                            \"self\": {
                                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                            }
                        },
                        \"title\": \"username/NONE: small change from onFocus to onClick to handle
    tabbing through the page and not expand the editor unless a click event triggers it\"
                    },
                    \"content\": {
                        \"raw\": \"inline with to a dn from lines\",
                        \"markup\": \"markdown\",
                        \"html\": \"<p>inline with to a dn from lines</p>\",
                        \"type\": \"rendered\"
                    },
                    \"created_on\": \"2019-09-27T00:33:46.039178+00:00\",
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"created_on\": \"2019-09-27T00:33:46.039178+00:00\",
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"updated_on\": \"2019-09-27T00:33:46.055384+00:00\",
                    \"inline\": {
                        \"context_lines\": \"\",
                        \"to\": null,
                        \"path\": \"\",
                        \"outdated\": false,
                        \"from\": 211
                    },
                    \"type\": \"pullrequest_comment\",
                    \"id\": 118571088
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Updates include a state property of OPEN, MERGED, or DECLINED.

    Update example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"update\": {
                    \"description\": \"\",
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\",
                    \"destination\": {
                        \"commit\": {
                            \"type\": \"commit\",
                            \"hash\": \"6a2c16e4a152\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/6a2c16e4a152\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-
    mk-2/commits/6a2c16e4a152\"
                                }
                            }
                        },
                        \"branch\": {
                            \"name\": \"master\"
                        },
                        \"repository\": {
                            \"name\": \"Atlaskit-MK-2\",
                            \"type\": \"repository\",
                            \"full_name\": \"atlassian/atlaskit-mk-2\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2\"
                                },
                                \"avatar\": {
                                    \"href\": \"https://bytebucket.org/ravatar/%7B%7D?ts=js\"
                                }
                            },
                            \"uuid\": \"{}\"
                        }
                    },
                    \"reason\": \"\",
                    \"source\": {
                        \"commit\": {
                            \"type\": \"commit\",
                            \"hash\": \"728c8bad1813\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/728c8bad1813\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-
    mk-2/commits/728c8bad1813\"
                                }
                            }
                        },
                        \"branch\": {
                            \"name\": \"username/NONE-add-onClick-prop-for-accessibility\"
                        },
                        \"repository\": {
                            \"name\": \"Atlaskit-MK-2\",
                            \"type\": \"repository\",
                            \"full_name\": \"atlassian/atlaskit-mk-2\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2\"
                                },
                                \"avatar\": {
                                    \"href\": \"https://bytebucket.org/ravatar/%7B%7D?ts=js\"
                                }
                            },
                            \"uuid\": \"{}\"
                        }
                    },
                    \"state\": \"OPEN\",
                    \"author\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"date\": \"2019-05-10T06:48:25.305565+00:00\"
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Approval example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"approval\": {
                    \"date\": \"2019-09-27T00:37:19.849534+00:00\",
                    \"pullrequest\": {
                        \"type\": \"pullrequest\",
                        \"id\": 5695,
                        \"links\": {
                            \"self\": {
                                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                            }
                        },
                        \"title\": \"username/NONE: small change from onFocus to onClick to handle
    tabbing through the page and not expand the editor unless a click event triggers it\"
                    },
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    }
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""List a pull request activity log

     Returns a paginated list of the pull request's activity log.

    This handler serves both a v20 and internal endpoint. The v20 endpoint
    returns reviewer comments, updates, approvals and request changes. The internal
    endpoint includes those plus tasks and attachments.

    Comments created on a file or a line of code have an inline property.

    Comment example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"comment\": {
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695/comments/118571088\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695/_/diff#comment-118571088\"
                        }
                    },
                    \"deleted\": false,
                    \"pullrequest\": {
                        \"type\": \"pullrequest\",
                        \"id\": 5695,
                        \"links\": {
                            \"self\": {
                                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                            }
                        },
                        \"title\": \"username/NONE: small change from onFocus to onClick to handle
    tabbing through the page and not expand the editor unless a click event triggers it\"
                    },
                    \"content\": {
                        \"raw\": \"inline with to a dn from lines\",
                        \"markup\": \"markdown\",
                        \"html\": \"<p>inline with to a dn from lines</p>\",
                        \"type\": \"rendered\"
                    },
                    \"created_on\": \"2019-09-27T00:33:46.039178+00:00\",
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"created_on\": \"2019-09-27T00:33:46.039178+00:00\",
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"updated_on\": \"2019-09-27T00:33:46.055384+00:00\",
                    \"inline\": {
                        \"context_lines\": \"\",
                        \"to\": null,
                        \"path\": \"\",
                        \"outdated\": false,
                        \"from\": 211
                    },
                    \"type\": \"pullrequest_comment\",
                    \"id\": 118571088
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Updates include a state property of OPEN, MERGED, or DECLINED.

    Update example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"update\": {
                    \"description\": \"\",
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\",
                    \"destination\": {
                        \"commit\": {
                            \"type\": \"commit\",
                            \"hash\": \"6a2c16e4a152\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/6a2c16e4a152\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-
    mk-2/commits/6a2c16e4a152\"
                                }
                            }
                        },
                        \"branch\": {
                            \"name\": \"master\"
                        },
                        \"repository\": {
                            \"name\": \"Atlaskit-MK-2\",
                            \"type\": \"repository\",
                            \"full_name\": \"atlassian/atlaskit-mk-2\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2\"
                                },
                                \"avatar\": {
                                    \"href\": \"https://bytebucket.org/ravatar/%7B%7D?ts=js\"
                                }
                            },
                            \"uuid\": \"{}\"
                        }
                    },
                    \"reason\": \"\",
                    \"source\": {
                        \"commit\": {
                            \"type\": \"commit\",
                            \"hash\": \"728c8bad1813\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/728c8bad1813\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-
    mk-2/commits/728c8bad1813\"
                                }
                            }
                        },
                        \"branch\": {
                            \"name\": \"username/NONE-add-onClick-prop-for-accessibility\"
                        },
                        \"repository\": {
                            \"name\": \"Atlaskit-MK-2\",
                            \"type\": \"repository\",
                            \"full_name\": \"atlassian/atlaskit-mk-2\",
                            \"links\": {
                                \"self\": {
                                    \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2\"
                                },
                                \"html\": {
                                    \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2\"
                                },
                                \"avatar\": {
                                    \"href\": \"https://bytebucket.org/ravatar/%7B%7D?ts=js\"
                                }
                            },
                            \"uuid\": \"{}\"
                        }
                    },
                    \"state\": \"OPEN\",
                    \"author\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    },
                    \"date\": \"2019-05-10T06:48:25.305565+00:00\"
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Approval example:
    ```
    {
        \"pagelen\": 20,
        \"values\": [
            {
                \"approval\": {
                    \"date\": \"2019-09-27T00:37:19.849534+00:00\",
                    \"pullrequest\": {
                        \"type\": \"pullrequest\",
                        \"id\": 5695,
                        \"links\": {
                            \"self\": {
                                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                            }
                        },
                        \"title\": \"username/NONE: small change from onFocus to onClick to handle
    tabbing through the page and not expand the editor unless a click event triggers it\"
                    },
                    \"user\": {
                        \"display_name\": \"Name Lastname\",
                        \"uuid\": \"{}\",
                        \"links\": {
                            \"self\": {
                                \"href\": \"https://api.bitbucket.org/2.0/users/%7B%7D\"
                            },
                            \"html\": {
                                \"href\": \"https://bitbucket.org/%7B%7D/\"
                            },
                            \"avatar\": {
                                \"href\": \"https://avatar-management--avatars.us-
    west-2.prod.public.atl-paas.net/:/128\"
                            }
                        },
                        \"type\": \"user\",
                        \"nickname\": \"Name\",
                        \"account_id\": \"\"
                    }
                },
                \"pull_request\": {
                    \"type\": \"pullrequest\",
                    \"id\": 5695,
                    \"links\": {
                        \"self\": {
                            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-
    mk-2/pullrequests/5695\"
                        },
                        \"html\": {
                            \"href\": \"https://bitbucket.org/atlassian/atlaskit-mk-2/pull-
    requests/5695\"
                        }
                    },
                    \"title\": \"username/NONE: small change from onFocus to onClick to handle tabbing
    through the page and not expand the editor unless a click event triggers it\"
                }
            }
        ]
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
