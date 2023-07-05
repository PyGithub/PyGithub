from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject

class GitObject(NonCompletableGithubObject):
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, str]) -> None: ...
    @property
    def sha(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def url(self) -> str: ...
