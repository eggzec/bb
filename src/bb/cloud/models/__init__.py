"""Contains all the data models used in inputs/outputs"""

from .account import Account
from .account_links import AccountLinks
from .app_user import AppUser
from .application_property import ApplicationProperty
from .application_property_attributes_item import ApplicationPropertyAttributesItem
from .author import Author
from .base_commit import BaseCommit
from .base_commit_summary import BaseCommitSummary
from .base_commit_summary_markup import BaseCommitSummaryMarkup
from .bitbucket_apps_permissions_serializers_project_permission_update_schema import (
    BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema,
)
from .bitbucket_apps_permissions_serializers_project_permission_update_schema_permission import (
    BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchemaPermission,
)
from .bitbucket_apps_permissions_serializers_repo_permission_update_schema import (
    BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
)
from .bitbucket_apps_permissions_serializers_repo_permission_update_schema_permission import (
    BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchemaPermission,
)
from .branch import Branch
from .branch_merge_strategies_item import BranchMergeStrategiesItem
from .branching_model import BranchingModel
from .branching_model_branch_types_item import BranchingModelBranchTypesItem
from .branching_model_branch_types_item_kind import BranchingModelBranchTypesItemKind
from .branching_model_development import BranchingModelDevelopment
from .branching_model_production import BranchingModelProduction
from .branching_model_settings import BranchingModelSettings
from .branching_model_settings_branch_types_item import BranchingModelSettingsBranchTypesItem
from .branching_model_settings_branch_types_item_kind import BranchingModelSettingsBranchTypesItemKind
from .branching_model_settings_development import BranchingModelSettingsDevelopment
from .branching_model_settings_links import BranchingModelSettingsLinks
from .branching_model_settings_production import BranchingModelSettingsProduction
from .branchrestriction import Branchrestriction
from .branchrestriction_branch_match_kind import BranchrestrictionBranchMatchKind
from .branchrestriction_branch_type import BranchrestrictionBranchType
from .branchrestriction_kind import BranchrestrictionKind
from .branchrestriction_links import BranchrestrictionLinks
from .comment import Comment
from .comment_content import CommentContent
from .comment_content_markup import CommentContentMarkup
from .comment_inline import CommentInline
from .comment_links import CommentLinks
from .comment_resolution import CommentResolution
from .commit import Commit
from .commit_comment import CommitComment
from .commit_file import CommitFile
from .commit_file_attributes import CommitFileAttributes
from .commitstatus import Commitstatus
from .commitstatus_links import CommitstatusLinks
from .commitstatus_state import CommitstatusState
from .committer import Committer
from .component import Component
from .component_links import ComponentLinks
from .default_reviewer_and_type import DefaultReviewerAndType
from .deploy_key import DeployKey
from .deploy_key_links import DeployKeyLinks
from .deployment import Deployment
from .deployment_environment import DeploymentEnvironment
from .deployment_release import DeploymentRelease
from .deployment_state import DeploymentState
from .deployment_state_completed import DeploymentStateCompleted
from .deployment_state_completed_name import DeploymentStateCompletedName
from .deployment_state_completed_status import DeploymentStateCompletedStatus
from .deployment_state_completed_status_failed import DeploymentStateCompletedStatusFailed
from .deployment_state_completed_status_failed_name import DeploymentStateCompletedStatusFailedName
from .deployment_state_completed_status_stopped import DeploymentStateCompletedStatusStopped
from .deployment_state_completed_status_stopped_name import DeploymentStateCompletedStatusStoppedName
from .deployment_state_completed_status_successful import DeploymentStateCompletedStatusSuccessful
from .deployment_state_completed_status_successful_name import DeploymentStateCompletedStatusSuccessfulName
from .deployment_state_in_progress import DeploymentStateInProgress
from .deployment_state_in_progress_name import DeploymentStateInProgressName
from .deployment_state_undeployed import DeploymentStateUndeployed
from .deployment_state_undeployed_name import DeploymentStateUndeployedName
from .deployment_variable import DeploymentVariable
from .diff_stat import DiffStat
from .diff_stat_status import DiffStatStatus
from .effective_repo_branching_model import EffectiveRepoBranchingModel
from .effective_repo_branching_model_branch_types_item import EffectiveRepoBranchingModelBranchTypesItem
from .effective_repo_branching_model_branch_types_item_kind import EffectiveRepoBranchingModelBranchTypesItemKind
from .effective_repo_branching_model_development import EffectiveRepoBranchingModelDevelopment
from .effective_repo_branching_model_production import EffectiveRepoBranchingModelProduction
from .error import Error
from .error_error import ErrorError
from .error_error_data import ErrorErrorData
from .export_options import ExportOptions
from .get_hook_events_subject_type_subject_type import GetHookEventsSubjectTypeSubjectType
from .get_pipelines_for_repository_sort import GetPipelinesForRepositorySort
from .get_pipelines_for_repository_status import GetPipelinesForRepositoryStatus
from .get_pipelines_for_repository_target_ref_type import GetPipelinesForRepositoryTargetRefType
from .get_pipelines_for_repository_target_selector_type import GetPipelinesForRepositoryTargetSelectorType
from .get_pipelines_for_repository_trigger_type import GetPipelinesForRepositoryTriggerType
from .get_repositories_workspace_repo_slug_forks_role import GetRepositoriesWorkspaceRepoSlugForksRole
from .get_repositories_workspace_repo_slug_pullrequests_state import GetRepositoriesWorkspaceRepoSlugPullrequestsState
from .get_repositories_workspace_repo_slug_src_commit_path_format import (
    GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat,
)
from .get_repositories_workspace_repo_slug_src_format import GetRepositoriesWorkspaceRepoSlugSrcFormat
from .get_repositories_workspace_role import GetRepositoriesWorkspaceRole
from .get_snippets_role import GetSnippetsRole
from .get_snippets_workspace_role import GetSnippetsWorkspaceRole
from .get_workspaces_role import GetWorkspacesRole
from .get_workspaces_workspace_pullrequests_selected_user_state import (
    GetWorkspacesWorkspacePullrequestsSelectedUserState,
)
from .gpg_account_key import GPGAccountKey
from .gpg_account_key_links import GPGAccountKeyLinks
from .group import Group
from .group_links import GroupLinks
from .hook_event import HookEvent
from .hook_event_event import HookEventEvent
from .issue import Issue
from .issue_attachment import IssueAttachment
from .issue_attachment_links import IssueAttachmentLinks
from .issue_change import IssueChange
from .issue_change_changes import IssueChangeChanges
from .issue_change_changes_assignee import IssueChangeChangesAssignee
from .issue_change_changes_component import IssueChangeChangesComponent
from .issue_change_changes_content import IssueChangeChangesContent
from .issue_change_changes_kind import IssueChangeChangesKind
from .issue_change_changes_milestone import IssueChangeChangesMilestone
from .issue_change_changes_priority import IssueChangeChangesPriority
from .issue_change_changes_state import IssueChangeChangesState
from .issue_change_changes_title import IssueChangeChangesTitle
from .issue_change_changes_version import IssueChangeChangesVersion
from .issue_change_links import IssueChangeLinks
from .issue_change_message import IssueChangeMessage
from .issue_change_message_markup import IssueChangeMessageMarkup
from .issue_comment import IssueComment
from .issue_content import IssueContent
from .issue_content_markup import IssueContentMarkup
from .issue_job_status import IssueJobStatus
from .issue_job_status_status import IssueJobStatusStatus
from .issue_kind import IssueKind
from .issue_links import IssueLinks
from .issue_priority import IssuePriority
from .issue_state import IssueState
from .link import Link
from .milestone import Milestone
from .milestone_links import MilestoneLinks
from .object_ import Object
from .page import Page
from .paginated_accounts import PaginatedAccounts
from .paginated_annotations import PaginatedAnnotations
from .paginated_branch_restrictions import PaginatedBranchRestrictions
from .paginated_branches import PaginatedBranches
from .paginated_commit_comments import PaginatedCommitComments
from .paginated_commit_statuses import PaginatedCommitStatuses
from .paginated_components import PaginatedComponents
from .paginated_default_reviewer_and_type import PaginatedDefaultReviewerAndType
from .paginated_deploy_keys import PaginatedDeployKeys
from .paginated_deployment_environments import PaginatedDeploymentEnvironments
from .paginated_deployment_variables import PaginatedDeploymentVariables
from .paginated_deployments import PaginatedDeployments
from .paginated_diff_stat import PaginatedDiffStat
from .paginated_files import PaginatedFiles
from .paginated_gpg_user_keys import PaginatedGPGUserKeys
from .paginated_hook_events import PaginatedHookEvents
from .paginated_issue_attachment import PaginatedIssueAttachment
from .paginated_issue_comments import PaginatedIssueComments
from .paginated_issues import PaginatedIssues
from .paginated_log_entries import PaginatedLogEntries
from .paginated_milestones import PaginatedMilestones
from .paginated_pipeline_cache import PaginatedPipelineCache
from .paginated_pipeline_known_hosts import PaginatedPipelineKnownHosts
from .paginated_pipeline_schedule import PaginatedPipelineSchedule
from .paginated_pipeline_schedule_executions import PaginatedPipelineScheduleExecutions
from .paginated_pipeline_steps import PaginatedPipelineSteps
from .paginated_pipeline_variables import PaginatedPipelineVariables
from .paginated_pipelines import PaginatedPipelines
from .paginated_project_deploy_keys import PaginatedProjectDeployKeys
from .paginated_project_group_permissions import PaginatedProjectGroupPermissions
from .paginated_project_user_permissions import PaginatedProjectUserPermissions
from .paginated_projects import PaginatedProjects
from .paginated_pull_request_comments import PaginatedPullRequestComments
from .paginated_pull_requests import PaginatedPullRequests
from .paginated_refs import PaginatedRefs
from .paginated_reports import PaginatedReports
from .paginated_repositories import PaginatedRepositories
from .paginated_repository_group_permissions import PaginatedRepositoryGroupPermissions
from .paginated_repository_permissions import PaginatedRepositoryPermissions
from .paginated_repository_user_permissions import PaginatedRepositoryUserPermissions
from .paginated_runners import PaginatedRunners
from .paginated_snippet_comments import PaginatedSnippetComments
from .paginated_snippet_commits import PaginatedSnippetCommits
from .paginated_snippets import PaginatedSnippets
from .paginated_ssh_user_keys import PaginatedSSHUserKeys
from .paginated_tags import PaginatedTags
from .paginated_tasks import PaginatedTasks
from .paginated_tree_entry import PaginatedTreeEntry
from .paginated_versions import PaginatedVersions
from .paginated_webhook_subscriptions import PaginatedWebhookSubscriptions
from .paginated_workspace_memberships import PaginatedWorkspaceMemberships
from .paginated_workspace_permissions import PaginatedWorkspacePermissions
from .paginated_workspaces import PaginatedWorkspaces
from .participant import Participant
from .participant_role import ParticipantRole
from .participant_state_type_1 import ParticipantStateType1
from .pipeline import Pipeline
from .pipeline_build_number import PipelineBuildNumber
from .pipeline_cache import PipelineCache
from .pipeline_cache_content_uri import PipelineCacheContentURI
from .pipeline_command import PipelineCommand
from .pipeline_commit_target import PipelineCommitTarget
from .pipeline_configuration_source import PipelineConfigurationSource
from .pipeline_error import PipelineError
from .pipeline_image import PipelineImage
from .pipeline_known_host import PipelineKnownHost
from .pipeline_ref_target import PipelineRefTarget
from .pipeline_ref_target_ref_type import PipelineRefTargetRefType
from .pipeline_runner import PipelineRunner
from .pipeline_runner_oauth_client import PipelineRunnerOauthClient
from .pipeline_runner_state import PipelineRunnerState
from .pipeline_runner_state_status import PipelineRunnerStateStatus
from .pipeline_runner_version import PipelineRunnerVersion
from .pipeline_schedule import PipelineSchedule
from .pipeline_schedule_execution import PipelineScheduleExecution
from .pipeline_schedule_execution_errored import PipelineScheduleExecutionErrored
from .pipeline_schedule_execution_executed import PipelineScheduleExecutionExecuted
from .pipeline_schedule_post_request_body import PipelineSchedulePostRequestBody
from .pipeline_schedule_post_request_body_target import PipelineSchedulePostRequestBodyTarget
from .pipeline_schedule_post_request_body_target_ref_type import PipelineSchedulePostRequestBodyTargetRefType
from .pipeline_schedule_put_request_body import PipelineSchedulePutRequestBody
from .pipeline_selector import PipelineSelector
from .pipeline_selector_type import PipelineSelectorType
from .pipeline_ssh_key_pair import PipelineSshKeyPair
from .pipeline_ssh_public_key import PipelineSshPublicKey
from .pipeline_state import PipelineState
from .pipeline_state_completed import PipelineStateCompleted
from .pipeline_state_completed_error import PipelineStateCompletedError
from .pipeline_state_completed_error_name import PipelineStateCompletedErrorName
from .pipeline_state_completed_expired import PipelineStateCompletedExpired
from .pipeline_state_completed_expired_name import PipelineStateCompletedExpiredName
from .pipeline_state_completed_failed import PipelineStateCompletedFailed
from .pipeline_state_completed_failed_name import PipelineStateCompletedFailedName
from .pipeline_state_completed_name import PipelineStateCompletedName
from .pipeline_state_completed_result import PipelineStateCompletedResult
from .pipeline_state_completed_stopped import PipelineStateCompletedStopped
from .pipeline_state_completed_stopped_name import PipelineStateCompletedStoppedName
from .pipeline_state_completed_successful import PipelineStateCompletedSuccessful
from .pipeline_state_completed_successful_name import PipelineStateCompletedSuccessfulName
from .pipeline_state_in_progress import PipelineStateInProgress
from .pipeline_state_in_progress_name import PipelineStateInProgressName
from .pipeline_state_in_progress_paused import PipelineStateInProgressPaused
from .pipeline_state_in_progress_paused_name import PipelineStateInProgressPausedName
from .pipeline_state_in_progress_running import PipelineStateInProgressRunning
from .pipeline_state_in_progress_running_name import PipelineStateInProgressRunningName
from .pipeline_state_in_progress_stage import PipelineStateInProgressStage
from .pipeline_state_pending import PipelineStatePending
from .pipeline_state_pending_name import PipelineStatePendingName
from .pipeline_step import PipelineStep
from .pipeline_step_error import PipelineStepError
from .pipeline_step_state import PipelineStepState
from .pipeline_step_state_completed import PipelineStepStateCompleted
from .pipeline_step_state_completed_error import PipelineStepStateCompletedError
from .pipeline_step_state_completed_error_name import PipelineStepStateCompletedErrorName
from .pipeline_step_state_completed_expired import PipelineStepStateCompletedExpired
from .pipeline_step_state_completed_expired_name import PipelineStepStateCompletedExpiredName
from .pipeline_step_state_completed_failed import PipelineStepStateCompletedFailed
from .pipeline_step_state_completed_failed_name import PipelineStepStateCompletedFailedName
from .pipeline_step_state_completed_name import PipelineStepStateCompletedName
from .pipeline_step_state_completed_not_run import PipelineStepStateCompletedNotRun
from .pipeline_step_state_completed_not_run_name import PipelineStepStateCompletedNotRunName
from .pipeline_step_state_completed_result import PipelineStepStateCompletedResult
from .pipeline_step_state_completed_stopped import PipelineStepStateCompletedStopped
from .pipeline_step_state_completed_stopped_name import PipelineStepStateCompletedStoppedName
from .pipeline_step_state_completed_successful import PipelineStepStateCompletedSuccessful
from .pipeline_step_state_completed_successful_name import PipelineStepStateCompletedSuccessfulName
from .pipeline_step_state_in_progress import PipelineStepStateInProgress
from .pipeline_step_state_in_progress_name import PipelineStepStateInProgressName
from .pipeline_step_state_pending import PipelineStepStatePending
from .pipeline_step_state_pending_name import PipelineStepStatePendingName
from .pipeline_step_state_ready import PipelineStepStateReady
from .pipeline_step_state_ready_name import PipelineStepStateReadyName
from .pipeline_target import PipelineTarget
from .pipeline_trigger import PipelineTrigger
from .pipeline_trigger_manual import PipelineTriggerManual
from .pipeline_trigger_push import PipelineTriggerPush
from .pipeline_variable import PipelineVariable
from .pipelines_config import PipelinesConfig
from .pipelines_links_section_href import PipelinesLinksSectionHref
from .pipelines_pipeline_links import PipelinesPipelineLinks
from .project import Project
from .project_branching_model import ProjectBranchingModel
from .project_branching_model_branch_types_item import ProjectBranchingModelBranchTypesItem
from .project_branching_model_branch_types_item_kind import ProjectBranchingModelBranchTypesItemKind
from .project_branching_model_development import ProjectBranchingModelDevelopment
from .project_branching_model_production import ProjectBranchingModelProduction
from .project_deploy_key import ProjectDeployKey
from .project_deploy_key_links import ProjectDeployKeyLinks
from .project_group_permission import ProjectGroupPermission
from .project_group_permission_links import ProjectGroupPermissionLinks
from .project_group_permission_permission import ProjectGroupPermissionPermission
from .project_links import ProjectLinks
from .project_user_permission import ProjectUserPermission
from .project_user_permission_links import ProjectUserPermissionLinks
from .project_user_permission_permission import ProjectUserPermissionPermission
from .pull_request_endpoint import PullRequestEndpoint
from .pull_request_endpoint_pull_request_branch import PullRequestEndpointPullRequestBranch
from .pull_request_endpoint_pull_request_branch_merge_strategies_item import (
    PullRequestEndpointPullRequestBranchMergeStrategiesItem,
)
from .pull_request_endpoint_pull_request_commit import PullRequestEndpointPullRequestCommit
from .pull_request_merge_parameters import PullRequestMergeParameters
from .pull_request_merge_parameters_merge_strategy import PullRequestMergeParametersMergeStrategy
from .pull_request_task_create import PullRequestTaskCreate
from .pull_request_task_create_task_raw_content import PullRequestTaskCreateTaskRawContent
from .pull_request_task_update import PullRequestTaskUpdate
from .pull_request_task_update_state import PullRequestTaskUpdateState
from .pull_request_task_update_task_raw_content import PullRequestTaskUpdateTaskRawContent
from .pullrequest import Pullrequest
from .pullrequest_comment import PullrequestComment
from .pullrequest_comment_task import PullrequestCommentTask
from .pullrequest_links import PullrequestLinks
from .pullrequest_pull_request_commit import PullrequestPullRequestCommit
from .pullrequest_rendered_pull_request_markup import PullrequestRenderedPullRequestMarkup
from .pullrequest_rendered_pull_request_markup_description import PullrequestRenderedPullRequestMarkupDescription
from .pullrequest_rendered_pull_request_markup_description_markup import (
    PullrequestRenderedPullRequestMarkupDescriptionMarkup,
)
from .pullrequest_rendered_pull_request_markup_reason import PullrequestRenderedPullRequestMarkupReason
from .pullrequest_rendered_pull_request_markup_reason_markup import PullrequestRenderedPullRequestMarkupReasonMarkup
from .pullrequest_rendered_pull_request_markup_title import PullrequestRenderedPullRequestMarkupTitle
from .pullrequest_rendered_pull_request_markup_title_markup import PullrequestRenderedPullRequestMarkupTitleMarkup
from .pullrequest_state import PullrequestState
from .pullrequest_summary import PullrequestSummary
from .pullrequest_summary_markup import PullrequestSummaryMarkup
from .pullrequest_task import PullrequestTask
from .pullrequest_task_links import PullrequestTaskLinks
from .ref import Ref
from .ref_links import RefLinks
from .report import Report
from .report_annotation import ReportAnnotation
from .report_annotation_annotation_type import ReportAnnotationAnnotationType
from .report_annotation_result import ReportAnnotationResult
from .report_annotation_severity import ReportAnnotationSeverity
from .report_data import ReportData
from .report_data_type import ReportDataType
from .report_data_value import ReportDataValue
from .report_report_type import ReportReportType
from .report_result import ReportResult
from .repository import Repository
from .repository_fork_policy import RepositoryForkPolicy
from .repository_group_permission import RepositoryGroupPermission
from .repository_group_permission_links import RepositoryGroupPermissionLinks
from .repository_group_permission_permission import RepositoryGroupPermissionPermission
from .repository_inheritance_state import RepositoryInheritanceState
from .repository_inheritance_state_override_settings import RepositoryInheritanceStateOverrideSettings
from .repository_links import RepositoryLinks
from .repository_permission import RepositoryPermission
from .repository_permission_permission import RepositoryPermissionPermission
from .repository_scm import RepositoryScm
from .repository_user_permission import RepositoryUserPermission
from .repository_user_permission_links import RepositoryUserPermissionLinks
from .repository_user_permission_permission import RepositoryUserPermissionPermission
from .search_code_search_result import SearchCodeSearchResult
from .search_content_match import SearchContentMatch
from .search_line import SearchLine
from .search_result_page import SearchResultPage
from .search_segment import SearchSegment
from .snippet import Snippet
from .snippet_comment import SnippetComment
from .snippet_comment_links import SnippetCommentLinks
from .snippet_commit import SnippetCommit
from .snippet_commit_links import SnippetCommitLinks
from .snippet_scm import SnippetScm
from .ssh_account_key import SshAccountKey
from .ssh_key import SshKey
from .ssh_key_links import SshKeyLinks
from .subject_types import SubjectTypes
from .subject_types_repository import SubjectTypesRepository
from .subject_types_workspace import SubjectTypesWorkspace
from .tag import Tag
from .task import Task
from .task_content import TaskContent
from .task_content_markup import TaskContentMarkup
from .task_state import TaskState
from .team import Team
from .team_links import TeamLinks
from .tree_entry import TreeEntry
from .user import User
from .user_links import UserLinks
from .version import Version
from .version_links import VersionLinks
from .webhook_subscription import WebhookSubscription
from .webhook_subscription_events_item import WebhookSubscriptionEventsItem
from .webhook_subscription_subject_type import WebhookSubscriptionSubjectType
from .workspace import Workspace
from .workspace_access import WorkspaceAccess
from .workspace_base import WorkspaceBase
from .workspace_base_links import WorkspaceBaseLinks
from .workspace_forking_mode import WorkspaceForkingMode
from .workspace_links import WorkspaceLinks
from .workspace_membership import WorkspaceMembership
from .workspace_membership_links import WorkspaceMembershipLinks

__all__ = (
    "Account",
    "AccountLinks",
    "ApplicationProperty",
    "ApplicationPropertyAttributesItem",
    "AppUser",
    "Author",
    "BaseCommit",
    "BaseCommitSummary",
    "BaseCommitSummaryMarkup",
    "BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema",
    "BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchemaPermission",
    "BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema",
    "BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchemaPermission",
    "Branch",
    "BranchingModel",
    "BranchingModelBranchTypesItem",
    "BranchingModelBranchTypesItemKind",
    "BranchingModelDevelopment",
    "BranchingModelProduction",
    "BranchingModelSettings",
    "BranchingModelSettingsBranchTypesItem",
    "BranchingModelSettingsBranchTypesItemKind",
    "BranchingModelSettingsDevelopment",
    "BranchingModelSettingsLinks",
    "BranchingModelSettingsProduction",
    "BranchMergeStrategiesItem",
    "Branchrestriction",
    "BranchrestrictionBranchMatchKind",
    "BranchrestrictionBranchType",
    "BranchrestrictionKind",
    "BranchrestrictionLinks",
    "Comment",
    "CommentContent",
    "CommentContentMarkup",
    "CommentInline",
    "CommentLinks",
    "CommentResolution",
    "Commit",
    "CommitComment",
    "CommitFile",
    "CommitFileAttributes",
    "Commitstatus",
    "CommitstatusLinks",
    "CommitstatusState",
    "Committer",
    "Component",
    "ComponentLinks",
    "DefaultReviewerAndType",
    "DeployKey",
    "DeployKeyLinks",
    "Deployment",
    "DeploymentEnvironment",
    "DeploymentRelease",
    "DeploymentState",
    "DeploymentStateCompleted",
    "DeploymentStateCompletedName",
    "DeploymentStateCompletedStatus",
    "DeploymentStateCompletedStatusFailed",
    "DeploymentStateCompletedStatusFailedName",
    "DeploymentStateCompletedStatusStopped",
    "DeploymentStateCompletedStatusStoppedName",
    "DeploymentStateCompletedStatusSuccessful",
    "DeploymentStateCompletedStatusSuccessfulName",
    "DeploymentStateInProgress",
    "DeploymentStateInProgressName",
    "DeploymentStateUndeployed",
    "DeploymentStateUndeployedName",
    "DeploymentVariable",
    "DiffStat",
    "DiffStatStatus",
    "EffectiveRepoBranchingModel",
    "EffectiveRepoBranchingModelBranchTypesItem",
    "EffectiveRepoBranchingModelBranchTypesItemKind",
    "EffectiveRepoBranchingModelDevelopment",
    "EffectiveRepoBranchingModelProduction",
    "Error",
    "ErrorError",
    "ErrorErrorData",
    "ExportOptions",
    "GetHookEventsSubjectTypeSubjectType",
    "GetPipelinesForRepositorySort",
    "GetPipelinesForRepositoryStatus",
    "GetPipelinesForRepositoryTargetRefType",
    "GetPipelinesForRepositoryTargetSelectorType",
    "GetPipelinesForRepositoryTriggerType",
    "GetRepositoriesWorkspaceRepoSlugForksRole",
    "GetRepositoriesWorkspaceRepoSlugPullrequestsState",
    "GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat",
    "GetRepositoriesWorkspaceRepoSlugSrcFormat",
    "GetRepositoriesWorkspaceRole",
    "GetSnippetsRole",
    "GetSnippetsWorkspaceRole",
    "GetWorkspacesRole",
    "GetWorkspacesWorkspacePullrequestsSelectedUserState",
    "GPGAccountKey",
    "GPGAccountKeyLinks",
    "Group",
    "GroupLinks",
    "HookEvent",
    "HookEventEvent",
    "Issue",
    "IssueAttachment",
    "IssueAttachmentLinks",
    "IssueChange",
    "IssueChangeChanges",
    "IssueChangeChangesAssignee",
    "IssueChangeChangesComponent",
    "IssueChangeChangesContent",
    "IssueChangeChangesKind",
    "IssueChangeChangesMilestone",
    "IssueChangeChangesPriority",
    "IssueChangeChangesState",
    "IssueChangeChangesTitle",
    "IssueChangeChangesVersion",
    "IssueChangeLinks",
    "IssueChangeMessage",
    "IssueChangeMessageMarkup",
    "IssueComment",
    "IssueContent",
    "IssueContentMarkup",
    "IssueJobStatus",
    "IssueJobStatusStatus",
    "IssueKind",
    "IssueLinks",
    "IssuePriority",
    "IssueState",
    "Link",
    "Milestone",
    "MilestoneLinks",
    "Object",
    "Page",
    "PaginatedAccounts",
    "PaginatedAnnotations",
    "PaginatedBranches",
    "PaginatedBranchRestrictions",
    "PaginatedCommitComments",
    "PaginatedCommitStatuses",
    "PaginatedComponents",
    "PaginatedDefaultReviewerAndType",
    "PaginatedDeployKeys",
    "PaginatedDeploymentEnvironments",
    "PaginatedDeployments",
    "PaginatedDeploymentVariables",
    "PaginatedDiffStat",
    "PaginatedFiles",
    "PaginatedGPGUserKeys",
    "PaginatedHookEvents",
    "PaginatedIssueAttachment",
    "PaginatedIssueComments",
    "PaginatedIssues",
    "PaginatedLogEntries",
    "PaginatedMilestones",
    "PaginatedPipelineCache",
    "PaginatedPipelineKnownHosts",
    "PaginatedPipelines",
    "PaginatedPipelineSchedule",
    "PaginatedPipelineScheduleExecutions",
    "PaginatedPipelineSteps",
    "PaginatedPipelineVariables",
    "PaginatedProjectDeployKeys",
    "PaginatedProjectGroupPermissions",
    "PaginatedProjects",
    "PaginatedProjectUserPermissions",
    "PaginatedPullRequestComments",
    "PaginatedPullRequests",
    "PaginatedRefs",
    "PaginatedReports",
    "PaginatedRepositories",
    "PaginatedRepositoryGroupPermissions",
    "PaginatedRepositoryPermissions",
    "PaginatedRepositoryUserPermissions",
    "PaginatedRunners",
    "PaginatedSnippetComments",
    "PaginatedSnippetCommits",
    "PaginatedSnippets",
    "PaginatedSSHUserKeys",
    "PaginatedTags",
    "PaginatedTasks",
    "PaginatedTreeEntry",
    "PaginatedVersions",
    "PaginatedWebhookSubscriptions",
    "PaginatedWorkspaceMemberships",
    "PaginatedWorkspacePermissions",
    "PaginatedWorkspaces",
    "Participant",
    "ParticipantRole",
    "ParticipantStateType1",
    "Pipeline",
    "PipelineBuildNumber",
    "PipelineCache",
    "PipelineCacheContentURI",
    "PipelineCommand",
    "PipelineCommitTarget",
    "PipelineConfigurationSource",
    "PipelineError",
    "PipelineImage",
    "PipelineKnownHost",
    "PipelineRefTarget",
    "PipelineRefTargetRefType",
    "PipelineRunner",
    "PipelineRunnerOauthClient",
    "PipelineRunnerState",
    "PipelineRunnerStateStatus",
    "PipelineRunnerVersion",
    "PipelineSchedule",
    "PipelineScheduleExecution",
    "PipelineScheduleExecutionErrored",
    "PipelineScheduleExecutionExecuted",
    "PipelineSchedulePostRequestBody",
    "PipelineSchedulePostRequestBodyTarget",
    "PipelineSchedulePostRequestBodyTargetRefType",
    "PipelineSchedulePutRequestBody",
    "PipelinesConfig",
    "PipelineSelector",
    "PipelineSelectorType",
    "PipelinesLinksSectionHref",
    "PipelinesPipelineLinks",
    "PipelineSshKeyPair",
    "PipelineSshPublicKey",
    "PipelineState",
    "PipelineStateCompleted",
    "PipelineStateCompletedError",
    "PipelineStateCompletedErrorName",
    "PipelineStateCompletedExpired",
    "PipelineStateCompletedExpiredName",
    "PipelineStateCompletedFailed",
    "PipelineStateCompletedFailedName",
    "PipelineStateCompletedName",
    "PipelineStateCompletedResult",
    "PipelineStateCompletedStopped",
    "PipelineStateCompletedStoppedName",
    "PipelineStateCompletedSuccessful",
    "PipelineStateCompletedSuccessfulName",
    "PipelineStateInProgress",
    "PipelineStateInProgressName",
    "PipelineStateInProgressPaused",
    "PipelineStateInProgressPausedName",
    "PipelineStateInProgressRunning",
    "PipelineStateInProgressRunningName",
    "PipelineStateInProgressStage",
    "PipelineStatePending",
    "PipelineStatePendingName",
    "PipelineStep",
    "PipelineStepError",
    "PipelineStepState",
    "PipelineStepStateCompleted",
    "PipelineStepStateCompletedError",
    "PipelineStepStateCompletedErrorName",
    "PipelineStepStateCompletedExpired",
    "PipelineStepStateCompletedExpiredName",
    "PipelineStepStateCompletedFailed",
    "PipelineStepStateCompletedFailedName",
    "PipelineStepStateCompletedName",
    "PipelineStepStateCompletedNotRun",
    "PipelineStepStateCompletedNotRunName",
    "PipelineStepStateCompletedResult",
    "PipelineStepStateCompletedStopped",
    "PipelineStepStateCompletedStoppedName",
    "PipelineStepStateCompletedSuccessful",
    "PipelineStepStateCompletedSuccessfulName",
    "PipelineStepStateInProgress",
    "PipelineStepStateInProgressName",
    "PipelineStepStatePending",
    "PipelineStepStatePendingName",
    "PipelineStepStateReady",
    "PipelineStepStateReadyName",
    "PipelineTarget",
    "PipelineTrigger",
    "PipelineTriggerManual",
    "PipelineTriggerPush",
    "PipelineVariable",
    "Project",
    "ProjectBranchingModel",
    "ProjectBranchingModelBranchTypesItem",
    "ProjectBranchingModelBranchTypesItemKind",
    "ProjectBranchingModelDevelopment",
    "ProjectBranchingModelProduction",
    "ProjectDeployKey",
    "ProjectDeployKeyLinks",
    "ProjectGroupPermission",
    "ProjectGroupPermissionLinks",
    "ProjectGroupPermissionPermission",
    "ProjectLinks",
    "ProjectUserPermission",
    "ProjectUserPermissionLinks",
    "ProjectUserPermissionPermission",
    "Pullrequest",
    "PullrequestComment",
    "PullrequestCommentTask",
    "PullRequestEndpoint",
    "PullRequestEndpointPullRequestBranch",
    "PullRequestEndpointPullRequestBranchMergeStrategiesItem",
    "PullRequestEndpointPullRequestCommit",
    "PullrequestLinks",
    "PullRequestMergeParameters",
    "PullRequestMergeParametersMergeStrategy",
    "PullrequestPullRequestCommit",
    "PullrequestRenderedPullRequestMarkup",
    "PullrequestRenderedPullRequestMarkupDescription",
    "PullrequestRenderedPullRequestMarkupDescriptionMarkup",
    "PullrequestRenderedPullRequestMarkupReason",
    "PullrequestRenderedPullRequestMarkupReasonMarkup",
    "PullrequestRenderedPullRequestMarkupTitle",
    "PullrequestRenderedPullRequestMarkupTitleMarkup",
    "PullrequestState",
    "PullrequestSummary",
    "PullrequestSummaryMarkup",
    "PullrequestTask",
    "PullRequestTaskCreate",
    "PullRequestTaskCreateTaskRawContent",
    "PullrequestTaskLinks",
    "PullRequestTaskUpdate",
    "PullRequestTaskUpdateState",
    "PullRequestTaskUpdateTaskRawContent",
    "Ref",
    "RefLinks",
    "Report",
    "ReportAnnotation",
    "ReportAnnotationAnnotationType",
    "ReportAnnotationResult",
    "ReportAnnotationSeverity",
    "ReportData",
    "ReportDataType",
    "ReportDataValue",
    "ReportReportType",
    "ReportResult",
    "Repository",
    "RepositoryForkPolicy",
    "RepositoryGroupPermission",
    "RepositoryGroupPermissionLinks",
    "RepositoryGroupPermissionPermission",
    "RepositoryInheritanceState",
    "RepositoryInheritanceStateOverrideSettings",
    "RepositoryLinks",
    "RepositoryPermission",
    "RepositoryPermissionPermission",
    "RepositoryScm",
    "RepositoryUserPermission",
    "RepositoryUserPermissionLinks",
    "RepositoryUserPermissionPermission",
    "SearchCodeSearchResult",
    "SearchContentMatch",
    "SearchLine",
    "SearchResultPage",
    "SearchSegment",
    "Snippet",
    "SnippetComment",
    "SnippetCommentLinks",
    "SnippetCommit",
    "SnippetCommitLinks",
    "SnippetScm",
    "SshAccountKey",
    "SshKey",
    "SshKeyLinks",
    "SubjectTypes",
    "SubjectTypesRepository",
    "SubjectTypesWorkspace",
    "Tag",
    "Task",
    "TaskContent",
    "TaskContentMarkup",
    "TaskState",
    "Team",
    "TeamLinks",
    "TreeEntry",
    "User",
    "UserLinks",
    "Version",
    "VersionLinks",
    "WebhookSubscription",
    "WebhookSubscriptionEventsItem",
    "WebhookSubscriptionSubjectType",
    "Workspace",
    "WorkspaceAccess",
    "WorkspaceBase",
    "WorkspaceBaseLinks",
    "WorkspaceForkingMode",
    "WorkspaceLinks",
    "WorkspaceMembership",
    "WorkspaceMembershipLinks",
)
