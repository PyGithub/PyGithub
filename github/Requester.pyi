from collections import OrderedDict
from io import BufferedReader
from typing import Any, Callable, Dict, Iterator, Optional, Tuple, Union

from requests.models import Response

from github.GithubObject import GithubObject

from urllib3.util import Retry

class HTTPRequestsConnectionClass:
    def __init__(
        self,
        host: str,
        port: Optional[int] = ...,
        strict: bool = ...,
        timeout: Optional[int] = ...,
        retry: Optional[Union[int, Retry]] = ...,
        pool_size: Optional[int] = ...,
        **kwargs: str
    ) -> None: ...
    def close(self) -> None: ...
    def getresponse(self) -> RequestsResponse: ...
    def request(
        self, verb: str, url: str, input: None, headers: Dict[str, str]
    ) -> None: ...

class HTTPSRequestsConnectionClass:
    def __init__(
        self,
        host: str,
        port: Optional[int] = ...,
        strict: bool = ...,
        timeout: Optional[int] = ...,
        retry: Optional[Union[int, Retry]] = ...,
        pool_size: Optional[int] = ...,
        **kwargs: str
    ) -> None: ...
    def close(self) -> None: ...
    def getresponse(self) -> RequestsResponse: ...
    def request(
        self,
        verb: str,
        url: str,
        input: Optional[Union[str, BufferedReader]],
        headers: Dict[str, str],
    ) -> None: ...

class Requester:
    def DEBUG_ON_RESPONSE(
        self, statusCode: int, responseHeader: Dict[str, str], data: str
    ) -> None: ...
    def NEW_DEBUG_FRAME(self, requestHeader: Dict[str, str]) -> None: ...
    def __check(
        self,
        status: int,
        responseHeader: Dict[str, Any],
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
        responseHeader: Dict[str, Any],
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
    def __log(
        self,
        verb: str,
        url: str,
        requestHeaders: Dict[str, str],
        input: Optional[str],
        status: Optional[int],
        responseHeader: Dict[str, Any],
        output: Optional[str],
    ) -> None: ...
    def __makeAbsoluteUrl(self, url: str) -> str: ...
    def __structuredFromJson(self, data: str) -> Optional[Dict[str, Any]]: ...
    def __requestEncode(
        self,
        verb: str,
        url: str,
        parameters: Dict[str, str] = ...,
        headers: Dict[str, str] = ...,
        input: Optional[str] = ...,
        encode: Callable[[str], str] = ...,
    ) -> Tuple[int, Dict[str, Any], str]: ...
    def __requestRaw(
        self,
        verb: str,
        url: str,
        parameters: Dict[str, str] = ...,
        headers: Dict[str, str] = ...,
        input: Optional[str] = ...,
    ) -> Tuple[int, Dict[str, Any], str]: ...
    def __init__(
        self,
        login_or_token: Optional[str],
        password: Optional[str],
        jwt: Optional[str],
        base_url: str,
        timeout: int,
        client_id: Optional[str],
        client_secret: Optional[str],
        user_agent: str,
        per_page: int,
        verify: bool,
        retry: Optional[Union[int, Retry]],
        pool_size: Optional[int],
    ) -> None: ...
    def _initializeDebugFeature(self) -> None: ...
    def check_me(self, obj: GithubObject) -> None: ...
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

class RequestsResponse:
    def __init__(self, r: Response) -> None: ...
    def getheaders(self) -> Iterator[Any]: ...
    def read(self) -> str: ...
