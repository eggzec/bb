from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_annotations_response_401 import AddAnnotationsResponse401
from ...models.add_annotations_response_404 import AddAnnotationsResponse404
from ...models.rest_bulk_add_insight_annotation_request import RestBulkAddInsightAnnotationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    body: RestBulkAddInsightAnnotationRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/insights/latest/projects/{project_key}/repos/{repository_slug}/commits/{commit_id}/reports/{key}/annotations".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            commit_id=quote(str(commit_id), safe=""),
            key=quote(str(key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = AddAnnotationsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = AddAnnotationsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkAddInsightAnnotationRequest | Unset = UNSET,
) -> Response[AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any]:
    r"""Add Code Insights annotations

     Add annotations to the given report. The request should be a JSON object mapping the string
    \"annotations\" to an array of maps containing the annotation data, as described below. See also the
    example request.

    A few things to note:- Annotations are an extension of a report, so a report must first exist in
    order to post annotations.   Annotations are posted separately from the report, and can be posted in
    bulk using this endpoint.
    - Only the annotations that are on lines changed in the unified diff will be displayed. This means
    it is  likely not all annotations posted will be displayed on the pull request  It also means that
    if the user is viewing a side-by-side diff,  commit diff or iterative review diff they will not be
    able to view the annotations.
    - A report cannot have more than 1000 annotations by default, however this property is congurable at
    an  instance level. If the request would result in more than the maximum number of annotations being
    stored  then the entire request is rejected and no new annotations are stored.
    - There is no de-duplication of annotations on Bitbucket so be sure that reruns of builds will first
    delete the report and annotations before creating them.

    # Annotation parameters

    |Parameter|Description|Required?|Restrictions|Type|
    |--- |--- |--- |--- |--- |
    |path|The path of the file on which this annotation should be placed. This is the path of the
    filerelative to the git repository. If no path is provided, then it will appear in the overview
    modalon all pull requests where the tip of the branch is the given commit, regardless of which files
    weremodified.|No||String|
    |line|The line number that the annotation should belong to. If no line number is provided, then it
    willdefault to 0 and in a pull request it will appear at the top of the file specified by the path
    field.|No|Non-negative integer|Integer|
    |message|The message to display to users|Yes|The maximum length accepted is 2000 characters, however
    the user interface may truncate this valuefor display purposes. We recommend that the message is
    short and succinct, with further detailsavailable to the user if needed on the page linked to by the
    the annotation link.|String|
    |severity|The severity of the annotation|Yes|One of: LOW, MEDIUM, HIGH|String|
    |link|An http or https URL representing the location of the annotation in the external
    tool|No||String|
    |type|The type of annotation posted|No|One of: VULNERABILITY, CODE_SMELL, BUG|String|
    |externalId|If the caller requires a link to get or modify this annotation, then an ID must be
    provided. It isnot used or required by Bitbucket, but only by the annotation creator for updating or
    deleting thisspecific annotation.|No|A string value shorter than 450 characters|String|

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        body (RestBulkAddInsightAnnotationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkAddInsightAnnotationRequest | Unset = UNSET,
) -> AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any | None:
    r"""Add Code Insights annotations

     Add annotations to the given report. The request should be a JSON object mapping the string
    \"annotations\" to an array of maps containing the annotation data, as described below. See also the
    example request.

    A few things to note:- Annotations are an extension of a report, so a report must first exist in
    order to post annotations.   Annotations are posted separately from the report, and can be posted in
    bulk using this endpoint.
    - Only the annotations that are on lines changed in the unified diff will be displayed. This means
    it is  likely not all annotations posted will be displayed on the pull request  It also means that
    if the user is viewing a side-by-side diff,  commit diff or iterative review diff they will not be
    able to view the annotations.
    - A report cannot have more than 1000 annotations by default, however this property is congurable at
    an  instance level. If the request would result in more than the maximum number of annotations being
    stored  then the entire request is rejected and no new annotations are stored.
    - There is no de-duplication of annotations on Bitbucket so be sure that reruns of builds will first
    delete the report and annotations before creating them.

    # Annotation parameters

    |Parameter|Description|Required?|Restrictions|Type|
    |--- |--- |--- |--- |--- |
    |path|The path of the file on which this annotation should be placed. This is the path of the
    filerelative to the git repository. If no path is provided, then it will appear in the overview
    modalon all pull requests where the tip of the branch is the given commit, regardless of which files
    weremodified.|No||String|
    |line|The line number that the annotation should belong to. If no line number is provided, then it
    willdefault to 0 and in a pull request it will appear at the top of the file specified by the path
    field.|No|Non-negative integer|Integer|
    |message|The message to display to users|Yes|The maximum length accepted is 2000 characters, however
    the user interface may truncate this valuefor display purposes. We recommend that the message is
    short and succinct, with further detailsavailable to the user if needed on the page linked to by the
    the annotation link.|String|
    |severity|The severity of the annotation|Yes|One of: LOW, MEDIUM, HIGH|String|
    |link|An http or https URL representing the location of the annotation in the external
    tool|No||String|
    |type|The type of annotation posted|No|One of: VULNERABILITY, CODE_SMELL, BUG|String|
    |externalId|If the caller requires a link to get or modify this annotation, then an ID must be
    provided. It isnot used or required by Bitbucket, but only by the annotation creator for updating or
    deleting thisspecific annotation.|No|A string value shorter than 450 characters|String|

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        body (RestBulkAddInsightAnnotationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkAddInsightAnnotationRequest | Unset = UNSET,
) -> Response[AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any]:
    r"""Add Code Insights annotations

     Add annotations to the given report. The request should be a JSON object mapping the string
    \"annotations\" to an array of maps containing the annotation data, as described below. See also the
    example request.

    A few things to note:- Annotations are an extension of a report, so a report must first exist in
    order to post annotations.   Annotations are posted separately from the report, and can be posted in
    bulk using this endpoint.
    - Only the annotations that are on lines changed in the unified diff will be displayed. This means
    it is  likely not all annotations posted will be displayed on the pull request  It also means that
    if the user is viewing a side-by-side diff,  commit diff or iterative review diff they will not be
    able to view the annotations.
    - A report cannot have more than 1000 annotations by default, however this property is congurable at
    an  instance level. If the request would result in more than the maximum number of annotations being
    stored  then the entire request is rejected and no new annotations are stored.
    - There is no de-duplication of annotations on Bitbucket so be sure that reruns of builds will first
    delete the report and annotations before creating them.

    # Annotation parameters

    |Parameter|Description|Required?|Restrictions|Type|
    |--- |--- |--- |--- |--- |
    |path|The path of the file on which this annotation should be placed. This is the path of the
    filerelative to the git repository. If no path is provided, then it will appear in the overview
    modalon all pull requests where the tip of the branch is the given commit, regardless of which files
    weremodified.|No||String|
    |line|The line number that the annotation should belong to. If no line number is provided, then it
    willdefault to 0 and in a pull request it will appear at the top of the file specified by the path
    field.|No|Non-negative integer|Integer|
    |message|The message to display to users|Yes|The maximum length accepted is 2000 characters, however
    the user interface may truncate this valuefor display purposes. We recommend that the message is
    short and succinct, with further detailsavailable to the user if needed on the page linked to by the
    the annotation link.|String|
    |severity|The severity of the annotation|Yes|One of: LOW, MEDIUM, HIGH|String|
    |link|An http or https URL representing the location of the annotation in the external
    tool|No||String|
    |type|The type of annotation posted|No|One of: VULNERABILITY, CODE_SMELL, BUG|String|
    |externalId|If the caller requires a link to get or modify this annotation, then an ID must be
    provided. It isnot used or required by Bitbucket, but only by the annotation creator for updating or
    deleting thisspecific annotation.|No|A string value shorter than 450 characters|String|

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        body (RestBulkAddInsightAnnotationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        commit_id=commit_id,
        key=key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    commit_id: str,
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestBulkAddInsightAnnotationRequest | Unset = UNSET,
) -> AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any | None:
    r"""Add Code Insights annotations

     Add annotations to the given report. The request should be a JSON object mapping the string
    \"annotations\" to an array of maps containing the annotation data, as described below. See also the
    example request.

    A few things to note:- Annotations are an extension of a report, so a report must first exist in
    order to post annotations.   Annotations are posted separately from the report, and can be posted in
    bulk using this endpoint.
    - Only the annotations that are on lines changed in the unified diff will be displayed. This means
    it is  likely not all annotations posted will be displayed on the pull request  It also means that
    if the user is viewing a side-by-side diff,  commit diff or iterative review diff they will not be
    able to view the annotations.
    - A report cannot have more than 1000 annotations by default, however this property is congurable at
    an  instance level. If the request would result in more than the maximum number of annotations being
    stored  then the entire request is rejected and no new annotations are stored.
    - There is no de-duplication of annotations on Bitbucket so be sure that reruns of builds will first
    delete the report and annotations before creating them.

    # Annotation parameters

    |Parameter|Description|Required?|Restrictions|Type|
    |--- |--- |--- |--- |--- |
    |path|The path of the file on which this annotation should be placed. This is the path of the
    filerelative to the git repository. If no path is provided, then it will appear in the overview
    modalon all pull requests where the tip of the branch is the given commit, regardless of which files
    weremodified.|No||String|
    |line|The line number that the annotation should belong to. If no line number is provided, then it
    willdefault to 0 and in a pull request it will appear at the top of the file specified by the path
    field.|No|Non-negative integer|Integer|
    |message|The message to display to users|Yes|The maximum length accepted is 2000 characters, however
    the user interface may truncate this valuefor display purposes. We recommend that the message is
    short and succinct, with further detailsavailable to the user if needed on the page linked to by the
    the annotation link.|String|
    |severity|The severity of the annotation|Yes|One of: LOW, MEDIUM, HIGH|String|
    |link|An http or https URL representing the location of the annotation in the external
    tool|No||String|
    |type|The type of annotation posted|No|One of: VULNERABILITY, CODE_SMELL, BUG|String|
    |externalId|If the caller requires a link to get or modify this annotation, then an ID must be
    provided. It isnot used or required by Bitbucket, but only by the annotation creator for updating or
    deleting thisspecific annotation.|No|A string value shorter than 450 characters|String|

    Args:
        project_key (str):
        repository_slug (str):
        commit_id (str):
        key (str):
        body (RestBulkAddInsightAnnotationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddAnnotationsResponse401 | AddAnnotationsResponse404 | Any
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            commit_id=commit_id,
            key=key,
            client=client,
            body=body,
        )
    ).parsed
