from github.NamedUser import NamedUser
from github.Repository import Repository
from typing import (
    Dict,
    Optional,
    Union,
)


class PullRequestPart:
    def _initAttributes(self) -> None: ...
    def _useAttributes(
        self,
        attributes: Dict[str, Union[str, Dict[str, Union[str, int]], Dict[str, Union[int, str, Dict[str, Union[str, int]], None, Dict[str, str]]], Dict[str, Union[str, int, Dict[str, Union[str, int]], None]], None]]
    ) -> None: ...
    @property
    def label(self) -> str: ...
    @property
    def ref(self) -> str: ...
    @property
    def repo(self) -> Repository: ...
    @property
    def sha(self) -> str: ...
    @property
    def user(self) -> Optional[NamedUser]: ...
