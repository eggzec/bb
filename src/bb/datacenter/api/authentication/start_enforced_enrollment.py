from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conversation_dto import ConversationDTO
from ...models.error_entity import ErrorEntity
from ...models.totp_user_enrollment_dto import TotpUserEnrollmentDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ConversationDTO | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tsv/latest/totp/start-enforced-enrollment",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEntity | TotpUserEnrollmentDTO | None:
    if response.status_code == 200:
        response_200 = TotpUserEnrollmentDTO.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEntity.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEntity | TotpUserEnrollmentDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConversationDTO | Unset = UNSET,
) -> Response[ErrorEntity | TotpUserEnrollmentDTO]:
    """Start enforced enrollment in 2SV

     Start or resume enforced enrollment in two-step verification by returning the conversation details.

    There are two ways to enroll in two-step verification: voluntary and enforced. Enrollment is a two-
    step process. First, the user starts the enrollment process via <code>/start-voluntary-
    enrollment</code> or <code>/start-enforced-enrollment</code>. Second and final step is to complete
    the enrollment via <code>/complete-voluntary-enrollment</code> or <code>/complete-enforced-
    enrollment</code>. In the case of enforced enrollment, the conversation is started at the time of
    login via <code>/authenticate</code>.

    Args:
        body (ConversationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEntity | TotpUserEnrollmentDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ConversationDTO | Unset = UNSET,
) -> ErrorEntity | TotpUserEnrollmentDTO | None:
    """Start enforced enrollment in 2SV

     Start or resume enforced enrollment in two-step verification by returning the conversation details.

    There are two ways to enroll in two-step verification: voluntary and enforced. Enrollment is a two-
    step process. First, the user starts the enrollment process via <code>/start-voluntary-
    enrollment</code> or <code>/start-enforced-enrollment</code>. Second and final step is to complete
    the enrollment via <code>/complete-voluntary-enrollment</code> or <code>/complete-enforced-
    enrollment</code>. In the case of enforced enrollment, the conversation is started at the time of
    login via <code>/authenticate</code>.

    Args:
        body (ConversationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEntity | TotpUserEnrollmentDTO
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConversationDTO | Unset = UNSET,
) -> Response[ErrorEntity | TotpUserEnrollmentDTO]:
    """Start enforced enrollment in 2SV

     Start or resume enforced enrollment in two-step verification by returning the conversation details.

    There are two ways to enroll in two-step verification: voluntary and enforced. Enrollment is a two-
    step process. First, the user starts the enrollment process via <code>/start-voluntary-
    enrollment</code> or <code>/start-enforced-enrollment</code>. Second and final step is to complete
    the enrollment via <code>/complete-voluntary-enrollment</code> or <code>/complete-enforced-
    enrollment</code>. In the case of enforced enrollment, the conversation is started at the time of
    login via <code>/authenticate</code>.

    Args:
        body (ConversationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEntity | TotpUserEnrollmentDTO]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConversationDTO | Unset = UNSET,
) -> ErrorEntity | TotpUserEnrollmentDTO | None:
    """Start enforced enrollment in 2SV

     Start or resume enforced enrollment in two-step verification by returning the conversation details.

    There are two ways to enroll in two-step verification: voluntary and enforced. Enrollment is a two-
    step process. First, the user starts the enrollment process via <code>/start-voluntary-
    enrollment</code> or <code>/start-enforced-enrollment</code>. Second and final step is to complete
    the enrollment via <code>/complete-voluntary-enrollment</code> or <code>/complete-enforced-
    enrollment</code>. In the case of enforced enrollment, the conversation is started at the time of
    login via <code>/authenticate</code>.

    Args:
        body (ConversationDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEntity | TotpUserEnrollmentDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
