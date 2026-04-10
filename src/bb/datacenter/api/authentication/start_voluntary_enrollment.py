from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.elevation_method_rest_dto import ElevationMethodRestDTO
from ...models.error_entity import ErrorEntity
from ...models.totp_user_enrollment_dto import TotpUserEnrollmentDTO
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tsv/latest/totp/start-voluntary-enrollment",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO | None:
    if response.status_code == 200:
        response_200 = TotpUserEnrollmentDTO.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEntity.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ElevationMethodRestDTO.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]:
    """Start voluntary enrollment in 2SV

     Start voluntary enrollment in two-step verification by creating a conversation.

    There are two ways to enroll in two-step verification: voluntary and enforced. Enrollment is a two-
    step process. First, the user starts the enrollment process via <code>/start-voluntary-
    enrollment</code> or <code>/start-enforced-enrollment</code>. Second and final step is to complete
    the enrollment via <code>/complete-voluntary-enrollment</code> or <code>/complete-enforced-
    enrollment</code>. In the case of enforced enrollment, the conversation is started at the time of
    login via <code>/authenticate</code>.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO | None:
    """Start voluntary enrollment in 2SV

     Start voluntary enrollment in two-step verification by creating a conversation.

    There are two ways to enroll in two-step verification: voluntary and enforced. Enrollment is a two-
    step process. First, the user starts the enrollment process via <code>/start-voluntary-
    enrollment</code> or <code>/start-enforced-enrollment</code>. Second and final step is to complete
    the enrollment via <code>/complete-voluntary-enrollment</code> or <code>/complete-enforced-
    enrollment</code>. In the case of enforced enrollment, the conversation is started at the time of
    login via <code>/authenticate</code>.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]:
    """Start voluntary enrollment in 2SV

     Start voluntary enrollment in two-step verification by creating a conversation.

    There are two ways to enroll in two-step verification: voluntary and enforced. Enrollment is a two-
    step process. First, the user starts the enrollment process via <code>/start-voluntary-
    enrollment</code> or <code>/start-enforced-enrollment</code>. Second and final step is to complete
    the enrollment via <code>/complete-voluntary-enrollment</code> or <code>/complete-enforced-
    enrollment</code>. In the case of enforced enrollment, the conversation is started at the time of
    login via <code>/authenticate</code>.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO | None:
    """Start voluntary enrollment in 2SV

     Start voluntary enrollment in two-step verification by creating a conversation.

    There are two ways to enroll in two-step verification: voluntary and enforced. Enrollment is a two-
    step process. First, the user starts the enrollment process via <code>/start-voluntary-
    enrollment</code> or <code>/start-enforced-enrollment</code>. Second and final step is to complete
    the enrollment via <code>/complete-voluntary-enrollment</code> or <code>/complete-enforced-
    enrollment</code>. In the case of enforced enrollment, the conversation is started at the time of
    login via <code>/authenticate</code>.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ElevationMethodRestDTO | ErrorEntity | TotpUserEnrollmentDTO
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
