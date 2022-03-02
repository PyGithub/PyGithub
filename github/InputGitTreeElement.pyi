from typing import Dict, Union

from github.GithubObject import NotSetType

class InputGitTreeElement:
    def __init__(
        self,
        path: str,
        mode: str,
        type: str,
        content: Union[str, NotSetType] = ...,
        sha: Union[str, NotSetType, None] = ...,
    ) -> None: ...
    @property
    def _identity(self) -> Dict[str, str]: ...
