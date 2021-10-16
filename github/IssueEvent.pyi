from datetime import datetime
from typing import Any, Dict, Optional, Union

from github.GithubObject import CompletableGithubObject
from github.Issue import Issue
from github.Label import Label
from github.Milestone import Milestone
from github.NamedUser import NamedUser

class IssueEvent(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def actor(self) -> NamedUser: ...
    @property
    def assignee(self) -> Optional[NamedUser]: ...
    @property
    def assigner(self) -> Optional[NamedUser]: ...
    @property
    def commit_id(self) -> Optional[str]: ...
    @property
    def commit_url(self) -> Optional[str]: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def dismissed_review(self) -> Optional[Dict[str, Union[str, int]]]: ...
    @property
    def event(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def issue(self) -> Issue: ...
    @property
    def label(self) -> Optional[Label]: ...
    @property
    def lock_reason(self) -> Optional[str]: ...
    @property
    def milestone(self) -> Optional[Milestone]: ...
    @property
    def node_id(self) -> str: ...
    @property
    def rename(self) -> Optional[Dict[str, str]]: ...
    @property
    def requested_reviewer(self) -> Optional[NamedUser]: ...
    @property
    def review_requester(self) -> Optional[NamedUser]: ...
    @property
    def url(self) -> str: ...
