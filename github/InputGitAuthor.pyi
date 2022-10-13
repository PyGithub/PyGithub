from typing import Dict, Union

from github.GithubObject import NotSetType

class InputGitAuthor:
    def __init__(
        self, name: str, email: str, date: Union[str, NotSetType] = ...
    ) -> None: ...
    @property
    def _identity(self) -> Dict[str, str]: ...
