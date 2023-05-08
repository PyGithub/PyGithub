from collections import OrderedDict
from io import BufferedReader
from typing import Any, Callable, Dict, Iterator, Optional, Tuple, Union

from requests.models import Response

from github.AppAuthentication import AppAuthentication
from github.GithubObject import GithubObject
from github.InstallationAuthorization import InstallationAuthorization

from urllib3.util import Retry

class Requester:
    __installation_authorization: Optional[InstallationAuthorization] = ...
    __app_auth: Optional[AppAuthentication] = ...

    def __check(
        self,
        status: int,
        responseHeaders: Dict[str, Any],
        output: str,
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]: ...
    def __addParametersToUrl(
        self,
        url: str,
        parameters: Dict[str, Any],
    ) -> str: ...
    def __authenticate(
        self,
        url: str,
        requestHeaders: Dict[str, Any],
        parameters: Dict[str, Any],
    ) -> None: ...
    def __customConnection(
        self,
        url: str,
    ) -> Optional[Union[HTTPRequestsConnectionClass, HTTPSRequestsConnectionClass]]: ...
    def __createConnection(
        self,
    ) -> Union[HTTPRequestsConnectionClass, HTTPSRequestsConnectionClass]: ...
    def __createException(
        self,
        status: int,
        headers: Dict[str, Any],
        output: str,
    ) -> Any: ...
    def __makeAbsoluteUrl(self, url: str) -> str: ...
    def __structuredFromJson(self, data: str) -> Optional[Dict[str, Any]]: ...
    def __requestEncode(
        self,
        cnx: Union[HTTPRequestsConnectionClass, HTTPSRequestsConnectionClass],
        verb: str,
        url: str,
        parameters: Dict[str, str],
        requestHeaders: Dict[str, str],
        input: Optional[str],
        encode: Callable[[str], str],
    ) -> Tuple[int, Dict[str, Any], str]: ...
    def __requestRaw(
        self,
        cnx: Union[HTTPRequestsConnectionClass, HTTPSRequestsConnectionClass],
        verb: str,
        url: str,
        requestHeaders: Dict[str, str],
        input: Optional[str],
    ) -> Tuple[int, Dict[str, Any], str]: ...
    def __init__(
        self,
        login_or_token: Optional[str],
        password: Optional[str],
        jwt: Optional[str],
        app_auth: Optional[AppAuthentication],
        base_url: str,
        timeout: int,
        user_agent: str,
        per_page: int,
        verify: bool,
        retry: Optional[Union[int, Retry]],
        pool_size: Optional[int],
    ) -> None: ...
    def _initializeDebugFeature(self) -> None: ...
    def check_me(self, obj: GithubObject) -> None: ...
    def _must_refresh_token(self) -> bool: ...
    def _get_installation_authorization(self) -> InstallationAuthorization: ...
    def _refresh_token_if_needed(self) -> None: ...
    def _refresh_token(self) -> None: ...
    @classmethod
    def injectConnectionClasses(
        cls, httpConnectionClass: Callable, httpsConnectionClass: Callable
    ) -> None: ...
    def requestBlob(
        self,
        verb: str,
        url: str,
        parameters: Dict[str, str] = ...,
        headers: Dict[str, str] = ...,
        input: Optional[str] = ...,
        cnx: Optional[
            Union[HTTPRequestsConnectionClass, HTTPSRequestsConnectionClass]
        ] = ...,
    ) -> Tuple[int, Dict[str, Any], str]: ...
    def requestBlobAndCheck(
        self,
        verb: str,
        url: str,
        parameters: Optional[Dict[str, Any]] = ...,
        headers: Optional[Dict[str, Any]] = ...,
        input: Optional[str] = ...,
    ) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]]]: ...
    def requestJson(
        self,
        verb: str,
        url: str,
        parameters: Optional[Dict[str, Any]] = ...,
        headers: Optional[Dict[str, Any]] = ...,
        input: Optional[Any] = ...,
        cnx: Optional[
            Union[HTTPRequestsConnectionClass, HTTPSRequestsConnectionClass]
        ] = ...,
    ) -> Tuple[int, Dict[str, Any], str]: ...
    def requestJsonAndCheck(
        self,
        verb: str,
        url: str,
        parameters: Optional[Dict[str, Any]] = ...,
        headers: Optional[Dict[str, str]] = ...,
        input: Optional[Any] = ...,
    ) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]]]: ...
    def requestMultipart(
        self,
        verb: str,
        url: str,
        parameters: Optional[Dict[str, Any]] = ...,
        headers: Optional[Dict[str, Any]] = ...,
        input: Optional[OrderedDict[str, str]] = ...,
        cnx: Optional[
            Union[HTTPRequestsConnectionClass, HTTPSRequestsConnectionClass]
        ] = ...,
    ) -> Tuple[int, Dict[str, Any], str]: ...
    def requestMultipartAndCheck(
        self,
        verb: str,
        url: str,
        parameters: Optional[Dict[str, Any]] = ...,
        headers: Optional[Dict[str, Any]] = ...,
        input: Optional[OrderedDict[str, str]] = ...,
    ) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]]]: ...
    @classmethod
    def resetConnectionClasses(cls) -> None: ...
    @classmethod
    def setDebugFlag(cls, flag: bool) -> None: ...
    @classmethod
    def setOnCheckMe(cls, onCheckMe: Callable) -> None: ...
