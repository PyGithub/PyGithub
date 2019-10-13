from github.Rate import Rate
from typing import Any, Dict
from deprecated import deprecated


class RateLimit:
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def core(self) -> Rate: ...
    @property
    def graphql(self) -> Rate: ...
    @property
    @deprecated
    def rate(self) -> Rate
    @property
    def search(self) -> Rate: ...
