from typing import Any, Dict, Optional

from github.AccessToken import AccessToken
from github.GithubObject import NonCompletableGithubObject

class ApplicationOAuth(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def client_id(self) -> str: ...
    @property
    def client_secret(self) -> str: ...
    def get_login_url(
        self,
        redirect_uri: Optional[str]=None,
        state: Optional[str]=None,
        login: Optional[str]=None
    ) -> str: ...
    def get_access_token(
        self,
        code: str,
        state: Optional[str]=None
    ) -> AccessToken: ...
