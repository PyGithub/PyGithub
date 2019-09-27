from github.GithubObject import _ValuedAttribute
from typing import (
    Any,
    Dict,
)


class Installation:
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def id(self) -> _ValuedAttribute: ...
