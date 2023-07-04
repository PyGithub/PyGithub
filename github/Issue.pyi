from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from github.GithubObject import CompletableGithubObject, _NotSetType
from github.IssueComment import IssueComment
from github.IssueEvent import IssueEvent
from github.IssuePullRequest import IssuePullRequest
from github.Label import Label
from github.Milestone import Milestone
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest
from github.Reaction import Reaction
from github.Repository import Repository
from github.TimelineEvent import TimelineEvent

class Issue(CompletableGithubObject):
    def __repr__(self) -> str: ...
    @property
    def _identity(self) -> int: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def add_to_assignees(self, *assignees: Union[NamedUser, str]) -> None: ...
    def add_to_labels(self, *labels: Union[Label, str]) -> None: ...
    def as_pull_request(self) -> PullRequest: ...
    @property
    def active_lock_reason(self) -> str: ...
    @property
    def assignee(self) -> Optional[NamedUser]: ...
    @property
    def assignees(self) -> List[NamedUser]: ...
    @property
    def body(self) -> str: ...
    @property
    def closed_at(self) -> datetime: ...
    @property
    def closed_by(self) -> Optional[NamedUser]: ...
    @property
    def comments(self) -> int: ...
    @property
    def comments_url(self) -> str: ...
    def create_comment(self, body: str) -> IssueComment: ...
    def create_reaction(self, reaction_type: str) -> Reaction: ...
    def get_timeline(self) -> PaginatedList[TimelineEvent]: ...
    @property
    def created_at(self) -> datetime: ...
    def delete_labels(self) -> None: ...
    def delete_reaction(self, reaction_id: int) -> bool: ...
    def edit(
        self,
        title: Union[str, _NotSetType] = ...,
        body: Union[str, _NotSetType] = ...,
        assignee: Optional[Union[str, _NotSetType, NamedUser]] = ...,
        state: Union[str, _NotSetType] = ...,
        milestone: Optional[Union[Milestone, _NotSetType]] = ...,
        labels: Union[_NotSetType, List[str]] = ...,
        assignees: Union[_NotSetType, List[str]] = ...,
    ) -> None: ...
    @property
    def events_url(self) -> str: ...
    def get_comment(self, id: int) -> IssueComment: ...
    def get_comments(self, since: Union[_NotSetType, datetime] = ...) -> PaginatedList[IssueComment]: ...
    def get_events(self) -> PaginatedList[IssueEvent]: ...
    def get_labels(self) -> PaginatedList[Label]: ...
    def get_reactions(self) -> PaginatedList[Reaction]: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def labels(self) -> List[Label]: ...
    @property
    def labels_url(self) -> str: ...
    def lock(self, lock_reason: str) -> None: ...
    @property
    def locked(self) -> bool: ...
    @property
    def milestone(self) -> Optional[Milestone]: ...
    @property
    def number(self) -> int: ...
    @property
    def pull_request(self) -> IssuePullRequest: ...
    def remove_from_assignees(self, *assignees: Union[NamedUser, str]) -> None: ...
    def remove_from_labels(self, label: Union[str, Label]) -> None: ...
    @property
    def repository(self) -> Repository: ...
    def set_labels(self, *labels: Union[str, Label]) -> None: ...
    @property
    def state(self) -> str: ...
    @property
    def title(self) -> str: ...
    def unlock(self) -> None: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def user(self) -> NamedUser: ...
