from datetime import datetime
from github.NamedUser import NamedUser
from typing import (
    Any,
    Dict,
    List,
    Optional,
)


class StatsContributor:
    def _initAttributes(self) -> None: ...
    def _useAttributes(
        self,
        attributes: Dict[str, Any]
    ) -> None: ...
    @property
    def author(self) -> NamedUser: ...
    @property
    def total(self) -> int: ...
    @property
    def weeks(self) -> List[Week]: ...
    class Week:
        def _initAttributes(self) -> None: ...
        def _useAttributes(self, attributes: Dict[str, int]) -> None: ...
        @property
        def a(self) -> int: ...
        @property
        def c(self) -> int: ...
        @property
        def d(self) -> int: ...
        @property
        def w(self) -> datetime: ...
