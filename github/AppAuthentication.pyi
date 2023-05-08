from typing import Optional, Dict, Union

class AppAuthentication:
    app_id: Union[str, int]
    private_key: str
    installation_id: int
    token_permissions: Optional[Dict[str, str]]

    def __init__(
        self,
        app_id: Union[int, str],
        private_key: str,
        installation_id: int,
        token_permissions: Optional[Dict[str, str]] = ...,
    ): ...
