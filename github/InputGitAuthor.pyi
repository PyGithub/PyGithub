from typing import Dict


class InputGitAuthor:
    def __init__(self, name: str, email: str, date: str = ...) -> None: ...
    @property
    def _identity(self) -> Dict[str, str]: ...
