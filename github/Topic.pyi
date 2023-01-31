import datetime
from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject

class Topic(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def display_name(self) -> str: ...
    @property
    def short_description(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def created_by(self) -> str: ...
    @property
    def released(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def updated_at(self) -> datetime.datetime: ...
    @property
    def featured(self) -> bool: ...
    @property
    def curated(self) -> bool: ...
    @property
    def score(self) -> float: ...
