from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subject_types_repository import SubjectTypesRepository
    from ..models.subject_types_workspace import SubjectTypesWorkspace


T = TypeVar("T", bound="SubjectTypes")


@_attrs_define
class SubjectTypes:
    """The mapping of resource/subject types pointing to their individual event types."""

    repository: SubjectTypesRepository | Unset = UNSET
    workspace: SubjectTypesWorkspace | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository: dict[str, Any] | Unset = UNSET
        if not isinstance(self.repository, Unset):
            repository = self.repository.to_dict()

        workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository is not UNSET:
            field_dict["repository"] = repository
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subject_types_repository import SubjectTypesRepository
        from ..models.subject_types_workspace import SubjectTypesWorkspace

        d = dict(src_dict)
        _repository = d.pop("repository", UNSET)
        repository: SubjectTypesRepository | Unset
        if isinstance(_repository, Unset):
            repository = UNSET
        else:
            repository = SubjectTypesRepository.from_dict(_repository)

        _workspace = d.pop("workspace", UNSET)
        workspace: SubjectTypesWorkspace | Unset
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = SubjectTypesWorkspace.from_dict(_workspace)

        subject_types = cls(
            repository=repository,
            workspace=workspace,
        )

        return subject_types
