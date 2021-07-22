from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from github.Event import Event
from github.GithubObject import CompletableGithubObject, _NotSetType
from github.Hook import Hook
from github.Issue import Issue
from github.Label import Label
from github.Migration import Migration
from github.Installation import Installation
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList
from github.Plan import Plan
from github.Project import Project
from github.PublicKey import PublicKey
from github.Repository import Repository
from github.Team import Team

class Organization(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def add_to_members(
        self, member: NamedUser, role: Union[_NotSetType, str] = ...
    ) -> None: ...
    def add_to_public_members(self, public_member: NamedUser) -> None: ...
    @property
    def avatar_url(self) -> str: ...
    @property
    def billing_email(self) -> str: ...
    @property
    def blog(self) -> Optional[str]: ...
    @property
    def collaborators(self) -> int: ...
    @property
    def company(self) -> Optional[str]: ...
    def convert_to_outside_collaborator(self, member: NamedUser) -> None: ...
    def create_fork(self, repo: Repository) -> Repository: ...
    def create_hook(
        self,
        name: str,
        config: Dict[str, str],
        events: Union[_NotSetType, List[str]] = ...,
        active: Union[bool, _NotSetType] = ...,
    ) -> Hook: ...
    def create_migration(
        self,
        repos: List[str],
        lock_repositories: Union[bool, _NotSetType] = ...,
        exclude_attachments: Union[bool, _NotSetType] = ...,
    ) -> Migration: ...
    def create_repo(
        self,
        name: str,
        description: Union[str, _NotSetType] = ...,
        homepage: Union[str, _NotSetType] = ...,
        private: Union[bool, _NotSetType] = ...,
        has_issues: Union[bool, _NotSetType] = ...,
        has_wiki: Union[bool, _NotSetType] = ...,
        has_downloads: Union[bool, _NotSetType] = ...,
        has_projects: Union[bool, _NotSetType] = ...,
        team_id: Union[int, _NotSetType] = ...,
        auto_init: Union[bool, _NotSetType] = ...,
        license_template: Union[str, _NotSetType] = ...,
        gitignore_template: Union[str, _NotSetType] = ...,
        allow_squash_merge: Union[bool, _NotSetType] = ...,
        allow_merge_commit: Union[bool, _NotSetType] = ...,
        allow_rebase_merge: Union[bool, _NotSetType] = ...,
    ) -> Repository: ...
    def create_secret(
        self,
        secret_name: str,
        unencrypted_value: str,
        visibility: str = ...,
        selected_repositories: Union[List[Repository], _NotSetType] = ...,
    ) -> bool: ...
    def create_team(
        self,
        name: str,
        repo_names: Union[List[Repository], _NotSetType] = ...,
        permission: Union[str, _NotSetType] = ...,
        privacy: Union[str, _NotSetType] = ...,
        description: Union[str, _NotSetType] = ...,
    ) -> Team: ...
    @property
    def created_at(self) -> datetime: ...
    def delete_hook(self, id: int) -> None: ...
    @property
    def default_repository_permission(self) -> str: ...
    def delete_secret(self, secret_name: str) -> bool: ...
    @property
    def description(self) -> str: ...
    @property
    def disk_usage(self) -> int: ...
    def edit(
        self,
        billing_email: Union[str, _NotSetType] = ...,
        blog: Union[str, _NotSetType] = ...,
        company: Union[str, _NotSetType] = ...,
        description: Union[str, _NotSetType] = ...,
        email: Union[str, _NotSetType] = ...,
        location: Union[str, _NotSetType] = ...,
        name: Union[str, _NotSetType] = ...,
    ) -> None: ...
    def edit_hook(
        self,
        id: int,
        name: str,
        config: Dict[str, str],
        events: Union[_NotSetType, List[str]] = ...,
        active: Union[bool, _NotSetType] = ...,
    ) -> Hook: ...
    @property
    def email(self) -> Optional[str]: ...
    @property
    def events_url(self) -> str: ...
    @property
    def followers(self) -> int: ...
    @property
    def following(self) -> int: ...
    def get_events(self) -> PaginatedList[Event]: ...
    def get_hooks(self) -> PaginatedList[Hook]: ...
    def get_issues(
        self,
        filter: Union[str, _NotSetType] = ...,
        state: Union[str, _NotSetType] = ...,
        labels: Union[List[Label], _NotSetType] = ...,
        sort: Union[str, _NotSetType] = ...,
        direction: Union[str, _NotSetType] = ...,
        since: Union[_NotSetType, datetime] = ...,
    ) -> PaginatedList[Issue]: ...
    def get_members(
        self,
        filter_: Union[str, _NotSetType] = ...,
        role: Union[str, _NotSetType] = ...,
    ) -> PaginatedList[NamedUser]: ...
    def get_migrations(self) -> PaginatedList[Migration]: ...
    def get_installations(self) -> PaginatedList[Installation]: ...
    def get_outside_collaborators(
        self, filter_: Union[str, _NotSetType] = ...
    ) -> PaginatedList[NamedUser]: ...
    def get_projects(
        self, state: Union[_NotSetType, str] = ...
    ) -> PaginatedList[Project]: ...
    def get_public_key(self) -> PublicKey: ...
    def get_public_members(self) -> PaginatedList[NamedUser]: ...
    def get_repo(self, name: str) -> Repository: ...
    def get_repos(
        self,
        type: Union[str, _NotSetType] = ...,
        sort: Union[str, _NotSetType] = ...,
        direction: Union[str, _NotSetType] = ...,
    ) -> PaginatedList[Repository]: ...
    def get_team(self, id: int) -> Team: ...
    def get_team_by_slug(self, slug: str) -> Team: ...
    def get_teams(self) -> PaginatedList[Team]: ...
    @property
    def gravatar_id(self) -> str: ...
    def has_in_members(self, member: NamedUser) -> bool: ...
    def has_in_public_members(self, public_member: NamedUser) -> bool: ...
    @property
    def has_organization_projects(self) -> bool: ...
    @property
    def has_repository_projects(self) -> bool: ...
    @property
    def hooks_url(self) -> str: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def issues_url(self) -> str: ...
    def invitations(self) -> PaginatedList[NamedUser]: ...
    def invite_user(
        self,
        user: Union[_NotSetType, NamedUser] = ...,
        email: Union[str, _NotSetType] = ...,
        role: Union[str, _NotSetType] = ...,
        teams: Union[List[Team], _NotSetType] = ...,
    ) -> None: ...
    @property
    def location(self) -> str: ...
    @property
    def login(self) -> str: ...
    @property
    def members_can_create_repositories(self) -> bool: ...
    @property
    def members_url(self) -> str: ...
    @property
    def name(self) -> Optional[str]: ...
    @property
    def owned_private_repos(self) -> int: ...
    @property
    def plan(self) -> Plan: ...
    @property
    def private_gists(self) -> int: ...
    @property
    def public_gists(self) -> int: ...
    @property
    def public_members_url(self) -> str: ...
    @property
    def public_repos(self) -> int: ...
    def remove_from_members(self, member: NamedUser) -> None: ...
    def remove_from_membership(self, member: NamedUser) -> None: ...
    def remove_from_public_members(self, public_member: NamedUser) -> None: ...
    def remove_outside_collaborator(self, collaborator: NamedUser) -> None: ...
    @property
    def repos_url(self) -> str: ...
    @property
    def total_private_repos(self) -> int: ...
    @property
    def two_factor_requirement_enabled(self) -> bool: ...
    @property
    def type(self) -> str: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
