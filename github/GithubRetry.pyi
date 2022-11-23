from datetime import datetime
from typing import Any

from urllib3 import Retry, HTTPResponse


class GithubRetry:
    secondaryRateWait: int
    def __init__(self, secondaryRateWait: int, **kwargs: Any) -> None: ...
    def increment(
        self,
        method=None,
        url=None,
        response=None,
        error=None,
        _pool=None,
        _stacktrace=None
    ) -> Retry: ...
    @staticmethod
    def get_content(resp: HTTPResponse, url: str) -> str: ...
    def __utc_now(self) -> datetime:
    def __log(self, level: int, message, **kwargs) -> None: ...
