from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_error_data import ErrorErrorData


T = TypeVar("T", bound="ErrorError")


@_attrs_define
class ErrorError:
    message: str
    detail: str | Unset = UNSET
    data: ErrorErrorData | Unset = UNSET
    """ Optional structured data that is endpoint-specific. """

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        detail = self.detail

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_error_data import ErrorErrorData

        d = dict(src_dict)
        message = d.pop("message")

        detail = d.pop("detail", UNSET)

        _data = d.pop("data", UNSET)
        data: ErrorErrorData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ErrorErrorData.from_dict(_data)

        error_error = cls(
            message=message,
            detail=detail,
            data=data,
        )

        return error_error
