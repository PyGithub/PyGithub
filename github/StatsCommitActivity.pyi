from datetime import datetime
from typing import (
    Any,
    Dict,
    List,
)


class StatsCommitActivity:
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def days(self) -> List[int]: ...
    @property
    def total(self) -> int: ...
    @property
    def week(self) -> datetime: ...
