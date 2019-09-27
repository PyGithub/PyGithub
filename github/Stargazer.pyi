from datetime import datetime
from github.NamedUser import NamedUser
from typing import (
    Dict,
    Union,
)


class Stargazer:
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Union[Dict[str, Union[str, int]], str]]) -> None: ...
    @property
    def starred_at(self) -> datetime: ...
    @property
    def user(self) -> NamedUser: ...
