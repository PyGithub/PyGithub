from datetime import datetime
from io import BytesIO
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union, overload

from urllib3.util import Retry

from github.AppAuthentication import AppAuthentication
from github.ApplicationOAuth import ApplicationOAuth
from github.Auth import Auth
from github.AuthenticatedUser import AuthenticatedUser
from github.Commit import Commit
from github.ContentFile import ContentFile
from github.Enterprise import Enterprise
from github.Event import Event
from github.Gist import Gist
from github.GithubApp import GithubApp
from github.GithubObject import GithubObject, _NotSetType
from github.GitignoreTemplate import GitignoreTemplate
from github.GlobalAdvisory import GlobalAdvisory
from github.HookDescription import HookDescription
from github.Issue import Issue
from github.License import License
from github.NamedUser import NamedUser
from github.Organization import Organization
from github.PaginatedList import PaginatedList
from github.Project import Project
from github.ProjectColumn import ProjectColumn
from github.RateLimit import RateLimit
from github.Repository import Repository
from github.Topic import Topic

TGithubObject = TypeVar("TGithubObject", bound=GithubObject)

DEFAULT_BASE_URL: str
DEFAULT_STATUS_URL: str
DEFAULT_TIMEOUT: int
DEFAULT_PER_PAGE: int

class Github:
    def __init__(
        self,
        login_or_token: Optional[str] = ...,
        password: Optional[str] = ...,
        jwt: Optional[str] = ...,
        app_auth: Optional[AppAuthentication] = ...,
        base_url: str = ...,
        timeout: int = ...,
        user_agent: str = ...,
        per_page: int = ...,
        verify: Union[bool, str] = ...,
        retry: Optional[Union[int, Retry]] = ...,
        pool_size: Optional[int] = ...,
        seconds_between_requests: Optional[float] = ...,
        seconds_between_writes: Optional[float] = ...,
        auth: Optional[Auth] = ...,
    ) -> None: ...
    @property
    def FIX_REPO_GET_GIT_REF(self) -> bool: ...
    @FIX_REPO_GET_GIT_REF.setter
    def FIX_REPO_GET_GIT_REF(self, value: bool) -> None: ...
    @property
    def per_page(self) -> int: ...
    @per_page.setter
    def per_page(self, value: int) -> None: ...
    def create_from_raw_data(
        self,
        klass: Type[TGithubObject],
        raw_data: Dict[str, Any],
        headers: Dict[str, Union[str, int]] = ...,
    ) -> TGithubObject: ...
    def dump(self, obj: GithubObject, file: BytesIO, protocol: int = ...) -> None: ...
    def get_emojis(self) -> Dict[str, str]: ...
    def get_events(self) -> PaginatedList[Event]: ...
    def get_gist(self, id: str) -> Gist: ...
    def get_gists(self, since: Union[datetime, _NotSetType] = ...) -> PaginatedList[Gist]: ...
    def get_gitignore_template(self, name: str) -> GitignoreTemplate: ...
    def get_gitignore_templates(self) -> List[str]: ...
    def get_global_advisory(self, ghsa_id: str) -> GlobalAdvisory: ...
    def get_global_advisories(
        self,
        type: Union[str, _NotSetType] = ...,
        ghsa_id: Union[str, _NotSetType] = ...,
        cve_id: Union[str, _NotSetType] = ...,
        ecosystem: Union[str, _NotSetType] = ...,
        severity: Union[str, _NotSetType] = ...,
        cwes: Union[list[Union[int, str]], str, _NotSetType] = ...,
        is_withdrawn: Union[bool, _NotSetType] = ...,
        affects: Union[list[str], str, _NotSetType] = ...,
        published: Union[str, _NotSetType] = ...,
        updated: Union[str, _NotSetType] = ...,
        modified: Union[str, _NotSetType] = ...,
        keywords: Union[str, _NotSetType] = ...,
        before: Union[str, _NotSetType] = ...,
        after: Union[str, _NotSetType] = ...,
        per_page: Union[str, _NotSetType] = ...,
        sort: Union[str, _NotSetType] = ...,
        direction: Union[str, _NotSetType] = ...,
    ) -> PaginatedList[GlobalAdvisory]: ...
    def get_hook(self, name: str) -> HookDescription: ...
    def get_hooks(self) -> List[HookDescription]: ...
    def get_license(self, key: Union[str, _NotSetType] = ...) -> License: ...
    def get_licenses(self) -> PaginatedList[License]: ...
    def get_organization(self, login: str) -> Organization: ...
    def get_organizations(self, since: Union[int, _NotSetType] = ...) -> PaginatedList[Organization]: ...
    def get_enterprise(self, login: str) -> Enterprise: ...
    def get_project(self, id: int) -> Project: ...
    def get_project_column(self, id: int) -> ProjectColumn: ...
    def get_rate_limit(self) -> RateLimit: ...
    def get_repo(self, full_name_or_id: Union[int, str], lazy: bool = ...) -> Repository: ...
    def get_repos(
        self,
        since: Union[int, _NotSetType] = ...,
        visibility: Union[str, _NotSetType] = ...,
    ) -> PaginatedList[Repository]: ...
    @overload
    def get_user(self, login: _NotSetType = ...) -> AuthenticatedUser: ...
    @overload
    def get_user(self, login: Union[str, _NotSetType] = ...) -> Union[NamedUser, AuthenticatedUser]: ...
    def get_user_by_id(self, user_id: int) -> NamedUser: ...
    def get_users(self, since: Union[int, _NotSetType] = ...) -> PaginatedList[NamedUser]: ...
    def load(self, f: BytesIO) -> Repository: ...
    # argument slug is deprecated, not included here
    def get_app(self) -> GithubApp: ...
    def get_oauth_application(self, client_id: str, client_secret: str) -> ApplicationOAuth: ...
    @property
    def oauth_scopes(self) -> Optional[List[str]]: ...
    @property
    def rate_limiting(self) -> Tuple[int, int]: ...
    @property
    def rate_limiting_resettime(self) -> int: ...
    def render_markdown(self, text: str, context: Union[Repository, _NotSetType] = ...) -> str: ...
    def search_code(
        self,
        query: str,
        sort: Union[str, _NotSetType] = ...,
        order: Union[str, _NotSetType] = ...,
        highlight: bool = ...,
        **qualifiers: Any,
    ) -> PaginatedList[ContentFile]: ...
    def search_commits(
        self, query: str, sort: Union[str, _NotSetType] = ..., order: Union[str, _NotSetType] = ..., **qualifiers: Any
    ) -> PaginatedList[Commit]: ...
    def search_issues(
        self, query: str, sort: Union[str, _NotSetType] = ..., order: Union[str, _NotSetType] = ..., **qualifiers: Any
    ) -> PaginatedList[Issue]: ...
    def search_repositories(
        self, query: str, sort: Union[str, _NotSetType] = ..., order: Union[str, _NotSetType] = ..., **qualifiers: Any
    ) -> PaginatedList[Repository]: ...
    def search_topics(self, query: str, **qualifiers: Any) -> PaginatedList[Topic]: ...
    def search_users(
        self, query: str, sort: Union[str, _NotSetType] = ..., order: Union[str, _NotSetType] = ..., **qualifiers: Any
    ) -> PaginatedList[NamedUser]: ...
