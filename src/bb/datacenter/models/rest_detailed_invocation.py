from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_detailed_invocation_event_scope import RestDetailedInvocationEventScope
    from ..models.rest_detailed_invocation_request import RestDetailedInvocationRequest
    from ..models.rest_detailed_invocation_result import RestDetailedInvocationResult


T = TypeVar("T", bound="RestDetailedInvocation")


@_attrs_define
class RestDetailedInvocation:
    duration: int | Unset = UNSET
    event: str | Unset = UNSET
    event_scope: RestDetailedInvocationEventScope | Unset = UNSET
    finish: int | Unset = UNSET
    id: int | Unset = UNSET
    request: RestDetailedInvocationRequest | Unset = UNSET
    result: RestDetailedInvocationResult | Unset = UNSET
    start: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        event = self.event

        event_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_scope, Unset):
            event_scope = self.event_scope.to_dict()

        finish = self.finish

        id = self.id

        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if event is not UNSET:
            field_dict["event"] = event
        if event_scope is not UNSET:
            field_dict["eventScope"] = event_scope
        if finish is not UNSET:
            field_dict["finish"] = finish
        if id is not UNSET:
            field_dict["id"] = id
        if request is not UNSET:
            field_dict["request"] = request
        if result is not UNSET:
            field_dict["result"] = result
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_detailed_invocation_event_scope import RestDetailedInvocationEventScope
        from ..models.rest_detailed_invocation_request import RestDetailedInvocationRequest
        from ..models.rest_detailed_invocation_result import RestDetailedInvocationResult

        d = dict(src_dict)
        duration = d.pop("duration", UNSET)

        event = d.pop("event", UNSET)

        _event_scope = d.pop("eventScope", UNSET)
        event_scope: RestDetailedInvocationEventScope | Unset
        if isinstance(_event_scope, Unset):
            event_scope = UNSET
        else:
            event_scope = RestDetailedInvocationEventScope.from_dict(_event_scope)

        finish = d.pop("finish", UNSET)

        id = d.pop("id", UNSET)

        _request = d.pop("request", UNSET)
        request: RestDetailedInvocationRequest | Unset
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = RestDetailedInvocationRequest.from_dict(_request)

        _result = d.pop("result", UNSET)
        result: RestDetailedInvocationResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = RestDetailedInvocationResult.from_dict(_result)

        start = d.pop("start", UNSET)

        rest_detailed_invocation = cls(
            duration=duration,
            event=event,
            event_scope=event_scope,
            finish=finish,
            id=id,
            request=request,
            result=result,
            start=start,
        )

        rest_detailed_invocation.additional_properties = d
        return rest_detailed_invocation

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
