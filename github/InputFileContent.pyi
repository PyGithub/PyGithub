from github.GithubObject import _NotSetType
from typing import (
    Dict,
    Union,
)


class InputFileContent:
    def __init__(self, content: str, new_name: Union[str, _NotSetType] = ...) -> None: ...
    @property
    def _identity(self) -> Dict[str, str]: ...
