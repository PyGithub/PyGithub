from typing import Optional, Dict, Union
from github.Requester import Requester


class AppAuthentication:
    def __init__(
        self,
        app_id: Union[int, str],
        private_key: str,
        installation_id: int,
        token_permissions: Optional[Dict[str, str]] = ...,
    ): ...

    def get_access_token(self, requester: Requester, permissions: dict = ...): ...
