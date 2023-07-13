from datetime import datetime
from typing import Any, Dict, List, Union

from github.CheckRunAnnotation import CheckRunAnnotation
from github.CheckRunOutput import CheckRunOutput
from github.GithubApp import GithubApp
from github.GithubObject import CompletableGithubObject, _NotSetType
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest

class CheckRun(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def get_annotations(self) -> PaginatedList[CheckRunAnnotation]: ...
    def edit(
        self,
        name: Union[_NotSetType, str] = ...,
        head_sha: Union[_NotSetType, str] = ...,
        details_url: Union[_NotSetType, str] = ...,
        external_id: Union[_NotSetType, str] = ...,
        status: Union[_NotSetType, str] = ...,
        started_at: Union[_NotSetType, datetime] = ...,
        conclusion: Union[_NotSetType, str] = ...,
        completed_at: Union[_NotSetType, datetime] = ...,
        output: Union[_NotSetType, Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]] = ...,
        actions: Union[_NotSetType, List[Dict[str, str]]] = ...,
    ) -> None: ...
    @property
    def app(self) -> GithubApp: ...
    @property
    def check_suite_id(self) -> int: ...
    @property
    def completed_at(self) -> datetime: ...
    @property
    def conclusion(self) -> str: ...
    @property
    def details_url(self) -> str: ...
    @property
    def external_id(self) -> str: ...
    @property
    def head_sha(self) -> str: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def node_id(self) -> str: ...
    @property
    def output(self) -> CheckRunOutput: ...
    @property
    def pull_requests(self) -> List[PullRequest]: ...
    @property
    def started_at(self) -> datetime: ...
    @property
    def status(self) -> str: ...
    @property
    def url(self) -> str: ...
