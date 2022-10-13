from typing import Dict, Union

from github.GithubObject import NotSetType

class InputFileContent:
    def __init__(
        self, content: str, new_name: Union[str, NotSetType] = ...
    ) -> None: ...
    @property
    def _identity(self) -> Dict[str, str]: ...
