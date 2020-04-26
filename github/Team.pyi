from typing import Any, Dict, Union

from github.GithubObject import CompletableGithubObject, _NotSetType
from github.NamedUser import NamedUser
from github.Organization import Organization
from github.PaginatedList import PaginatedList
from github.Repository import Repository
from github.TeamDiscussion import TeamDiscussion

class Team(CompletableGithubObject):
    def __repr__(self) -> str: ...
    @property
    def _identity(self) -> int: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def add_membership(
        self, member: NamedUser, role: Union[str, _NotSetType] = ...
    ) -> None: ...
    def add_to_members(self, member: NamedUser) -> None: ...
    def add_to_repos(self, repo: Repository) -> None: ...
    def delete(self) -> None: ...
    @property
    def description(self) -> str: ...
    def edit(
        self,
        name: str,
        description: Union[str, _NotSetType] = ...,
        permission: Union[str, _NotSetType] = ...,
        privacy: Union[str, _NotSetType] = ...,
    ) -> None: ...
    def get_discussions(self) -> PaginatedList[TeamDiscussion]: ...
    def get_members(
        self, role: Union[str, _NotSetType] = ...
    ) -> PaginatedList[NamedUser]: ...
    def get_repos(self) -> PaginatedList[Repository]: ...
    def has_in_members(self, member: NamedUser) -> bool: ...
    def has_in_repos(self, repo: Repository) -> bool: ...
    @property
    def id(self) -> int: ...
    def invitations(self) -> PaginatedList[NamedUser]: ...
    @property
    def members_count(self) -> int: ...
    @property
    def members_url(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def organization(self) -> Organization: ...
    @property
    def permission(self) -> str: ...
    @property
    def privacy(self) -> str: ...
    def remove_from_members(self, member: NamedUser) -> None: ...
    def remove_from_repos(self, repo: Repository) -> None: ...
    def remove_membership(self, member: NamedUser) -> None: ...
    @property
    def repos_count(self) -> int: ...
    @property
    def repositories_url(self) -> str: ...
    def set_repo_permission(self, repo: Repository, permission: str) -> None: ...
    @property
    def slug(self) -> str: ...
    @property
    def url(self) -> str: ...
