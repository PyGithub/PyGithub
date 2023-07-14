from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List

from github.CheckRun import CheckRun
from github.GitCommit import GitCommit
from github.GithubApp import GithubApp
from github.GithubObject import CompletableGithubObject
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest
from github.Repository import Repository

class CheckSuite(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def after(self) -> str: ...
    @property
    def app(self) -> GithubApp: ...
    @property
    def before(self) -> str: ...
    @property
    def check_runs_url(self) -> str: ...
    @property
    def conclusion(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def head_branch(self) -> str: ...
    @property
    def head_commit(self) -> GitCommit: ...
    @property
    def head_sha(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def latest_check_runs_count(self) -> int: ...
    @property
    def pull_requests(self) -> List[PullRequest]: ...
    @property
    def repository(self) -> Repository: ...
    @property
    def status(self) -> str: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    def rerequest(self) -> bool: ...
    def get_check_runs(self, check_name: str, status: str, filter: str) -> PaginatedList[CheckRun]: ...
