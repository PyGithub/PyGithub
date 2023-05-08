from typing import Dict, Optional, Union

from github.Installations import Installations


class Auth:
    @property
    def token_type(self) -> str: ...
    @property
    def token(self) -> str: ...
class Login(Auth):
    _login: str
    __password: str
    def __init__(self, login, password): ...
    @property
    def login(self) -> str: ...
class Token(Auth):
    __token: str
    def __init__(self, token): ...
class JWT(Auth):
    ...
class AppAuth(Auth):
    _app_id: Union[int, str]
    _private_key: str
    def __init__(
        self,
        app_id: Union[int, str],
        private_key: str,
        jwt_expiry: int=...,
        jwt_issued_at: int=...,
        jwt_algorithm: str=...,
    ): ...
    @property
    def app_id(self) -> Union[int, str]: ...
    @property
    def private_key(self) -> str: ...
class AppAuthToken(Auth):
    __token: str
    def __init__(self, token: str): ...
class AppInstallationAuth(Auth):
    __app_auth: AppAuth
    __installations: Optional[Installations]
    _installation_id: int
    _token_permissions: Optional[Dict[str, str]]
    def __init__(
        self,
        app_auth: AppAuth,
        installation_id: int,
        token_permissions: Optional[Dict[str, str]] = ...,
    ): ...
    @property
    def app_id(self) -> Union[int, str]: ...
    @property
    def private_key(self) -> str: ...
    @property
    def installation_id(self) -> int: ...
    @property
    def token_permissions(self) -> Optional[Dict[str, str]]: ...
