from io import BufferedReader
from collections import OrderedDict
from github.GithubObject import GithubObject
from requests.models import Response
from tests.Framework import ReplayingHttpsConnection
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    Optional,
    Tuple,
    Union,
)
from urllib3.util.retry import Retry


class HTTPRequestsConnectionClass:
    def __init__(
        self,
        host: str,
        port: Optional[int] = ...,
        strict: bool = ...,
        timeout: Optional[int] = ...,
        retry: None = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    def getresponse(self) -> RequestsResponse: ...
    def request(self, verb: str, url: str, input: None, headers: Dict[str, str]) -> None: ...


class HTTPSRequestsConnectionClass:
    def __init__(
        self,
        host: str,
        port: None = ...,
        strict: bool = ...,
        timeout: Optional[int] = ...,
        retry: Optional[Retry] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    def getresponse(self) -> RequestsResponse: ...
    def request(
        self,
        verb: str,
        url: str,
        input: Optional[Union[str, BufferedReader]],
        headers: Dict[str, str]
    ) -> None: ...


class Requester:
    def DEBUG_ON_RESPONSE(self, statusCode: int, responseHeader: Dict[str, str], data: str) -> None: ...
    def NEW_DEBUG_FRAME(self, requestHeader: Dict[str, str]) -> None: ...
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
        api_preview: bool,
        verify: bool,
        retry: Optional[Retry]
    ) -> None: ...
    def _initializeDebugFeature(self) -> None: ...
    def check_me(self, obj: GithubObject) -> None: ...
    @classmethod
    def injectConnectionClasses(cls, httpConnectionClass: Callable, httpsConnectionClass: Callable) -> None: ...
    def requestBlob(
        self,
        verb: str,
        url: str,
        parameters: Dict[str, str] = ...,
        headers: Dict[str, str] = ...,
        input: Optional[str] = ...,
        cnx: Optional[ReplayingHttpsConnection] = ...
    ) -> Tuple[int, Dict[str, Union[str, int]], str]: ...
    def requestBlobAndCheck(
        self,
        verb: str,
        url: str,
        parameters: Optional[Dict[str, str]] = ...,
        headers: Optional[Dict[str, str]] = ...,
        input: Optional[str] = ...
    ) -> Tuple[Dict[str, Union[str, int]], Dict[str, str]]: ...
    def requestJson(
        self,
        verb: str,
        url: str,
        parameters: Optional[Union[Dict[str, bool], Dict[str, int], Dict[str, Union[str, int]], Dict[str, str]]] = ...,
        headers: Optional[Dict[str, str]] = ...,
        input: Optional[Any] = ...,
        cnx: None = ...
    ) -> Union[Tuple[int, Dict[str, int], str], Tuple[int, Dict[str, Union[str, int]], str]]: ...
    def requestJsonAndCheck(
        self,
        verb: str,
        url: str,
        parameters: Optional[Union[Dict[str, bool], Dict[str, int], Dict[str, Union[str, int]], Dict[str, str]]] = ...,
        headers: Optional[Dict[str, str]] = ...,
        input: Optional[Any] = ...
    ) -> Any: ...
    def requestMultipart(
        self,
        verb: str,
        url: str,
        parameters: None = ...,
        headers: None = ...,
        input: Optional[OrderedDict] = ...,
        cnx: None = ...
    ) -> Tuple[int, Dict[str, Union[str, int]], str]: ...
    def requestMultipartAndCheck(
        self,
        verb: str,
        url: str,
        parameters: None = ...,
        headers: None = ...,
        input: Optional[OrderedDict] = ...
    ) -> Tuple[Dict[str, Union[str, int]], None]: ...
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
