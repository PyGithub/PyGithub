from datetime import datetime
from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject

class Rate(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def limit(self) -> int: ...
    @property
    def remaining(self) -> int: ...
    @property
    def reset(self) -> datetime: ...
    @property
    def used(self) -> int: ...