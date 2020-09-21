from typing import Dict
from typing import List
from datetime import datetime
from github.GithubObject import CompletableGithubObject

class AuthorizationOrganization(CompletableGithubObject):
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, str]) -> None: ...
    @property
    def login(self) -> str: ...
    @property
    def credential_id(self) -> int: ...
    @property
    def credential_type(self) -> str: ...
    @property
    def credential_authorized_at(self) -> datetime: ...
    @property
    def credential_accessed_at(self) -> datetime: ...
    @property
    def token_last_eight(self) -> str: ...
    @property
    def scopes(self) -> List[str]: ...
