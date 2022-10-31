from typing import Union, Optional

from github.Installation import Installation
from github.InstallationAuthorization import InstallationAuthorization
from github.PaginatedList import PaginatedList

class GithubIntegration:
    def __init__(
        self,
        integration_id: Union[int, str],
        private_key: str,
        base_url: str = ...,
        jwt_expiry: int = ...,
    ) -> None: ...
    def _get_installed_app(self, url: str) -> Installation: ...
    def _get_headers(self) -> dict: ...
    def create_jwt(self, expiration: int = ...) -> str: ...
    def get_access_token(
        self, installation_id: int, user_id: Optional[int] = ...
    ) -> InstallationAuthorization: ...
    def get_installation(self, owner: str, repo: str) -> Installation: ...
    def get_installations(self) -> PaginatedList[Installation]: ...
    def get_org_installation(self, org: str) -> Installation: ...
    def get_repo_installation(self, owner: str, repo: str) -> Installation: ...
    def get_user_installation(self, username: str) -> Installation: ...
