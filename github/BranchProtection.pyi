from typing import Any, Dict

from github.GithubObject import CompletableGithubObject
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList
from github.RequiredPullRequestReviews import RequiredPullRequestReviews
from github.RequiredStatusChecks import RequiredStatusChecks
from github.Team import Team

class BranchProtection(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def enforce_admins(self) -> bool: ...
    def get_team_push_restrictions(self) -> PaginatedList[NamedUser]: ...
    def get_user_push_restrictions(self) -> PaginatedList[Team]: ...
    @property
    def required_pull_request_reviews(self) -> RequiredPullRequestReviews: ...
    @property
    def required_status_checks(self) -> RequiredStatusChecks: ...
    @property
    def url(self) -> str: ...
    @property
    def required_linear_history(self) -> bool: ...
    @property
    def allow_force_pushes(self) -> bool: ...
    @property
    def allow_deletions(self) -> bool: ...
