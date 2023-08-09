from typing import Dict, Optional, Union

from urllib3 import Retry

import github
from github.Auth import AppAuth
from github.Installation import Installation
from github.InstallationAuthorization import InstallationAuthorization
from github.PaginatedList import PaginatedList
from github.Requester import Requester

class GithubIntegration:
    auth: AppAuth = ...
    base_url: str = ...
    __requester: Requester = ...
    def __init__(
        self,
        integration_id: Optional[Union[int, str]] = ...,
        private_key: Optional[str] = ...,
        base_url: str = ...,
        *,
        timeout: int = ...,
        user_agent: str = ...,
        per_page: int = ...,
        verify: Union[bool, str] = ...,
        retry: Optional[Union[int, Retry]] = ...,
        pool_size: Optional[int] = ...,
        seconds_between_requests: Optional[float] = ...,
        seconds_between_writes: Optional[float] = ...,
        jwt_expiry: int = ...,
        jwt_issued_at: int = ...,
        jwt_algorithm: str = ...,
        auth: Optional[AppAuth] = ...,
    ) -> None: ...
    def get_github_for_installation(self, installation_id: int) -> github.Github: ...
    def _get_installed_app(self, url: str) -> Installation: ...
    def _get_headers(self) -> Dict[str, str]: ...
    def create_jwt(self, expiration: Optional[int] = ...) -> str: ...
    def get_access_token(
        self, installation_id: int, permissions: Optional[Dict[str, str]] = ...
    ) -> InstallationAuthorization: ...
    def get_app_installation(self, installation_id: int) -> Installation: ...
    def get_installation(self, owner: str, repo: str) -> Installation: ...
    def get_installations(self) -> PaginatedList[Installation]: ...
    def get_org_installation(self, org: str) -> Installation: ...
    def get_repo_installation(self, owner: str, repo: str) -> Installation: ...
    def get_user_installation(self, username: str) -> Installation: ...
