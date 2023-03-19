from typing import Optional, Dict, Union
from github.Requester import Requester


def create_jwt(integration_id: int = ..., private_key: str = ..., expiration: int = ..., issued_at: int = ...) -> str: ...

class AppAuthentication:
    def __init__(
        self,
        app_id: Union[int, str],
        private_key: str,
        installation_id: int,
        token_permissions: Optional[Dict[str, str]] = ...,
    ): ...

    def get_access_token(self, requester: Requester, permissions: dict = ...): ...
